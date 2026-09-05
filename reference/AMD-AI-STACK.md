# The AMD AI Stack — Model to Hardware

**Written for someone who has never seen this before.** Every layer explained, every arrow labelled,
every name decoded.

**Sources:** AMD's own documentation (ROCm docs, Ryzen AI docs, AMD developer site), plus the vLLM
project and the AITER repository. Checked 2026-09-05. Anything from community analysis or
forward-looking reporting is marked, and Section 20 lists exactly what is verified and what is not.

**Where this fits:** supporting reference for the roadmap's Section 10.17 (model-to-hardware
specialisation track). Companion document to [`QUALCOMM-AI-STACK.md`](QUALCOMM-AI-STACK.md).

---

## Contents

| § | Section |
|---|---|
| 1 | The 30-second version |
| 2 | The whole stack, one picture |
| 3 | **Name decoder — read this first** |
| 4 | Three hardware families, one software stack |
| 5 | Inside a CDNA datacenter GPU |
| 6 | Inside the XDNA client NPU |
| 7 | ROCm, layer by layer |
| 8 | **HIP — and porting from CUDA** |
| 9 | The library layer |
| 10 | **AITER — the AI kernel layer** |
| 11 | Frameworks: PyTorch, JAX, Triton |
| 12 | Serving: vLLM and SGLang |
| 13 | The client stack: Ryzen AI |
| 14 | Quantisation: AMD Quark |
| 15 | Profiling and tools |
| 16 | End-to-end journey — datacenter |
| 17 | End-to-end journey — client |
| 18 | If you already know CUDA or the Qualcomm stack |
| 19 | The mistakes everyone makes |
| 20 | Verification status |

---

## 1. The 30-second version

AMD has **two completely different AI paths**, and confusing them wastes weeks:

```
┌──────────────────────────────┐   ┌──────────────────────────────┐
│  DATACENTER                  │   │  CLIENT / EDGE               │
│                              │   │                              │
│  Instinct GPUs (CDNA)        │   │  Ryzen AI NPU (XDNA)         │
│  MI300X · MI350X · MI355X    │   │  in laptop processors        │
│                              │   │                              │
│  Software: ROCm              │   │  Software: Ryzen AI Software │
│  Language: HIP               │   │  Path: ONNX Runtime +        │
│  Kernels: AITER, CK, Triton  │   │        Vitis AI EP           │
│  Serving: vLLM, SGLang       │   │  LLMs: OGA / llama.cpp,      │
│                              │   │        Lemonade              │
│  Train AND infer             │   │  Infer only                  │
└──────────────────────────────┘   └──────────────────────────────┘
         │                                       │
         └───────── shared: AMD Quark ───────────┘
                    (quantisation toolkit)
```

> **The one thing to remember:** ROCm is the datacenter/GPU stack. Ryzen AI Software is the client/NPU
> stack. They are different software with different tools, and only the quantisation toolkit is
> shared.

---

## 2. The whole stack, one picture

The datacenter path, top to bottom:

```
╔══════════════════════════════════════════════════════════════════════╗
║  LAYER 7 — YOUR APPLICATION / SERVICE                                ║
╠══════════════════════════════════════════════════════════════════════╣
║  LAYER 6 — SERVING ENGINES                                           ║
║  vLLM · SGLang · ATOM · Hugging Face TGI                             ║
╠══════════════════════════════════════════════════════════════════════╣
║  LAYER 5 — FRAMEWORKS                                                ║
║  PyTorch (ROCm build) · JAX · TensorFlow · ONNX Runtime              ║
╠══════════════════════════════════════════════════════════════════════╣
║  LAYER 4 — AI KERNEL LAYER            ★ the part people miss          ║
║  AITER  (attention, MoE, GEMM, RMSNorm, RoPE, collectives)           ║
║  backed by: Triton · Composable Kernel · hand-tuned assembly · HIP   ║
╠══════════════════════════════════════════════════════════════════════╣
║  LAYER 3 — MATH & COMMS LIBRARIES                                    ║
║  rocBLAS · hipBLASLt · MIOpen · RCCL · Composable Kernel             ║
║  rocFFT · rocRAND · rocSOLVER · rocSPARSE · MIGraphX                 ║
╠══════════════════════════════════════════════════════════════════════╣
║  LAYER 2 — LANGUAGE, COMPILER, RUNTIME                               ║
║  HIP (C++ dialect) · HIPIFY · LLVM/hipcc · ROCr runtime              ║
╠══════════════════════════════════════════════════════════════════════╣
║  LAYER 1 — KERNEL DRIVER                                             ║
║  amdgpu (Linux kernel driver) · KFD                                  ║
╠══════════════════════════════════════════════════════════════════════╣
║  LAYER 0 — SILICON                                                   ║
║  CDNA GPU: XCDs → Compute Units → Matrix Cores · LDS · Infinity      ║
║            Cache · HBM · Infinity Fabric                             ║
╚══════════════════════════════════════════════════════════════════════╝
```

The client path is much shorter:

