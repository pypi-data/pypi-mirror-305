"""
- trains & tests: designed for classification task, running on single-gpu.
- trainm & testm: designed for classification task, running on multi-gpus.
- trainllm: designed for pretraining, without evaluation process.
"""

import math
import torch
import evaluate

from pathlib import Path
from .utils import get_current_lr, get_grad_norm2
from torch.utils.tensorboard import SummaryWriter


_LOG_DIR = "./logs"
_MODEL_SAVE_DIR = "./checkpoint"
_DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

# if you want to use macro-f1, macro-precision, macro-recall, please modify in `./metrics`
_PATH_TO_METRICS = Path(__file__).parent / "metrics"
_CLF_METRICS = evaluate.combine([str(_PATH_TO_METRICS / "accuracy"), str(_PATH_TO_METRICS / "f1"), 
                                 str(_PATH_TO_METRICS / "precision"), str(_PATH_TO_METRICS / "recall")])


def _one_batch_forward_trains(model, batch, loss_fn, device):
    """designed for trains, custom your own"""
    inputs, targets = batch
    inputs, targets = inputs.to(device), targets.to(device)
    logits = model(inputs)
    loss = loss_fn(logits, targets)
    return logits, targets, loss


def _one_batch_forward_trainm(model, batch, loss_fn, accelerator):
    """designed for trainm, custom your own, return logits, targets, and loss on each process"""
    inputs, targets = batch
    logits = model(inputs)
    with accelerator.autocast():
        loss = loss_fn(logits, targets)
    return logits, targets, loss


def _one_batch_forward_trainllm(model, batch, loss_fn, accelerator):
    """designed for trainllm, custom your own, return loss on each process"""
    inputs, targets = batch
    logits = model(inputs)
    with accelerator.autocast():
        loss = loss_fn(logits, targets)
    return loss


@torch.no_grad()
def _one_batch_forward_tests(model, batch, device):
    """designed for tests, custom your own""" 
    inputs = batch  # test dataset has no targets
    inputs = inputs.to(device)
    logits = model(inputs)
    return logits


@torch.no_grad()
def _one_batch_forward_testm(model, batch, accelerator):
    """designed for testm, custom your own, return logits on each process"""
    inputs = batch  # test dataset has no targets
    logits = model(inputs)
    return logits


@torch.no_grad()
def _valid_trains(model, valid_dl, loss_fn, device, metrics, one_batch_forward_fn):
    """designed for trains"""
    model.eval()
    valid_loss = 0.0
    for batch in valid_dl:
        logits, targets, loss = one_batch_forward_fn(model, batch, loss_fn, device)
        metrics.add_batch(predictions=logits.argmax(dim=-1), references=targets)
        valid_loss += loss.item()
    valid_info = {"loss": valid_loss / len(valid_dl)} | metrics.compute()
    return valid_info


@torch.no_grad()
def _valid_trainm(model, valid_dl, loss_fn, accelerator, metrics, one_batch_forward_fn):
    """designed for trainm"""
    accelerator.wait_for_everyone()
    model.eval()
    valid_loss = 0.0
    for batch in valid_dl:
        logits, targets, loss = one_batch_forward_fn(model, batch, loss_fn, accelerator)
        all_predictions, all_targets = accelerator.gather_for_metrics((logits.argmax(dim=-1), targets))
        metrics.add_batch(predictions=all_predictions, references=all_targets)
        loss = accelerator.reduce(loss, reduction="mean")
        valid_loss += loss.item()
    valid_info = {"loss": valid_loss / len(valid_dl)} | metrics.compute()
    return valid_info


