# Lab 3.4 — Framework Internals

## Task
Trace a PyTorch operation from Python API to GPU activity.

## Protocol
1. Record hardware, software versions and baseline.
2. State a hypothesis and choose one independent variable; hold other relevant conditions fixed.
3. Validate correctness or expected behavior before measuring.
4. For performance tests, warm up, repeat trials, report median and variability; for asynchronous GPU work synchronize or use CUDA events as appropriate.
5. Save code, commands and raw results here; explain confounders and limitations.

## Acceptance
Explain the observed dispatch path with evidence, including backend-dependent choices. No fabricated measurements. Hardware-dependent steps may be deferred with a reason.