```
╔══════════════════════════════════════════════════════════════════════╗
║  Your app  ·  Lemonade Server  ·  GAIA                               ║
╠══════════════════════════════════════════════════════════════════════╣
║  Lemonade SDK (Python API)                                           ║
╠══════════════════════════════════════════════════════════════════════╣
║  OnnxRuntime GenAI (OGA)   or   llama.cpp  (iGPU only)               ║
╠══════════════════════════════════════════════════════════════════════╣
║  ONNX Runtime  +  Vitis AI Execution Provider                        ║
╠══════════════════════════════════════════════════════════════════════╣
║  Ryzen AI driver                                                     ║
╠══════════════════════════════════════════════════════════════════════╣
║  XDNA NPU (AIE tile array)  ·  Radeon iGPU  ·  Zen CPU               ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 3. Name decoder — read this before anything else

| Name | What it is | Notes |
|---|---|---|
| **ROCm** | The whole open datacenter/GPU software platform | The umbrella |
| **HIP** | AMD's C++ dialect for GPU kernels | Deliberately CUDA-shaped |
| **HIPIFY** | Tool that translates CUDA source into HIP | Mechanical for most code |
| **CDNA** | Datacenter GPU architecture | MI-series Instinct |
| **RDNA** | Client/gaming GPU architecture | Radeon |
| **XDNA** | NPU architecture in Ryzen AI chips | From the Xilinx acquisition |
| **AIE** | AI Engine — the tile inside XDNA | Xilinx lineage |
| **Matrix Cores** | The matrix-multiply hardware in CDNA CUs | ≈ NVIDIA Tensor Cores |
| **MFMA** | Matrix Fused Multiply-Add — the instruction family | What Matrix Cores execute |
| **XCD** | Accelerator Complex Die — a chiplet of CUs | MI300+ are multi-die |
| **IOD** | I/O Die — hosts memory controllers, cache, fabric | |
| **LDS** | Local Data Share — fast per-CU scratchpad | ≈ CUDA shared memory |
| **AITER** | AMD's AI operator/kernel library | ★ the modern AI fast path |
| **CK** | Composable Kernel — templated kernel building blocks | ≈ CUTLASS |
| **Quark** | AMD's quantisation toolkit | **Replaced the Vitis AI Quantizer** |
| **OGA** | OnnxRuntime GenAI | The client LLM runtime |
| **gfx942 / gfx950** | LLVM compiler targets | gfx942 = CDNA3, gfx950 = CDNA4 |

**Deprecated or superseded — do not learn these first:**

| Old | Replaced by |
|---|---|
| `rocprof`, `rocprofv2`, ROCProfiler, ROCTracer | **`rocprofv3`** / ROCprofiler-SDK |
| Omniperf | **ROCm Compute Profiler** (`rocprofiler-compute`) |
| Omnitrace | **ROCm Systems Profiler** (`rocprofiler-systems`) |
| `rocm-smi` | **`amd-smi`** |
| Vitis AI Quantizer | **AMD Quark** |

> AMD documentation states the legacy profilers are anticipated to reach end of support by the end
> of 2026 Q2. If a tutorial tells you to run `rocprof`, it is out of date.

---

## 4. Three hardware families, one software stack

```
                    ┌──────────── AMD AI SILICON ────────────┐
                    │                                        │
      ┌─────────────┴──────────┐  ┌──────────┐  ┌────────────┴──────────┐
      │  CDNA — Instinct       │  │  RDNA    │  │  XDNA — Ryzen AI NPU  │
      │  datacenter GPU        │  │  Radeon  │  │  laptop NPU           │
      │                        │  │  client  │  │                       │
      │  MI210/250  (gfx90a)   │  │  GPU     │  │  XDNA 1  ~10-16 TOPS  │
      │  MI300X/325 (gfx942)   │  │          │  │  XDNA 2  ~50-55 TOPS  │
      │  MI350X/355 (gfx950)   │  │          │  │                       │
      │                        │  │          │  │                       │
      │  train + infer         │  │  infer + │  │  infer only,          │
      │  HBM, 100s of GB       │  │  some    │  │  low power            │
      │                        │  │  train   │  │                       │
      └────────────┬───────────┘  └────┬─────┘  └───────────┬───────────┘
                   │                   │                    │
                 ROCm                ROCm            Ryzen AI Software
```

---

## 5. Inside a CDNA datacenter GPU

### The chiplet structure

A modern Instinct part is **not one piece of silicon**:

```
   ┌─────────────────────────────────────────────────────────────┐
   │                    ONE MI350X PACKAGE                       │
   │                                                             │
   │   ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐  ← XCDs stacked   │
   │   │  XCD  │ │  XCD  │ │  XCD  │ │  XCD  │    on top         │
   │   │ 32 CU │ │ 32 CU │ │ 32 CU │ │ 32 CU │    (N3P process)  │
   │   │ 4MB L2│ │ 4MB L2│ │ 4MB L2│ │ 4MB L2│                   │
   │   └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘                   │
   │   ┌───┴─────────┴─────────┴─────────┴───┐                   │
   │   │   I/O DIE  (N6)                     │  ← 2 IODs total   │
   │   │   HBM controllers · 256MB Infinity  │    on MI350       │
   │   │   Cache · Infinity Fabric · PCIe    │    (was 4 on      │
   │   └──────────────┬──────────────────────┘     MI300)        │
   │                  │                                          │
   │   [HBM3E] [HBM3E] [HBM3E] [HBM3E]   288 GB @ 8.0 TB/s       │
   └─────────────────────────────────────────────────────────────┘
