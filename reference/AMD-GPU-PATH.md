# The AMD GPU Path — From `model.py` to Electrons

**A deep dive on the GPU line of the AMD stack: what actually happens between your Python and the
silicon, and how to learn it in an order that works.**

This document assumes you want the **GPU** path. The NPU (XDNA) is covered in
[`AMD-AI-STACK.md`](AMD-AI-STACK.md) §6 and §13B and is deliberately out of scope here.

- [`AMD-AI-STACK.md`](AMD-AI-STACK.md) is the **map** — every component, named and placed.
- **This document is the deep dive** — the layers of the GPU path, top to bottom, with the commands
  that let you see each one for yourself.

> **How to read this.** Every stage ends with a **"See it yourself"** block. Do not read this
> document like a novel. Read one stage, run the commands, then read the next. The whole point is
> that this stack is *inspectable* — you can watch your Python become machine code — and almost
> nobody bothers to look.

---

## Contents

| § | Section | What you learn |
|---|---|---|
| 1 | The whole path in one picture | The ten layers, and which ones matter |
| 2 | From PyTorch to a kernel launch | How an operator becomes a GPU call |
| 3 | **Compilation — HIP to `hsaco`** | The single biggest difference from CUDA |
| 4 | **Dispatch — the AQL journey** | What `hipLaunchKernel` really does |
| 5 | **The execution model** | Grid, workgroup, wavefront, lane |
| 6 | **The memory hierarchy** | Registers to HBM, and occupancy |
| 7 | **Matrix cores and MFMA** | The instructions that do the AI maths |
| 8 | **Triton and `torch.compile`** | The modern portable kernel path |
| 9 | **Profiling and the roofline** | How to know what is actually slow |
| 10 | Multi-GPU | When one GPU is not enough |
| 11 | The optimisation ladder | A repeatable method, not a bag of tricks |
| 12 | **The learning path** | A concrete curriculum with milestones |
| 13 | The debugging toolbox | Environment variables and tools |
| 14 | `gfx` target reference | Which architecture is which |
| 15 | Verification status | What is sourced, what is not |

*The "LAYER 1–10" labels in §1's diagram describe the runtime stack. The section numbers above are
just reading order — they are not the same numbering.*

---

## 1. The whole path in one picture

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │  LAYER 1   your_model.py                                            │
  │            torch.matmul(a, b)                          [§2]         │
  ├─────────────────────────────────────────────────────────────────────┤
  │  LAYER 2   PyTorch dispatcher  ──►  picks an implementation         │
  │              ├── a library call    (hipBLASLt / MIOpen / AITER)     │
  │              └── a compiled kernel (Triton via Inductor)  [§8]      │
  ├─────────────────────────────────────────────────────────────────────┤
  │  LAYER 3   HIP C++ source / Triton IR                               │
  │                    │                                                │
  │                    ▼  amdclang++ / hipcc            [§3]            │
  │            LLVM IR ──► AMDGPU backend ──► AMDGCN assembly           │
  │                    │                                                │
  │                    ▼                                                │
  │            code object (.hsaco)  bundled into a fat binary          │
  ├─────────────────────────────────────────────────────────────────────┤
  │  LAYER 4   hipLaunchKernelGGL(...)                  [§4]            │
  │                    │                                                │
  │                    ▼                                                │
  │            ROCclr software queue                                    │
  │                    │  converts to a 64-byte AQL packet              │
  │                    ▼                                                │
  │            HSA queue (ROCr)  ──►  ring buffer + doorbell            │
  ├─────────────────────────────────────────────────────────────────────┤
  │  LAYER 5   ROCt  ──►  KFD  ──►  amdgpu kernel driver                │
  ├──────────────────────────── PCIe / XGMI ────────────────────────────┤
  │  LAYER 6   Command Processor (CP) / ACE firmware    [§4]            │
  │            reads the packet, sets up registers, launches waves      │
  ├─────────────────────────────────────────────────────────────────────┤
  │  LAYER 7   Compute Units                            [§5]            │
  │            grid ─► workgroups ─► wavefronts ─► lanes                │
  ├─────────────────────────────────────────────────────────────────────┤
  │  LAYER 8   VALU (vector ALU)  ·  MFMA (matrix cores)   [§7]         │
  ├─────────────────────────────────────────────────────────────────────┤
  │  LAYER 9   VGPR ─ LDS ─ L1 ─ L2 ─ Infinity Cache ─ HBM  [§6]        │
  ├─────────────────────────────────────────────────────────────────────┤
  │  LAYER 10  electrons                                                │
  └─────────────────────────────────────────────────────────────────────┘
```

**Which layers actually pay your salary?** Layers 3, 7, 8 and 9 — compilation, the execution model,
the matrix instructions, and the memory hierarchy. Layers 4–6 are worth understanding *once* so you
stop being confused by dispatch overhead and queue behaviour, but you will rarely modify them.

---

## 2. From PyTorch to a kernel launch

When you write `torch.matmul(a, b)` on a ROCm build of PyTorch, nothing about your Python is
special. What happens is:

```
  torch.matmul(a, b)
        │
        ▼
  PyTorch dispatcher  — keyed on (operator, device type, dtype, layout)
        │
        ├──► ROCm build routes "CUDA" device keys to HIP.  This is why
        │    torch.cuda.is_available() returns True on an AMD GPU. It is
        │    not a bug — see AMD-AI-STACK.md §11.
        │
        ▼
  one of:
    hipBLASLt / rocBLAS   ── a hand-tuned GEMM library kernel
    MIOpen                ── convolution and DL primitives
    AITER                 ── AMD's AI operator library (§10 of the map doc)
    a Triton kernel       ── if torch.compile generated one  [§8]
        │
        ▼
  hipLaunchKernelGGL(...)  ── the actual launch  [§4]
```

**The consequence for you:** most "AMD GPU performance work" is not writing kernels from scratch.
It is (a) making sure the dispatcher lands on the *fast* implementation, and (b) writing a better
kernel only when it does not. Step (a) is where most wins live, and it is why `AITER` and
`max_autotune` exist.

### See it yourself

```bash
# Which backend did PyTorch actually call?
export AMD_LOG_LEVEL=3          # HIP runtime API logging
python -c "import torch; a=torch.randn(4096,4096,device='cuda',dtype=torch.float16); (a@a).sum()"

