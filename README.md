## PyForge — Complete README.md

```markdown
# 🔥 PyForge

> A lightweight PyTorch training framework built from scratch.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## What is PyForge?

PyForge is a minimal PyTorch training framework that:
- Auto detects your hardware — CUDA, MPS, or CPU
- Trains any PyTorch model automatically
- Validates and reports loss after training
- Works on any machine — no configuration needed

---

## How it Works

```
Your Model
    ↓
PyForge(model)
    ↓
Hardware Detection
    ↓
Auto Training + Validation
    ↓
Loss Report
```

---

## Project Structure

```
PyForge/
├── hardware.py       # Device detection
├── model.py          # Neural network
├── trainer.py        # PyForge core class
├── main.py           # Run from here
├── requirements.txt  # Dependencies
└── README.md
```

---

## Installation

```bash
git clone https://github.com/username/PyForge.git
cd PyForge
pip install -r requirements.txt
```

---

## How to Run

```bash
python main.py
```

---

## Output

```
[PyForge] Device: cpu
[PyForge] Running on cpu
[PyForge] Supported: ['cuda', 'mps', 'cpu']
[PyForge] Epoch 1 Loss: 0.8921
[PyForge] Epoch 2 Loss: 0.6543
[PyForge] Epoch 3 Loss: 0.4321
[PyForge] Validation Loss: 0.4102
```

---

## Features

| Feature | Status |
|---|---|
| Auto Hardware Detection | ✅ |
| CPU Support | ✅ |
| CUDA Support | ✅ |
| MPS Support (Apple) | ✅ |
| Auto Training Loop | ✅ |
| Validation Loop | ✅ |
| Loss Reporting | ✅ |
| AMP Support | 🔜 Coming Soon |
| GPU Profiler | 🔜 Coming Soon |
| Benchmark Reports | 🔜 Coming Soon |

---

## Built With

- Python 3.11
- PyTorch 2.0
- psutil

---

## What I Learned Building This

- Day 1 — Python OOP
  - Classes, Objects, Constructors
  - @staticmethod and @property
  - Context Managers
  - Python Packaging

- Day 2 — PyTorch Basics
  - Tensors and GPU
  - nn.Module
  - DataLoader

- Day 3 — Training Loop
  - Loss Functions
  - Backpropagation
  - Optimizer
  - Validation Loop

---

## Roadmap

- v1.0 — Basic Training Loop ✅
- v2.0 — AMP Engine 🔜
- v3.0 — GPU Profiler 🔜
- v4.0 — Benchmark Reports 🔜
- v5.0 — Full Optimization Engine 🔜

---

## Author

**Arush Kumar**
Building in Public 🚀

---

## License

MIT License — Free to use
```

---