```

### The generation table — from AMD's own documentation

| Feature | MI300X | MI325X | MI350X | MI355X |
|---|---|---|---|---|
| Architecture | CDNA3 | CDNA3 | **CDNA4** | **CDNA4** |
| **LLVM target** | `gfx942` | `gfx942` | `gfx950` | `gfx950` |
| Process (XCD / IOD) | N5 / N6 | N5 / N6 | N3P / N6 | N3P / N6 |
| I/O dies | 4 | 4 | **2** | **2** |
| XCDs | 8 | 8 | 8 | 8 |
| CUs per XCD (total/active) | 40 / 38 | 40 / 38 | 36 / 32 | 36 / 32 |
| **Total active CUs** | 304 | 304 | **256** | **256** |
| Stream processors | 19,456 | 19,456 | 16,384 | 16,384 |
| Matrix Cores | 1,216 | 1,216 | 1,024 | 1,024 |
| Max engine clock | 2,100 MHz | 2,100 MHz | 2,200 MHz | 2,400 MHz |
| **LDS per CU** | 64 KB | 64 KB | **160 KB** | **160 KB** |
| L1 data cache | 32 KB | 32 KB | 32 KB | 32 KB |
| L2 per XCD | 4 MB | 4 MB | 4 MB | 4 MB |
| Infinity Cache | 256 MB | 256 MB | 256 MB | 256 MB |
| Transistors | 153 B | 153 B | 185 B | 185 B |
| Max power | 750 W | 1000 W | 1000 W | 1400 W |
| **Memory** | 192 GB HBM3 | 256 GB HBM3E | **288 GB HBM3E** | **288 GB HBM3E** |
| **Bandwidth** | 5.3 TB/s | 6.0 TB/s | **8.0 TB/s** | **8.0 TB/s** |
| Infinity Fabric link | 32 Gbps | 32 Gbps | 38.4 Gbps | 38.4 Gbps |
| P2P ring aggregate | 896 GB/s | 896 GB/s | 1,075.2 GB/s | 1,075.2 GB/s |

### What actually changed in CDNA 4 — and why it's interesting

**Fewer CUs, more throughput.** 256 CUs versus 304 — a *reduction* — but per-CU Matrix Core
throughput for ≤16-bit types **doubled**. AMD chose performance per unit over unit count.

**Native low precision.** MXFP8 / MXFP6 / MXFP4 are supported in hardware, via scaled-MFMA with an
E8M0 scale over 32-element blocks.

**LDS grew 2.5×** — 64 KB → 160 KB per CU. That is a big deal for tiling strategy: more of your
working set stays on-chip.

**Fewer, better-connected dies.** 4 IODs → 2, directly connected. Fewer die crossings, and the
freed area widened the fabric — which is how HBM read bandwidth went 5.3 → 8.0 TB/s.

**Two porting traps:**
- MI350 uses **OCP FP8** variants; MI300 used **FNUZ**. FP8 code is not automatically portable
  between them.
- **TF32 moved from hardware to software emulation via BF16** on MI350. If you relied on hardware
  TF32, re-check your assumptions.

### The memory hierarchy you must reason about

```
   registers          fastest, per-thread
        ↓
   LDS (160 KB/CU)    software-managed scratchpad  ← you control this
        ↓
   L1 (32 KB)         per-CU
        ↓
   L2 (4 MB/XCD)      per-chiplet
        ↓
   Infinity Cache     256 MB, package-wide
        ↓
   HBM3E              288 GB @ 8.0 TB/s
        ↓
   Infinity Fabric    to other GPUs
```

> **A single logical GPU with non-uniform internal behaviour.** Because MI300+ are multi-die, memory
> access cost is not flat across the package. Partitioning modes (per-IOD, per-XCD) exist precisely
> to let you exploit that. This surprises people coming from monolithic GPUs.

---

## 6. Inside the XDNA client NPU

Completely different silicon philosophy: a **spatial dataflow array**, not a SIMT machine.

```
        XDNA 2  —  a 4 x 8 array of AI Engine tiles
        ══════════════════════════════════════════

   col:   0     1     2     3     4     5     6     7
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐
  row 3 │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│  compute tiles
        ├───┤ ├───┤ ├───┤ ├───┤ ├───┤ ├───┤ ├───┤ ├───┤  64 KB L1 each
  row 2 │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│
        ├───┤ ├───┤ ├───┤ ├───┤ ├───┤ ├───┤ ├───┤ ├───┤  32 compute
  row 1 │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│  cores total
        ├───┤ ├───┤ ├───┤ ├───┤ ├───┤ ├───┤ ├───┤ ├───┤
  row 0 │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│ │AIE│
        └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘
        ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐
        │MEM│ │MEM│ │MEM│ │MEM│ │MEM│ │MEM│ │MEM│ │MEM│  memory tiles
        │512│ │512│ │512│ │512│ │512│ │512│ │512│ │512│  512 KB L2,
        │ KB│ │ KB│ │ KB│ │ KB│ │ KB│ │ KB│ │ KB│ │ KB│  one per column
        └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘
        ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐
        │SHM│ │SHM│ │SHM│ │SHM│ │SHM│ │SHM│ │SHM│ │SHM│  shim tiles
        └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘  → host DDR
          └─────┴─────┴─────┴──┬──┴─────┴─────┴─────┘
                          host DDR (shared with the whole system)
