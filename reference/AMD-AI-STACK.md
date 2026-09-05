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
| 4 | Three hardware families, **two** software stacks |
| 5 | Inside a CDNA datacenter GPU |
| 5B | **Inside an RDNA client GPU** |
| 6 | Inside the XDNA client NPU |
| 7 | ROCm, layer by layer |
| 8 | **HIP — and porting from CUDA** |
| 9 | The library layer |
| 10 | **AITER — the AI kernel layer** |
| 11 | Frameworks: PyTorch, JAX, Triton |
| 12 | Serving: vLLM and SGLang |
| 13 | The client stack: Ryzen AI |
| 13B | **Heterogeneous execution — NPU + GPU + CPU together** |
| 14 | Quantisation: AMD Quark |
| 15 | Profiling and tools |
| 16 | End-to-end journey — datacenter |
| 17 | End-to-end journey — client |
| 18 | If you already know CUDA or the Qualcomm stack |
| 18B | **AMD's strategy versus Qualcomm's** |
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

## 4. Three hardware families, two software stacks

```
                    ┌──────────── AMD AI SILICON ────────────┐
                    │                                        │
      ┌─────────────┴──────────┐  ┌──────────────────┐  ┌────────┴──────────┐
      │  CDNA — Instinct       │  │  RDNA — Radeon   │  │  XDNA — Ryzen AI  │
      │  datacenter GPU        │  │  client GPU      │  │  laptop NPU       │
      │                        │  │                  │  │                   │
      │  MI210/250  (gfx90a)   │  │  RDNA 3 (gfx11)  │  │  XDNA 1  ~10-16   │
      │  MI300X/325 (gfx942)   │  │  RDNA 4 (gfx12)  │  │          TOPS     │
      │  MI350X/355 (gfx950)   │  │  iGPUs: gfx1151  │  │  XDNA 2  ~50-55   │
      │                        │  │                  │  │          TOPS     │
      │  MFMA matrix cores     │  │  WMMA matrix     │  │  AIE tile array   │
      │  wavefront 64          │  │  wave32 or 64    │  │                   │
      │  HBM, 100s of GB       │  │  GDDR6, 12-32 GB │  │  shared LPDDR5X   │
      │  train + infer         │  │  infer + some    │  │  infer only,      │
      │                        │  │  train           │  │  low power        │
      └────────────┬───────────┘  └────────┬─────────┘  └─────────┬─────────┘
                   │                       │                      │
                 ROCm                    ROCm            Ryzen AI Software
                   └───────────┬───────────┘                      │
                     same stack, different              ← entirely separate →
                     matrix instructions                  tools and runtime
```

**Read the bottom row carefully — it is the thing people get wrong.** The two GPU families share
ROCm but **not** their matrix instructions (MFMA versus WMMA, §5B). The NPU shares neither: it has
its own tools and runtime (§13), and only **Quark** crosses the divide.

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

## 5B. Inside an RDNA client GPU

RDNA is the **gaming and client** GPU line — Radeon RX, and the integrated GPUs inside Ryzen chips.
It is easy to dismiss as "the gaming one," and that is a mistake: RDNA 3 and RDNA 4 have real matrix
hardware, and on a Ryzen AI laptop the **iGPU is an RDNA GPU sitting next to the XDNA NPU**.

### CDNA versus RDNA — two different design goals

| | **CDNA** (Instinct) | **RDNA** (Radeon) |
|---|---|---|
| Built for | HPC + AI training and inference | Graphics, with AI added |
| **Matrix instruction** | **`MFMA`** | **`WMMA`** |
| AMD's name for the unit | Matrix Cores | "AI Accelerators" — but see the naming note below |
| Wave size | **64** (wavefront) | **32 or 64** (wave32 is typical) |
| Memory | HBM, 100s of GB | GDDR6, 12–32 GB |
| Graphics pipeline | stripped out | full raster + ray tracing |
| FP64 | strong | weak |

> **The instruction families differ.** CDNA uses **MFMA**; RDNA uses **WMMA**. Kernels hand-tuned for
> one do not automatically run well — or at all — on the other. This is the single biggest surprise
> for people who assume "an AMD GPU is an AMD GPU."

### WMMA — Wave Matrix Multiply Accumulate

WMMA performs a matrix multiply **cooperatively across a whole wave** (32 threads in wave32, 64 in
wave64), sharing operand data across lanes instead of per-thread work. That reduces register
pressure and memory traffic.

Three ways to reach it:

