# ML Systems Engineering Roadmap v2.0

Self-paced, competency-based curriculum with inference specialization. No calendar deadlines. Modules 01–05 are the recommended core path; 06 is breadth and 07 is cross-cutting. Validate prerequisites rather than completing every chapter mechanically.

Depth: L1 awareness; L2 explain and reason; L3 implement and validate; L4 profile and optimize. These are target competencies, not current ratings.

## 01 — [Computer Systems Fundamentals](modules/01-computer-systems/README.md)

Capstone: Memory & Concurrency Lab

- [1.1 Computer Architecture](modules/01-computer-systems/01-computer-architecture/README.md) — L3: CPU execution; Registers and caches; RAM; SIMD

- [1.2 Memory Systems](modules/01-computer-systems/02-memory-systems/README.md) — L3: Stack and heap; Virtual memory; Cache lines; Locality; Alignment

- [1.3 Modern C++](modules/01-computer-systems/03-modern-c/README.md) — L3: Pointers and references; Object lifetime; RAII; Smart pointers; STL; Move semantics

- [1.4 Operating Systems](modules/01-computer-systems/04-operating-systems/README.md) — L2: Processes; Threads; Context switches; System calls

- [1.5 Concurrency](modules/01-computer-systems/05-concurrency/README.md) — L3: Race conditions; Mutexes; Condition variables; Deadlock; Thread pools

- [1.6 Python Runtime](modules/01-computer-systems/06-python-runtime/README.md) — L3: GIL; Threads; Multiprocessing; AsyncIO; Event loop

- [1.7 Networking](modules/01-computer-systems/07-networking/README.md) — L2: TCP; HTTP; Sockets; RPC; Client-server

- [1.8 Performance Fundamentals](modules/01-computer-systems/08-performance-fundamentals/README.md) — L3: Latency; Throughput; Bandwidth; Warmup; Statistics

## 02 — [Parallel & GPU Computing](modules/02-gpu-computing/README.md)

Capstone: GPU Kernel Optimization Lab

- [2.1 Parallel Computing](modules/02-gpu-computing/01-parallel-computing/README.md) — L3: Amdahl's law; SIMD; SIMT; Task and data parallelism

- [2.2 GPU Architecture](modules/02-gpu-computing/02-gpu-architecture/README.md) — L4: SM; Warp; Block; CUDA cores; Tensor cores

- [2.3 CUDA Programming](modules/02-gpu-computing/03-cuda-programming/README.md) — L3: Kernel; Grid; Indexing; Host and device; Error checking

- [2.4 GPU Memory Hierarchy](modules/02-gpu-computing/04-gpu-memory-hierarchy/README.md) — L4: Global; Shared; Registers; L1 and L2

- [2.5 Memory Optimization](modules/02-gpu-computing/05-memory-optimization/README.md) — L4: Coalescing; Bank conflicts; Tiling

- [2.6 Parallel Algorithms](modules/02-gpu-computing/06-parallel-algorithms/README.md) — L4: Reduction; Scan; Matrix multiplication

- [2.7 GPU Execution](modules/02-gpu-computing/07-gpu-execution/README.md) — L3: Streams; Events; Synchronization; Transfers

- [2.8 Performance Modeling](modules/02-gpu-computing/08-performance-modeling/README.md) — L4: Roofline; Arithmetic intensity; Occupancy

- [2.9 GPU Profiling](modules/02-gpu-computing/09-gpu-profiling/README.md) — L4: Timeline; Kernel metrics; Bottleneck diagnosis

## 03 — [Deep Learning Systems](modules/03-deep-learning-systems/README.md)

Capstone: Mini Autograd / Operator Optimization Lab

- [3.1 Tensor Fundamentals](modules/03-deep-learning-systems/01-tensor-fundamentals/README.md) — L3: Shape; Stride; Layout; Contiguity; Broadcasting

- [3.2 Deep Learning Operators](modules/03-deep-learning-systems/02-deep-learning-operators/README.md) — L3: MatMul; Convolution; Softmax; Normalization

- [3.3 Computation Graphs](modules/03-deep-learning-systems/03-computation-graphs/README.md) — L3: Forward; Backward; Chain rule; Autograd

- [3.4 Framework Internals](modules/03-deep-learning-systems/04-framework-internals/README.md) — L3: Dispatcher; ATen; Backend; Operator execution

- [3.5 Tensor Memory Management](modules/03-deep-learning-systems/05-tensor-memory-management/README.md) — L3: Allocation; Caching allocator; Lifetime

- [3.6 ML Compilation](modules/03-deep-learning-systems/06-ml-compilation/README.md) — L2: Graph capture; IR; Lowering; Code generation

- [3.7 Operator Optimization](modules/03-deep-learning-systems/07-operator-optimization/README.md) — L4: Triton; Kernel fusion; torch.compile

## 04 — [Efficient Model Inference](modules/04-efficient-inference/README.md)

Capstone: Model Inference Runtime Benchmark

- [4.1 Inference Execution](modules/04-efficient-inference/01-inference-execution/README.md) — L3: Model graph; Runtime; Static and dynamic shapes

- [4.2 Numerical Representation](modules/04-efficient-inference/02-numerical-representation/README.md) — L3: FP32; FP16; BF16; INT8; INT4