# Confirm you are on ROCm and see the gfx target
python -c "import torch; print(torch.version.hip, torch.cuda.get_device_properties(0))"
```

---

## 3. Compilation — HIP source to a code object

**This is the most important section in this document,** because it contains the one structural
difference between AMD and NVIDIA that trips up everybody.

### The two-pass structure

HIP compilation splits into host and device passes. `amdclang++` or `hipcc` handles both, and the
device code ends up **embedded inside the host object file**.

```
  kernel.hip
      │
      ├── HOST pass ────────► x86-64 object code
      │                            │
      │                            │  device code embedded as a named section
      │                            ▼
      └── DEVICE pass                 ┌──────────────────────────┐
            │                         │  .hip_fatbin section     │
            ▼                         │  symbol: __hip_fatbin    │
      Clang HIPAMD toolchain          └──────────────────────────┘
            │
            ▼  AMDGPU backend
      AMDGCN assembly
            │
            ▼
      code object:  .hsaco       ← per gfx target
            │
            ▼  clang-offload-bundler
      fat binary  (one bundle, many targets)
```

### The difference from CUDA that matters most

| | **NVIDIA** | **AMD** |
|---|---|---|
| Device code format | `cubin` (binary) **or PTX** (assembly text) | **`hsaco`** (binary) |
| Forward compatibility | **the driver JIT-compiles PTX at runtime** | **no equivalent layer** |
| Fat binary | `.fatbin` | `.hip_fatbin` |
| Module load API | `hipModuleLoad` ← `.cubin` or PTX | `hipModuleLoad` ← `.hsaco` |

> **Read the second row twice, because it explains a whole class of AMD frustration.** NVIDIA ships
> PTX inside the binary, and if you run on a newer GPU than the build targeted, the driver compiles
> that PTX for the new chip at load time. Your binary keeps working.
>
> **AMD has no PTX-equivalent JIT layer in this path.** The `hsaco` is compiled ahead of time for a
> specific `gfx` target. Run it on an architecture you did not list in `--offload-arch` and it does
> not run.
>
> **What follows practically:** `--offload-arch` is not an optimisation flag, it is a *compatibility
> contract*. You must enumerate every target you intend to support. This single fact is why ROCm
> builds are large, why "does ROCm support my GPU?" is a real question with a real answer per part,
> and why Docker images are published per architecture.

You *can* compile at runtime — but you have to ask for it explicitly, via the **`hiprtc*` API**,
which takes the kernel as a **text string** and compiles it on the spot. That is HIP's answer to
runtime codegen, and it is what Triton effectively leans on (§8).

### The flags that matter

| Flag | What it does | When you need it |
|---|---|---|
| `--offload-arch=gfx942` | Generate code for this target. **Repeatable** for a multi-target fat binary | **Always.** Get this wrong and nothing runs |
| `-fgpu-rdc` | Relocatable device code — a kernel in one translation unit may call a device function in another | Multi-file device code, device-function libraries |
| `-fno-gpu-rdc` | Self-contained fully linked binary per architecture; **no cross-TU device calls** | The default; faster builds |
| `-save-temps` | Keep every intermediate the compiler produced | **Learning, and debugging codegen** |
| `-v` | Print the compilation steps | Seeing the pipeline for real |
| `-ggdb` | Debug info tuned for GDB | Before using `rocgdb` |
| `--gpu-max-threads-per-block=N` | Generate code supporting up to N threads per block | Large workgroups |
| `--emit-static-lib` | Static library exporting **host** functions only, linkable with `gcc` | Shipping a library to non-`hipcc` users |

**Two kinds of static library — a real trap.** `--emit-static-lib` produces a library that exports
and launches *host* functions only, with device code embedded as fat binaries; it can be linked by
`gcc`. If you instead want to export **device** functions for other code objects to link against,
you need `-fgpu-rdc` plus plain `ar`, and the consumer must link with `hipcc`/`amdclang++`:

```bash
hipcc hipDevice.cpp -c -fgpu-rdc -o hipDevice.o
ar rcsD libHipDevice.a hipDevice.o
hipcc libHipDevice.a test.cpp -fgpu-rdc -o test.out
```

### Preprocessor macros you will see in real code

| Macro | Meaning |
|---|---|
| `__HIP__` | Compiling with HIP language support |
| `__HIP_DEVICE_COMPILE__` | Defined **during the device pass only** — this is how one source file behaves differently on host and device |
| `__CLANG_RDC__` | Compiling in relocatable-device-code mode (`-fgpu-rdc`) |

### See it yourself

This is the single most educational thing in this whole document. Run it.

```bash
# 1. Write the smallest possible kernel
cat > k.hip <<'EOF'
#include <hip/hip_runtime.h>
__global__ void add(float* o, const float* a, const float* b, int n) {
  int i = blockIdx.x * blockDim.x + threadIdx.x;
  if (i < n) o[i] = a[i] + b[i];
}
EOF

# 2. Watch the compiler pipeline run
hipcc -v --offload-arch=gfx942 -c k.hip -o k.o

# 3. Keep every intermediate: you get .bc, .s (AMDGCN assembly), .hsaco
hipcc -save-temps --offload-arch=gfx942 -c k.hip -o k.o
ls k-hip-amdgcn-amd-amdhsa*

# 4. Read the actual machine instructions your GPU will execute
llvm-objdump -d --triple=amdgcn-amd-amdhsa k.o | head -60

# 5. Prove the fat binary section exists
readelf -S k.o | grep hip_fatbin
```

Step 4 is the moment the stack stops being magic. You are looking at the real ISA — `v_add_f32`,
`global_load_dword`, `s_endpgm`. Every performance discussion in §6 to §9 is ultimately about which
of these instructions appear and how often they stall.

---

## 4. Dispatch — what `hipLaunchKernel` actually does

You call one function. Six things happen. Knowing them is what lets you reason about launch
overhead instead of guessing.

```
  1.  hipLaunchKernelGGL(kernel, grid, block, shmem, stream, args...)
              │
              │  parameter validation: workgroup size, LDS usage vs hardware limits
              ▼
  2.  HIP runtime enqueues a launch command into a ROCclr SOFTWARE queue
              │
              ▼
  3.  ROCclr converts the command into an AQL packet
              │      AQL = Architected Queuing Language (an HSA concept)
              │      every AQL packet is exactly 64 BYTES
              │      carries: grid size, workgroup size, segment sizes,
              │               kernel code-object address, completion signal
              ▼
  4.  the packet is written into an HSA QUEUE — a ring buffer in memory
              │      the packet's `format` field is flipped
              │      INVALID ──► KERNEL_DISPATCH   (atomically!)
              ▼
  5.  DOORBELL write — an MMIO store that wakes the firmware
              │
              ▼
  6.  Command Processor (CP) / Asynchronous Compute Engine (ACE)
              ├─ fetches the packet
              ├─ runs microcode to configure GPU state
              ├─ sets up SGPRs and VGPRs per the kernel's metadata
              ├─ launches wavefronts onto the Compute Units
              └─ on completion, signals the packet's completion signal