```

| Generation | Array | Compute tiles | Peak | Found in |
|---|---|---|---|---|
| **XDNA 1** | 5 col × 4 row | 20 | ~10 TOPS | Ryzen 7040 "Phoenix" |
| XDNA 1 refresh | 5 × 4 | 20 | ~16 TOPS | Ryzen 8040 "Hawk Point" |
| **XDNA 2** | **8 col × 4 row** | **32** | **~50–55 TOPS** | Ryzen AI 300 / 400 series |

**Three-level memory hierarchy, all software-managed:** 64 KB L1 per compute tile → 512 KB memory
tile (L2) per column, shared by its four compute tiles → shim tiles connecting to host DDR. Tiles
talk over streaming interconnects and cascade connections.

**Data types:** int8, int16, bf16, and block-FP16.

**How it differs from a GPU, in one line:** a GPU hides latency by oversubscribing threads; a spatial
array hides it by **explicitly scheduling data movement**. The compiler decides tile placement, DMA
timing and fusion. There is no scheduler bailing you out.

**Low-level programming** (rarely needed, but this is what's underneath): **IRON** exposes compute
tiles, memory tiles, shim tiles, ObjectFifos and DMA tasks; **MLIR-AIE** and **MLIR-AIR** are the
compiler layers; **llvm-aie** ("Peano") is the backend.

> **Caveat.** Community investigation reports XDNA 2's actual LLVM target is `aie2p`, which differs
> slightly from the documented AIE-MLv2 (for example, 5 accumulator registers rather than 8), and
> notes that low-level XDNA documentation is thinner than Xilinx's older AIE documentation. Treat
> tile-level details as approximate.

---

## 7. ROCm, layer by layer

ROCm is **open source**, which is genuinely its biggest differentiator — you can read every layer.

```
  ┌──────────────────────────────────────────────────────────────┐
  │  APPLICATION                                                 │
  ├──────────────────────────────────────────────────────────────┤
  │  FRAMEWORKS      PyTorch · JAX · TensorFlow · ONNX Runtime   │
  ├──────────────────────────────────────────────────────────────┤
  │  AI KERNELS      AITER                                       │
  ├──────────────────────────────────────────────────────────────┤
  │  MATH LIBS       rocBLAS  hipBLAS  hipBLASLt  MIOpen         │
  │                  rocFFT  rocRAND  rocSOLVER  rocSPARSE       │
  │                  rocPRIM  rocThrust  hipCUB  rocWMMA  CK     │
  ├──────────────────────────────────────────────────────────────┤
  │  COMMS           RCCL  ·  rocSHMEM                           │
  ├──────────────────────────────────────────────────────────────┤
  │  GRAPH/INFER     MIGraphX  (includes rocMLIR)                │
  ├──────────────────────────────────────────────────────────────┤
  │  LANGUAGE        HIP  ·  HIPIFY  ·  OpenMP                   │
  ├──────────────────────────────────────────────────────────────┤
  │  COMPILER        LLVM (hipcc, flang)                         │
  ├──────────────────────────────────────────────────────────────┤
  │  RUNTIME         ROCr Runtime (HSA)                          │
  ├──────────────────────────────────────────────────────────────┤
  │  DRIVER          amdgpu (in the Linux kernel) · KFD          │
  └──────────────────────────────────────────────────────────────┘
```

**Media and vision, often forgotten:** rocDecode (video decode), rocJPEG, rocAL (augmentation),
MIVisionX, ROCm Performance Primitives (RPP). Data loading is frequently the real bottleneck, so
these matter more than their profile suggests.

**Packaging note.** AMD has been regrouping ROCm packages (the "TheRock" transition): `amdrocm-blas`,
`amdrocm-dnn`, `amdrocm-profiler` and so on. Notably, **rocMLIR is now inside MIGraphX** and
**HIPCC is now inside `amdrocm-llvm`**. If a package name from an old guide doesn't resolve, this is
why.

---

## 8. HIP — and porting from CUDA

**HIP is deliberately CUDA-shaped.** That is the entire strategy: make porting mechanical.

```
   CUDA                          HIP
   ────                          ───
   cudaMalloc()          →       hipMalloc()
   cudaMemcpy()          →       hipMemcpy()
   __global__            →       __global__        (same)
   threadIdx.x           →       threadIdx.x       (same)
   kernel<<<g,b>>>()     →       hipLaunchKernelGGL()  or  kernel<<<g,b>>>()
   cuBLAS                →       rocBLAS / hipBLAS
   cuDNN                 →       MIOpen
   NCCL                  →       RCCL
   CUTLASS               →       Composable Kernel
   nvcc                  →       hipcc
   nvidia-smi            →       amd-smi