def trains(epochs, 
           train_dl, 
           valid_dl, 
           model, 
           loss_fn, 
           optimizer,
           scheduler=None,
           device=_DEVICE,
           max_grad_norm=None,
           early_stop_patience=6,
           log_global_steps=100,
           log_dir=_LOG_DIR, 
           model_save_dir=_MODEL_SAVE_DIR,
           metrics=_CLF_METRICS,
           one_batch_forward_fn=_one_batch_forward_trains):
    """
    Training Function.
    
    SUPPORTED:
        - classification task
        - single gpu or cpu training
        
    NOTICE:
        - metrics must have accuracy
        - early_stop is based on validation accuracy on each epoch
        - you need to custom `one_batch_forward_fn`, please refer to `_one_batch_forward_trains`

    Parameters
    ----------
    early_stop_patience : int, by default 6
        If the **accuracy** on the **validation set** does not improve after `early_stop_patience` epochs, then we will halt the training session.
    log_global_steps : int, by default 100
        Print and record the training information in tensorboard every `log_global_steps` global steps.
    log_dir : str, by default `./logs`
        Tensorboard log directory.
    model_save_dir : str, by_default `./checkpoint`
        During the early stopping process, dynamically save the model parameters with the highest accuracy on the validation set.
    metrics : huggingface evaluate
        Please refer to `_CLF_METRICS`, all supported metrics: https://github.com/huggingface/evaluate/tree/main/metrics.
        **[Notice]**: metrics must include accuracy, for early_stop needed.
    one_batch_forward_fn : Callable
        Please refer to `_one_batch_forward_trains`. 
        The body of the function can be adjusted, but you need to ensure that the input parameters and return values are consistent.
    """
    
    assertion = "early_stop needs to be based on the accuracy of the validation set, so the metrics must include accuracy."
    if hasattr(metrics, "evaluation_module_names"):
        assert "accuracy" in metrics.evaluation_module_names, assertion
    else:
        assert metrics.name == "accuracy", assertion
    Path(model_save_dir).mkdir(exist_ok=True)
    
    print(f"-------------------- start training, total training epochs: {epochs} --------------------")
    
    model = model.to(device)
    writer, global_step, best_valid_accuracy, early_stop_counts = SummaryWriter(log_dir), 0.0, 0.0, 0.0
    for epoch in range(epochs):
        model.train()
        for batch in train_dl:
            logits, targets, loss = one_batch_forward_fn(model, batch, loss_fn, device)
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm) if max_grad_norm is not None else ...
            optimizer.step()
            scheduler.step() if scheduler is not None else ...
            global_step += 1

            if global_step % log_global_steps == 0:
                train_info = {"loss": loss.item(), 
                              "lr": get_current_lr(optimizer), 
                              "grad_norm2": get_grad_norm2(model)} | metrics.compute(predictions=logits.argmax(dim=-1), references=targets)
                print(f"\033[92m[Train | Epoch: {epoch+1} | Global_Step: {global_step}]\033[0m", train_info)
                writer.add_scalars("Train", train_info, global_step)

        # validation
        valid_info = _valid_trains(model, valid_dl, loss_fn, device, metrics, one_batch_forward_fn)
        print(f"\033[91m[Valid | Epoch: {epoch+1} | Global_Step: {global_step}]\033[0m", valid_info)
        writer.add_scalars("Valid", valid_info, global_step)
        
        # early_stop
        if valid_info["accuracy"] > best_valid_accuracy:
            best_valid_accuracy = valid_info["accuracy"]
            torch.save(model.state_dict(), Path(model_save_dir) / "pytorch_model.pth")
            print(f"Current best valid accuracy: {best_valid_accuracy}, model saved in {model_save_dir}")
            early_stop_counts = 0.0
        else:
            early_stop_counts += 1
        
        if early_stop_counts == early_stop_patience:
            print(f"Model was not improved in {early_stop_patience} epochs, so we halt the training session!")
            break

    writer.close()


