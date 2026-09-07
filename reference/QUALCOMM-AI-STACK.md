# The Qualcomm AI Stack — Model to Hardware

**Written for someone who has never seen this before.** Every layer explained, every arrow labelled,
every name decoded.

**Sources:** Qualcomm's own documentation, checked 2026-09-04. Items that come from community
analysis rather than vendor documentation are marked, and Section 14 lists exactly what is verified
and what is not.

**Where this fits:** supporting reference for the roadmap's Section 10.17 (model-to-hardware
specialisation track), Stage 6 — edge, NPU and client AI inference.

---

## Contents

| § | Section |
|---|---|
| 1 | The 30-second version |
| 2 | The whole stack, one picture |
| 3 | **Name decoder — read this first** |
| 3B | **The five backends, and the one rule that picks one** |
| 4 | The offline pipeline — preparing the model |
| 5 | **Graph partitioning — what decides your performance** |
| 6 | Inside the Hexagon NPU |
| 6B | **Heterogeneous execution — which engine runs what** |
| 7 | The complete journey — one worked example |
| 8 | Which door do I use? |
| 9 | Genie — the LLM layer |
| 10 | The datacenter branch |
| 11 | If you already know CUDA or ROCm |
| 12 | The mistakes everyone makes |
| 13 | Learning order |
| 14 | Verification status |

---

## 1. The 30-second version

You have a trained model. It is a file full of numbers. You want it to run fast on a phone.

```
   YOUR MODEL                                        THE CHIP
   (a PyTorch file)                                  (a phone SoC)
        │                                                 ▲
        │        ┌──────────────────────────────┐         │
        └───────►│  Everything in this document │─────────┘
                 └──────────────────────────────┘
                   translates one into the other
```

There are **two halves** to that translation, and confusing them is the most common beginner
mistake:

```
┌─────────────────────────────┐      ┌─────────────────────────────┐
│  OFF-DEVICE (your laptop)   │      │  ON-DEVICE (the phone)      │
│                             │      │                             │
│  Shrink the model and       │ ───► │  Load it and run it,        │
│  compile it for the chip    │      │  millions of times          │
│                             │      │                             │
│  Slow. Happens once.        │      │  Fast. Happens forever.     │
│  Tools: AIMET, QAIRT tools  │      │  Runtime: QNN, Genie        │
└─────────────────────────────┘      └─────────────────────────────┘
```

---

## 2. The whole stack, one picture

Read it **top to bottom** — that is the path your data travels.

```
╔═══════════════════════════════════════════════════════════════════════╗
║  LAYER 6 — YOUR APPLICATION                                           ║
║  ─────────────────────────────                                        ║
║  A camera app · a chatbot · a translator                              ║
║  Helpers: QAI AppBuilder · IM SDK                                     ║
╠═══════════════════════════════════════════════════════════════════════╣
║  LAYER 5 — GENAI FRAMEWORK          "run an LLM without the pain"     ║
║  ─────────────────────────                                            ║
║  Genie:  GeniePipeline → GenieEngine                                  ║
║          handles tokeniser · KV cache · sampling · multi-turn chat    ║
║  Tools:  genie-t2t-run · genie-profile · genie-app                    ║
╠═══════════════════════════════════════════════════════════════════════╣
║  LAYER 4 — FRAMEWORK DOORS          "how your model gets in"          ║
║  ─────────────────────────                                            ║
║   ONNX Runtime      LiteRT          ExecuTorch       Windows ML       ║
║   (QNN EP)          (QNN delegate)  (Qualcomm        (auto-downloads  ║
║                                      backend)         the QNN EP)     ║
║        └────────────────┴─────────────────┴───────────────┘           ║
║                    all four funnel into ↓                             ║
╠═══════════════════════════════════════════════════════════════════════╣
║  LAYER 3 — QNN  (Qualcomm AI Engine Direct)   THE UNIFIED API         ║
║  ──────────────────────────────────────────                           ║
║  Objects:  Backend → Device → Context → Graph → Op Registry           ║
║  Does:     graph optimisation                                         ║
║  Does NOT: model parsing, network partitioning  ← left to Layer 4     ║
╠═══════════════════════════════════════════════════════════════════════╣
║  LAYER 2 — BACKEND LIBRARIES     "one .so implements the QNN API"     ║
║  ───────────────────────────                                          ║
║   libQnnHtp     libQnnGpu     libQnnCpu   │  libQnnSaver   IR backend ║
║   ↓ NPU         ↓ GPU         ↓ CPU       │  ↓ records     ↓ emits    ║
║   QUANTISED     FLOAT         FLOAT       │    API calls     a DLC    ║
║   models only   models        reference   │                           ║
║   → PRODUCTION  + pre/post    → VALIDATE  │  ← THESE TWO EXECUTE      ║
║                                           │    NOTHING                ║
╠═══════════════════════════════════════════════════════════════════════╣
║  LAYER 1 — SILICON                                                    ║
║  ─────────────────                                                    ║
║   ┌───────────────┐  ┌───────────────┐  ┌─────────────────────────┐   ║
║   │  Kryo/Oryon   │  │    Adreno     │  │  HEXAGON NPU  (HTP)     │   ║
║   │     CPU       │  │     GPU       │  │  ← where quantised AI   │   ║
║   │               │  │  (OpenCL)     │  │    wants to run         │   ║
║   └───────────────┘  └───────────────┘  └─────────────────────────┘   ║
╚═══════════════════════════════════════════════════════════════════════╝
```

Three things in that Layer 2 row trip people up, so they are called out here and explained in full
in §3B:

1. **"One `.so` per backend" is the software view, not the file count.** The HTP backend alone is
   delivered as *several* cooperating libraries — a CPU-side backend, a CPU-side stub, and a
   skeleton library that runs on the DSP itself. §3B has the chain.
2. **Saver and the IR backend implement the QNN API but never run your model.** They are tools
   wearing a backend costume, which is why they can be dropped in without changing your code.
3. **The GPU is a real inference backend, not a pre-processing helper.** It runs whole models in
   FP32/FP16. Pre- and post-processing is its *second* job. Believing otherwise is the single most
   common misconception about this stack — see §3B and §12, mistake 8.

---

## 3. Name decoder — read this before anything else

Qualcomm renamed things over the years and **the old names are still everywhere in filenames**.
This table prevents hours of confusion.

| Name you will see | What it really is | Alive? |
|---|---|---|
| **QAIRT** (Qualcomm AI Runtime SDK) | The **whole SDK box**. Contains the three below | current |
| **QNN** / **Qualcomm AI Engine Direct** | The **low-level API** inside the box | current |
| **SNPE** / Neural Processing SDK | The older high-level SDK | folded into QAIRT |
| **Genie** | GenAI / LLM framework inside the box | current |
| **AIMET** | Off-device quantisation toolkit | current |
| **HTP** (Hexagon Tensor Processor) | Hexagon NPU **with** the fused AI accelerator | current |
| **cDSP** | Hexagon NPU **without** the accelerator | older chips |
| **HTA** | Standalone tensor accelerator | legacy |

> **Why "QNN" is everywhere if QAIRT is the current name:** QNN is the *layer*; QAIRT is the *box it
> ships in*. You will type `QnnHtp.dll` and `QNNExecutionProvider` constantly. Both names are
> correct — they describe different things.

**The three compute engines**, as Qualcomm's own developer-workflow documentation names them:

| Engine | Brand | Role in AI |
|---|---|---|
| CPU | Kryo (Oryon on newer parts) | Fallback, control, small ops |
| GPU | Adreno | **Runs whole models in FP32/FP16 via OpenCL**; also pre/post-processing |
| **NPU** | **Hexagon (HTP)** | **Low power, high performance — needs quantised models** |

---

## 3B. The five backends, and the one rule that picks one

If you read only one section of this document, read this one. It is the material that was missing
when people kept asking "so does Qualcomm use the GPU for AI or not?"

### First, what a backend actually is