```

`hipify-perl` and `hipify-clang` do the translation automatically.

### What HIPIFY cannot fix — the interesting part

This list is what an interview will probe, and what actually costs you days:

| Hazard | Why |
|---|---|
| **Wavefront size** | CDNA uses **64**; NVIDIA warps are **32**. Any hard-coded 32, any warp-level primitive, any occupancy calculation must be revisited |
| Warp-level intrinsics | Shuffles and votes have different semantics at width 64 |
| Inline PTX assembly | No equivalent — must be rewritten |
| Vendor-specific library calls | Some have no direct counterpart |
| Tuned launch configurations | Block sizes and LDS budgets tuned for one architecture are wrong for the other |
| FP8 variants | OCP versus FNUZ differ between MI300 and MI350 |

> **Wavefront 64 versus warp 32 is the single most common porting bug.** It compiles fine and gives
> wrong answers or terrible performance.

---

## 9. The library layer

| Library | Purpose | NVIDIA analogue |
|---|---|---|
| **rocBLAS** | Dense linear algebra (GEMM) | cuBLAS |
| **hipBLAS** | Portable BLAS wrapper — dispatches to rocBLAS *or* cuBLAS | — |
| **hipBLASLt** | Extended GEMM with a flexible API, epilogue fusion | cuBLASLt |
| **MIOpen** | Deep-learning primitives (convolution etc.) | cuDNN |
| **RCCL** | Collective communication — all-reduce, all-gather | NCCL |
| **Composable Kernel (CK)** | Templated, tunable kernel building blocks | CUTLASS |
| **MIGraphX** | Graph inference engine | TensorRT (loosely) |
| **rocWMMA** | Matrix-core programming from C++ | WMMA / `mma` |
| **rocPRIM / hipCUB / rocThrust** | Parallel primitives | CUB / Thrust |
| **rocFFT / rocRAND / rocSOLVER / rocSPARSE** | FFT, RNG, solvers, sparse | cuFFT / cuRAND / cuSOLVER / cuSPARSE |

**`hipBLAS` versus `hipBLASLt` — a real performance lever.** PyTorch chooses a BLAS library by
heuristic. Setting `TORCH_BLAS_PREFER_HIPBLASLT=1` forces hipBLASLt, which AMD documents as improving
linear-layer performance in some workloads. Worth measuring on your model.

**Why Composable Kernel exists.** The tuning space for a GEMM — tile sizes, layouts, pipelining,
scheduling — is far too large to hand-explore. CK is a template library that generates and tunes
candidates. It is one of AITER's backends.

---

## 10. AITER — the AI kernel layer

**This is the layer most people miss, and it is where modern AMD inference performance actually
comes from.**

**AITER** (AI Tensor Engine for ROCm) is AMD's AI operator library — production-ready kernels that
framework developers plug straight into their stacks. AMD describes it as **the default kernel
backend for LLM inference on AMD GPUs**.

```
        ┌───────────────────────────────────────────────────┐
        │                    AITER                          │
        │   C++ API    ·    Python API                      │
        ├───────────────────────────────────────────────────┤
        │  OPERATORS                                        │
        │   MHA (flash attention)   ·  MLA (DeepSeek-style) │
        │   Paged Attention         ·  Fused MoE            │
        │   GEMM (incl. block-scale)·  RMSNorm / LayerNorm  │
        │   RoPE (+ fused KV cache) ·  Quantisation         │
        │   All-reduce / collectives                        │
        ├───────────────────────────────────────────────────┤
        │  BACKENDS  (chosen per operator)                  │
        │   Triton  │  Composable Kernel  │  hand-tuned ASM │
        │           │                     │  HIP           │
        └───────────────────────────────────────────────────┘
```

**Architecture support:**

| Architecture | Target | GPUs |
|---|---|---|
| CDNA 2 | `gfx90a` | MI210, MI250, MI250X |
| CDNA 3 | `gfx942` | MI300A, MI300X |
| CDNA 4 | `gfx950` | MI350X |

**Framework integrations:**

| Framework | Status | Role |
|---|---|---|
| **vLLM** | Production | Default attention backend on ROCm |
| **SGLang** | Production | Default in the ROCm Docker image |
| **ATOM** | Active development | Built natively on AITER |
| **JAX** | Experimental | Via an XLA FFI bridge, no PyTorch dependency |

**Sample API:**

```python
import aiter