```

### The pieces, named

| Component | What it is |
|---|---|
| **ROCclr** | ROCm Common Language Runtime — owns the software queue, builds AQL packets |
| **ROCr** | The HSA runtime — creates and manages the memory-mapped queues and signals |
| **ROCt** | Thin interface layer exposing the `amdgpu` kernel module to userspace |
| **KFD** | Kernel Fusion Driver — the runtime uses it to initialise and register an AQL queue with the CP |
| **CP / ACE** | The on-GPU **packet processor** in firmware. The CP *is* what AQL calls the packet processor |
| **MQD / HQD** | Memory / Hardware Queue Descriptor. The driver keeps queue state in an MQD; scheduling firmware loads it into an HQD when the queue is mapped to real hardware |
| **Doorbell** | A region of the device's MMIO BAR mapped per queue. Writing to it wakes the firmware |

**A detail that explains multi-tenant behaviour:** hardware queue slots are finite. When user queues
outnumber available slots, scheduling firmware **dynamically maps and unmaps** queues by priority
and time quantum. A 4K doorbell page provides 512 64-bit doorbells, so up to 512 user queues. If you
have ever wondered why many concurrent streams stop scaling, this is the mechanism to look at.

### See it yourself

```bash
# Decode and print every AQL packet the runtime builds.
# LOG_AQL = 0x00000008 in AMD_LOG_MASK. Genuinely worth watching once.
export AMD_LOG_LEVEL=4          # raise verbosity (higher = more)
export AMD_LOG_MASK=0x8         # restrict to AQL packet decoding
./your_app

# Serialise kernel launches to isolate which one misbehaves.
# Check `AMD_SERIALIZE_KERNEL` accepted values for your ROCm version --
# they select waiting for completion before enqueue, after enqueue, or both.
export AMD_SERIALIZE_KERNEL=3
```

---

## 5. The execution model

### The hierarchy, and the vocabulary trap

```
  GRID                     your whole launch
   └── WORKGROUP           (CUDA: "block")   — shares LDS, can barrier
        └── WAVEFRONT      (CUDA: "warp")    — the real unit of execution
             └── WORK-ITEM (CUDA: "thread")  — one lane
```

| CUDA word | AMD word | Size on CDNA | Size on RDNA |
|---|---|---|---|
| warp | **wavefront** | **64** | **32** (or 64) |
| thread | work-item / lane | — | — |
| block | workgroup | — | — |
| shared memory | **LDS** (Local Data Share) | — | — |

> **The wavefront-64 hazard.** This is the number-one porting bug. CUDA code is saturated with
> hard-coded `32` — warp-shuffle strides, ballot masks, reduction trees, `laneId & 31`. On CDNA the
> wavefront is **64**. The code compiles, runs, and produces *wrong answers* or half the throughput.
> Audit every literal `32`. (RDNA is wave32-typical, which is why a kernel can be correct on a
> Radeon card and broken on an Instinct one.)

### Inside a Compute Unit

A CU contains multiple **SIMD** units, and each SIMD hosts several resident wavefronts. Your
**occupancy** — how many wavefronts are resident per SIMD — is capped by whichever of these runs out
first:

```
  ┌───────────────── COMPUTE UNIT ─────────────────┐
  │                                                │
  │   SIMD 0     SIMD 1     SIMD 2     SIMD 3      │  ← wavefronts scheduled here
  │   ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐     │
  │   │VGPR │    │VGPR │    │VGPR │    │VGPR │     │  ← vector registers   (per SIMD)
  │   │AGPR │    │AGPR │    │AGPR │    │AGPR │     │  ← accumulation regs, MFMA
  │   │SGPR │    │SGPR │    │SGPR │    │SGPR │     │  ← scalar registers
  │   └─────┘    └─────┘    └─────┘    └─────┘     │
  │                                                │
  │   ┌────────────────────────────────────────┐   │
  │   │            LDS  (shared)               │   │  ← per WORKGROUP
  │   └────────────────────────────────────────┘   │
  └────────────────────────────────────────────────┘

  Occupancy limiters:   VGPR count  ·  LDS bytes per workgroup  ·  SGPR count
                        ·  workgroup size  ·  a hard architectural cap
```

**AGPRs are an AMD-specific concept worth knowing.** In addition to VGPRs, CDNA has accumulation
registers used by the matrix pipeline (§7). Register pressure on an MFMA-heavy kernel is a
two-dimensional problem, not one.

### See it yourself

Do not guess the numbers for your specific part — ask the driver. `rocprofv3` emits an agent-info
table containing exactly the fields you need:

```
  Simd_Count · Simd_Per_Cu · Cu_Count · Num_Xcc · Wave_Front_Size
  Max_Waves_Per_Simd · Max_Waves_Per_Cu · Lds_Size_In_Kb
  Workgroup_Max_Size · Gfx_Target_Version · Local_Mem_Size
```

```bash
rocminfo | less                 # agent properties, wavefront size, CU count
rocprofv3 --kernel-trace -- ./your_app     # emits agent info + per-kernel resources
```

And per kernel, `rocprofv3` reports the resources that determine your occupancy directly:
`VGPR_Count`, `SGPR_Count`, `LDS_Block_Size`, `Scratch_Size`, `Grid_Size`, `Workgroup_Size`.

> **`Scratch_Size` greater than zero is an alarm.** Scratch means register spilling to memory. If
> you see it on a hot kernel, reduce register pressure before optimising anything else.

---

## 6. The memory hierarchy

```
                        latency ──────────────►        capacity ◄──────────
  ┌──────────────────────────────────────────────────────────────────────┐
  │  VGPR / AGPR / SGPR      registers, per SIMD          ~1 cycle      │
  ├──────────────────────────────────────────────────────────────────────┤
  │  LDS                     per workgroup, software-managed            │
  │                          banked — beware BANK CONFLICTS             │
  ├──────────────────────────────────────────────────────────────────────┤
  │  L1 / vector cache       per CU                                     │
  ├──────────────────────────────────────────────────────────────────────┤
  │  L2                      per XCD on multi-die parts                 │
  ├──────────────────────────────────────────────────────────────────────┤
  │  Infinity Cache (MALL)   device-wide last level                     │
  ├──────────────────────────────────────────────────────────────────────┤
  │  HBM                     MI355X: 288 GB @ 8.0 TB/s                  │
  └──────────────────────────────────────────────────────────────────────┘