Qualcomm's definition, near-verbatim: a QNN backend is **a software entity that implements the QNN
API, typically compiled as a shared library**. "QNN backend" and "QNN backend library" are used
interchangeably.

So QNN is only a contract — a list of function names. A backend is code that honours the contract.
Qualcomm ships several, they all speak the same API, and **your application picks one**. That is why
switching engines is a one-string change rather than a rewrite.

```
        your app calls the QNN API
                    │
      "which library implements it today?"
                    │
   ┌──────┬─────────┼─────────┬────────┐
   ▼      ▼         ▼         ▼        ▼
  Htp    Gpu       Cpu      Saver     IR
```

### The five, and the split that matters

| Backend | Library | Targets | Model it accepts | Use it for |
|---|---|---|---|---|
| **HTP** | `libQnnHtp.so` / `QnnHtp.dll` | Hexagon NPU | **quantised only** | production |
| **GPU** | `libQnnGpu.so` / `QnnGpu.dll` | Adreno GPU | **float** (FP32/FP16) | float models, pre/post |
| **CPU** | `libQnnCpu.so` / `QnnCpu.dll` | Kryo/Oryon CPU | **float** | correctness reference |
| **Saver** | `libQnnSaver.so` / `QnnSaver.dll` | *nothing* | any | debugging, support tickets |
| **IR** | selected as `--backend ir` | *nothing* | any | emit a DLC |

The bottom two rows are the structural surprise. Qualcomm says of Saver that it "is a backend in the
sense that it is a shared library that implements all QNN APIs, but **unlike all other backends,
Saver does not execute any graphs.** Instead, it records all QNN API calls and their arguments into
files which can be replayed on any QNN backend."

The IR backend likewise produces a **DLC file** rather than a result — in the AI Engine Direct
Delegate flow it is selected with `--backend ir` plus `--ir_dlc_path`.

```
  REAL BACKENDS                        TOOLS IN A BACKEND COSTUME
  ─────────────                        ──────────────────────────
  in  → your tensors                   in  → your QNN API calls
  out → computed tensors               out → a .c/.bin trace  (Saver)
                                             a .dlc file      (IR)
```

> **Why fake backends at all?** Because they need zero code changes. Point `backend_path` at
> `QnnSaver.dll` instead of `QnnHtp.dll` and your unmodified app dumps a perfect, replayable record
> of everything it asked QNN to do. That is the fastest way to hand Qualcomm a reproducible bug.

### THE RULE: precision picks the backend

This is a hard compatibility constraint from Qualcomm's own quantisation documentation, not a
performance preference:

| Backend | Requirement, in Qualcomm's words |
|---|---|
| **CPU** | "Choose a non-quantized model. Quantized models are currently **incompatible** with the CPU backend." |
| **GPU** | "Choose a non-quantized model. Quantized models are currently **incompatible** with the GPU backend." |
| **HTP** | "Choose a quantized model. Quantized models are **required** when running on the HTP backend." |
| **DSP** | quantised model required |
| **HTA** | quantised model required |

ONNX Runtime states the HTP half identically: "The QNN HTP backend only supports quantized models."

So the decision tree has nothing to do with speed:

```
  Is your model fully quantised to integer (QDQ)?
        │
        ├── YES ──►  HTP is your ONLY option.
        │            GPU and CPU backends will not take it.
        │
        └── NO (still float) ──►  GPU or CPU.
                     HTP will not take it.
```

**The NPU eats integers. The GPU and CPU eat floats.** They are not a fast lane and a slow lane —
they accept different input. Almost every "why won't my model load on the NPU / why is it on the
CPU" question resolves to this one table.

### The nuance that stops this being a lie

Two refinements, both worth knowing before you quote the rule as absolute:

**1. Weight-only quantisation works on the GPU.** ONNX Runtime: the GPU backend runs FP32/FP16
models without prior quantisation, and "to help reduce the size of large models, **quantizing
weights to `uint8`, while keeping activations in float, is also supported**." So you can get most of
the size saving without the full integer conversion. What the GPU refuses is a *fully* quantised
graph with integer activations.

**2. The Adreno hardware does support INT8.** Qualcomm's own generative-AI whitepaper says the
Adreno GPU is "designed for parallel processing AI in high precision formats, supporting 32-bit
floating point (FP32), 16-bit floating point (FP16), and 8-bit integer (INT8)." The restriction in
the table above is a property of the **QNN GPU backend's model intake**, not a claim that Adreno
silicon cannot do integer maths. Keep those two statements separate or you will confuse yourself.

### How the NPU is actually reached — the library chain

"One `.so` and you're on the NPU" is wrong, and knowing why explains several otherwise baffling
deployment errors. Qualcomm documents the HTP backend as a set of cooperating libraries:

```
  Your app  (running on the Kryo/Oryon CPU)
      │
      ▼
  libQnnHtp.so            CPU-side backend library.
      │                   Picks the right stub for this SoC.
      ▼
  libQnnHtpV##Stub.so     CPU-side PROXY. Talks to the DSP.
      │                   (## = Hexagon version: 68/69/73/75/79/81)
      │
      │   ═══ RPC channel ═══   (FastRPC: libcdsprpc.so,
      │                          DSP firmware, kernel driver)
      ▼
  libQnnHtpV##Skel.so     Runs ON the Hexagon DSP side.
      │                   "responsible for executing graphs on the
      ▼                    HTP accelerator as a proxy for CPU side backend"
  Hexagon HTP hardware
```

Two more libraries appear in real deployments:

- **`libQnnHtpPrepare.so`** — composes and finalises graphs on the device CPU side. Qualcomm notes
  it is loaded automatically by the HTP backend *only* when you validate an op config, add a node,
  finalise a graph, or register an op package for the CPU target. If you ship a pre-built context
  binary and never do those things, **it does not need to be on the device.**
- **`libQnnSystem.so`** — required to interpret a cached context binary. If you ship `.bin` files,
  you ship this too.

There is also **`libQnnHtpV##.so`**, described as an "HTP native backend library that allows direct
integration on HTP without RPC" — for code already running on the DSP.

**Why you should care:** this is the deepest structural difference from a GPU stack. On a GPU the
CPU enqueues work to a device in the same address space. Here, your CPU makes a **remote procedure
call into a separate DSP subsystem** with its own firmware and its own library search path. That is
what `ADSP_LIBRARY_PATH` is for, and it is why a missing skeleton library fails at runtime with an
error that looks nothing like "file not found."

### Choosing a backend in code

ONNX Runtime QNN EP gives you two equivalent ways. Prefer `backend_type` — it is platform-neutral:

```python
provider_options = [{"backend_type": "htp"}]     # 'cpu' | 'gpu' | 'htp' | 'saver'
# or
provider_options = [{"backend_path": "QnnHtp.dll"}]   # explicit file, platform-specific
```

`htp` is the default. Qualcomm's ORT documentation is explicit that **`backend_path` is an
alternative to `backend_type` and at most one of the two should be specified.**

In Genie it is a configuration field:

```
backend::type =  QnnHtp                 # the NPU (HTP)
                 QnnGenAiTransformer    # transformer-specialised path
                 QnnGpu                 # Adreno
```

### Availability is platform-dependent — check before you plan

Do not assume all three hardware backends exist on your target. Qualcomm's Windows-on-Snapdragon AI
overview says QNN "currently ... allows access to the **CPU and Qualcomm® Hexagon Tensor Processor**
hardware for unquantized and quantized models" — the GPU is not named in that sentence. On the same
page the Adreno GPU is described as "suitable to execute AI workloads with medium-power and
medium-performance ... accelerated with OpenCL kernels," and separately as usable for pre/post-processing.

The practical reading: on some platforms the GPU-for-AI route is **LiteRT's OpenCL GPU delegate or
the Adreno OpenCL ML SDK rather than `libQnnGpu.so`**. Both are genuine GPU AI paths to the same
silicon; they are different software routes. Verify which exists for your SoC, OS and QAIRT version
instead of assuming the full CPU/GPU/HTP trio is always present.