def trainm(epochs, 
           train_dl, 
           valid_dl, 
           model, 
           loss_fn, 
           optimizer, 
           accelerator, 
           scheduler=None,
           max_grad_norm=None,
           early_stop_patience=6,
           log_global_steps=100,
           log_dir=_LOG_DIR, 
           model_save_dir=_MODEL_SAVE_DIR,
           metrics=_CLF_METRICS,
           one_batch_forward_fn=_one_batch_forward_trainm):
    """
    Training Function.
    
    SUPPORTED:
        - classification task
        - multi-gpus
        - gradient_accumulation
        - mixed_precision
        
    NOTICE:
        - metrics must have accuracy
        - early_stop is based on validation accuracy on each epoch
        - you need to custom `one_batch_forward_fn`, please refer to `_one_batch_forward_trainm`
        - use huggingface accelerate to configure distributed training environments
        - prepare your model, optimizer, dataloader, and scheduler before using this function.

    Parameters
    ----------
    accelerator : accelerate.Accelerator
        huggingface accelerate.
    early_stop_patience : int, by default 6
        If the **accuracy** on the **validation set** does not improve after `early_stop_patience` epochs, then we will halt the training session.
    log_global_steps : int, by default 100
        Print and record the training information in tensorboard every `log_global_steps` global steps.
    log_dir : str, by default `./logs`
        Tensorboard log directory.
    model_save_dir : str, by_default `./checkpoint`
        During the early stopping process, dynamically save the model parameters with the highest accuracy on the validation set.
    metrics : huggingface evaluate
        Please refer to `_CLF_METRICS`, all supported metrics: https://github.com/huggingface/evaluate/tree/main/metrics.
        **[Notice]**: metrics must include accuracy, for early_stop needed.
    one_batch_forward_fn : Callable
        Please refer to `_one_batch_forward_trainm`. 
        The body of the function can be adjusted, but you need to ensure that the input parameters and return values are consistent.
    """
    
    assertion = "early_stop needs to be based on the accuracy of the validation set, so the metrics must include accuracy."
    if hasattr(metrics, "evaluation_module_names"):
        assert "accuracy" in metrics.evaluation_module_names, assertion
    else:
        assert metrics.name == "accuracy", assertion

    if accelerator.is_main_process:
        Path(model_save_dir).mkdir(exist_ok=True)
        writer = SummaryWriter(log_dir=log_dir)
    
    accelerator.print(f"-------------------- start training, total training epochs: {epochs} --------------------")

    global_step, best_valid_accuracy, early_stop_counts = 0.0, 0.0, 0.0
    for epoch in range(epochs):
        accelerator.wait_for_everyone()
        model.train()
        with accelerator.accumulate(model):
            for batch in train_dl:
                logits, targets, loss = one_batch_forward_fn(model, batch, loss_fn, accelerator)
                optimizer.zero_grad()
                accelerator.backward(loss)
                accelerator.clip_grad_norm_(model.parameters(), max_grad_norm) if accelerator.sync_gradients and max_grad_norm is not None else ...
                optimizer.step()
                global_step += 1 if accelerator.sync_gradients else ...
                scheduler.step() if scheduler is not None else ...
                
                if global_step % log_global_steps == 0:
                    all_predictions, all_targets = accelerator.gather_for_metrics((logits.argmax(dim=-1), targets))
                    train_info = {"loss": accelerator.reduce(loss, reduction="mean").item(), 
                                  "lr": get_current_lr(optimizer), 
                                  "grad_norm2": get_grad_norm2(model)} | metrics.compute(predictions=all_predictions, references=all_targets)
                    accelerator.print(f"\033[92m[Train | Epoch: {epoch+1} | Global_Step: {global_step}]\033[0m", train_info)
                    writer.add_scalars("Train", train_info, global_step) if accelerator.is_main_process else ...
        
        # validation
        valid_info = _valid_trainm(model, valid_dl, loss_fn, accelerator, metrics, one_batch_forward_fn)
        accelerator.print(f"\033[91m[Valid | Epoch: {epoch+1} | Global_Step: {global_step}]\033[0m", valid_info)
        writer.add_scalars("Valid", valid_info, global_step) if accelerator.is_main_process else ...
        
        # early_stop
        if valid_info["accuracy"] > best_valid_accuracy:
            best_valid_accuracy = valid_info["accuracy"]
            accelerator.wait_for_everyone()
            accelerator.save_model(model, model_save_dir) if accelerator.is_main_process else ...
            accelerator.print(f"Current best valid accuracy: {best_valid_accuracy}, model saved in {model_save_dir}")
            early_stop_counts = 0.0
        else:
            early_stop_counts += 1
        
        if early_stop_counts == early_stop_patience:
            accelerator.print(f"Model was not improved in {early_stop_patience} epochs, so we halt the training session!")
            break

    writer.close() if accelerator.is_main_process else ...