aiter.flash_attn_func(...)             # MHA
aiter.rms_norm(...)                    # RMSNorm
aiter.rope_fwd(...)                    # RoPE forward
aiter.layernorm2d_with_add_asm(...)    # fused LayerNorm + residual
aiter.ops.triton.mla_decode(...)       # MLA decode (Triton path)
```

AITER uses a `@compile_ops` decorator for JIT kernel loading, and ships **Opus**, a single-header
C++ template library with layout abstractions and MFMA support.

> **The lesson in AITER's existence.** A vendor's *general* math libraries (rocBLAS, MIOpen) are not
> enough for modern LLM inference. Fused attention, fused MoE and block-scale GEMM need dedicated,
> hand-tuned kernels. **AMD's answer is a separate AI-specific kernel library sitting above the
> classical ones** — and knowing that this layer exists is the difference between getting default
> performance and good performance.

---

## 11. Frameworks: PyTorch, JAX, Triton

**PyTorch** — ROCm builds are official. The critical thing to internalise:

> **`torch.cuda` is the API on ROCm builds too.** `torch.cuda.is_available()` returning `True` on an
> AMD system is **correct behaviour, not a bug.** AMD kept the namespace deliberately so PyTorch code
> ports unchanged. It confuses every newcomer exactly once.

**Triton** — OpenAI's Python kernel language compiles for AMD backends. This matters enormously for
your learning path: **the same Triton kernel you write for NVIDIA runs on AMD.** It is also one of
AITER's backends, and TorchInductor's GPU codegen target.

**JAX** — supported; AITER has an experimental XLA FFI bridge.

**ONNX Runtime** — ROCm and MIGraphX execution providers.

---

## 12. Serving: vLLM and SGLang

vLLM on ROCm has **multiple attention backends**, and picking correctly is worth several-fold
throughput. From the vLLM project's own documentation:

| Category | Backend | Notes |
|---|---|---|
| MHA | `TRITON_ATTN` | Baseline; works on Radeon |
| MHA | `ROCM_ATTN` | Custom HIP paged-attention decode; Radeon support |
| MHA | `ROCM_AITER_UNIFIED_ATTN` | Single-kernel AITER path |
| MHA | **`ROCM_AITER_FA`** | **Recommended**; auto-selected with AITER |
| MLA | `TRITON_MLA` | Baseline; Radeon support |
| MLA | **`ROCM_AITER_MLA`** | **Recommended**; auto-selected with AITER |
| MLA | `ROCM_AITER_TRITON_MLA` | Alternative AITER MLA path |

The AITER MLA backends share a hand-tuned **assembly** decode kernel (`mla_decode_fwd`), which the
vLLM project identifies as the source of most of the gain — they report **1.2–4.4× higher
throughput** from the AITER paths.

**The environment-variable trap:**

```bash
export VLLM_ROCM_USE_AITER=1          # REQUIRED — enables AITER for GEMM, RMSNorm, MoE
export HIP_FORCE_DEV_KERNARG=1        # faster kernel launch
export SAFETENSORS_FAST_GPU=1         # faster model load
export TORCH_BLAS_PREFER_HIPBLASLT=1  # prefer hipBLASLt for GEMM
```

> **`--attention-backend` alone is not enough.** It overrides only the attention kernel. You still
> need `VLLM_ROCM_USE_AITER=1` to get AITER's GEMM, RMSNorm and MoE kernels. AMD's docs call this out
> explicitly, which tells you how often people get it wrong.

For MXFP4 models on MI350X/MI355X there is `VLLM_ROCM_USE_AITER_FP4_ASM_GEMM=1`, which swaps Triton
for hand-tuned assembly FP4 GEMM — faster at small batch sizes (M ≤ 64), paired with
`--quantization quark`.

---

## 13. The client stack: Ryzen AI

Entirely separate software from ROCm.

```
  PyTorch / TensorFlow model
          │
          ▼  export
     ONNX model
          │
          ▼  AMD Quark  (quantise: INT8, or FP32 → internal BF16)
     quantised ONNX
          │
          ▼  ONNX Runtime + VitisAIExecutionProvider
     ┌────────────────────────────────────────┐
     │  The EP decides which parts of the     │
     │  model run on the NPU                  │  ← graph partitioning
     └────────────────────────────────────────┘
          │
          ├──► XDNA NPU   (low power, quantised)
          ├──► Radeon iGPU
          └──► Zen CPU    (fallback)
```

**Deployment in code:**

```python
session = onnxruntime.InferenceSession(
    model,
    providers=['VitisAIExecutionProvider'],
    provider_options=[vai_ep_options])
```

### The LLM path on client

AMD's client LLM stack is layered — all three entry points sit on the same base:

```
  ┌─────────────────┬──────────────────────┬────────────────────┐
  │ Python app      │  Your LLM stack      │  Native app        │
  ├─────────────────┼──────────────────────┼────────────────────┤
  │ Lemonade        │  Lemonade Server     │  OGA C++ headers   │
  │ Python API      │  Interface           │  OR llama.cpp      │
  ├─────────────────┴──────────────────────┴────────────────────┤
  │  OnnxRuntime GenAI (OGA)   OR   llama.cpp (iGPU only)       │
  ├─────────────────────────────────────────────────────────────┤
  │  AMD Ryzen AI driver and hardware                           │
  └─────────────────────────────────────────────────────────────┘
```

**The supporting cast:**

| Tool | What it does |
|---|---|
| **Lemonade SDK** | Multi-vendor open source; the quickest route to LLMs on OGA or llama.cpp |
| **GAIA** | Open-source demo: multi-agent RAG running local LLMs across CPU, GPU and NPU |
| **TurnkeyML** | No-code CLIs and low-code APIs for ONNX export and optimisation |
| **AI Analyzer** | Model analysis, profiling and visualisation for models on the NPU |
| **`xrt-smi`** | Platform and NPU inspection/management — the client equivalent of `amd-smi` |

Windows integration: AMD NPU acceleration is exposed through the **Windows ML** runtime on
Copilot+ PCs.

---

## 14. Quantisation: AMD Quark

**Quark is the one tool that spans both halves of the stack** — datacenter and client.

- Cross-platform toolkit supporting **PyTorch and ONNX** models
- On client: produces INT8 models for the Vitis AI EP. **It replaced the Vitis AI Quantizer**, which
  is deprecated
- On datacenter: `--quantization quark` is how vLLM consumes MXFP4 models on MI350X/MI355X

```
                    ┌──────────────┐
                    │  AMD Quark   │
                    └──────┬───────┘
             ┌─────────────┴─────────────┐
             ▼                           ▼
     CLIENT (Ryzen AI)            DATACENTER (Instinct)
     INT8 for XDNA NPU            MXFP4 / FP8 for CDNA
     via Vitis AI EP              via vLLM --quantization quark