---

## 4. The offline pipeline — preparing the model

All of this happens on **your laptop**, once.

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  STEP 0 — you have a trained model                               │
  │  PyTorch · TensorFlow · ONNX                                     │
  └──────────────────────────────┬───────────────────────────────────┘
                                 ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │  STEP 1 — AIMET:  make it small enough to run on the NPU         │
  │                                                                  │
  │   float32 weights ──► 8-bit or 4-bit integers                    │
  │                                                                  │
  │   Recommended order:                                             │
  │     1. AutoQuant        <- start here, wraps the rest            │
  │     2. CLE              <- equalise weight ranges across layers  │
  │     3. AdaRound         <- learn the rounding, don't just round  │
  │     4. BN re-estimation <- fix BatchNorm stats before folding    │
  │     5. QAT              <- only if 1-4 aren't enough             │
  │        (bias correction is DEPRECATED - use AdaRound)            │
  │                                                                  │
  │   OUT:  model_qdq.onnx  +  encodings.json                        │
  └──────────────────────────────┬───────────────────────────────────┘
                                 ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │  STEP 2 — qairt-converter                                        │
  │  framework model + encodings.json  ──►  model.dlc                │
  └──────────────────────────────┬───────────────────────────────────┘
                                 ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │  STEP 3 — qairt-quantizer                                        │
  │  model.dlc  ──►  model_quant.dlc                                 │
  └──────────────────────────────┬───────────────────────────────────┘
                                 ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │  STEP 4 — qnn-context-binary-generator      /!\ SoC-SPECIFIC     │
  │  model_quant.dlc  ──►  model.bin                                 │
  └──────────────────────────────┬───────────────────────────────────┘
                                 ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │  STEP 5 — run it on the device                                   │
  │  qnn-net-run                                                     │
  └──────────────────────────────────────────────────────────────────┘
```

### The actual commands

```bash
# STEP 2 — framework model to DLC, injecting AIMET's encodings
qairt-converter --input_network model.onnx \
                --quantization_overrides encodings.json \
                --output_path model.dlc

# STEP 3 — float DLC to quantised DLC
qairt-quantizer --input_dlc model.dlc \
                --output_dlc model_quant.dlc \
                --float_fallback            # FP32 for ops without encodings

# STEP 4 — quantised DLC to HTP context binary (ahead-of-time compile)
qnn-context-binary-generator --model libQnnModelDlc.so \
                             --backend libQnnHtp.so \
                             --dlc_path model_quant.dlc \
                             --output_dir out --binary_file model

# STEP 5 — execute on target
qnn-net-run --backend libQnnHtp.so --retrieve_context out/model.bin
```

`qairt-quantizer` can also call AIMET directly, via `--use_aimet_quantizer` and
`--apply_algorithms adaround`.

> **Check `qnn-context-binary-generator --help` against your installed SDK before copying step 4.**
> The flag surface for the DLC path has moved across QAIRT releases: some flows pass a model library
> via `--model` alongside `--dlc_path`, while others take `--dlc_path` alone. Community tooling also
> reports that `--binary_file` takes a bare name because the tool appends `.bin` itself. Treat the
> command above as the shape of the step, not as a version-stable invocation. **UNVERIFIED** against
> the current SDK at the time of writing.

### The three model formats — and what you trade

```
 LIBRARY (.so)          DLC (.dlc)              CONTEXT BINARY (.bin)
 ─────────────          ──────────              ─────────────────────
 portable across        portable across         LOCKED to one SoC /
 backends               backends                HTP architecture
 compiles at runtime    compiles at runtime     PRE-COMPILED
                                                -> fastest startup
                                                -> needs libQnnSystem
```

> **The trade in one sentence:** a context binary removes runtime compilation but stops being
> portable. Ship it for the wrong chip and it will not load.

> **File portability is NOT backend compatibility — do not confuse the two.** A `.so` or `.dlc`
> can be handed to any backend, but §3B's precision rule still decides whether that backend will
> accept the *contents*. A **quantised** DLC will not run on the GPU or CPU backend, and a **float**
> DLC will not run on HTP. "Portable" here means the container format travels; it does not mean
> every engine can execute what is inside it.

---

## 5. Graph partitioning — the concept that decides your performance

Your model is a chain of operations. **The NPU cannot run all of them.** The runtime cuts your graph
into pieces and assigns each piece to hardware that can handle it.

```
  YOUR MODEL                          WHAT ACTUALLY HAPPENS
  ──────────                          ─────────────────────

  Conv ──┐                            ┌─ Conv ─┐
  ReLU   │                            │  ReLU  │  PARTITION 1 -> NPU  ok
  Conv   │                            │  Conv  │
  ReLU   │  ─── partitioner ───►      └────────┘
  ???    │      decides                    │ data leaves the NPU  COST
  Conv   │                            ┌─ ??? ──┐  PARTITION 2 -> CPU  bad
  ReLU   │                            └────────┘  (unsupported op)
  Softmax┘                                 │ data returns to the NPU  COST
                                      ┌─ Conv ─┐
                                      │  ReLU  │  PARTITION 3 -> NPU  ok
                                      │ Softmax│
                                      └────────┘
```

**Every boundary costs a round trip off the accelerator.** So:

```
  1 partition,  slightly slow kernels   ->  FAST
 11 partitions, perfectly tuned kernels ->  SLOW
```

> **This is why "the NPU is slow" is almost never about the NPU.** It is about how many times your
> data had to leave it. **Read the partition report first, before optimising anything.**

**Who does the partitioning?** Layer 4, not QNN. Qualcomm's documentation is explicit that QNN
handles graph optimisation internally but leaves **model parsing and network partitioning to
higher-level frameworks**. That is why ExecuTorch's `QnnPartitioner` exposes `skip_node_id_set`,
`skip_node_op_set` and `skip_mutable_buffer` — so you can override its choices by hand when the
automatic decision is wrong.

---

## 6. Inside the Hexagon NPU

The NPU is **not a small GPU**. It is four cooperating units.

```
╔════════════════════════════════════════════════════════════════════╗
║                     HEXAGON NPU  (HTP)                             ║
║                                                                    ║
║   ┌──────────────────────────────────────────────────────────┐     ║
║   │  SCALAR CORE                                             │     ║
║   │  The manager. Runs program logic, schedules threads,     │     ║
║   │  kicks off DMA — then goes back to idling.               │     ║
║   └──────────────────────────────────────────────────────────┘     ║
║                                                                    ║
║   ┌────────────────────────────┐  ┌────────────────────────────┐   ║
║   │  HVX — Vector unit         │  │  HMX — Matrix unit         │   ║
║   │  1024-bit SIMD             │  │  Systolic array            │   ║
║   │  128 x INT8 per instruction│  │  INT4/INT8/INT16/FP16 GEMM │   ║
║   │                            │  │                            │   ║
║   │  DOES:                     │  │  DOES:                     │   ║
║   │  activations (SiLU, GeLU)  │  │  every matrix multiply     │   ║
║   │  normalisation, RoPE       │  │  every weight projection   │   ║
║   │  residual adds             │  │                            │   ║
║   │  -> anything elementwise   │  │  <- THIS is where the      │   ║
║   │                            │  │     speed lives            │   ║
║   └────────────────────────────┘  └────────────────────────────┘   ║
║                     ▲                        ▲                     ║
║                     └──────────┬─────────────┘                     ║
║                                │                                   ║
║   ┌────────────────────────────┴─────────────────────────────┐     ║
║   │  VTCM / TCM  —  ~8 MB software-managed on-chip SRAM      │     ║
║   │  (+ ~1 MB L2 cache)                                      │     ║
║   │  Fast scratchpad. The compiler manages it explicitly.    │     ║
║   └────────────────────────────┬─────────────────────────────┘     ║
║                                │                                   ║
║   ┌────────────────────────────┴─────────────────────────────┐     ║
║   │  DMA ENGINE — moves tiles between DDR and VTCM           │     ║
║   └──────────────────────────────────────────────────────────┘     ║
╚════════════════════════════════════════════════════════════════════╝
                                 ▲
                                 │  slow, far away
                    ┌────────────┴────────────┐
                    │   DDR  (main memory)    │
                    └─────────────────────────┘