def trainllm(epochs, 
             train_dl,
             model,
             loss_fn,  
             optimizer, 
             accelerator,
             scheduler=None, 
             max_grad_norm=None,
             log_global_steps=1000,
             log_dir=_LOG_DIR,
             resume_dir=None,
             train_state_save_dir=_MODEL_SAVE_DIR,
             train_state_save_global_steps=5000,
             one_batch_forward_fn=_one_batch_forward_trainllm):
    """Train Function.
    
    NOTICE:
        - using huggingface format model.
        - dataloader should be stateful.

    Parameters
    ----------
    train_dl : torchdata.stateful_dataloader.StatefulDataLoader
        StatefulDataLoader is required.
        
        **Example 1:**
        >>> from torch.utils.data import DataLoader
        >>> from accelerate import Accelerator, DataLoaderConfiguration
        >>> accelerator = Accelerator(dataloader_config=DataLoaderConfiguration(use_stateful_dataloader=True))
        >>> train_dl = DataLoader(train_ds)
        
        **Example 2:**
        >>> from torchdata.stateful_dataloader import StatefulDataLoader
        >>> train_dl = StatefulDataLoader(train_ds)
        
    max_grad_norm : float | None, by default None
        Apply clip_grad_norm function.
    log_global_steps : int, by default 1000
        Print train information every `log_global_steps`, 
        The printed training information will also write to tensorboard.
    log_dir : str, by default `./logs`
        Tensorboard log directory.
    resume_dir : str, by default None
        If you want to resume training, you can specify the checkpoint directory.
    train_state_save_dir : str, by default `./checkpoint`
        Training state will be saved in `train_state_save_dir`.
    train_state_save_global_steps : int, by default 5000
        Training state will be saved every `train_state_save_global_steps`,
        It is recommended to save eight times for each epoch, as follows: `len(train_dl) // accelerator.gradient_accumulation_steps // 8`.
    one_batch_forward_fn : Callable
        Please refer to `_one_batch_forward_trainllm`. 
        The body of the function can be adjusted, but you need to ensure that the input parameters and return values are consistent.
    """
    
    try:
        accelerator.register_for_checkpoint(train_dl)
    except:
        accelerator.print("Please use `torchdata.stateful_dataloader.StatefulDataLoader`, notice torchdata >= 0.8.0")

    writer = SummaryWriter(log_dir=log_dir) if accelerator.is_main_process else ...
    accelerator.print(f"-------------------- start training, total training epochs: {epochs} --------------------")

    global_step = 0
    resume_step = 0
    resume_epoch = 0

    if resume_dir is not None:
        accelerator.load_state(resume_dir)
        steps_per_epoch = math.ceil(len(train_dl) / accelerator.gradient_accumulation_steps)
        resume_step = int(resume_dir.split("step_")[-1])
        global_step = resume_step
        resume_epoch = resume_step // steps_per_epoch
        # resume_step -= resume_epoch * steps_per_epoch
        accelerator.print(f"resume from checkpoint -> {resume_dir}")
    
    for epoch in range(resume_epoch, epochs):
        accelerator.wait_for_everyone()
        model.train()
        # if resume_dir and epoch == resume_epoch and resume_step != 0:
        #     train_dl = accelerator.skip_first_batches(train_dl, resume_step * accelerator.gradient_accumulation_steps)
        with accelerator.accumulate(model):
            for batch in train_dl:
                loss = one_batch_forward_fn(model, batch, loss_fn, accelerator)
                optimizer.zero_grad()
                accelerator.backward(loss)
                accelerator.clip_grad_norm_(model.parameters(), max_grad_norm, ) if accelerator.sync_gradients else ...
                optimizer.step()
                global_step += 1 if accelerator.sync_gradients else ...
                scheduler.step() if scheduler is not None else ...
                
                if global_step % log_global_steps == 0:
                    train_info = {"loss": accelerator.reduce(loss, reduction="mean").item(), 
                                  "lr": get_current_lr(optimizer), 
                                  "grad_norm2": get_grad_norm2(model)}
                    accelerator.print(f"\033[92m[Train | Epoch: {epoch+1} | Global_Step: {global_step}]\033[0m", train_info)
                    writer.add_scalars("Train", train_info, global_step) if accelerator.is_main_process else ...
                
                if global_step % train_state_save_global_steps == 0:
                    accelerator.wait_for_everyone()
                    accelerator.save_state(Path(train_state_save_dir) / f"train_state_step_{global_step}")
                    accelerator.unwrap_model(model).save_pretrained(
                        save_directory=Path(train_state_save_dir / f"train_state_step_{global_step}" / "model"),
                        is_main_process=accelerator.is_main_process,
                        state_dict=accelerator.get_state_dict(model),
                        save_func=accelerator.save
                    )
                    
    writer.close() if accelerator.is_main_process else ...


@torch.no_grad()
def tests(model, test_dl, device, one_batch_forward_fn=_one_batch_forward_tests):
    """Test Function.

    Parameters
    ----------
    one_batch_forward_fn : by default _one_batch_forward_tests
        Custom your own, please refer to `_one_batch_forward_tests`,
        The body of the function can be adjusted, but you need to ensure that the input parameters and return values are consistent.
    """
    model.eval()
    model = model.to(device)
    test_results = []
    for batch in test_dl:
        logits = one_batch_forward_fn(model, batch, device)
        test_results.append(logits.argmax(dim=-1).view(-1))
    return torch.cat(test_results)


@torch.no_grad()
def testm(model, test_dl, accelerator, one_batch_forward_fn=_one_batch_forward_testm):
    """Test Function.

    Parameters
    ----------
    one_batch_forward_fn : by default _one_batch_forward_testm
        Custom your own, please refer to `_one_batch_forward_testm`,
        The body of the function can be adjusted, but you need to ensure that the input parameters and return values are consistent.
    """
    accelerator.wait_for_everyone()
    model.eval()
    test_results = []
    for batch in test_dl:
        logits = one_batch_forward_fn(model, batch, accelerator)
        all_outputs = accelerator.gather_for_metrics(logits.argmax(dim=-1)).view(-1)
        test_results.append(all_outputs)
    return torch.cat(test_results)


if __name__ == "__main__":
    pass