```

### The three rules that matter more than everything else

**1. Coalescing.** Adjacent lanes in a wavefront should read adjacent addresses. When they do, the
hardware merges 64 lane requests into a few wide memory transactions. When they do not — strided or
random access — you get many transactions for the same data volume, and you have thrown away most of
your bandwidth. **This is usually the single largest factor in a naive kernel's performance.**

**2. LDS bank conflicts.** LDS is banked. If lanes in a wavefront hit different addresses in the
*same* bank, the accesses serialise. The classic fix is **padding**: make your tile stride
`TILE + 1` instead of `TILE` so that a column walk spreads across banks.

**3. Arithmetic intensity decides your ceiling.** Compute FLOPs ÷ bytes moved. Compare it to the
machine's ratio of peak FLOP/s to peak bandwidth. Below that ratio you are **memory-bound** and no
amount of matrix hardware helps; above it you are **compute-bound**. This is the roofline model, and
§9 shows how to measure it rather than reason about it.

> **Why LLM decode is hard, in one line:** a decode step reads the entire weight matrix to produce
> one token. Arithmetic intensity is roughly 1 FLOP per byte. You are pinned to the HBM roof, and
> the matrix cores sit idle. See `AMD-AI-STACK.md` §13B for what to do about it.

### The multi-die wrinkle

MI300 and later are **chiplet** parts: multiple XCDs, each with its own L2, over a shared Infinity
Fabric and Infinity Cache. Memory access is therefore **not uniform** — where a page lives relative
to where your workgroup runs matters. This shows up as unexplained run-to-run variance on
bandwidth-sensitive kernels, and `Num_Xcc` in the agent table is your hint that you are on such a
part.

---

## 7. Matrix cores and MFMA

This is where the AI maths actually happens, and where the biggest speedups live.

### Four ways to reach the matrix cores

AMD's own guidance, in their order of preference:

| Approach | Verdict |
|---|---|
| **`rocBLAS` / `hipBLASLt` / `rocWMMA` libraries** | **Recommended.** Start here, always |
| **Compiler intrinsics in HIP** | Good — the compiler understands the semantics. But **built-ins may change between releases** |
| Inline assembly sprinkled in HIP | Not recommended |
| Whole kernels in assembly | Not practical |

### The intrinsic syntax

```c
d = __builtin_amdgcn_mfma_<CDfmt>_<M>x<N>x<K><ABfmt>(a, b, c, cbsz, abid, blgp);
//                          │       └───┬───┘   │     │  │  │      │      │
//                          │           │       │     │  │  │      │      └─ broadcast flags,
//                          │           │       │     │  │  └─ accumulator in  set 0 normally
//                          │           │       │     │  └─ B fragment
//                          │           │       │     └─ A fragment
//                          │           │       └─ dtype of A and B
//                          │           └─ matrix shape
//                          └─ dtype of C and D
```

**MFMA is a wavefront-wide instruction.** All 64 lanes cooperate on *one* matrix operation, and the
A, B, C, D matrices are **distributed across the lanes' vector registers**. This is the conceptual
leap: you are not writing per-thread code any more. You must know exactly which lane holds which
matrix element, or your results are garbage.

Worked example from AMD's lab notes: `__builtin_amdgcn_mfma_f32_16x16x4f32` computes the sum of four
outer products in one invocation. With a thread block of (16, 4) — that is exactly **one
wavefront** — two vector registers hold A and B (64 lanes each), and **four** vector registers hold
the 16×16 output D.

### The CDNA 3 instruction set — verified

Extracted directly from AMD's own `amd_matrix_instruction_calculator` source. Single-block
instructions on `cdna3` (gfx942, MI300X/MI325X):

| Instruction | In | Out | M×N×K | Cycles |
|---|---|---|---|---|
| `v_mfma_f32_16x16x16_f16` | FP16 | FP32 | 16×16×16 | 16 |
| `v_mfma_f32_32x32x8_f16` | FP16 | FP32 | 32×32×8 | 32 |
| `v_mfma_f32_16x16x16_bf16` | BF16 | FP32 | 16×16×16 | 16 |
| `v_mfma_f32_32x32x8_bf16` | BF16 | FP32 | 32×32×8 | 32 |
| `v_mfma_i32_16x16x32_i8` | INT8 | INT32 | 16×16×32 | 16 |
| `v_mfma_i32_32x32x16_i8` | INT8 | INT32 | 32×32×16 | 32 |
| `v_mfma_f32_16x16x32_fp8_fp8` | FP8 | FP32 | 16×16×32 | 16 |
| `v_mfma_f32_32x32x16_fp8_fp8` | FP8 | FP32 | 32×32×16 | 32 |
| `v_mfma_f32_16x16x8_xf32` | XF32 | FP32 | 16×16×8 | 16 |
| `v_mfma_f32_16x16x4_f32` | FP32 | FP32 | 16×16×4 | 32 |
| `v_mfma_f64_16x16x4_f64` | FP64 | FP64 | 16×16×4 | 32 |

**Three things to notice, because each is an exam question:**

1. **Lower precision buys a bigger K, not a bigger M or N.** FP16 gets K=16 at the 16×16 shape;
   INT8 gets K=32; FP8 gets K=32. The tile face stays the same and you consume more of the reduction
   dimension per instruction. That *is* the speedup.

2. **FP8 comes in mixed-input variants.** The real instruction set includes `fp8_fp8`, `fp8_bf8`,
   `bf8_fp8` and `bf8_bf8` — you can feed A and B *different* 8-bit formats. Combined with the
   FNUZ-versus-OCP difference across MI300 and MI350 (`AMD-AI-STACK.md` §19), FP8 is the easiest
   place in the whole stack to get subtly wrong numerics.

3. **`v_smfmac_*` is the sparse family.** Structured sparsity **doubles K** for the same shape and
   cycle count: `v_mfma_f32_16x16x16_f16` (K=16, 16 cycles) becomes
   `v_smfmac_f32_16x16x32_f16` (K=32, 16 cycles). That is the 2× — and you only get it if your
   weights genuinely match the sparsity pattern.

### The tool that removes all guesswork

AMD publishes `amd_matrix_instruction_calculator`, which answers the lane-mapping question exactly:

```bash
git clone https://github.com/ROCm/amd_matrix_instruction_calculator
cd amd_matrix_instruction_calculator

# Everything about one instruction: registers, throughput, co-execution
./matrix_calculator.py --architecture cdna3 \
    --instruction v_mfma_f32_16x16x16_f16 --detail-instruction