```

### The single most important idea: overlap

VTCM is small (~8 MB). A single 4096x4096 FP16 weight tensor is 32 MB — it does not fit. So the
compiler **slices work into tiles** and streams them through.

```
  BAD — no overlap (you lose roughly half your performance)

  DMA:     [load tile 1]              [load tile 2]              [load 3]
  HMX:                    [compute 1]               [compute 2]
           └──── idle ────┘           └─── idle ───┘


  GOOD — overlapped (this is the goal)

  DMA:     [load 1][load 2][load 3][load 4][load 5]
  HMX:             [comp 1][comp 2][comp 3][comp 4]
                   └── HMX never waits ──┘
```

### The performance cliff you must not fall off

```
  Your matmul's data types
            │
            ├── in HMX's supported set?  ──► YES ──► full speed
            │
            └── not in the set?          ──► NO  ──► falls back to HVX
                                                     roughly 300x slower
```

That 300x figure is **community-reported**, citing published work — it is not a Qualcomm number.
But the *direction* is certain, and it is the whole reason quantisation is mandatory rather than
optional on this hardware.

### Bottleneck priority order

```
  DMA throughput  >  VTCM capacity  >  HMX utilisation  >  operator support
  ────────────────────────────────────────────────────────────────────────►
  fix this first                                        then worry about this
```

*(Community analysis, not a vendor statement — but it matches the architecture.)*

### A note on Hexagon versions

Hexagon generations **v73 / v75 / v79 / v81** exist, and newer versions add real capability — one
source reports byte-granularity VTCM reservation arriving in v81, which matters for fitting large
models.

**However, sources actively conflict on which version ships in which chip.** Verify the version for
your specific part against Qualcomm's own documentation. Also note that HMX's instruction-level
microarchitecture is **not publicly documented** — QNN generates those instructions internally, so
any description of specific systolic-array dimensions is community inference, not vendor spec.

---

## 6B. Heterogeneous execution — which engine runs what

A Snapdragon SoC is not "a CPU plus an NPU." It is several engines on a shared memory system, and
Qualcomm's own framing is explicit: Genie "orchestrates execution across heterogeneous compute
units (CPU, GPU, NPU)."

| Engine | Name | Strength | Typical AI role |
|---|---|---|---|
| **CPU** | Kryo / **Oryon** | flexibility, mature libraries, large caches | control flow, unsupported ops, small GEMMs, correctness reference |
| **GPU** | **Adreno** | wide FP throughput, FP32/FP16/hybrid precision modes | **full float-model inference**; also image/vision pre- and post-processing |
| **NPU** | **Hexagon** | matrix throughput per watt | quantised, static-shape, sustained workloads |

> **Correction worth internalising:** earlier drafts of this table credited the GPU with *dynamic
> shapes*. That is **not supported** by the ONNX Runtime QNN EP documentation, which states the EP
> "does not support models with dynamic shapes" and that, apart from the quantised-model
> requirement, "all other requirements are valid for the GPU backend also." **Fixed shapes are
> required on every QNN backend, GPU included.** The GPU's genuine advantages are float support and
> skipping quantisation — not shape flexibility.

### How much AI can the GPU really do?

Enough that "Qualcomm doesn't use the GPU for AI" is simply false. Qualcomm's own generative-AI
whitepaper counts the Adreno GPU as one of the engines making up the **Qualcomm AI Engine**
(alongside the Hexagon NPU, the Kryo/Oryon CPU, the Sensing Hub and the memory subsystem), and cites
**Llama 2-7B generating more than 13 tokens per second on the Adreno GPU**.

A 7-billion-parameter language model is not pre-processing. The accurate framing is a three-tier one,
matching Qualcomm's own "medium-power, medium-performance" description of the GPU:

```
  NPU (HTP)     highest perf/watt, integers only     ← ship quantised models here
  GPU (Adreno)  medium power, medium perf, floats    ← ship float models here
  CPU           lowest perf, floats, always works    ← reference and fallback
```

You select the engine per graph. In Genie it is a configuration field, not a code change:

```
backend::type =  QnnHtp                 # the NPU (HTP)
                 QnnGenAiTransformer    # transformer-specialised path
                 QnnGpu                 # Adreno
```

The `genie-t2t-run` CLI runs LLM inference on **CPU, GPU or HTP** backends, so switching engines to
compare is genuinely a one-line experiment. Do that experiment — because the results are not what
marketing slides imply.

### The uncomfortable evidence: the NPU is not always faster

Two 2026 arXiv preprints benchmarked this properly, and **they disagree with each other**. That
disagreement is the most useful thing in this section, so here it is undisguised.

*(Both are academic preprints, not Qualcomm documentation. Different chips, different models.)*

| | **Study A** — Snapdragon 8 Gen 3, LLM | **Study B** — Snapdragon 8 Elite (SM8750), VLM |
|---|---|---|
| **Prefill** on NPU | **slower** — CPU won by 1.27–1.62× | **1.64× faster** than CPU |
| **Decode** on NPU | 1.05–1.20× faster | 1.18× faster |
| **Vision encoder** on NPU | not measured | **20–45× faster** than CPU |
| **Energy** | up to **51% higher** with more NPU offload | **2.52× lower** |

**What they agree on:** NPU gains in the **decode** phase are small — 1.05–1.20× and 1.18×
respectively. Both studies, independently, on different silicon.

**Why they disagree on prefill** is almost certainly the workload. Study A ran LLM prefill, where
Study A's authors credit the CPU's "mature GEMM libraries and larger caches." Study B ran a
vision-language model, whose prefill is dominated by a vision encoder — the exact dense,
static-shape, quantisation-friendly workload an NPU is built for. The 20–45× encoder speedup and
the 51% LLM energy regression are **both true**, of different things.

> **The lesson to carry into an interview:** "Does the NPU help?" is not a hardware question, it is
> a **per-stage, per-operator** question. Answer it with a measurement, per phase, on the target
> device.

### Three reasons NPU offload underdelivers — and what to do

**1. Dispatch latency dominates small operators.** Study A found lightweight operators with
**call-time to op-time ratios of 8–22×** — the cost of *invoking* the operator was up to 22 times
the operator's own work. Their guideline: get dispatch below **10 µs**, via batched dispatch,
persistent command queues, or **operator fusion**.
→ *Your lever:* fuse aggressively; do not send tiny ops to the NPU one at a time.

**2. Operator coverage gaps force fallback.** Study A calls out FlashAttention specifically as an
operator that should be on the NPU and often is not. Every unsupported op is a partition boundary
and a round trip — which is §5's graph-partitioning problem showing up as a measured regression.
→ *Your lever:* check the partition report **before** optimising anything else.

**3. Unsupported architectures never reach the NPU at all.** Study B reports that a **four-step
graph rewrite** brought previously unsupported encoders (such as Phi-3.5-V) onto the QNN path for
up to **22× speedup**.
→ *Your lever:* rewriting the graph to fit the backend often beats tuning the backend.

### The NPU's real, reliable win: thermals and energy

Latency is the wrong headline metric for on-device AI. Study B measured, on the same work, a
**10.47 °C lower steady-state temperature** across 100 runs and **2.52× lower energy** — and
crucially, that **avoided thermal throttling in always-on settings**.

That is the argument that matters on a phone. A GPU path that is 10% faster for thirty seconds and
then throttles loses to an NPU path that holds its rate indefinitely. Sustained throughput under
thermal limits is the number to report, not peak.

### Adreno Neural Fusion — announced, not shipped

On **2 September 2026** Qualcomm disclosed the GPU architecture for its next premium Snapdragon
platform, named **Adreno Neural Fusion**. It matters to this document because it moves AI *into* the
graphics pipeline, which changes the tidy three-tier picture above.

```
  BEFORE                                  NEURAL FUSION
  ──────                                  ─────────────
  GPU renders the frame                   GPU renders the frame
        │                                       │
        ▼  cross-chip trip                      ▼  stays in the slice
  NPU runs the AI upscaler                Adreno Matrix Cores run it,
        │                                 reading the same on-chip
        ▼                                 18 MB Adreno HPM
  back to the GPU