```
  1. Compiler intrinsics      __builtin_amdgcn_wmma_f32_16x16x16_f16_w32_gfx12
  2. Inline assembly          (rarely worth it)
  3. rocWMMA                  ← the portable option
```

**`rocWMMA` is the one to know.** AMD documents it as portable with `nvcuda::wmma`, and it supports
**both MFMA and WMMA** — so one source can target CDNA and RDNA.

### Generational throughput — from AMD's GPUOpen documentation

FLOPS per clock per CU:

| Type | RDNA 2 (RX 6950 XT) | RDNA 3 (RX 7900 XTX) | RDNA 4 (RX 9070 XT) |
|---|---|---|---|
| FP16 | 256 | 512 | **1024** |
| BF16 | N/A | 512 | **1024** |
| INT8 | 512 | 512 | **2048** |
| **FP8 / BF8** | N/A | N/A | **2048** |

### What RDNA 4 changed, and why it matters for AI

> **A naming conflict inside AMD's own documentation.** The AMD RDNA product page calls RDNA 4's
> matrix hardware **"2nd Generation AI Accelerators"** (counting RDNA 3 as the 1st). The GPUOpen
> article on the same hardware calls them **"3rd-generation Matrix Cores"** (apparently counting
> RDNA 2 as the 1st, which is consistent with RDNA 2 already doing 256 FP16 and 512 INT8 per clock
> per CU). Both are AMD sources. **Cite the throughput numbers, not the generation label** — the
> label is ambiguous.

The changes themselves:

- **Doubled FP16/BF16** and **quadrupled INT8** matrix throughput per CU versus RDNA 3
- **New FP8 and BF8 formats** — 4× the RDNA 3 16-bit float WMMA rate
- **Hardware 4:2 structured sparsity** — doubles dense WMMA throughput when a model actually exploits
  it. AMD's headline "up to 8× versus previous generation" combines the INT gain with sparsity
- **Simplified register layout.** This one is subtle but important: on RDNA 3, chaining WMMA
  operations (as an MLP does) required **shuffling data between lanes** to convert a D matrix into
  the next B matrix. **RDNA 4 removes that requirement**, needs half the registers, and enables 2×
  larger tiling
- **New intrinsics with a `_gfx12` postfix** — and they are **not backward compatible** with RDNA 3

> **The porting trap within the porting trap.** RDNA 3 → RDNA 4 WMMA is a **source change**, not a
> recompile. The VGPR layout changed, so you must use the new `_gfx12` intrinsics.

### Client GPU reference points

*(Specifications below are from a community reference table, not AMD documentation — treat as
indicative.)*

| | RX 9070 XT | RX 9070 | Radeon AI PRO R9700 |
|---|---|---|---|
| Compute Units | 64 | 56 | 64 |
| Stream processors | 4,096 | 3,584 | 4,096 |
| AI Accelerators (WMMA) | 128 | 112 | 128 |
| Wave size | 32 or 64 | 32 or 64 | 32 or 64 |
| **VRAM** | 16 GB GDDR6 | 16 GB GDDR6 | **32 GB GDDR6** |
| Bandwidth | 640 GB/s | 640 GB/s | 640 GB/s |
| Infinity Cache | 64 MB | 64 MB | 64 MB |
| Board power | 304 W | 220 W | 300 W |

**Why the Radeon AI PRO R9700 matters to you:** 32 GB on a client card is the cheapest legitimate
route to running mid-size models locally with ROCm. Note the memory-bandwidth reality though —
640 GB/s against an MI355X's 8.0 TB/s is more than a 12× gap. For memory-bound decode, that gap
*is* the performance difference.

### ROCm on Radeon

ROCm supports Radeon, but **support is narrower than for Instinct** and varies by exact part. Check
the current compatibility list against your specific GPU before buying anything. In the vLLM
attention-backend table (§12), note which backends are marked "Radeon support" — not all of them
are, and the AITER paths generally target Instinct.

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

## 13B. Heterogeneous execution — using the NPU, GPU and CPU together

This is the part almost every tutorial skips, and it is where the real engineering lives. A Ryzen AI
laptop has **three compute engines sharing one memory pool**: Zen CPU cores, an RDNA integrated GPU,
and an XDNA NPU. The interesting question is not "how do I use the NPU?" It is **"which engine
should run which part of my model, and when?"**

### Why the question exists: prefill and decode are different workloads

An LLM has two phases with opposite characteristics:

