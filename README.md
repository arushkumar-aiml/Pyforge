<div align="center">

# 🔥 PyForge

**A lightweight PyTorch training framework — built from scratch.**

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-v1.0%20Live-ff6b00?style=for-the-badge)

*Auto-detects your hardware. Trains your model. Reports your loss. Zero config.*

</div>

---

## 🤔 What is PyForge?

PyForge is a minimal PyTorch training framework that handles the boring parts of the ML loop — so you can focus on building smarter models.

- ⚡ **Auto-detects** CUDA, MPS (Apple Silicon), or CPU — no config needed
- 🔁 **Trains any PyTorch model** automatically
- 📊 **Validates and reports loss** after every epoch
- 💻 **Works on any machine** — plug in your model and go

---

## 🏗️ How it Works

```
Your Model  →  PyForge(model)  →  Hardware Detection  →  Auto Training  →  Loss Report
```

---

## 📁 Project Structure

```
PyForge/
├── hardware.py       # Device detection — CUDA / MPS / CPU
├── model.py          # Neural network definition
├── trainer.py        # PyForge core training class
├── main.py           # Entry point — run from here
├── requirements.txt  # Dependencies
└── README.md
```

---

## 🚀 Installation

```bash
git clone https://github.com/username/PyForge.git
cd PyForge
pip install -r requirements.txt
```

## ▶️ Run

```bash
python main.py
```

---

## 📟 Output

```
[PyForge] Device: cpu
[PyForge] Running on cpu
[PyForge] Supported: ['cuda', 'mps', 'cpu']

[PyForge] Epoch 1 Loss: 0.8921
[PyForge] Epoch 2 Loss: 0.6543
[PyForge] Epoch 3 Loss: 0.4321

[PyForge] Validation Loss: 0.4102 ✓
```

---

## ✅ Feature Status

| Feature | Status |
|---|---|
| Auto Hardware Detection | ✅ Available |
| CPU Support | ✅ Available |
| CUDA Support | ✅ Available |
| MPS Support (Apple Silicon) | ✅ Available |
| Auto Training Loop | ✅ Available |
| Validation Loop | ✅ Available |
| Loss Reporting | ✅ Available |
| AMP (Mixed Precision) | 🔜 Coming Soon |
| GPU Profiler | 🔜 Coming Soon |
| Benchmark Reports | 🔜 Coming Soon |

---

## 📚 What We Learned Building This

**Day 1 — Python OOP**
> Classes · Objects · Constructors · `@staticmethod` · `@property` · Context Managers · Python Packaging

**Day 2 — PyTorch Basics**
> Tensors & GPU · `nn.Module` · DataLoader

**Day 3 — Training Loop**
> Loss Functions · Backpropagation · Optimizer · Validation Loop

---

## 🗺️ Roadmap

- [x] `v1.0` — Basic Training Loop
- [ ] `v2.0` — AMP Engine (Mixed Precision)
- [ ] `v3.0` — GPU Profiler
- [ ] `v4.0` — Benchmark Reports
- [ ] `v5.0` — Full Optimization Engine

---

## 🛠️ Built With

- [Python 3.11](https://www.python.org/)
- [PyTorch 2.0](https://pytorch.org/)
- [psutil](https://pypi.org/project/psutil/)

---

## 👥 Authors

| | Name | Role |
|---|---|---|
| 🚀 | **Arush Kumar** | Creator · Building in Public |
| ⚡ | **Ayushi Shukla** | Co-Author |

---

## 📄 License

[MIT License](LICENSE) — Free to use, modify, and distribute.

---

<div align="center">

Made with 🔥 by Arush Kumar & Ayushi Shukla

</div>