```

Reported specifics: **Adreno Matrix Cores** inside each of **three GPU slices clocked at 1.45 GHz**,
paired with **18 MB of Adreno High Performance Memory (HPM)**; up to **40% power improvement** with
the technology enabled, of which **12%** is attributed to HPM; native **Unity and Unreal** support.
Qualcomm has not named the Snapdragon SKU, and said further detail arrives at Snapdragon Summit,
**22–24 September 2026**.

> **Read the intended purpose carefully.** Neural Fusion's stated job is **AI-enhanced rendering** —
> super-resolution and frame generation, in the DLSS mould — not general model inference. Prior
> Adreno generations did spatial upscaling in fixed-function hardware (GSR v1) or temporal upscaling
> on general shader cores (GSR v2); the new part is dedicated AI hardware inside the graphics
> pipeline itself.

**UNVERIFIED, and important not to assume:** that QNN or QAIRT exposes Adreno Matrix Cores as a
general-purpose inference target you could point an arbitrary model at. Nothing in the current QNN
GPU backend documentation mentions Matrix Cores. Today the defensible statement is that **Neural
Fusion is rendering-pipeline silicon, not a replacement for HTP as your model-inference engine.**
Re-check after the Summit.

**Sourcing caveat:** every figure in this subsection comes from press coverage quoting Qualcomm's
blog and press materials, **not** from a Qualcomm page retrieved directly. Treat them as vendor
claims relayed second-hand. See §14.

---

## 7. The complete journey — one worked example

A photo classifier, from your laptop to a phone screen:

```
 1. You train MobileNet in PyTorch                       [your laptop]
       │  float32 weights, ~14 MB
       ▼
 2. AIMET quantises it to INT8                           [your laptop]
       │  ~3.5 MB. Accuracy checked on a real eval set.
       │  OUT: model_qdq.onnx + encodings.json
       ▼
 3. qairt-converter  ->  model.dlc                       [your laptop]
       ▼
 4. qairt-quantizer  ->  model_quant.dlc                 [your laptop]
       ▼
 5. qnn-context-binary-generator  ->  model.bin          [your laptop]
       │  /!\ compiled for ONE specific SoC
       ▼
 6. Ship model.bin inside your app                       [app store]
       ▼
 7. App opens an ONNX Runtime session with the QNN EP    [the phone]
       │  backend_path = "QnnHtp.dll"
       ▼
 8. Runtime partitions the graph and loads it onto HTP   [the phone]
       ▼
 9. Camera frame arrives                                 [the phone]
       │
       ├─ Adreno GPU: resize + colour convert (pre-processing)
       ├─ Hexagon NPU: the network itself
       │     DMA streams weight tiles DDR -> VTCM
       │     HMX does the convolutions
       │     HVX does the activations
       └─ CPU: argmax -> "golden retriever, 0.94"
       ▼
 10. Your UI shows the label
```

---

## 8. Which door do I use?

```
                    What framework is your model in?
                                 │
        ┌────────────────┬───────┴────────┬────────────────┐
        ▼                ▼                ▼                ▼
     ONNX            TF / LiteRT      PyTorch         Windows app
        │                │                │                │
        ▼                ▼                ▼                ▼
  ONNX Runtime      LiteRT QNN      ExecuTorch        Windows ML
    QNN EP           delegate     Qualcomm backend   (auto-fetches
        │                │                │            the QNN EP)
        │                │                │                │
        └────────────────┴────────┬───────┴────────────────┘
                                  ▼
                        QNN -> libQnnHtp -> NPU

  Doing LLMs?       ──►  skip all of the above, use GENIE
  Want zero setup?  ──►  use QUALCOMM AI HUB (hosted real devices)
```

### ONNX Runtime QNN EP — the most transferable door

```python
import onnxruntime as ort

opts = {"backend_type": "htp",                 # 'cpu' | 'gpu' | 'htp' | 'saver'
        "enable_htp_fp16_precision": "1",
        "htp_performance_mode": "high_performance"}

so = ort.SessionOptions()
so.add_session_config_entry("session.disable_cpu_ep_fallback", "1")   # see below

sess = ort.InferenceSession("model.qdq.onnx",  # QUANTISED — htp takes nothing else
                            sess_options=so,
                            providers=["QNNExecutionProvider"],
                            provider_options=[opts])
```

> **Set `disable_cpu_ep_fallback` to `1` during bring-up.** Without it, a silent fall back to the CPU
> looks exactly like "the NPU is slow," and people lose days to it.

**Two hard model requirements before any of this works**, both from the ONNX Runtime QNN EP
documentation:

1. **No dynamic shapes.** "QNN EP does not support models with dynamic shapes (e.g., a dynamic batch
   size). Dynamic shapes must be fixed to a specific value." This applies to *every* backend, GPU
   included.
2. **A subset of ONNX operators.** Loops and Ifs are explicitly not supported. Everything unsupported
   becomes a partition boundary — §5's problem, showing up as a measured regression.

### The provider options worth knowing

| Option | Values | Why you care |
|---|---|---|
| `backend_type` | `cpu` · `gpu` · `htp` · `saver` | Platform-neutral engine selection. `htp` is the default |
| `backend_path` | `QnnHtp.dll` / `libQnnHtp.so`, etc. | Explicit file. **Mutually exclusive with `backend_type`** |
| `htp_performance_mode` | `burst` · `balanced` · `default` · `high_performance` · `sustained_high_performance` · power-saver variants | `burst` for benchmarks, `sustained_high_performance` for always-on |
| `htp_graph_finalization_optimization_mode` | `0`–`3` | Higher = longer prepare, better graph. `3` is the most aggressive |
| `vtcm_mb` | size in MB | Defaults to `0` (not set). Ties directly to §6's VTCM tiling story |
| `htp_arch` + `soc_model` | e.g. `73`, `60` | Pin the target for offline preparation |
| `enable_htp_fp16_precision` | `0` · `1` | Default `1`: runs an FP32 model at FP16 precision on HTP |
| `offload_graph_io_quantization` | `0` · `1` | **Default `1`** — graph input/output quantise/dequantise is pushed to the CPU EP |
| `enable_htp_shared_memory_allocator` | `0` · `1` | Default `0`. Needs `libcdsprpc.so`/`.dll` — the FastRPC library from §3B |
| `qnn_context_priority` | `low` · `normal` · `normal_high` · `high` | Contention with other NPU clients on the device |
| `profiling_level` | `off` · `basic` · `detailed` · `optrace` | `optrace` needs QAIRT 2.39+ and yields QHAS/chrometrace data |
| `qnn_saver_path` | path to Saver lib | Dump the whole QNN call sequence for a bug report |

### Running a full model on the GPU

You **can** run a complete model on the Adreno GPU, and this is the code that does it. The change is
two-fold — the backend *and* the model file:

```python
# Note: model.onnx is FLOAT, not quantised. That is the point.
sess = ort.InferenceSession("model.onnx",
                            sess_options=so,
                            providers=["QNNExecutionProvider"],
                            provider_options=[{"backend_type": "gpu"}])