- [4.3 Quantization](modules/04-efficient-inference/03-quantization/README.md) — L4: PTQ; QAT; Calibration; Accuracy trade-offs

- [4.4 Model Compression](modules/04-efficient-inference/04-model-compression/README.md) — L2: Pruning; Sparsity; Distillation

- [4.5 Graph Optimization](modules/04-efficient-inference/05-graph-optimization/README.md) — L3: Constant folding; Fusion; Layout optimization

- [4.6 Inference Runtime](modules/04-efficient-inference/06-inference-runtime/README.md) — L4: ONNX Runtime; TensorRT; Execution providers

- [4.7 Inference Performance](modules/04-efficient-inference/07-inference-performance/README.md) — L4: Batch size; Latency; Throughput; Memory footprint

- [4.8 Correctness & Validation](modules/04-efficient-inference/08-correctness-validation/README.md) — L3: Numerical parity; Error analysis; Reproducibility

## 05 — [LLM Inference & Serving](modules/05-llm-inference-serving/README.md)

Capstone: LLM Inference Lab / Mini Inference Engine

- [5.1 Transformer Architecture](modules/05-llm-inference-serving/01-transformer-architecture/README.md) — L3: Attention; MLP; RoPE; Normalization

- [5.2 Autoregressive Generation](modules/05-llm-inference-serving/02-autoregressive-generation/README.md) — L3: Tokenization; Sampling; Generation loop

- [5.3 KV Cache](modules/05-llm-inference-serving/03-kv-cache/README.md) — L4: Cache layout; Memory complexity; GQA; MQA

- [5.4 Prefill & Decode](modules/05-llm-inference-serving/04-prefill-decode/README.md) — L4: Compute and memory limits; TTFT; TPOT

- [5.5 Efficient Attention](modules/05-llm-inference-serving/05-efficient-attention/README.md) — L3: FlashAttention; IO-aware computation

- [5.6 Serving Architecture](modules/05-llm-inference-serving/06-serving-architecture/README.md) — L3: API; Engine; Scheduler; Executor

- [5.7 Request Batching](modules/05-llm-inference-serving/07-request-batching/README.md) — L4: Static; Dynamic; Continuous batching

- [5.8 Cache Management](modules/05-llm-inference-serving/08-cache-management/README.md) — L4: PagedAttention; Blocks; Prefix caching

- [5.9 Advanced Scheduling](modules/05-llm-inference-serving/09-advanced-scheduling/README.md) — L3: Preemption; Chunked prefill; Speculative decoding

- [5.10 Inference Frameworks](modules/05-llm-inference-serving/10-inference-frameworks/README.md) — L3: vLLM; SGLang; TensorRT-LLM

- [5.11 Serving Benchmark](modules/05-llm-inference-serving/11-serving-benchmark/README.md) — L4: Concurrency; Tail latency; Goodput; Workload modeling

## 06 — [Distributed ML Systems](modules/06-distributed-ml/README.md)

Capstone: Distributed Communication Lab

- [6.1 Distributed Fundamentals](modules/06-distributed-ml/01-distributed-fundamentals/README.md) — L2: Communication; Synchronization; Failure models

- [6.2 GPU Interconnect](modules/06-distributed-ml/02-gpu-interconnect/README.md) — L2: PCIe; NVLink; Network bandwidth

- [6.3 Collective Communication](modules/06-distributed-ml/03-collective-communication/README.md) — L2: AllReduce; AllGather; ReduceScatter; NCCL

- [6.4 ML Parallelism](modules/06-distributed-ml/04-ml-parallelism/README.md) — L2: Data; Tensor; Pipeline; Expert parallelism

- [6.5 Training Systems](modules/06-distributed-ml/05-training-systems/README.md) — L2: DDP; FSDP; Gradient accumulation

- [6.6 Distributed Inference](modules/06-distributed-ml/06-distributed-inference/README.md) — L2: Model sharding; Communication overhead

- [6.7 Resource Management](modules/06-distributed-ml/07-resource-management/README.md) — L2: GPU allocation; Job scheduling; Slurm

## 07 — [Production Engineering](modules/07-production-engineering/README.md)

Capstone: Production-ready Inference Service

- [7.1 Software Architecture](modules/07-production-engineering/01-software-architecture/README.md) — L3: Modularity; Abstraction; Interfaces

- [7.2 Testing & Validation](modules/07-production-engineering/02-testing-validation/README.md) — L3: Unit; Integration; Numerical correctness

- [7.3 Serving Reliability](modules/07-production-engineering/03-serving-reliability/README.md) — L3: Queues; Backpressure; Timeout; Cancellation

- [7.4 Observability](modules/07-production-engineering/04-observability/README.md) — L3: Logging; Metrics; Tracing; SLO

- [7.5 Deployment](modules/07-production-engineering/05-deployment/README.md) — L3: Linux; Containers; CI/CD

- [7.6 Benchmark Engineering](modules/07-production-engineering/06-benchmark-engineering/README.md) — L4: Workload design; Warmup; Statistics; Reproducibility

- [7.7 Technical Communication](modules/07-production-engineering/07-technical-communication/README.md) — L3: Design docs; Performance reports; Trade-offs
