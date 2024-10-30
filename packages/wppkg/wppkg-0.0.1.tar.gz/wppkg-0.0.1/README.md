# wppkg

_Description: some useful functions I often use in my work.

## 1. Structure

```txt
.
└── wppkg
    ├── dl
    │   ├── __init__.py
    │   ├── metrics
    │   │   ├── accuracy
    │   │   │   ├── accuracy.py
    │   │   │   ├── app.py
    │   │   │   ├── README.md
    │   │   │   └── requirements.txt
    │   │   ├── f1
    │   │   │   ├── app.py
    │   │   │   ├── f1.py
    │   │   │   ├── README.md
    │   │   │   └── requirements.txt
    │   │   ├── precision
    │   │   │   ├── app.py
    │   │   │   ├── precision.py
    │   │   │   ├── README.md
    │   │   │   └── requirements.txt
    │   │   └── recall
    │   │       ├── app.py
    │   │       ├── README.md
    │   │       ├── recall.py
    │   │       └── requirements.txt
    │   ├── trainer.py
    │   └── utils.py
    └── __init__.py
```

## 2. Commit Message

- Some training functions have been added, see ***trains***, ***trainm***, and ***trainllm*** in `trainer.py` for details.