```

ONNX Runtime's own wording: the QNN GPU backend "can run models with 32-bit/16-bit floating-point
activations and weights as such **without prior quantization**," a 16-bit model "generally can run
inference faster on the GPU compared to its 32-bit version," and weight-only `uint8` quantisation is
supported for size reduction.

**Precision is a graph-level config, not a provider option.** The GPU backend exposes precision
modes through the QNN graph custom config, driven by JSON:

```json
{
  "graph_names": ["<your graph name>"],
  "precision_mode": "fp16"
}
```

Valid values are `fp16`, `fp32` and `hybrid`. With no override, `qnn-net-run` runs the GPU backend in
**USER_PROVIDED** mode — i.e. it does not force a precision. The same JSON schema also exposes
`kernel_repo_path`, `disable_memory_optimizations`, `disable_node_optimizations`,
`disable_queue_recording` and `weight_sharing`.

**GPU zero-copy.** The GPU backend supports the `QnnMem` API with user-provided **OpenCL buffers**
for input and output tensors, which "eliminates the need of data copy between the host CPU and GPU."
That is the mechanism behind an efficient GPU pre-processing → GPU inference pipeline.

**What the GPU path costs you:**

```
  ✗ No pre-compiled context binary   → graph prepared at session creation
  ✗ Narrower operator coverage       → documented separately in
                                        OpDef/GpuOpDefSupplement
  ✗ Availability varies by platform  → see §3B; on Snapdragon X the
                                        documented QNN targets are CPU + HTP
  ✓ No quantisation workflow at all
  ✓ FP32 / FP16 / hybrid
  ✓ OpenCL zero-copy I/O
```

### ExecuTorch — the PyTorch-native door

`QnnPartitioner` uses `QnnOperatorSupport` to check each node against the QNN SDK, tags supported
nodes with a `delegation_tag`, and handles constants, buffers and mutable state. Its constructor
gives you manual override:

```python
QnnPartitioner(
    compiler_specs,           # required
    skip_node_id_set=None,    # exclude specific nodes
    skip_node_op_set=None,    # exclude specific op types
    skip_mutable_buffer=False # don't delegate mutable buffers
)
```

PyTorch's documentation lists supported SoCs from SM8450 (Snapdragon 8 Gen 1) through SM8750
(Snapdragon 8 Elite), plus automotive (SA8295), XR (SXR2330P) and IoT (QCS9100) parts.

---

## 9. Genie — the LLM layer

Running an LLM by hand means juggling multiple binaries, a tokeniser and a KV cache. Genie does it
for you.

```
  ┌──────────────────────────────────────────────────────────┐
  │                        GENIE                             │
  │                                                          │
  │   GeniePipeline  ── orchestrates the whole thing         │
  │        │                                                 │
  │        ├── Tokeniser      text ──► token IDs             │
  │        ├── GenieEngine    the forward pass               │
  │        │      └── backend::type =                        │
  │        │          QnnHtp | QnnGenAiTransformer | QnnGpu   │
  │        ├── KV cache       managed for you                │
  │        └── Sampler        picks the next token           │
  │                                                          │
  │   APIs:  Dialog (multi-turn)  ·  Token generation        │
  │   CLI:   genie-t2t-run · genie-profile · genie-app       │
  └──────────────────────────────────────────────────────────┘
```

A model bundle for Genie contains **QNN binaries + tokeniser files + configuration JSON**.

### LLM quantisation types — note the direction of the trade

Produced by `qnn-genai-transformer-composer`:

| Type | Bits | Block size | Accuracy | Throughput |
|---|---|---|---|---|
| `Q4` | 4 | 32 | **highest** | lowest |
| `Z4` | 4 | 128 | good | good |
| `Z8` | 8 | 128 | good | **highest** |
| `Q5_K` | 5 | 256 | — | — |

> **Smaller blocks mean more scale factors: better accuracy, worse throughput.** That is the
> opposite of what most people assume, and it is a good interview answer.

### Gen AI Builder — the API that removes the manual steps

Recall the three-step LLM workflow: **quantise → compile & package → deploy**. Gen AI Builder is a
Python API that automates the whole middle step. You hand it a quantised ONNX model plus its
encodings file (the output of the AIMET step), and one `build()` call returns a `GenAIContainer`
ready to run on device.

```python
builder = GenAIBuilderFactory.create(
    Path(MODEL_EXPORTS),
    BackendType.HTP,
    cache_root=cache_root,
)
container = builder.build()
```

The factory **auto-detects the model architecture from `config.json`**, with preconfigured builders
for Llama, Qwen, Phi, Mistral, Baichuan and others. An unrecognised architecture falls back to a
default `GenAIBuilderHTP` **with a warning** — worth noticing, because a silent fallback means you
are no longer on a tuned path.

**What that single call is actually doing** — this list is the best summary of what LLM deployment
on a Hexagon NPU really involves:

1. **AR/CL conversion** — generate ONNX models for each autoregressive × context-length combination
2. **ONNX splitting** — partition the model into N splits (it does not fit as one graph)
3. **MHA2SHA transformation** — convert **multi-head attention into single-head** attention per split
4. **ONNX → DLC** conversion, applying quantisation overrides from the encodings file
5. **DLC quantisation** — activations at 16-bit, biases at 32-bit
6. **LoRA graph building** and import, when a LoRA config is supplied
7. **Context binary generation** — with **weight sharing** across splits and native KV-cache format

> **Read step 3 twice.** Multi-head attention is rewritten to single-head form to fit the NPU's
> execution model. This is the kind of graph surgery that separates "exported a model" from
> "deployed a model," and it is exactly the sort of thing an interviewer probes for.

### Speculative decoding — three supported methods

Decode is bandwidth-bound (see §6B), so the standard escape is to produce several tokens per
expensive pass. Qualcomm's builder supports three methods, selected at build time:

| Method | Full name | How it drafts |
|---|---|---|
| **LADE** | Look-ahead decoding | Predicts multiple future tokens, selects the most promising continuation |
| **SSD** | Self-speculative decoding | Uses **the model itself** as the draft — no second model to ship |
| **Eaglet** | Adaptation of EAGLE | Modified EAGLE algorithm for generating speculative tokens |

```python
SPECULATIVE_TYPE = "lade"   # or "ssd", or "eaglet"
```

**SSD is the pragmatic one for mobile** — no separate draft model means no extra weights in your
already-tight memory budget.

**Host requirement worth planning for:** Qualcomm recommends **at least 64 GB of RAM** on the build
machine, and notes the workflow may take around 40 minutes with less (increase swap to avoid
out-of-memory failures). The build is a heavyweight offline job, not something you iterate on
casually.

---

## 10. The datacenter branch

The same IP scaled up — Qualcomm states their datacenter parts reuse **Hexagon NPU and Oryon CPU**
technology.

```
        ┌────────────────────────────────────────────────┐
        │  Qualcomm's stated design thesis:              │
        │  optimise for MEMORY BANDWIDTH, CAPACITY and   │
        │  DATA-MOVEMENT ENERGY — not peak FLOPS         │
        └────────────────────────────────────────────────┘

  SHIPPING                        ANNOUNCED (dates are company claims)
  ────────                        ────────────────────────────────────
  Cloud AI 100 Ultra              Dragonfly AI200   -> 2026
    128 GB LPDDR4X                  768 GB LPDDR per card
    548 GB/s per card             Dragonfly AI250   -> 2027
                                    "High Bandwidth Compute",
  Toolchain:                        near-memory, >10x effective BW
    Cloud AI SDK                  Dragonfly AI300   -> on roadmap
    qaic-compile -> QPC
    efficient-transformers        Both: liquid-cooled, PCIe scale-up,
    (QEfficient)                  Ethernet scale-out, 160 kW racks