# "Which register and lane holds A[3][7]?"
./matrix_calculator.py --architecture cdna3 \
    --instruction v_mfma_f32_16x16x16_f16 --get-register --A-matrix ...

# The full register/lane map for a whole matrix
./matrix_calculator.py --architecture cdna3 \
    --instruction v_mfma_f32_16x16x16_f16 --register-layout --D-matrix
```

Its five modes are `--detail-instruction`, `--get-register`, `--matrix-entry`, `--register-layout`
and `--matrix-layout`. **It also covers RDNA's WMMA instructions**, so it is the one tool that
serves both GPU families.

> **This tool is the answer to "how do I learn MFMA?"** The register layouts are not memorisable and
> not guessable. Generate them, put them next to your kernel, and check your indexing against them.

---

## 8. Triton and `torch.compile`

Writing HIP by hand teaches you the machine. Triton is how you *ship* kernels, because one Python
source targets both vendors.

### The compilation path, stage by stage

```
  @triton.jit Python function
        │
        ▼  frontend walks the Python AST
  TTIR        Triton IR                        (vendor-neutral)
        │
        ▼  make_ttgir  — layout selection + AMD-specific passes
  TTGIR       TritonGPU IR                     (hardware-dependent!)
        │
        ▼  make_llir   — LDS/shared-memory opts, then generic LLVM opts
  LLVM IR
        │
        ▼  make_amdgcn — translateLLVMIRToASM, triple "amdgcn-amd-amdhsa"
  AMDGCN assembly
        │
        ▼  make_hsaco  — assemble + ROCm linker
  .hsaco      the same code-object format as §3
