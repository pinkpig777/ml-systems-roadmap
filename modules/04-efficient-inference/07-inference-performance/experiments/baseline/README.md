# Experiment 001 — GPU inference baseline

Question: How does synchronized end-to-end generation time change with cache enabled?

Use Linux with a CUDA-capable PyTorch installation from https://pytorch.org/get-started/locally/. Install `transformers` in the same environment. Start with `Qwen/Qwen2.5-0.5B` (download required). Verify model license and available VRAM. Run from this directory:

```bash
python -m pip install transformers
python env_probe.py > environment.json
python benchmark.py --output metrics.csv
python -m pip freeze > requirements.lock.txt
```

The starter measures total model.generate wall time, not TTFT or TPOT. It uses greedy decoding, fixed minimum/maximum new tokens, warmup and CUDA synchronization. Results exclude model loading and tokenization. Peak allocated memory includes resident model weights. Compare output tokens across cache modes before interpreting speed; near-tied logits may differ numerically. Extend with separate prefill/decode timing in Week 1. Code is syntax checked only; GPU execution remains to be verified on your hardware.
