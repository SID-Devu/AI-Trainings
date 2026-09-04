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
| 4 | The offline pipeline — preparing the model |
| 5 | **Graph partitioning — what decides your performance** |
| 6 | Inside the Hexagon NPU |
| 7 | The complete journey — one worked example |
| 8 | Which door do I use? |
| 9 | Genie — the LLM layer |
| 10 | The datacenter branch |
| 11 | If you already know CUDA or ROCm |
| 12 | The five mistakes everyone makes |
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
║  LAYER 2 — BACKEND LIBRARIES        "one .so per piece of silicon"    ║
║  ───────────────────────────                                          ║
║   libQnnHtp   libQnnGpu   libQnnCpu     libQnnSaver   libQnnIr        ║
║   ↓ NPU       ↓ GPU       ↓ CPU         ↓ trace       ↓ IR dump       ║
║   PRODUCTION  pre/post    VALIDATION    debug         debug           ║
║                           ONLY                                        ║
╠═══════════════════════════════════════════════════════════════════════╣
║  LAYER 1 — SILICON                                                    ║
║  ─────────────────                                                    ║
║   ┌───────────────┐  ┌───────────────┐  ┌─────────────────────────┐   ║
║   │  Kryo/Oryon   │  │    Adreno     │  │  HEXAGON NPU  (HTP)     │   ║
║   │     CPU       │  │     GPU       │  │  ← where AI actually    │   ║
║   │               │  │  (OpenCL)     │  │    wants to run         │   ║
║   └───────────────┘  └───────────────┘  └─────────────────────────┘   ║
╚═══════════════════════════════════════════════════════════════════════╝
```

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
| GPU | Adreno | AI via OpenCL kernels; also pre/post-processing |
| **NPU** | **Hexagon (HTP)** | **Low power, high performance — needs quantised models** |

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

### The three model formats — and what you trade

```
 LIBRARY (.so)          DLC (.dlc)              CONTEXT BINARY (.bin)
 ─────────────          ──────────              ─────────────────────
 CPU / GPU / NPU        CPU / GPU / NPU         NPU ONLY
 portable               portable                LOCKED to one SoC
 compiles at runtime    compiles at runtime     PRE-COMPILED
                                                -> fastest startup
```

> **The trade in one sentence:** a context binary removes runtime compilation but stops being
> portable. Ship it for the wrong chip and it will not load.

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

opts = {"backend_path": "QnnHtp.dll",          # QnnCpu.dll / QnnGpu.dll also exist
        "enable_htp_fp16_precision": "1",
        "htp_performance_mode": "high_performance"}

so = ort.SessionOptions()
so.add_session_config_entry("session.disable_cpu_ep_fallback", "1")   # see below

sess = ort.InferenceSession("model.onnx",
                            sess_options=so,
                            providers=["QNNExecutionProvider"],
                            provider_options=[opts])
```

> **Set `disable_cpu_ep_fallback` to `1` during bring-up.** Without it, a silent fall back to the CPU
> looks exactly like "the NPU is slow," and people lose days to it.

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
| ONNX Runtime EP | TensorRT EP | VitisAI / MIGraphX | **QNN EP** |
| Deep learning primitives | cuDNN | MIOpen | (inside HTP backend) |
| Hosted benchmarking | — | — | **AI Hub** |

---

## 12. The five mistakes everyone makes

| # | Mistake | What you see | Fix |
|---|---|---|---|
| 1 | Model not quantised | Runs, but slowly | The NPU wants INT8/INT4. Use AIMET |
| 2 | **Silent CPU fallback** | "The NPU is slow" | Set `session.disable_cpu_ep_fallback = 1` while bringing up |
| 3 | Too many partitions | Slow despite fast kernels | Read the partition report. Fix operator coverage |
| 4 | Wrong SoC's context binary | Fails to load | Recompile for the target chip |
| 5 | QAIRT version mismatch | Odd, hard-to-place failures | Match the version stated on the AI Hub model card |

---

## 13. Learning order

```
  1. Partitioning        "how much landed on the NPU, and why not the rest?"
        ▼                 <- everything else is secondary to this
  2. Quantisation        QDQ · W8A8 · W4A8 · block sizes
        ▼                 <- without this you never touch HMX
  3. The four commands   converter -> quantizer -> context binary -> net-run
        ▼
  4. One framework door  ONNX Runtime QNN EP is the most transferable
        ▼
  5. DMA/VTCM overlap    the real performance story
        ▼
  6. Genie               once single-model inference works
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
options.

### From PyTorch documentation

The ExecuTorch `QnnPartitioner` API and the supported-SoC list.

### Community or secondary — treat with care

Hexagon internals beyond the scalar / HVX / HMX / VTCM decomposition · the ~300x HVX-versus-HMX
figure · the bottleneck priority ordering · any specific systolic-array dimensions, since Qualcomm
does **not** publish HMX instruction details · **the Hexagon version-to-chip mapping, where sources
actively conflict** — verify v73 / v75 / v79 / v81 against Qualcomm documentation for your part.

### Announced, not shipped

Dragonfly AI200 / AI250 / AI300 specifications and availability dates.

---

## Primary sources

- Qualcomm AI Runtime (QAIRT) SDK overview —
  <https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/QNN_general_overview.html>
- AI developer workflow — <https://docs.qualcomm.com/doc/80-70030-15B/topic/ai-ml-developer-workflow.html>
- Qualcomm AI Engine Direct SDK — <https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk>
- AIMET quantisation workflow — <https://quic.github.io/aimet-pages/releases/latest/tutorials/quantization_workflow.html>
- AIMET on-target inference (the four-tool chain) —
  <https://qualcomm.github.io/aimet-pages/releases/latest/tutorials/on_target_inference.html>
- Genie — <https://docs.qualcomm.com/doc/80-80020-15B/topic/use-genai-model-with-genie.html>
- `qnn-genai-transformer-composer` —
  <https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/qnn-genai-transformer-composer.html>
- ONNX Runtime QNN EP on Snapdragon — <https://docs.qualcomm.com/doc/80-62010-1/topic/ort-qnn-ep.html>
- ONNX Runtime QNN EP reference — <https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html>
- ExecuTorch Qualcomm backend — <https://docs.pytorch.org/executorch/1.2/backends-qualcomm.html>
- Data center AI accelerators — <https://www.qualcomm.com/data-center/expertise/ai-accelerators>
- Cloud AI LLM guide — <https://quic.github.io/cloud-ai-sdk-pages/latest/Getting-Started/Model-Architecture-Support/Large-Language-Models/llm/>
- efficient-transformers — <https://github.com/quic/efficient-transformers>
- Qualcomm AI Hub models — <https://aihub.qualcomm.com/models>

---

*Compiled 2026-09-04. Vendor stacks move quickly — re-verify any specific tool name, flag or version
before relying on it.*