```

Note where it converges: **Triton and `hipcc` produce the identical artefact type.** Triton is a
different front door onto the same compiler backend, not a separate runtime.

The AMD backend also loads AMD's device bitcode libraries — **`ocml`** (math) and **`ockl`**
(kernel-level primitives) — which is how `exp`, `sqrt` and friends resolve.

### See it yourself — the best learning trick in this document

Triton caches **every intermediate** on disk. You can read your Python kernel at every level of
lowering, including final assembly.

```bash
python your_triton_kernel.py
ls ~/.triton/cache/*/
#   matmul_kernel.ttir     ← Triton IR
#   matmul_kernel.ttgir    ← TritonGPU IR   (where AMD-specific layout lives)
#   matmul_kernel.llir     ← LLVM IR
#   matmul_kernel.amdgcn   ← AMDGCN assembly + kernel resource usage
#   matmul_kernel.hsaco    ← final binary
#   matmul_kernel.json     ← metadata incl. the HIPOptions used
```

Diff the `.ttgir` before and after changing `num_warps` and you can *see* the layout change. Read
the `.amdgcn` and you can count your MFMA instructions and check your register usage.

You can also compile for a target explicitly, without owning the GPU:

```python
from triton.backends.compiler import GPUTarget
target = GPUTarget("hip", "gfx942", 64)   # MI300X, wavefront 64
output = triton.compile(src, target=target)
```

### Tuning knobs

| Knob | Effect |
|---|---|
| `num_warps` | Wavefronts per workgroup — your occupancy dial |
| `num_stages` | Software-pipelining depth. **AMD documents per-kernel-shape guidance; the right value differs by kernel structure — consult current ROCm docs rather than copying a number** |
| `matrix_instr_nonkdim` | Selects the MFMA tile size (ties directly to §7's table) |
| `BLOCK_M/N/K` | Your tiling, and therefore your arithmetic intensity |

**Debugging tip:** set `num_stages=1` to disable software pipelining. If a bug disappears, the
pipeliner is implicated. This is the cheapest bisection available.

### Through `torch.compile`

```bash
TORCHINDUCTOR_MAX_AUTOTUNE=1     # benchmark Triton configs per shape, pick the fastest
TORCHINDUCTOR_FREEZING=1         # inline weights as constants, enable constant folding
                                 #   -> documented as a large inference win on AMD
TORCH_COMPILE_DEBUG=1            # writes torch_compile_debug/, incl. output_code.py
                                 #   containing the generated Triton kernel source
```

Two AMD-specific notes from ROCm's documentation: `max_autotune_gemm_backends` defaults to
`TRITON,ATEN,NV`, and **restricting it to `TRITON` can improve performance** by enabling more fused
matmul kernels instead of falling back to rocBLAS. But Inductor will not use Triton at all if MIOpen
or rocBLAS is simply faster for that operation — which is the right behaviour, and worth knowing
before you spend a day wondering why your Triton kernel never ran.

---

## 9. Profiling and the roofline

**Rule zero: never optimise without a measurement.** Everything above is theory until a profiler
tells you which of it applies.

### Two tools, two jobs

| Tool | Question it answers |
|---|---|
| **`rocprofv3`** | *"What ran, for how long, and what did the counters say?"* — tracing and raw counters |
| **`rocprof-compute`** (ROCm Compute Profiler) | *"Is this kernel compute-bound or memory-bound, and how far from the roof?"* — modelled analysis and roofline |

> Use `rocprofv3`, **not** `rocprof` — the legacy tool is deprecated (`AMD-AI-STACK.md` §15).

### `rocprofv3` — the commands worth memorising

```bash
# What can this GPU even measure?
rocprofv3 --list-avail
rocprofv3-avail list --pmc

# Will these counters fit in one pass together?  (Ask BEFORE profiling.)
rocprofv3-avail pmc-check SQ_WAVES SQ_INSTS_VALU

# Broad first look: HIP API + kernels + memory copies
rocprofv3 --runtime-trace -- ./your_app

# Where is the time going, by domain?
rocprofv3 --runtime-trace --summary-per-domain \
          --summary-groups "KERNEL_DISPATCH|MEMORY_COPY" -- ./your_app

# Now narrow to counters on the hot kernel
rocprofv3 --kernel-trace --pmc SQ_WAVES,SQ_INSTS_VALU -- ./your_app

# Data-movement focus
rocprofv3 --memory-copy-trace --memory-allocation-trace -- ./your_app
```

Counter collection is **multi-pass by nature** — the hardware has a limited number of counter slots,
which is why `pmc-check` exists. Asking for too many counters at once silently forces extra passes
or fails.

### `rocprof-compute` — the roofline workflow

```bash
# Profile. This runs TWO stages: application counters, then roofline microbenchmarks.
rocprof-compute profile -n my_run -- ./your_app

# Skip the roofline benchmark stage (faster)
rocprof-compute profile -n my_run --no-roof -- ./your_app

# Only the roofline
rocprof-compute profile -n my_run --roof-only -- ./your_app

# Render the analysis, including roofline HTML plots
rocprof-compute analyze -p workloads/my_run
```

Output artefacts: `roofline.csv` (the machine's measured peaks), `sysinfo.csv` (target device
settings), `log.txt` (all profiling output). Rendering a roofline chart needs **both**
`roofline.csv` and application counters — a `--bench-only` run alone will not plot.

### How to read a roofline

```
   FLOP/s
     ▲
     │                          ┌──────────────  MFMA peak
     │                     ┌────┘
     │                ┌────┘ ················  VALU peak
     │           ╱
     │      ╱          ← the slope IS your memory bandwidth
     │  ╱
     │╱   ● your kernel
     └────────────────────────────────────────►  arithmetic intensity (FLOP/byte)
          ↑                    ↑
      on the slope         under the roof
      = MEMORY-BOUND       = COMPUTE-BOUND
      fix data movement    fix instruction mix / occupancy
```

A published MI300X profiling study is instructive here: across prefill kernels — including matrix
multiplies, quantised GEMMs and FlashAttention — **every kernel sat on the HBM bandwidth roof rather
than near the MFMA or VALU compute roofs**, clustering around 1–3 FLOP/byte. The highest-intensity
kernel measured (a FlashAttention tile, ~15 FLOP/byte) still only reached on the order of
10 TFLOP/s. *(Third-party measurement, not an AMD figure — see §15.)*

**The lesson, and it generalises:** on real LLM work you are usually moving weights, KV cache and
activations, not doing arithmetic. Reach for tiling, fusion, cache reuse and layout before reaching
for a fancier matrix instruction.

---

## 10. Multi-GPU

Briefly, because it becomes the whole job at scale:

| Piece | Role |
|---|---|
| **RCCL** | AMD's collectives library — the NCCL equivalent. `AllReduce`, `AllGather`, etc. |
| **xGMI / Infinity Fabric** | GPU-to-GPU interconnect. Much faster than PCIe, and **not uniform** — topology matters |
| **`rocm-smi` / `amd-smi`** | Query the link topology before you choose a parallelism strategy |

The methodology point: at single-GPU scale you profile kernels; at multi-GPU scale your bottleneck
usually moves to **communication and load imbalance**. Profile the collective, not the kernel.

---

## 11. The optimisation ladder

Work top to bottom. Do not skip. Each rung is cheaper than the one below it.

```
  0.  MEASURE.  Get a baseline number and a roofline position.        [§9]
      │         Without this, everything below is superstition.
      ▼
  1.  Are you calling the fast library at all?                        [§2]
      │  hipBLASLt / MIOpen / AITER.  Enable AITER: VLLM_ROCM_USE_AITER=1
      │  Biggest wins in the whole list, for the least work.
      ▼
  2.  Is the problem SHAPE the issue?
      │  Batch more. Pad to tile boundaries. Fuse adjacent ops.
      ▼
  3.  Is precision leaving throughput on the table?                   [§7]
      │  FP16/BF16 -> FP8 -> INT8.  Each step buys a bigger K.
      │  Validate accuracy at every step, and mind FNUZ vs OCP.
      ▼
  4.  MEMORY-BOUND?  (roofline says: on the slope)                    [§6]
      │  ├─ Fix coalescing first. Usually the single biggest factor.
      │  ├─ Tile through LDS to create reuse.
      │  ├─ Pad LDS strides to kill bank conflicts.
      │  └─ Fuse to avoid a round trip to HBM entirely.
      ▼
  5.  COMPUTE-BOUND?  (roofline says: under the roof)                 [§7]
      │  ├─ Are MFMA instructions actually being emitted?  Read the .amdgcn.
      │  ├─ Pick a better MFMA shape (matrix_instr_nonkdim).
      │  └─ Check Scratch_Size == 0. Spilling silently destroys throughput.
      ▼
  6.  Occupancy too low?                                              [§5]
      │  Reduce VGPR pressure, reduce LDS per workgroup, retune num_warps.
      │  NOTE: maximum occupancy is NOT the goal. A high-register kernel
      │  with great reuse often beats a low-register kernel with none.
      ▼
  7.  Only now: hand-write or hand-tune the kernel.
      │  Triton first (§8). HIP + MFMA intrinsics if Triton cannot express it.
      ▼
  8.  MEASURE AGAIN, and keep the numbers. A speedup you cannot
      reproduce and explain is not a result.
```

---

## 12. The learning path

*This ladder is my recommended sequence, not vendor guidance. The facts it points at are sourced;
the ordering is a teaching judgement.*

### Stage 0 — Prerequisites

C++ that you are comfortable in, and the linear algebra from
[`WEEK-01-MATHEMATICS-FOUNDATIONS.md`](../textbook/WEEK-01-MATHEMATICS-FOUNDATIONS.md). Specifically:
you must be fluent in what a matrix multiply *is* before you try to make one fast.

### Stage 1 — Get a GPU you can actually use

| Route | Cost | Notes |
|---|---|---|
| Cloud MI300X instance | rental | The real target. Best signal per hour |
| Radeon with ROCm support | one-off | Check the compatibility list for your exact part first (`AMD-AI-STACK.md` §5B) |
| No GPU | free | You can still do §3 and §8 — **compilation and IR inspection need no GPU.** `hipcc --offload-arch=gfx942` and `triton.compile(target=GPUTarget("hip","gfx942",64))` both work on a CPU-only box |

**Milestone:** `rocminfo` prints your agent, and `hipcc` compiles the §3 example.

### Stage 2 — The path itself (this document, §3 to §5)

Do every "See it yourself" block. Write the vector-add kernel, dump the AMDGCN, watch the AQL
packets, read your own occupancy numbers.

**Milestone:** you can explain, without notes, what happens between `hipLaunchKernelGGL` and a
wavefront starting — and you can point at the `v_add_f32` in your own disassembly.

### Stage 3 — The GEMM ladder

The canonical exercise, and the one every interviewer probes. Implement matrix multiply repeatedly,
measuring at each step:

```
  1. naive             one thread per output element        ← baseline
  2. + coalescing      fix the access pattern               ← usually the biggest single jump
  3. + LDS tiling      create reuse                          [§6]
  4. + register tiling each thread computes a micro-tile
  5. + MFMA            matrix cores via intrinsics           [§7]
  6. + double buffer   overlap load with compute
  7. compare           against hipBLASLt
```

**Milestone:** a table of seven measured TFLOP/s numbers, each with a one-sentence explanation of
*why* it moved, and an honest statement of what fraction of hipBLASLt you reached. **This table is
a portfolio artefact.** It is worth more than any certificate.

### Stage 4 — Triton (§8)

Reimplement steps 1–5 of the GEMM ladder in Triton. Compare against your HIP versions. Read the
`.ttgir` and `.amdgcn` for each.

**Milestone:** you can articulate what Triton does *better* than your hand-written HIP, and what it
does *worse*, with disassembly to back both claims.

### Stage 5 — Profiling seriously (§9)

Take a real workload — a small LLM under vLLM — and produce a roofline. Identify the top three
kernels. Explain each one's position on the plot.

**Milestone:** a profiling report that names a bottleneck and proposes a specific, mechanism-level
fix. This is roughly the artefact a "GPU performance engineer" job interview is looking for.

### Stage 6 — Choose a specialisation

| Direction | What you do |
|---|---|
| **Kernel engineering** | Attention variants, quantised GEMMs, fused epilogues. Read AITER's source |
| **Model enablement** | Bring new architectures up on ROCm; fix operator gaps; upstream patches |
| **Compiler** | LLVM AMDGPU backend, Triton's AMD backend, MLIR passes |
| **Distributed** | RCCL, topology, parallelism strategies at scale (§10) |

### The single highest-leverage habit

**Read the generated assembly.** Almost nobody does. The ability to open a `.amdgcn` file, count the
MFMA instructions, spot register spilling, and see that your "optimised" kernel did not actually
vectorise, is what separates people who *guess* about GPU performance from people who *know*. Every
tool in §3 and §8 exists to let you do this, and it costs you nothing but the habit.

---

## 13. The debugging toolbox

| Variable / tool | What it does |
|---|---|
| `AMD_LOG_LEVEL` | HIP runtime logging verbosity — higher prints more |
| `AMD_LOG_MASK=0x8` | `LOG_AQL` — decode and display AQL packets (§4) |
| `AMD_SERIALIZE_KERNEL` | Serialise kernel launches — isolates which kernel misbehaves |
| `HIP_VISIBLE_DEVICES` | Restrict visible GPUs |
| `rocgdb` | The ROCm GPU debugger. **Compile with `-ggdb` first** |
| `llvm-objdump -d --triple=amdgcn-amd-amdhsa` | Disassemble a code object |
| `readelf -S \| grep hip_fatbin` | Prove the fat binary is embedded |
| `rocminfo` | Agent properties: wavefront size, CU count, LDS size |
| `amd-smi` | Device state, topology, utilisation |

**Permissions gotcha:** profiling and dispatch require access to **`/dev/kfd`**. "Counter collection
failed" or "no agents found" is very often a group-membership problem, not a code problem.

---

## 14. `gfx` target reference

Every `--offload-arch` value maps to an architecture generation. From AMD's matrix-instruction
calculator source (CDNA) and Triton's AMD backend (all four):

| `gfx` target | Generation | Example hardware | Wavefront | Matrix |
|---|---|---|---|---|
| `gfx908` | CDNA 1 | MI100 | 64 | MFMA |
| `gfx90a` | CDNA 2 | MI200 series (MI210/250/250X) | 64 | MFMA |
| `gfx940` / `gfx941` / `gfx942` | CDNA 3 | MI300A / MI300X / MI325X | 64 | MFMA, XF32 |
| `gfx950` | CDNA 4 | MI350 series | 64 | MFMA, MXFP (FP4/FP8) |
| `gfx1100`–`gfx1103` | RDNA 3 | RX 7000 series | **32** | WMMA |
| `gfx1150`–`gfx1153` | RDNA 3 | integrated GPUs (incl. Strix Halo `gfx1151`) | **32** | WMMA |
| `gfx1200` / `gfx1201` | RDNA 4 | RX 9000 series | **32** | WMMA (`_gfx12` intrinsics) |

> **The rule this table encodes:** wavefront **64 on CDNA, 32 on RDNA**; **MFMA on CDNA, WMMA on
> RDNA**. Nearly every cross-architecture bug traces back to one of those two lines.

---

## 15. Verification status

Stated plainly, because a reference document that blurs this is worse than useless.

### From AMD primary documentation

The two-pass host/device compilation structure · `amdclang++` and `hipcc` roles · `hsaco` versus
`cubin`/PTX and the statement that on CUDA platforms the driver compiles PTX at runtime ·
`clang-offload-bundler`, the `__hip_fatbin` symbol and the `.hip_fatbin` ELF section · `-fgpu-rdc`
versus `-fno-gpu-rdc` semantics including cross-translation-unit device calls · the flag table
(`--offload-arch`, `-save-temps`, `-v`, `-ggdb`, `--gpu-max-threads-per-block`, `--emit-static-lib`)
· the two static-library types and the `ar rcsD` recipe · the `hiprtc*` runtime-compilation API ·
`hipModuleLoad`/`hipModuleLoadData`/`hipModuleLoadFatBin` and their accepted formats · the
`__HIP__`, `__HIP_DEVICE_COMPILE__` and `__CLANG_RDC__` macros · the Clang HIPAMD toolchain and
AMDGPU backend.

**Dispatch:** the AQL queue concept, the **64-byte** packet size, the statement that the packet
processor is implemented by the Command Processor, the runtime's use of KFD to register the queue,
the atomic `INVALID → KERNEL_DISPATCH` format transition, the doorbell signal, CP microcode setting
up SGPRs/VGPRs, the kernel prolog, and the completion signal — all from AMD's Compute ABI
documentation. The MQD/HQD model, dynamic queue mapping under slot pressure, the doorbell-as-MMIO-BAR
description and the 512-queues-per-4K-page figure come from the **Linux kernel** `amdgpu`
documentation.

**Tooling:** `rocprofv3` subcommands and flags, the per-dispatch output columns (`VGPR_Count`,
`SGPR_Count`, `LDS_Block_Size`, `Scratch_Size`, `Grid_Size`, `Workgroup_Size`), the agent-info field
names, `rocprofv3-avail pmc-check`, the `/dev/kfd` permission note, and the entire
`rocprof-compute` roofline workflow including its two-stage profile, `--no-roof` / `--roof-only` /
`--bench-only`, and the `roofline.csv` + `sysinfo.csv` + `log.txt` artefacts.

**MFMA:** the intrinsic syntax, the wavefront-wide semantics, the four access routes in AMD's stated
order of preference (including the caveat that built-ins may change between releases), the
`f32_16x16x4f32` worked example with its (16,4) thread block and 2/4 register counts, and the
matrix-instruction calculator's five modes.

**The CDNA 3 instruction table in §7 was extracted programmatically from AMD's own
`amd_matrix_instruction_calculator` source**, including the cycle counts and the `v_smfmac_*` sparse
family. Shapes, data types and cycles are as that source states them.

**Triton:** the TTIR → TTGIR → LLVM IR → AMDGCN → `hsaco` pipeline, the `make_ttgir` / `make_llir` /
`make_amdgcn` / `make_hsaco` stage functions, `translateLLVMIRToASM` with the
`amdgcn-amd-amdhsa` triple, and the Inductor variables (`TORCHINDUCTOR_MAX_AUTOTUNE`,
`TORCHINDUCTOR_FREEZING`, `TORCH_COMPILE_DEBUG`, the `TRITON,ATEN,NV` default for
`max_autotune_gemm_backends` and the note that Triton is skipped when rocBLAS/MIOpen is faster) come
from ROCm documentation and the ROCm blog. **The Inductor guidance was published against ROCm 6.1
documentation — re-verify against your installed version.**

### Community, secondary, or third-party

The `~/.triton/cache` artefact listing and the `GPUTarget("hip", "gfx942", 64)` invocation come from
a Triton-contributor blog and a community wiki, not AMD · the `gfx`-target-to-generation table in §14
combines AMD's calculator source (CDNA rows, which I verified directly) with a **community wiki** for
the RDNA rows and the `gfx950` MXFP characterisation · the five-step `hipLaunchKernelGGL` → ROCclr →
AQL → HSA queue → ACE sequence is corroborated by an academic paper on AMD GPU scheduling, which is
also the source for the ROCclr layering description · the ROCt/ROCr split description comes from a
community wiki · **the MI300X roofline finding in §9 (all prefill kernels on the HBM roof,
1–3 FLOP/byte, ~10 TFLOP/s at ~15 FLOP/byte) is a single third-party blog measurement on one
workload — directional only, and explicitly not an AMD figure.**

### Not verified here — do not treat as fact

**CDNA 4 MFMA instruction names and shapes.** The calculator snapshot I parsed covers CDNA 1–3 and
RDNA 3–4 but contains **no CDNA 4 entries**, so §7's table stops at CDNA 3. `gfx950` appears in §14
only as a target identifier. If you need the CDNA 4 instruction set, pull the current calculator
release and re-run the query — do not extrapolate from the CDNA 3 table.

Specific `num_stages` values are **deliberately omitted**: the sources I found gave conflicting
guidance, so §8 points at the documentation instead of quoting a number.

The occupancy-limiter list in §5 names the right resources, but **exact per-architecture register
file sizes, LDS capacity and maximum waves per SIMD are not quoted** — read them from `rocminfo` and
the `rocprofv3` agent table on your own hardware, which is more reliable than any table here.

**Environment-variable value ranges.** `AMD_LOG_MASK`'s `LOG_AQL = 0x00000008` bit is sourced, but
the accepted numeric ranges for `AMD_LOG_LEVEL` and `AMD_SERIALIZE_KERNEL` are **not** verified
here — check them for your ROCm version rather than trusting the values in the examples.

**Coalescing, bank conflicts and the padding fix (§6)** are stated as general GPU-architecture
principles rather than quoted from an AMD document. They are standard and correct, but the specific
transaction widths and bank counts for your part are not given and should be read from the ISA
guide for that architecture.

---

## Primary sources

**Compilation**
- HIP compilers (7.0.2) — <https://rocm.docs.amd.com/projects/HIP/en/docs-7.0.2/understand/compilers.html>
- HIP compilers (6.4.3), incl. the flag table and `hsaco` vs `cubin`/PTX —
  <https://rocm.docs.amd.com/projects/HIP/en/docs-6.4.3/understand/compilers.html>
- HIP porting: driver API and code-object formats —
  <https://rocm.docs.amd.com/projects/HIP/en/docs-6.3.2/how-to/hip_porting_driver_api.html>
- Clang HIP support (HIPAMD toolchain, RDC modes, macros) —
  <https://rocm.docs.amd.com/projects/llvm-project/en/latest/LLVM/clang/html/HIPSupport.html>
- Clang offloading design —
  <https://rocm.docs.amd.com/projects/llvm-project/en/latest/LLVM/clang/html/OffloadingDesign.html>

**Dispatch and runtime**
- AMDGPU Compute ABI (AQL queues, packet processor, dispatch sequence) —
  <https://github.com/RadeonOpenCompute/ROCm-ComputeABI-Doc/blob/master/AMDGPU-ABI.md>
- Linux kernel `amdgpu` user-mode queues (MQD/HQD, doorbells) —
  <https://kernel.org/doc/html/latest/gpu/amdgpu/userq.html>
- *Exploring AMD GPU Scheduling Details* (academic) —
  <https://par.nsf.gov/servlets/purl/10385873>

**Matrix cores**
- AMD matrix cores, lab notes — <https://gpuopen.com/learn/amd-lab-notes/amd-lab-notes-matrix-cores-readme/>
- AMD Matrix Instruction Calculator — <https://github.com/ROCm/amd_matrix_instruction_calculator>
- Matrix core programming on CDNA 3 / CDNA 4 (third-party) — <https://salykova.github.io/matrix-cores-cdna>

**Triton and Inductor**
- Kernel development and optimisation with Triton on AMD (ROCm blog) —
  <https://rocm.blogs.amd.com/software-tools-optimization/kernel-development-optimizations-with-triton-on-/README.html>
- Optimizing Triton kernels + Inductor knobs (ROCm 6.1 docs) —
  <https://rocm.docs.amd.com/en/docs-6.1.0/how-to/llm-fine-tuning-optimization/optimizing-triton-kernel.html>
- Triton AMD HIP backend (community wiki) — <https://deepwiki.com/triton-lang/triton/5.7-amd-hip-backend>
- Triton compiler development tips (community) — <https://www.lei.chat/posts/triton-compiler-development-tips/>

**Profiling**
- ROCprofiler-SDK quick reference —
  <https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-7.14.0/quick-reference/quick_guide.html>
- Using `rocprofv3` — <https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-6.4.0/how-to/using-rocprofv3.html>
- ROCm Compute Profiler, profile mode —
  <https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/how-to/profile/mode.html>

---

*Compiled 2026-09-05. Companion to [`AMD-AI-STACK.md`](AMD-AI-STACK.md). Tool names and flags in the
ROCm ecosystem change between releases — re-verify anything you are about to depend on.*
