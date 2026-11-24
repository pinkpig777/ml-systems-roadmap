# Setup

CPU labs can begin on any machine with Python 3 and a C++17 compiler. GPU labs require an NVIDIA CUDA-capable system (e.g. RTX 3060 on Linux or WSL2) and compatible driver/toolkit. Check available VRAM; choose small models and verify backend support before installing serving runtimes. Use separate virtual environments for incompatible dependencies.

```bash
python --version
c++ --version
nvidia-smi
nvcc --version
```

Install PyTorch using the official selector at https://pytorch.org/get-started/locally/ for your platform. Do not assume the CUDA version shown by nvidia-smi is the installed toolkit version.

## Initialize GitHub
From the extracted repository directory:

```bash
git init -b main
git add .
git commit -m "Initialize competency-based ML systems roadmap"
gh auth login
gh repo create ml-systems-roadmap --private --source=. --remote=origin --push
```

Choose --public instead only if you want to publish your notes. If a remote already exists, review and merge changes instead of recreating or force-pushing it.
