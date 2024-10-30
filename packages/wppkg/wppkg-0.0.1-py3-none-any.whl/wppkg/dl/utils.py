import os
import torch
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from pathlib import Path
from safetensors.torch import load_model


def set_seed(seed=42):
    """Fixes random number generator seeds for reproducibility."""
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True


def forward_hook(module, input, output):
    """usage: model.layer_name.register_forward_hook(forward_hook)"""
    print(f"{module.__class__.__name__}  [output_shape]: {output.shape}")
    print(f"{module.__class__.__name__}  [output_value]: {output}")


def print_trainable_parameters(model):
    all_params = sum([param.numel() for param in model.parameters()])
    trainable_params = sum([param.numel() for param in model.parameters() if param.requires_grad])
    
    print(
        f"trainable params: {trainable_params:,d} || all params: {all_params:,d} || trainable%: {100 * trainable_params / all_params:.4f}"
    )


def plot_model_params_distribution(model,
                                   n_bins=200,
                                   x_range=(-0.1, 0.1),
                                   figsize=(16, 9),
                                   dpi=100,
                                   bar_color=None,
                                   figure_save_path=None):
    
    def _get_model_params(model):
        params = []
        for param in model.parameters():
            params.append(param.view(-1))
        return torch.cat(params)
    
    params = _get_model_params(model)
    hist, _ = torch.histogram(input=params.float(), bins=n_bins, range=x_range)
        
    plt.figure(figsize=figsize, dpi=dpi)
    x = range(n_bins)
    plt.bar(x, hist.detach().cpu().numpy(), color=random.choice(["#ff8a00", "#015697", "#1b5523"]) if bar_color is None else bar_color)
    plt.xticks(x, np.linspace(x_range[0], x_range[-1], n_bins).round(3))
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
    plt.title("Model Parameters Distribution")
    
    if figure_save_path:
        plt.savefig(figure_save_path, dpi=dpi)
        
    plt.show()


def load_model_checkpoint(model, checkpoint, strict=True, device="cpu"):
    """load model state_dict

    Parameters
    ----------
    model : torch.nn.Module
        Pytorch Model.
    checkpoint : str
        Your model checkpoint file path, only support format `pt`, `pth`, `bin`, and `safetensors`.
    strict : bool, by default True
        Whether all parameters should be loaded.
    device : torch.device, by default "cpu"
        The device where the tensors need to be located after load.
    """

    checkpoint_suffix = Path(checkpoint).suffix
    if checkpoint_suffix == ".safetensors":
        load_model(model, checkpoint, strict, device)
    elif checkpoint_suffix in [".bin", ".pt", ".pth"]:
        model.load_state_dict(torch.load(checkpoint, device), strict)
    else:
        raise ValueError(f"load_checkpoint did not support {checkpoint_suffix} format.")


def get_current_lr(optimizer):
    return optimizer.state_dict()['param_groups'][0]['lr']


def get_grad_norm2(model):
    """get model grad l2 norm."""
    grad_norm2 = 0
    for param in model.parameters():
        if param.grad is not None:
            grad_norm2 += (param.data.norm(2).item()) ** 2
    return torch.sqrt(torch.tensor(grad_norm2)).item()


class Accumulator:
    """For accumulating sums over `n` variables."""
    def __init__(self, n):
        self.data = [0.0] * n

    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]

    def reset(self):
        self.data = [0.0] * len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


if __name__ == "__main__":
    pass