```

**Note the client precision paths:** you can either quantise to **INT8** explicitly with Quark, or
hand the compiler an **FP32** model and let it convert internally to **BF16**. Two different routes
with different accuracy and effort profiles.

---

## 15. Profiling and tools

**Use the current tools. The old ones are deprecated.**

| Task | Tool | Replaces |
|---|---|---|
| System-wide trace | **ROCm Systems Profiler** (`rocprofiler-systems`) | Omnitrace |
| Kernel-level counters | **ROCm Compute Profiler** (`rocprofiler-compute`) | Omniperf |
| CLI tracing/counters | **`rocprofv3`** / ROCprofiler-SDK | `rocprof`, `rocprofv2` |
| Device management | **`amd-smi`** | `rocm-smi` |
| Debugging | ROCgdb, ROCdbgapi, ROCr Debug Agent | — |
| Bandwidth testing | ROCm Bandwidth Test, TransferBench | — |
| NPU inspection (client) | `xrt-smi` | — |

**`rocprofv3` options worth knowing:**

```bash
rocprofv3 --kernel-trace          -- ./app    # kernel dispatches
rocprofv3 --hip-trace             -- ./app    # HIP API
rocprofv3 --hip-runtime-trace     -- ./app    # runtime API only
rocprofv3 --hip-compiler-trace    -- ./app    # __hip* compiler-generated
rocprofv3 --rccl-trace            -- ./app    # collectives  ← new, very useful
rocprofv3 --kernel-rename         -- ./app    # use roctx region names
```

> **Behaviour change that will confuse you:** run `rocprofv3` with no options and it collects *agent
> information*, not kernel traces. `rocprof` and `rocprofv2` defaulted to kernel traces. You must
> pass `--kernel-trace` explicitly.

**The workflow, in order:**

```
  1. ROCm Systems Profiler    →  where does wall-clock time go?
        ▼                         (often the dataloader, not the GPU)
  2. rocprofv3 --kernel-trace →  which kernels dominate?
        ▼
  3. ROCm Compute Profiler    →  hardware counters for that kernel
        ▼
  4. Roofline                 →  memory-bound or compute-bound?
        ▼
  5. Achieved bandwidth as a % of the device peak  ← the number that means something
```

---

## 16. End-to-end journey — datacenter

Serving an LLM on an MI300X:

```
  1. Model on Hugging Face (PyTorch weights)
        ▼
  2. (optional) Quantise with AMD Quark  →  MXFP4 / FP8
        ▼
  3. Pull the ROCm vLLM Docker image
        ▼
  4. Set the environment
        VLLM_ROCM_USE_AITER=1
        HIP_FORCE_DEV_KERNARG=1
        SAFETENSORS_FAST_GPU=1
        ▼
  5. Launch vLLM
        --tensor-parallel-size 8      (RCCL handles the collectives)
        --attention-backend ROCM_AITER_FA
        ▼
  6. What happens underneath, per token:
        vLLM
          └─► AITER          fused attention, MoE, RMSNorm, RoPE
                └─► CK / Triton / hand-tuned ASM
                      └─► HIP → LLVM → GPU ISA
                            └─► Matrix Cores (MFMA) on 304 CUs
                                  reading HBM3E at up to 5.3 TB/s
        ▼
  7. Profile:  rocprofv3 --kernel-trace  →  ROCm Compute Profiler  →  roofline
```

---

## 17. End-to-end journey — client

Running a vision model on a Ryzen AI laptop:

```
  1. Train in PyTorch
        ▼
  2. Export to ONNX
        ▼
  3. Quantise with AMD Quark  →  INT8
        ▼
  4. ONNX Runtime session with VitisAIExecutionProvider
        ▼
  5. The EP partitions the graph:
        supported subgraphs  →  XDNA NPU
        the rest             →  iGPU or CPU
        ▼
  6. On the NPU:
        shim tiles pull data from host DDR
          └─► memory tiles (512 KB L2 per column)
                └─► compute tiles (64 KB L1) run the kernels
                      └─► results stream back out
        ▼
  7. Inspect with xrt-smi; profile with AI Analyzer