```

**Two datacenter ideas worth knowing:**

- **Network Specialization** — prefill and decode compiled into **one QPC sharing weights**, because
  the two stages need different input shapes.
- **MX6** (shared micro-exponents) — 6 bits per weight instead of FP16's 16, for when FP16 will not
  fit in memory.

Compilation is **ahead-of-time and pre-allocating**: prompt length, generation length, KV cache size
and batch size are all fixed at compile time, and the whole KV cache lives in device memory.

**efficient-transformers / QEfficient** ports Hugging Face checkpoints to Cloud AI 100 with
reimplemented LLM blocks, on-device retention of intermediate states, and graph transformations.

---

## 11. If you already know CUDA or ROCm

| Function | NVIDIA | AMD | **Qualcomm** |
|---|---|---|---|
| Low-level runtime | CUDA | HIP | **QNN** |
| Matrix hardware | Tensor Cores | Matrix Cores | **HMX** |
| Vector / SIMD | CUDA cores | SIMD | **HVX** |
| Fast on-chip memory | shared memory | LDS | **VTCM** |
| Pre-compiled artefact | TensorRT engine | — | **context binary** |
| Quantisation toolkit | — | AMD Quark | **AIMET** |
| ONNX Runtime EP | TensorRT EP | VitisAI (NPU) / MIGraphX (GPU) | **QNN EP** |
| DL primitives, accelerator | cuDNN | MIOpen | inside the HTP backend (closed) |
| DL primitives, GPU | cuDNN | MIOpen | **Adreno OpenCL ML SDK** |
| Hosted benchmarking | — | — | **AI Hub** |

**Two corrections to the usual mental map**, both of which matter if you are moving between stacks:

**Qualcomm does have a GPU ML kernel library.** The **Adreno OpenCL ML SDK** ships "hand-optimized
OpenCL kernels written by Adreno GPU experts using Adreno specific hardware features for ML
operators." That is the structural counterpart to MIOpen — and note it targets the *GPU*, not the
NPU. The genuinely closed part of Qualcomm's stack is the HTP backend's internals, not GPU ML kernels.

**On AMD, the ONNX Runtime ROCm EP was removed in ORT 1.23**; AMD's guidance is to use the MIGraphX
EP for GPU inference. If you are comparing EPs across vendors, do not cite the ROCm EP as current.

### The deeper structural difference: how work reaches the accelerator

This is the part that surprises people arriving from CUDA or ROCm, and §3B has the detail.

```
  AMD GPU (ROCm)                       Qualcomm NPU (HTP)
  ──────────────                       ──────────────────
  CPU builds a 64-byte AQL packet      CPU calls into a stub library
  writes it to a ring buffer                   │
  rings a doorbell                       FastRPC over an RPC channel
        │                                      │
  on-GPU Command Processor pulls it      skeleton library on the DSP
  and launches waves                     executes the graph

  → same address space, enqueue model  → separate subsystem, RPC model
```

A GPU is a device you *enqueue to*. The Hexagon NPU is a co-processor you *call*, with its own
firmware and its own library search path (`ADSP_LIBRARY_PATH`). That single difference explains most
of the deployment errors that have no CUDA/ROCm equivalent.

---

## 12. The mistakes everyone makes

| # | Mistake | What you see | Fix |
|---|---|---|---|
| 1 | Float model sent to the **HTP** backend | Load or session-creation failure | HTP takes quantised models only (§3B). Quantise it, or switch to the GPU backend |
| 2 | Quantised model sent to the **GPU/CPU** backend | Load failure or nonsense output | Those backends take float only (§3B). This is the mirror image of mistake 1 |
| 3 | **Silent CPU fallback** | "The NPU is slow" | Set `session.disable_cpu_ep_fallback = 1` while bringing up |
| 4 | **Dynamic shapes** left in the model | Nodes rejected, or the whole graph falls to CPU | QNN EP requires fixed shapes on *every* backend. Freeze batch size and input dims |
| 5 | Unsupported operators (Loops, Ifs, …) | Many partitions, slow despite fast kernels | Read the partition report. Rewrite the graph — §6B shows a rewrite worth up to 22× |
| 6 | Wrong SoC's context binary | Fails to load | Recompile for the target HTP architecture |
| 7 | Missing target-side libraries | Cryptic runtime errors, not "file not found" | Ship the V## stub **and** skel, plus `libQnnSystem.so` for `.bin` files; set `ADSP_LIBRARY_PATH` (§3B) |
| 8 | Believing **"Qualcomm doesn't use the GPU for AI"** | You never evaluate a viable path | False. The GPU runs whole float models — Qualcomm cites Llama 2-7B at >13 tok/s on Adreno (§6B) |
| 9 | Assuming the NPU is always fastest | Surprising benchmark results | It is not. §6B has two preprints disagreeing, and a case where the GPU won |
| 10 | QAIRT version mismatch | Odd, hard-to-place failures | Match the version stated on the AI Hub model card |

> **Mistakes 1 and 2 are the same mistake seen from two directions**, and between them they account
> for most first-week failures. Learn the §3B precision table before touching anything else.

---

## 13. Learning order

```
  0. Backend + precision  "which backend, and what model does it accept?"
        ▼                  <- §3B. Skip this and nothing else makes sense
  1. Partitioning         "how much landed on the NPU, and why not the rest?"
        ▼                  <- everything else is secondary to this
  2. Quantisation         QDQ · W8A8 · W4A8 · block sizes
        ▼                  <- without this you never touch HMX
  3. The four commands    converter -> quantizer -> context binary -> net-run
        ▼
  4. One framework door   ONNX Runtime QNN EP is the most transferable
        ▼
  5. DMA/VTCM overlap     the real performance story
        ▼
  6. Genie                once single-model inference works
```

**No hardware? Use Qualcomm AI Hub** — <https://aihub.qualcomm.com/models> — which compiles,
profiles and benchmarks on **real hosted Snapdragon devices**. You can get genuine measurements
without buying anything, which makes it the practical route for the roadmap's artefact 19.

---

## 14. Verification status

Stated plainly, because a reference document that blurs this is worse than useless.

### From Qualcomm primary documentation

The QAIRT / QNN / SNPE lineage · the HTP / cDSP / HTA distinction · backend library names · the QNN
object model and its parsing/partitioning boundary · the four-tool chain and its flags · the three
model formats and their portability · AIMET's techniques and Qualcomm's own guidance on when QAT is
and is not needed · Genie's architecture and tools · the GenAI quantisation types and their
trade-offs · Cloud AI 100 Ultra specifications · Network Specialization · MX6 · ONNX Runtime QNN EP
options · Genie's heterogeneous framing and the `QnnHtp` / `QnnGpu` / `QnnGenAiTransformer` backend
values · the Gen AI Builder API, its seven automated stages (including the MHA2SHA rewrite),
architecture auto-detection with warned fallback, the 16-bit activation / 32-bit bias settings, the
three speculative-decoding methods (LADE / SSD / Eaglet) and the 64 GB host-RAM recommendation.

**Added in this revision, all primary-sourced:** the definition of a QNN backend as a shared library
implementing the QNN API · the **per-backend quantised/non-quantised compatibility rule** for CPU,
GPU, HTP, DSP and HTA · Saver's explicit "does not execute any graphs" behaviour and its replay
purpose · the IR backend's DLC-emitting role via `--backend ir` · the **HTP library chain**
(`libQnnHtp` → `libQnnHtpV##Stub` → RPC → `libQnnHtpV##Skel`), plus `libQnnHtpPrepare`'s four
trigger conditions, `libQnnHtpV##.so` for RPC-free integration, and `libQnnSystem` for context-binary
interpretation · the QNN GPU backend's FP32/FP16/hybrid precision modes, its JSON config schema,
USER_PROVIDED default mode, OpenCL `QnnMem` zero-copy support, and the separate
`GpuOpDefSupplement` operator documentation · ONNX Runtime QNN EP `backend_type` versus
`backend_path` mutual exclusivity and the full provider-options surface · the QNN EP **fixed-shape
requirement** and unsupported-operator note · GPU **weight-only `uint8`** quantisation support ·
Adreno's documented FP32/FP16/INT8 AI support, its "medium-power, medium-performance" role, the
Llama 2-7B >13 tok/s figure, and the Adreno OpenCL ML SDK's hand-optimised ML kernels · the
Windows-on-Snapdragon statement that QNN currently exposes CPU and HTP on that platform.