| | **Prefill** (process the prompt) | **Decode** (generate each token) |
|---|---|---|
| Shape of the maths | large **GEMM** — matrix × matrix | thin **GEMV** — matrix × vector |
| Parallelism | all prompt tokens at once, huge | one token at a time, tiny |
| Bottleneck | **compute-bound** | **memory-bandwidth-bound** |
| What you feel | time-to-first-token (**TTFT**) | tokens per second (**TPS**) |

A decode step reads the *entire* weight matrix to produce *one* token. Arithmetic per byte loaded is
terrible, so it is bandwidth-limited — adding matrix throughput barely helps. Prefill is the
opposite. **One engine is rarely best at both.** That is the whole reason hybrid execution exists.

### AMD's four documented execution modes

From AMD's Ryzen AI documentation:

| Mode | Framework | Compute allocation | Primary use case |
|---|---|---|---|
| **NPU-only** | OGA | NPU exclusive | Maximum NPU use **while keeping the iGPU free** for other work |
| **Hybrid** | OGA | **Dynamic NPU + iGPU partitioning** | Interactive inference — best prefill *and* decode |
| **GPU** | llama.cpp | dedicated GPU | High-throughput inference on integrated or discrete GPU |
| **CPU** | OGA or llama.cpp | CPU | Baseline compatibility everywhere |

**Hybrid mode is the headline feature:** AMD describes it as using both NPU and iGPU "to achieve the
best TTFT and TPS during the prefill and decode phases" — that is, it maps each phase to the engine
that suits it, dynamically.

### The hardware support cliff — check this first

| Processor series | NPU-only | Hybrid | GPU / CPU |
|---|---|---|---|
| **Ryzen AI 300** (Strix, Krackan Point) | yes | yes | yes |
| **Ryzen AI 7000 / 8000** | **no** | **no** | yes |

AMD states plainly that the OGA flow supports **Strix and Krackan Point**, and that **Phoenix (PHX)
and Hawk Point (HPT) are not supported**. So a "Ryzen AI 7000" laptop has an NPU you cannot reach
through this path at all. Verify your exact silicon before designing around hybrid mode.

### NPU-only has two flavours

If you choose NPU-only, AMD offers two model builds with a real trade-off:

| Build | Optimised for | Context |
|---|---|---|
| **Token Fusion** | long-context workloads | up to **16K tokens** (input + output), no extra configuration |
| **Full Fusion** | best throughput on shorter sequences | shorter |

For **hybrid** models the limit is per-model: input + output must not exceed the `context_length`
field in `genai_config.json`. Read that file — do not assume.

AMD ships pre-optimised builds for common architectures (Llama-2/3, Mistral, DeepSeek-R1 distills,
Qwen-2/2.5/3, Gemma-2, Phi-3/3.5/4) against **OGA version 0.14.0**.

### The other reason to use the NPU: it barely disturbs the GPU

Here is the insight that reframes the NPU. It is not only "the low-power engine" — it is a
**separate execution lane that does not compete for the same resources**.

Independent community measurement on a Strix Halo system (Ryzen AI MAX+ 395, Radeon 8060S iGPU,
128 GB LPDDR5X) ran an auxiliary model alongside a main iGPU workload at 64K context:

| Auxiliary model placed on… | Added latency to the main iGPU workload |
|---|---|
| **the NPU** | **+3.3%** |
| another iGPU process | **+69.0%** |

Same auxiliary work, 20× difference in interference. The explanation is bandwidth accounting: a
1.7–8B model reads roughly 2 GB per token, while a 30B Q4 model reads about 17 GB. The small model
on the NPU consumes a few percent of the memory bus; the same model on the iGPU fights the big one
for both compute *and* bandwidth. Reported combined throughput was ~1.7–1.9× versus serving the
two workloads sequentially.

> **The design pattern:** put always-on background work — classification, routing, RAG embedding,
> draft generation for speculative decoding — on the NPU, and keep the iGPU for the one workload
> whose latency the user actually notices.

**Caveat worth stating plainly:** these are community figures on one machine, not AMD numbers, and
the same project honestly reports a failure — a 1.7B NPU-hosted request classifier scored only
39.1% exact-class accuracy on a 100-sample gate, so they kept it advisory rather than
authoritative. Small models on the NPU are cheap; that does not make them correct.

### Unified memory is what makes this possible

On these APUs the CPU, iGPU and NPU share **one physical memory pool** (LPDDR5X on Strix Halo,
roughly 256 GB/s theoretical, with community measurements landing nearer 158–170 GB/s effective).
No PCIe copy between engines. That is what makes handing a KV cache or an intermediate tensor
between engines cheap enough to be worth doing.