```

> **The same rule as any NPU:** count your partitions first. An unsupported operator in the middle of
> the graph forces a round trip off the accelerator, and partition count usually matters more than
> kernel quality.

---

## 18. If you already know CUDA or the Qualcomm stack

| Function | NVIDIA | **AMD datacenter** | **AMD client** | Qualcomm |
|---|---|---|---|---|
| Kernel language | CUDA | **HIP** | (n/a) | (n/a — QNN API) |
| Matrix hardware | Tensor Cores | **Matrix Cores (MFMA)** | AIE tiles | HMX |
| Vector/SIMD | CUDA cores | **Stream processors** | AIE vector | HVX |
| Fast scratchpad | shared memory | **LDS** | tile L1/L2 | VTCM |
| Warp width | 32 | **64 (wavefront)** | (spatial) | (n/a) |
| Dense linear algebra | cuBLAS | **rocBLAS / hipBLASLt** | — | — |
| DNN primitives | cuDNN | **MIOpen** | — | — |
| Collectives | NCCL | **RCCL** | — | — |
| Kernel templates | CUTLASS | **Composable Kernel** | — | — |
| AI operator library | (various) | **AITER** ★ | — | — |
| Graph inference | TensorRT | **MIGraphX** | Vitis AI EP | QNN HTP backend |
| Quantiser | — | **AMD Quark** | **AMD Quark** | AIMET |
| System profiler | Nsight Systems | **ROCm Systems Profiler** | AI Analyzer | — |
| Kernel profiler | Nsight Compute | **ROCm Compute Profiler** | — | — |
| CLI profiler | `nsys` / `ncu` | **`rocprofv3`** | — | — |
| Device query | `nvidia-smi` | **`amd-smi`** | `xrt-smi` | — |
| Python kernels | Triton | **Triton** (same tool) | — | — |

> **Triton is the bridge.** One kernel language, both vendors. If you are choosing what to learn for
> portability, that is the answer.

---

## 19. The mistakes everyone makes

| # | Mistake | Symptom | Fix |
|---|---|---|---|
| 1 | Assuming warp size 32 | Wrong results or bad performance after porting | CDNA wavefront is **64**. Audit every hard-coded 32 |
| 2 | `torch.cuda` "must be a bug" | Confusion, wasted hours | It is correct on ROCm builds. Deliberate API compatibility |
| 3 | **Not enabling AITER** | Mediocre LLM throughput | `VLLM_ROCM_USE_AITER=1` — and `--attention-backend` alone is *not* enough |
| 4 | Using `rocprof` | Deprecated, missing features | Use `rocprofv3`. EoS anticipated end of 2026 Q2 |
| 5 | FP8 code across generations | Numerical differences | MI300 uses FNUZ, MI350 uses OCP variants |
| 6 | Assuming hardware TF32 | Slower than expected on MI350 | TF32 is software-emulated via BF16 on CDNA4 |
| 7 | Confusing ROCm and Ryzen AI | Tools don't exist | Datacenter = ROCm. Client NPU = Ryzen AI Software |
| 8 | Ignoring the multi-die layout | Unexplained memory variance | MI300+ have non-uniform internal memory behaviour |

---

## 20. Verification status

### From AMD primary documentation

The full MI300X/MI325X/MI350X/MI355X specification table and the CDNA 3 → CDNA 4 change list
(including OCP-vs-FNUZ FP8 and the TF32 software-emulation change) · the ROCm component inventory ·
the profiler deprecations and their replacements, and the anticipated EoS timing · `rocprofv3`
option semantics and its changed default behaviour · ROCm package regrouping · the vLLM-on-ROCm
environment variables and AITER flags · Ryzen AI Software architecture, the Vitis AI EP, Quark
replacing the Vitis AI Quantizer, the OGA/llama.cpp/Lemonade layering, GAIA, TurnkeyML, AI Analyzer
and `xrt-smi`.

### From project documentation (AITER repo, vLLM project)

AITER's operator list, backend mix, architecture support and framework integrations · the vLLM ROCm
attention backend table and the 1.2–4.4× throughput figure (a project measurement, not independently
reproduced here).

### Vendor performance claims — treat as marketing until reproduced

AMD's published DeepSeek V3/R1 figure of 6,484 → 13,704 tok/s with AITER.

### Community or secondary — treat with care

XDNA tile-level internals (the 4×8 array, 64 KB L1, 512 KB memory tiles, shim tiles) come from
academic and community sources, not an AMD architecture manual · the `aie2p` versus AIE-MLv2
distinction, and the observation that low-level XDNA documentation is thin · exact TOPS figures per
Ryzen AI SKU.

### Forward-looking — announced or reported, not shipped

MI400 / MI455X, the `gfx1250` target, N2 process, HBM4 at 432 GB per package, native NVFP4 in the
matrix engine, and UALink/UALoE fabrics. This is reported by industry analysts rather than confirmed
in AMD product documentation, and **should not be relied on**.

---

## Primary sources

- What is ROCm — <https://rocm.docs.amd.com/en/latest/what-is-rocm.html>
- ROCm release notes — <https://rocm.docs.amd.com/en/latest/about/release-notes.html>
- MI300/MI350 workload optimisation (the specification table) —
  <https://rocmdocs.amd.com/en/develop/how-to/rocm-for-ai/inference-optimization/workload.html>
- ROCprofiler-SDK vs legacy tools —
  <https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/conceptual/comparing-with-legacy-tools.html>
- ROCProfiler deprecation notice — <https://rocmdocs.amd.com/projects/rocprofiler/en/latest/>
- ROCm package transition guide — <https://rocm.docs.amd.com/en/latest/about/transition-guide-TheRock.html>
- AITER repository — <https://github.com/ROCm/aiter/>
- AITER documentation — <https://rocm.github.io/aiter/>
- AITER blog — <https://rocm.blogs.amd.com/software-tools-optimization/aiter-ai-tensor-engine/README.html>
- vLLM V1 optimisation on ROCm —
  <https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/optimization/vllm-v1-optimization.html>
- vLLM ROCm attention backends — <https://vllm.ai/blog/2026-02-27-rocm-attention-backend>
- AMD Ryzen AI Software — <https://www.amd.com/en/developer/resources/ryzen-ai-software.html>
- Ryzen AI documentation — <https://ryzenai.docs.amd.com/>
- AMD Quark — <https://quark.docs.amd.com/>

---

*Compiled 2026-09-05. Vendor stacks move quickly — AMD's profiler tooling in particular changed
names recently. Re-verify any specific tool name, flag or version before relying on it.*