### From PyTorch documentation

The ExecuTorch `QnnPartitioner` API and the supported-SoC list.

### Community or secondary — treat with care

Hexagon internals beyond the scalar / HVX / HMX / VTCM decomposition · the ~300x HVX-versus-HMX
figure · the bottleneck priority ordering · any specific systolic-array dimensions, since Qualcomm
does **not** publish HMX instruction details · **the Hexagon version-to-chip mapping, where sources
actively conflict** — verify v73 / v75 / v79 / v81 against Qualcomm documentation for your part.

### Academic preprints — cited as measurements, not as vendor fact

Every number in §6B's comparison table comes from two 2026 arXiv preprints, **not** from Qualcomm:
the prefill/decode speedups and reversals, the 1.27–1.62× CPU-over-NPU prefill result, the
8–22× dispatch-overhead ratios, the sub-10 µs dispatch guideline, the up-to-51% energy increase,
the 20–45× vision-encoder speedup, the 1.64× / 1.18× phase split, the 10.47 °C and 2.52× energy
figures, and the four-step graph rewrite yielding up to 22×. These are single-paper results on
specific chips and models; **the two papers contradict each other on prefill**, which is exactly
why §6B presents them side by side rather than picking one. Reproduce on your own target before
quoting any of it as fact.

### Announced, not shipped

Dragonfly AI200 / AI250 / AI300 specifications and availability dates.

**Adreno Neural Fusion (§6B)** — disclosed 2 September 2026. Every figure quoted (Matrix Cores in
three 1.45 GHz slices, 18 MB Adreno HPM, the 40% and 12% power claims, Unity/Unreal support, the
22–24 September 2026 Summit date) comes from **press coverage quoting Qualcomm's blog and press
materials**, not from a Qualcomm page retrieved directly. Qualcomm's documentation site is
JavaScript-rendered and the marketing URL was not retrievable at the time of writing. Treat these as
second-hand vendor claims. The Snapdragon SKU is unnamed by Qualcomm, and **whether QNN exposes
Adreno Matrix Cores as a general inference target is unverified and should not be assumed.**

### Corrected in this revision — previously wrong in this document

Recorded deliberately, so the same errors do not get re-introduced:

| Was | Now | Why |
|---|---|---|
| Layer 2 titled "one `.so` per piece of silicon" | "one `.so` implements the QNN API" | The HTP backend is several cooperating libraries, not one file |
| GPU backend labelled `pre/post` | `FLOAT models + pre/post` | The GPU runs whole models; pre/post is its second job |
| Saver and IR shown beside hardware backends with no distinction | Explicitly marked as executing nothing | They implement the API but run no graphs |
| GPU credited with "dynamic shapes" (§6B) | Removed; fixed shapes required everywhere | ORT QNN EP does not support dynamic shapes on any backend |
| `.so`/`.dlc` described as portable to "CPU / GPU / NPU" | Portable *format*, with the precision rule called out | A quantised DLC still will not run on GPU or CPU |
| `qnn-context-binary-generator` command presented as stable | Marked UNVERIFIED with a `--help` warning | Flag surface has shifted across QAIRT releases |
| §11 listed no Qualcomm GPU DL-primitive library | Adreno OpenCL ML SDK added | It exists and is the MIOpen counterpart |
| §11 implied the ROCm EP is AMD's current ORT path | MIGraphX EP noted for GPU | ROCm EP was removed in ONNX Runtime 1.23 |

---

## Primary sources

- Qualcomm AI Runtime (QAIRT) SDK overview —
  <https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/QNN_general_overview.html>
- AI developer workflow — <https://docs.qualcomm.com/doc/80-70030-15B/topic/ai-ml-developer-workflow.html>
- Qualcomm AI Engine Direct SDK — <https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk>
- **QNN backends and backend libraries** (the HTP stub/skel chain) —
  <https://docs.qualcomm.com/doc/80-63442-10/topic/backend.html>
- **QNN GPU backend** (precision modes, JSON config, OpenCL buffers) —
  <https://docs.qualcomm.com/doc/80-63442-10/topic/gpu_backend.html>
- **QNN GPU `QnnMem` / OpenCL zero-copy tutorial** —
  <https://docs.qualcomm.com/doc/80-63442-10/topic/gpu_qnnmem_api_tutorial.html>
- **QNN Saver backend** (implements the API, executes nothing) —
  <https://docs.qualcomm.com/doc/80-63442-10/topic/saver_backend.html>
- **QNN IR backend tutorial** (`--backend ir`, DLC generation) —
  <https://docs.qualcomm.com/doc/80-63442-10/topic/tutorial_ir_backend.html>
- **Quantisation — the per-backend quantised/non-quantised rule** —
  <https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/quantization.html>
- **Windows on Snapdragon AI overview** (engine roles; QNN exposing CPU + HTP there) —
  <https://docs.qualcomm.com/doc/80-62010-1/topic/ai-overview.html>
- **Unlocking on-device generative AI with an NPU and heterogeneous computing** (whitepaper; Adreno
  FP32/FP16/INT8 AI support, Llama 2-7B >13 tok/s on Adreno) —
  <https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Unlocking-on-device-generative-AI-with-an-NPU-and-heterogeneous-computing.pdf>
- **Adreno OpenCL ML SDK via TVM** (hand-optimised Adreno ML kernels) —
  <https://www.qualcomm.com/developer/blog/2022/09/accelerate-your-machine-learning-networks-using-tvm-and-adreno-opencl-ml-apis-adreno-gpus>
- AIMET quantisation workflow — <https://quic.github.io/aimet-pages/releases/latest/tutorials/quantization_workflow.html>
- AIMET on-target inference (the four-tool chain) —
  <https://qualcomm.github.io/aimet-pages/releases/latest/tutorials/on_target_inference.html>
- Genie — <https://docs.qualcomm.com/doc/80-80020-15B/topic/use-genai-model-with-genie.html>
- Gen AI Builder overview —
  <https://docs.qualcomm.com/doc/80-87189-2/topic/genai_overview.html>
- Speculative decoding tutorial (LADE / SSD / Eaglet) —
  <https://docs.qualcomm.com/doc/80-87189-2/topic/speculative_decoding_tutorial.html>
- *When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference* (preprint) —
  <https://arxiv.org/html/2605.27435>
- *Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC* (preprint) —
  <https://arxiv.org/html/2606.27906>
- `qnn-genai-transformer-composer` —
  <https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/qnn-genai-transformer-composer.html>
- ONNX Runtime QNN EP on Snapdragon — <https://docs.qualcomm.com/doc/80-62010-1/topic/ort-qnn-ep.html>
- ONNX Runtime QNN EP reference — <https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html>
- ExecuTorch Qualcomm backend — <https://docs.pytorch.org/executorch/1.2/backends-qualcomm.html>
- Data center AI accelerators — <https://www.qualcomm.com/data-center/expertise/ai-accelerators>
- Cloud AI LLM guide — <https://quic.github.io/cloud-ai-sdk-pages/latest/Getting-Started/Model-Architecture-Support/Large-Language-Models/llm/>
- efficient-transformers — <https://github.com/quic/efficient-transformers>
- Qualcomm AI Hub models — <https://aihub.qualcomm.com/models>

### Secondary — press coverage of Qualcomm's Adreno Neural Fusion disclosure (§6B)

- <https://9to5google.com/2026/09/02/qualcomm-details-adreno-neural-fusion-gpu-for-next-snapdragon-chip/>
- <https://www.thelec.net/news/articleView.html?idxno=13648>

---

*Compiled 2026-09-04. Revised 2026-09-07: added §3B (backends and the precision rule), the HTP
library chain and FastRPC path, the GPU inference path in §8, Adreno Neural Fusion in §6B, and an
explicit list of corrected errors in §14. Vendor stacks move quickly — re-verify any specific tool
name, flag or version before relying on it.*