It also sets the ceiling. Shared bandwidth means every engine draws from the same well — which is
precisely why the interference numbers above matter more than peak TOPS.

### Platform reality check

**AMD's hybrid OGA flow is Windows-first.** On Linux the NPU appears as `/dev/accel/accel0` and the
community has built its own routing (FastFlowLM for the NPU, llama.cpp on the iGPU), but you are
assembling the orchestration yourself rather than calling a supported hybrid API. If your target is
Linux, plan for that.

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

## 18B. Two different bets — AMD's strategy versus Qualcomm's

Both companies sell CPUs, GPUs and NPUs. Both want your AI workload. But they arrived from opposite
directions, and once you see the direction, every other difference stops being a random fact and
becomes a consequence.

> **The one-sentence thesis:**
> **AMD scales a GPU architecture *down* toward the client. Qualcomm scales an NPU architecture *up*
> toward the datacenter.**

### The direction of travel

```
   AMD                                    QUALCOMM
   ───                                    ────────
   CDNA datacenter GPU   (the core bet)   Hexagon NPU in a phone   (the core bet)
        │                                      │
        ▼ scale down                           ▼ scale up
   RDNA client GPU                        Hexagon NPU in a laptop
        │                                      │
        ▼ add a low-power engine               ▼ same IP, more of it
   XDNA NPU  (client only)                Cloud AI 100 / datacenter
                                          ("reuses Hexagon NPU and Oryon CPU")

   Primary engine: THE GPU                Primary engine: THE NPU
   The NPU is the addition.               The GPU (Adreno) is the assist.
```

Qualcomm's datacenter parts reuse Hexagon and Oryon IP — the phone architecture grown up. AMD's
client NPU is a genuinely different architecture (an AIE tile array) bolted alongside a GPU lineage.

### What follows from that

| | **AMD** | **Qualcomm** |
|---|---|---|
| **Primary AI engine** | GPU — CDNA in datacenter, RDNA on client | **NPU** — Hexagon, everywhere |
| **Secondary engine** | XDNA NPU, **client only** | Adreno GPU, assist and fallback |
| **Number of AI architectures** | **three** (CDNA, RDNA, XDNA) | essentially **one** (Hexagon), scaled |
| **Software stacks** | **two, and they are separate** — ROCm (datacenter) vs Ryzen AI (client) | **one** — QAIRT/QNN from phone to datacenter |
| **What crosses the divide** | almost nothing except **Quark** | the whole toolchain |
| **Programming model** | **write kernels** — HIP, Triton, CK, assembly | **compile graphs** — converter → context binary |
| **Matrix instructions you can target** | MFMA (CDNA), WMMA (RDNA) — documented, callable | HVX/HMX driven by the compiler, not hand-written in the normal flow |
| **Training** | **first-class** on CDNA | inference only; QAT runs on a host |
| **Quantiser** | AMD Quark | **AIMET** |
| **Precision floor in practice** | FP16/BF16/FP8, INT8 optional | **quantisation is mandatory**, INT8/INT4 typical |
| **Ecosystem posture** | upstream PyTorch, vLLM, Triton run natively | ONNX-centric, vendor SDK is the path |

### The difference that should shape your career choice

**On AMD you can write the kernel. On Qualcomm's NPU, in the mainstream flow, you cannot.**

AMD hands you HIP, Triton, Composable Kernel, `rocWMMA`, and documented MFMA/WMMA intrinsics. If a
GEMM is slow, you can go and write a faster one, and AITER exists precisely because AMD does that
itself. The ceiling is your skill.

Qualcomm hands you a converter, a quantiser and a graph compiler. Adreno is reachable through
OpenCL kernels, but Hexagon's HVX and HMX are driven by the compiler; your levers are quantisation
choice, graph shape, operator coverage and partitioning. Study B in the Qualcomm doc's §6B makes
the point neatly — the winning move there was a **four-step graph rewrite**, not a hand-tuned
kernel.

| If you want to… | Go here |
|---|---|
| Write matrix kernels, chase roofline numbers, do performance archaeology | **AMD** (or NVIDIA) |
| Do model surgery, quantisation, operator coverage, power/thermal engineering | **Qualcomm** |

Neither is easier. They are different jobs that happen to share a job title.

### How each vendor combines GPU and NPU

This is where the two philosophies produce visibly different products.

**AMD — the NPU and the GPU are peers on the client.** Hybrid mode dynamically partitions prefill
and decode across the XDNA NPU and the RDNA iGPU (§13B), because AMD has a *capable* iGPU sitting
right there. Unified memory makes the handoff cheap. On the datacenter side the NPU does not exist
at all — it is GPUs, end to end.

**Qualcomm — the NPU is the destination and the others are support staff.** The CPU takes control
flow and unsupported operators; Adreno takes pre/post-processing and FP fallback; Hexagon takes the
model. Genie exposes this as a backend field (`QnnHtp` / `QnnGpu` / `QnnGenAiTransformer`), and the
same shape of stack runs on a phone and in Cloud AI 100.

**Where they converge, interestingly:** both ended up needing **software-managed on-chip memory**
for their NPUs — Qualcomm's **VTCM** and AMD's **XDNA tile memory**. Both abandoned the GPU's
hardware-managed cache hierarchy for the NPU, because deterministic, compiler-scheduled data
movement is what makes performance-per-watt work. Different companies, different decades, same
conclusion.

### Both stacks' shared honest lesson

Read the Qualcomm doc's §6B measurement table and AMD's hybrid-mode design together and the same
conclusion falls out of both:

1. **Decode is bandwidth-bound.** No amount of matrix hardware fixes it. Both vendors' answer is
   speculative decoding — Qualcomm ships LADE/SSD/Eaglet; AMD's community uses the NPU as a draft
   engine for the iGPU.
2. **The NPU's dependable win is energy and thermals**, not peak latency.
3. **Graph shape and operator coverage beat micro-optimisation** — a fallback to CPU costs more
   than any kernel tuning recovers.
4. **Measure per phase, on the target device.** Every published speedup in this document is
   conditional on a workload you probably do not have.

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

**Added for RDNA and heterogeneous execution (§5B, §13B):** the RDNA 2/3/4 FLOPS-per-clock-per-CU
table · RDNA 4's 2nd-generation AI accelerators, FP8/BF8 support, 4:2 structured sparsity, the
simplified VGPR layout that removes RDNA 3's inter-lane shuffle, the halved register requirement and
2× tiling · the `_gfx12` intrinsic postfix and its **lack of backward compatibility** with RDNA 3 ·
`rocWMMA` portability with `nvcuda::wmma` and its support for both MFMA and WMMA · the four OGA
execution modes and their compute allocations · the Ryzen AI 300 versus 7000/8000 support matrix and
the explicit exclusion of Phoenix and Hawk Point · Token Fusion versus Full Fusion, the 16K-token
long-context figure, the `context_length` constraint in `genai_config.json`, OGA 0.14.0 and the
pre-optimised model list.

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

**Added in §5B and §13B, and clearly marked in place:** the RX 9070 / 9070 XT / Radeon AI PRO R9700
specification table is from a community reference page, not AMD product documentation · the
statement that RDNA 4 WMMA requires wave32 · the `gfx1151` target identifier for the Strix Halo
Radeon 8060S iGPU shown in §4 · **every Strix Halo heterogeneous figure** — the +3.3%
versus +69.0% interference result, the ~1.7–1.9× combined throughput, the ~2 GB versus ~17 GB
per-token bandwidth arithmetic, the 158–170 GB/s measured effective bandwidth, the `/dev/accel/accel0`
device path, and the 39.1% classifier-accuracy failure — comes from independent community projects
on single machines. Treat all of it as directional, not specified behaviour.

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
- Ryzen AI LLM execution modes — <https://ryzenai.docs.amd.com/en/latest/llm/overview.html>
- Ryzen AI hybrid OGA execution — <https://ryzenai.docs.amd.com/en/latest/hybrid_oga.html>
- AMD Quark — <https://quark.docs.amd.com/>
- AMD RDNA architecture — <https://www.amd.com/en/technologies/rdna.html>
- WMMA on RDNA 3 (GPUOpen) — <https://gpuopen.com/learn/wmma_on_rdna3/>
- Matrix cores on RDNA 4 (GPUOpen) — <https://gpuopen.com/learn/using_matrix_core_amd_rdna4/>
- Accelerating generative AI on Radeon (GPUOpen) —
  <https://gpuopen.com/learn/accelerating_generative_ai_on_amd_radeon_gpus/>

---

*Compiled 2026-09-05. Vendor stacks move quickly — AMD's profiler tooling in particular changed
names recently. Re-verify any specific tool name, flag or version before relying on it.*
