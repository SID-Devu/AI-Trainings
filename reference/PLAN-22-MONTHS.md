# The 15-month plan, then seven months to architect — every day, cloud and edge

**Six hundred and sixty days, each naming the concepts it teaches, the work it does and the
evidence it leaves. Months 1–15 walk all of roadmap #2, from school mathematics to a capstone in
the cloud and on a device. Months 16–22 walk all of roadmap #1, from logic gates to a hardware
proposal. A daily track hour covers the parts of both syllabi that no stage teaches, and an index
shows the day on which every subject reaches every level.**

This is the calendar for both role roadmaps. Roadmap #2,
[`ROADMAP-AI-PERFORMANCE-ENGINEER.md`](ROADMAP-AI-PERFORMANCE-ENGINEER.md), fills days 1–450,
and roadmap #1, [`ROADMAP-AI-SYSTEMS-ARCHITECT.md`](ROADMAP-AI-SYSTEMS-ARCHITECT.md), fills days
451–660. The roadmaps explain each concept, give its sources and set its tests; this plan says
which day you learn it. Every Learn topic of every stage is named, in its roadmap's own words, in
a row of that stage, and every subject of both syllabi has its days in §27, so nothing in either
roadmap is left out.

> **How to read this.** Each month has 30 numbered days. Days 7, 14, 21 and 28 are review days,
> day 29 is a buffer and day 30 is the month gate, so every month has 24 study days (§3). A row
> names the stage, the day's concepts and work, and what you have at the end of the day. A
> concept written as "Label: details" is a Learn topic of that stage, and its roadmap holds the
> explanation and the sources. "Build 2" or "Check yourself 3" points to that stage's lists.
>
> Each month also has a track-hour table: one hour a day for the parts of the two syllabi that no
> stage teaches (§3). §27 maps every subject of both syllabi to the days on which it reaches
> Basic, Intermediate, Advanced and Expert, and §28 turns the Expert levels into tracks.
>
> The calendar is a plan; the gates decide. A stage is finished when its **Done when** test passes,
> not when its days run out. If you fall behind, move the calendar, never the gate (§3).

---

## Contents

| § | Section | What you get |
| --- | --- | --- |
| 1 | What the plan can and cannot do | The pace, what it covers, what no plan can do, and where it leaves you |
| 2 | The whole plan in one table | Each month's stages, tech stack and gates, and the stack by layer |
| 3 | Every day, every week, every month | The daily routine and the track hour, review days, buffers, gates, and what to do when you fall behind |
| 4 | What you need, and when | Hardware, accounts and rentals, by the day you first need them |
| 5 | Month 1: school mathematics, first programs, first tools | Days 1–30 |
| 6 | Month 2: vectors, probability, electronics and the on-ramp gates | Days 31–60 |
| 7 | Month 3: computing from zero, then mathematics for machine learning | Days 61–90 |
| 8 | Month 4: optimisation and numerics, then C, a shell and an allocator | Days 91–120 |
| 9 | Month 5: data structures, Python, modern C++ and concurrency | Days 121–150 |
| 10 | Month 6: deep learning, from autograd to your own GPT | Days 151–180 |
| 11 | Month 7: LLM arithmetic, then your first GPU kernels | Days 181–210 |
| 12 | Month 8: measurement, operating systems and networks | Days 211–240 |
| 13 | Month 9: consensus and storage, then the GEMM ladder | Days 241–270 |
| 14 | Month 10: kernels and compilers, on the GPU and on the NPU | Days 271–300 |
| 15 | Month 11: distributed training and serving at scale | Days 301–330 |
| 16 | Month 12: serving on a device, quantisation and data engineering | Days 331–360 |
| 17 | Month 13: device telemetry, cloud deployment and operations | Days 361–390 |
| 18 | Month 14: security, and the edge application with its cloud side | Days 391–420 |
| 19 | Month 15: the capstone, in the cloud and on a device | Days 421–450 |
| 20 | Month 16: logic, RTL and silicon, then the quantitative method | Days 451–480 |
| 21 | Month 17: caches, memory and the cost of silicon, then the GPU from the inside | Days 481–510 |
| 22 | Month 18: a model of your GPU, then accelerators and dataflow | Days 511–540 |
| 23 | Month 19: number formats in silicon, then performance modelling | Days 541–570 |
| 24 | Month 20: the device model, the cluster and its facility | Days 571–600 |
| 25 | Month 21: storage and the fleet, on both sides | Days 601–630 |
| 26 | Month 22: the hardware proposal | Days 631–660 |
| 27 | The syllabus index: every subject, every level, its days | Both syllabi, Basic to Expert |
| 28 | Expert tracks, after day 660 | Every Expert level, where it starts and what proves it |
| 29 | After day 660 | The job, and the habits that keep you there |
| 30 | Verification status | What is sourced and what is planning judgement |
| — | Primary sources | Where the links are |

---

## 1. What the plan can and cannot do

- **The pace.** Six study days a week at about eight focused hours, and one review day. Months
  1–15 hold 360 study days, about 2,900 hours; months 16–22 hold 168 more, about 1,300 hours. It
  is aggressive: few people hold it for twenty-two months, and nobody should skip a gate to stay
  on it.
- **What it covers.** All of roadmap #2 in months 1–15: the on-ramp from class 10 (Z1–Z4), the
  foundations (F0–F7) and every P-stage on both sides, cloud and edge (roadmap #2 §3H), ending in
  the P11 capstone. All of roadmap #1 in months 16–22: A1–A10, each with its datacenter and edge
  sides (roadmap #1 §3E), ending in the A10 proposal. Every Learn topic of every stage is named on
  its day, and the track hour takes every subject of both syllabi (roadmap #2 §3D, roadmap #1 §3D)
  to Advanced where no stage does.
- **Alongside school or a job.** At about four hours a day, each plan day takes two calendar days,
  and the plan takes about 44 months. That matches the route in roadmap #2 §3E: the on-ramp beside
  classes 11 and 12, then the foundations and the P-stages across a degree.
- **What no plan can do.** Nobody is the best in every field. Expert level in all 51 syllabus
  subjects is the work of several careers, and experts specialise: §28 lists every Expert level as
  a track, and you choose the ones your work needs. The levels above senior in roadmap #2 §3G are
  also judged on evidence that only years of work produce: scope, incidents led and people grown.
- **Where it leaves you.** On day 450, with the technical evidence that roadmap #2 §3G asks of a
  mid-level and a senior AI systems engineer, on both sides. On day 660, with a hardware proposal
  that a chip team could fund, a validated model behind it, and every syllabus subject studied to
  Advanced, all in a public repository that proves it.

---

## 2. The whole plan in one table

Each month's stages, the tools you work in, and the gates that fall due. The day tables in §5–§26
give the detail, and each month's track-hour table adds the tools of its track.

| Month | Days | Stages | The stack you work in | Gates due |
| --- | --- | --- | --- | --- |
| 1 | 1–30 | Z1, Z2, Z3 | Python 3, VS Code, Git and GitHub, a Linux terminal through WSL2, Khan Academy, CS50x | Z3 |
| 2 | 31–60 | Z1, Z2, Z4 | NumPy, Matplotlib, pandas, a circuit simulator, Logisim-evolution | Z1, Z2, Z4 |
| 3 | 61–90 | F0, F1 | The Nand2Tetris simulators, C with gcc, `gcc -S` and `objdump`, NumPy | F0 |
| 4 | 91–120 | F1, F2 | NumPy; C, Valgrind, `nm`, `readelf` and `LD_PRELOAD`; POSIX processes, pipes and signals | F1 |
| 5 | 121–150 | F2 | Modern C++ and the STL, CMake, GoogleTest, ASan, UBSan, TSan, gdb, pybind11, pytest, GitHub Actions | F2 |
| 6 | 151–180 | F3, F4 | PyTorch; your own autograd engine, tokenizer and GPT | F3 |
| 7 | 181–210 | F4, F5 | `llm_calc.py`; ROCm, HIP, `rocminfo`, `amd-smi`, PyTorch for ROCm, `rocprofv3`, ROCm Compute Profiler | F4, F5 |
| 8 | 211–240 | F6, F7 | `perf`, flame graphs, Perfetto, your `bench/` harness; xv6 on QEMU, sockets, SSE, a load generator, Go | F6 |
| 9 | 241–270 | F7, P1 | Raft in Go, fio, namespaces and cgroups; HIP, MFMA or WMMA, hipBLASLt, `-save-temps` | F7 |
| 10 | 271–300 | P1, P2 | Triton, Composable Kernel, AITER, `rocgdb`; ONNX Runtime with the Vitis AI or QNN execution provider, IRON; `torch.library`, `torch.compile`, Inductor, MLIR, `torch.export`, ExecuTorch | P1, P1 edge, P2, P2 edge |
| 11 | 301–330 | P3, P4 | RCCL, `torch.distributed`, FSDP, tensor and pipeline parallelism, LoRA; distillation and federated averaging; vLLM, SGLang, speculative decoding, FastAPI, BentoML, Triton Inference Server or Ray Serve | P3, P3 edge, P4 |
| 12 | 331–360 | P4, P5, P6 | OGA and Lemonade, llama.cpp or Genie; FP8, MXFP4, AMD Quark, GPTQ, AWQ, AIMET and INT8 QDQ; DuckDB, Parquet, Iceberg, DataTrove, WebDataset, MosaicML Streaming, `StatefulDataLoader`, DCP | P4 edge, P5, P5 edge, P6 |
| 13 | 361–390 | P6, P7, P8 | Terraform or OpenTofu, Docker, Kubernetes, the AMD GPU Operator, KEDA, Kueue, LWS, Slurm, KServe; a build farm and an update service; MLflow or Weights & Biases, lm-evaluation-harness, Prometheus, Grafana, OpenTelemetry | P6 edge, P7, P7 edge, P8 |
| 14 | 391–420 | P8, P9, P10 | MITRE ATLAS, the OWASP LLM Top 10, SBOMs, cosign, SLSA, safetensors; the NPU runtimes, signed model updates and a cloud cascade sized from the fleet | P8 edge, P9, P9 edge, P10, P10 cloud |
| 15 | 421–450 | P11 | Everything above, plus HIPIFY, parity testing and an upstream pull request | P11 |
| 16 | 451–480 | A1, A2 | The OSS CAD Suite (Yosys, Verilator, cocotb, GTKWave or Surfer), SymbiYosys, OpenSTA and OpenROAD with an open PDK; `perf stat` | A1, A1 edge |
| 17 | 481–510 | A2, A3 | Your cache simulator, `perf` and gem5; DRAMSim3 or Ramulator 2; Spike and a RISC-V core in RTL; HIP microbenchmarks and the Matrix Instruction Calculator | A2, A2 edge |
| 18 | 511–540 | A3, A4, A5 | Your GPU model and Accel-Sim; an RDNA GPU; Timeloop and Accelergy in Docker, or SCALE-Sim; an FPGA flow | A3, A3 edge, A4, A4 edge |
| 19 | 541–570 | A5, A6 | Format emulation in PyTorch on real LLM tensors; multipliers in SystemVerilog; your performance model, ASTRA-sim and Chakra traces | A5, A5 edge, A6 |
| 20 | 571–600 | A6, A7, A8 | Your device model; ASTRA-sim network what-ifs; a TCO spreadsheet; McPAT and CACTI | A6 edge, A7, A7 edge |
| 21 | 601–630 | A8, A9, A10 | DuckDB over Parquet traces; fio; the Philly and Alibaba traces with Git LFS; the Caliptra specification | A8, A8 edge, A9, A9 edge |
| 22 | 631–660 | A10 | Everything above: the proposal, its model, its RTL cost and its one-command key figure | A10 |

### The stack you will have used by day 660

| Layer | Cloud side | Edge side |
| --- | --- | --- |
| Languages | Python, C, modern C++, HIP, Triton, Go for the distributed-systems labs, and SystemVerilog from month 16 | The same, plus the application code around a model |
| Hardware | Instinct GPUs with MFMA, usually rented; Radeon GPUs with WMMA | The XDNA NPU and RDNA iGPU of Ryzen AI; Hexagon and Adreno on Snapdragon |
| Measurement | `perf`, flame graphs, `rocprofv3`, the ROCm Compute and Systems Profilers, Perfetto and your `bench/` harness | Power telemetry or a meter; sustained against burst runs; partition reports |
| Kernels | The GEMM ladder, MFMA, Triton, hipBLASLt, Composable Kernel, AITER and FlashAttention | Kernels on the iGPU; operator fusion for the NPU; **[KNOW]** IRON on XDNA |
| Compilers | `torch.compile`, Inductor, MLIR and Triton's IR stages | `torch.export`, ONNX, ExecuTorch's partitioner, QNN context binaries and shape buckets |
| Training | RCCL, DDP, FSDP, tensor and pipeline parallelism, LoRA | Distillation, quantisation-aware training and federated averaging |
| Serving | vLLM, SGLang, speculative decoding, FastAPI, BentoML, Triton Inference Server and Ray Serve | OGA, Lemonade, llama.cpp and Genie; batch size one; hybrid NPU and iGPU modes |
| Numerics | FP8, MX formats, AMD Quark, GPTQ, AWQ and SmoothQuant | INT8 QDQ, AIMET, 4- to 8-bit weights with 16-bit activations, and Quark again |
| Data | DuckDB, Parquet, Iceberg, DataTrove, MinHash, WebDataset, MosaicML Streaming, DCP and Faiss | Calibration sets that match the device, and a telemetry pipeline that counts exactly once |
| Cloud | Terraform or OpenTofu, Docker, Kubernetes, the AMD GPU Operator, KEDA, Kueue, LWS, Slurm and KServe | A build farm per target, manifests, an update service with staged rollouts, and Qualcomm AI Hub |
| Operations | MLflow or Weights & Biases, lm-evaluation-harness, HELM, Prometheus, Grafana, OpenTelemetry and `amd-smi` | One registry and one harness for both sides, release gates per device class, and a kill switch |
| Security | MITRE ATLAS, the OWASP LLM Top 10, SBOMs, cosign, SLSA and safetensors; roots of trust and Caliptra | Signed models, keys held outside CI and rotated, and a threat model in which the attacker holds the device |
| RTL and silicon | SystemVerilog, Verilator, Yosys, cocotb, SymbiYosys, OpenSTA and OpenROAD: a systolic array verified, synthesised and placed | Clock and power gating, toggle counts as a proxy for switching energy, and INT8 × INT16 multipliers priced |
| Architecture models | A cache simulator validated against `perf`, a GPU model built from microbenchmarks, Timeloop or SCALE-Sim, a validated end-to-end model, and ASTRA-sim | An XDNA-like array model, and a device model of latency and energy per token |
| Systems and fleet | A 1,024-accelerator cluster, its storage tiers, the Philly and Alibaba traces, and a fleet-health plan | A device support matrix, staged rollouts with halt criteria, and cloud capacity for devices without an NPU |

---

## 3. Every day, every week, every month

### A study day, about eight hours

1. **Recall (30 minutes).** Flashcards, and yesterday's hardest problem from memory.
2. **Learn (2.5 hours).** The concepts named in the day's row, from the reading, lecture or paper
   named there.
3. **Build (3.5 hours).** The code, derivation or experiment named in the row, committed to your
   project repository (roadmap #2 §3C, then roadmap #1 §3C).
4. **Track hour (1 hour).** This week's row of the month's track-hour table: the parts of the two
   syllabi (roadmap #2 §3D, roadmap #1 §3D) that no stage teaches, each with a small piece of
   work. Week 1 is days 1–6 of the month, week 2 days 8–13, week 3 days 15–20 and week 4 days
   22–27.
5. **Check and log (30 minutes).** The Check yourself questions that the day covered, answered in
   writing from memory, then a learning-log entry: what you did, what broke, and tomorrow's first
   task.

In months 1 and 2 a row often names two steps, such as Z1 and Z2. Split the Learn and Build blocks
between them: mathematics in the morning and programming in the afternoon, for example.

### The week

Days 7, 14, 21 and 28 of every month are review days. Redo the week's Check yourself questions
cold, close the weakest topic, write a one-paragraph weekly note, and rest for the rest of the day.
Rest is part of the plan: spaced review is what makes the learning last (roadmap #2 Z3). From
month 9 on, each review day also takes one paper from the week's references, read slowly with
notes: the habit of reading research that roadmap #2 §3G asks for.

### The month

Day 29 is a buffer: finish anything late, or retry a gate that failed. Day 30 is the month gate:
re-run, cold, every **Done when** test that fell due that month, tick it in roadmap #2 §23 or
roadmap #1 §15, and write a one-page month report in the F6 format.

### When you fall behind

- **One or two days late:** use day 29. The track hour gives way first: a missed track week moves
  to the next buffer day, never into a gate.
- **A week or more:** move every later row by the same number of days. Never skip a gate, and never
  drop an edge side; the edge sides are what let you work on both sides of every domain.
- **A gate fails twice:** go back to the stage's Study path in roadmap #2, and ask for help with the
  reproduction attached (roadmap #2 §3B).

---

## 4. What you need, and when

| From day | Hardware | Software and accounts | Plan ahead |
| --- | --- | --- | --- |
| 1 | Any laptop, with Linux through WSL2, a virtual machine or a spare machine | Python, VS Code, Git, and a GitHub account with two-factor authentication | Nothing to buy |
| 42 | The same laptop | A free circuit simulator and Logisim-evolution | A breadboard kit is optional |
| 188 (F5) | One AMD GPU supported by ROCm, owned or rented (roadmap #2 §3B) | ROCm, PyTorch for ROCm and the ROCm profilers | If you rent, set a budget alert first |
| 219 (F7) | Any Linux machine with an NVMe drive | QEMU, a RISC-V cross-compiler, Go and fio | — |
| 278 (P1 edge) | A laptop with an NPU (Ryzen AI 300-series or Snapdragon), or Qualcomm AI Hub's hosted devices | ONNX Runtime and the vendor's NPU toolchain | Check AMD's supported processors (AMD-AI-STACK §13B) before you buy |
| 304 (P3) | 2–8 GPUs in one node for a few days, and two nodes for a multi-node run | PyTorch distributed and RCCL | The largest rental in the plan: book it for named days |
| 363 (P7) | A cloud account with GPU quota, and a local Kubernetes cluster | Terraform or OpenTofu, kubectl, Helm and the AMD GPU Operator | Request GPU quota in month 12, before you need it |
| 421 (P11) | Rented GPUs, as for P3 and P7, and your edge device | Everything above | Budget the capstone before month 15 starts |
| 451 (A1) | Any 64-bit computer running Linux (native, a VM or WSL2) | The OSS CAD Suite (roadmap #1 §3B), Python and NumPy; an open PDK for place-and-route | Record the tool versions and the cell library |
| 451 (A2) | A Linux machine on which `perf stat` reads real hardware counters; bare metal if a VM hides them | `perf`, gcc or clang; gem5 is optional | Check the counters on day 451, weeks before A2 needs them |
| 500 (A3) | The AMD GPU of your P1 ladder; for the edge side, an RDNA GPU that ROCm supports | ROCm, HIP and the ROCm profilers | Instinct (MFMA) and Radeon (WMMA) differ, so measure the family your ladder used |
| 511 (track) | An FPGA board, if you want the optional board build in month 18 | Yosys and nextpnr, or AMD Vivado | Optional: the rest of the FPGA track needs no board |
| 522 (A4) | Any computer that runs Docker or Python | Timeloop and Accelergy through Docker, or SCALE-Sim v3 | — |
| 545 (A5) | A CPU is enough; a GPU is faster | PyTorch, and the weights of an open-weight LLM | — |
| 611 (A9) | Any computer with room for the trace: the Philly trace unpacks to 6.6 GB | Git LFS, and Python with DuckDB or pandas | Install Git LFS before you clone, or you get a small pointer file |

---

## 5. Month 1: school mathematics, first programs, first tools

**Goal:** algebra through the start of calculus, your first nine programs, and the tools every
engineer uses. **Gate this month:** Z3.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 1 | Z2, Z3 | Z2: Getting started: install Python and VS Code, run a script and use the interactive shell. Z3: The computer as a tool: files, folders and paths, and installing software; Safe computing: a GitHub account with a strong password and two-factor authentication. Start a learning log and a flashcard deck, then take a class-10 mathematics revision test to find your gaps | `hello.py` running, a learning log, and a list of weak topics |
| 2 | Z1, Z2 | Z1: Algebra and functions: linear equations and inequalities. Z2: The language: CS50x week 0 (Scratch), then Python variables, types, input and output | 30 worked problems; a script that reads a number and prints its square |
| 3 | Z1, Z2 | Z1: quadratic equations by factoring, by completing the square and by the formula. Z2: `if`, `for` and `while` | A quadratic solver that handles no, one and two real roots |
| 4 | Z1, Z3 | Z1: functions and their graphs; domain and range. Z3: The terminal and Linux: install WSL2 or a Linux virtual machine; *The Missing Semester* on the shell: `cd`, `ls` and `pwd`; `cp`, `mv` and `rm`; `cat` and `less` | Five functions graphed by hand; files moved and read from a terminal |
| 5 | Z1, Z2 | Z1: exponents and logarithms, and why power laws are straight lines on log–log plots. Z2: functions, arguments and return values | The log laws, each with a worked example; three functions tested with `assert` |
| 6 | Z1, Z2 | Z1: exponential growth and decay. Z2: lists and loops; program 1, a calculator | Program 1; 15 growth and decay problems |
| 7 | Review | Redo the week's hardest problems cold; flashcards; weekly note; rest | Weekly note 1 |
| 8 | Z1, Z2 | Z1: Trigonometry and coordinate geometry: angles, radians and the unit circle; sine and cosine, and why the rotary position embeddings of transformers are rotations. Z2: dictionaries, sets and tuples; program 2, a number-guessing game | The unit circle drawn from memory; program 2 |
| 9 | Z1, Z3 | Z1: trigonometric identities, and the graphs of sine and cosine. Z3: Git and GitHub: `init`, `add`, `commit` and `log` from *Pro Git*, then push to GitHub | A public repository holding programs 1 and 2 |
| 10 | Z1, Z2 | Z1: coordinate geometry: lines, slopes, distances and midpoints. Z2: strings; program 3, a quiz read from a file | Program 3; 20 geometry problems |
| 11 | Z1, Z2 | Z1: circles and parabolas in coordinates. Z2: files and exceptions; program 4, a word counter | Program 4, which reports a missing file clearly instead of crashing |
| 12 | Z1, Z3 | Z1: Sequences, series and counting: arithmetic and geometric progressions; sigma notation. Z3: searching with `grep` and `find`, and pipes | Both sum formulas derived on paper; a pipeline that lists every `.py` file you wrote |
| 13 | Z1, Z2 | Z1: series in use, such as compound interest. Z2: program 5, a to-do list saved to disk | Program 5; 15 series problems |
| 14 | Review | Close the week's weakest topic; flashcards; weekly note; rest | Weekly note 2 |
| 15 | Z1, Z2 | Z1: permutations and combinations. Z2: problem solving: write the steps in plain words before the code | 10 practice-site problems solved without looking at answers (10 of 50) |
| 16 | Z1, Z2 | Z1: the binomial theorem and Pascal's triangle. Z2: program 6, a marks calculator with statistics | Program 6; Pascal's triangle printed by your code |
| 17 | Z1, Z3 | Z1: limits: the idea, one-sided limits and limits at infinity. Z3: branches and pull requests on your own repository | A merged pull request |
| 18 | Z1, Z2 | Z1: the derivative as a slope and as a rate (*Essence of Calculus*). Z2: program 7, a unit converter | 20 polynomials differentiated; program 7 |
| 19 | Z1, Z2 | Z1: the product and quotient rules. Z2: reading tracebacks; the VS Code debugger | A bug you planted, found with the debugger and written up |
| 20 | Z1, Z2 | Z1: the chain rule; the derivatives of eˣ, ln x, sin x and cos x. Z2: 10 practice problems | e^(−x²) differentiated; 20 of 50 problems |
| 21 | Review | Re-derive the product, quotient and chain rules from memory; flashcards; weekly note; rest | Weekly note 3 |
| 22 | Z1, Z2 | Z1: maxima and minima; the second derivative. Z2: program 8, a password checker | Program 8; five optimisation word problems |
| 23 | Z1, Z3 | Z1: curve sketching with derivatives. Z3: Technical English: read Python's documentation for `open`, `str.split` and `dict` and one real error message, search well, then write one good question with a minimal example | A question written the way roadmap #2 Z3 describes |
| 24 | Z1, Z2 | Z1: gradient descent by hand: minimise a quadratic in five steps. Z2: program 9, tic-tac-toe | Program 9; a hand-computed descent table |
| 25 | Z1, Z2 | Z1: integrals as areas; antiderivatives. Z2: First libraries: installing packages with `pip`, NumPy arrays and Matplotlib | A plot of x², with its area estimated by rectangles |
| 26 | Z1, Z2 | Z1: definite integrals and the fundamental theorem of calculus. Z2: a plot of a function and its derivative (Z2 Build 2) | Z2 Build 2 committed |
| 27 | Z3 | Z3's exit test: on a fresh Linux environment, clone a repository, fix a bug on a branch and open a pull request from the terminal. Then the first module of *Learning How to Learn* | Z3 **Done when** passed |
| 28 | Review | A timed test on the month's mathematics; flashcards; weekly note; rest | Weekly note 4 |
| 29 | Buffer | Finish anything late; redo any problem set you skipped | Nothing left over from month 1 |
| 30 | Month gate | Re-run Z3's test cold; write the month report: hours, what passed, what is on track (Z1, Z2) and the weakest topic | Month report 1; Z3 ticked in roadmap #2 §23 |

### Track hour, month 1

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Z3 | The computer as a tool: touch typing, practised for twenty minutes of every track hour from now on, and files, folders and paths | A typing speed recorded, to beat each month |
| Week 2 | Z3 | How to learn (KNOW): active recall and spaced repetition with flashcards, deliberate practice on what you cannot yet do, and explaining an idea in simple words (*Learning How to Learn*) | A flashcard routine that you keep every day |
| Week 3 | Z3 | Technical English: reading documentation and error messages, searching well, and asking a good question | Five real error messages, each explained in your own words |
| Week 4 | Z3 | Safe computing (KNOW): strong passwords and two-factor authentication, never running code you do not trust, and respecting software licences | Two-factor authentication on every account; the licence of every tool you use, noted |

---

## 6. Month 2: vectors, probability, electronics and the on-ramp gates

**Goal:** finish school mathematics, programming and electronics, and pass the whole on-ramp.
**Gates this month:** Z1, Z2 and Z4.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 31 | Z1, Z2 | Z1: Vectors and matrices: vectors as arrows and as lists; adding and scaling them (*Essence of Linear Algebra*). Z2: program 10, a text adventure | Program 10: all ten Z2 programs done |
| 32 | Z1, Z2 | Z1: the dot product, length and angle. Z2: 10 practice problems | Dot products checked in NumPy; 30 of 50 problems |
| 33 | Z1, Z4 | Z1: matrices, and matrix multiplication by hand. Z4: Electricity: charge, current, voltage and resistance; Ohm's law (V = IR) | 2×2 and 3×3 products checked in NumPy; 10 Ohm's-law problems |
| 34 | Z1, Z2 | Z1: a matrix as a transformation: what a product does to a vector. Z2: 10 practice problems | Three 2×2 transformations drawn; 40 of 50 problems |
| 35 | Z1, Z4 | Z1: determinants as areas. Z4: power (P = VI); series and parallel circuits | 15 circuit problems; the determinant as an area, explained in writing |
| 36 | Z1, Z2 | Z1: solving linear systems by elimination. Z2: the last 10 practice problems | 50 of 50 problems (Z2 Build 3) |
| 37 | Review | Redo the week's matrix problems cold; flashcards; weekly note; rest | Weekly note 5 |
| 38 | Z1, Z4 | Z1: Probability and statistics: the probability of events; complements and independence. Z4: Semiconductors: diodes, transistors used as switches, and why smaller transistors let a chip hold more of them | 20 probability problems; a paragraph on a transistor used as a switch |
| 39 | Z1, Z2 | Z1: conditional probability from a table of counts. Z2: reading a CSV file with the `csv` module | One conditional probability computed by hand and by code from the same table |
| 40 | Z1, Z4 | Z1: mean, median, variance and standard deviation. Z4: Binary and logic: bits and bytes; binary and hexadecimal | One data set's statistics by hand and in Python; 20 conversions |
| 41 | Z1, Z4 | Z1: the normal distribution; reading a histogram. Z4: AND, OR, NOT and XOR, with truth tables | A histogram of 10,000 simulated dice sums; four truth tables from memory |
| 42 | Z4 | Circuits in a free simulator: an LED with a resistor, a switch, and the gates of one logic chip (Z4 Build 1). Then the first chapters of Petzold's *Code* | Screenshots and notes for each circuit |
| 43 | Z4, Z2 | Z4: a half adder and a full adder in Logisim-evolution (Z4 Build 2). Z2: the first lessons of Kaggle Learn's pandas course | A one-bit full adder that matches its truth table |
| 44 | Review | Redo the probability problems you got wrong; flashcards; weekly note; rest | Weekly note 6 |
| 45 | Z4 | The parts of a computer: CPU, memory, storage and GPU; the operating system; networks; what the cloud is physically. AI hardware (AWARE): GPUs in datacenters, and the NPUs in phones and laptops (*Crash Course Computer Science*) | The Z4 paragraph: what each part does while an AI model answers a question |
| 46 | Z4 | Z4's exit test, cold: Ohm's law, number bases, XOR's truth table and the paragraph | Z4 **Done when** passed |
| 47 | Z1, Z2 | Z1: revise the weak topics from day 1's test. Z2: an unseen problem, solved against a timer | Two weak topics closed |
| 48 | Z1 | Calculus revision: the chain rule, optimisation and integrals | 30 mixed problems |
| 49 | Z1, Z2 | Z1: matrix and probability revision. Z2: a CS50x Python problem set | 20 mixed problems; one problem set |
| 50 | Z1, Z2 | Z1: a timed test on every topic. Z2: rewrite one early program cleanly, with tests | A marked test; a refactored program |
| 51 | Review | Every flashcard in the deck; weekly note; rest | Weekly note 7 |
| 52 | Z1, Z2 | Check a sample of your Z1 answers with Python, NumPy, SciPy and SymPy: derivatives against finite differences, matrix products and statistics (Z1 Build) | A folder of checking scripts |
| 53 | Z2 | How programs run: the interpreter, memory, and why code is slow. Time a Python loop against the same work in NumPy | A timing table and a paragraph that explains it |
| 54 | Z1 | Z1's exit test, cold: e^(−x²) by the chain rule; a 2×2 product and what it does; mean, variance and a conditional probability; a quadratic's minimum found two ways | Z1 **Done when** passed |
| 55 | Z2 | Z2's exit test: read a CSV file of marks and print each student's average and the class topper, written, tested and debugged alone | Z2 **Done when** passed |
| 56 | F0 | An early start: Petzold's *Code*, on switches, relays and logic | Notes on each chapter |
| 57 | F0 | An early start: the C lecture of CS50x (compiling, variables, loops and functions) | Three small C programs |
| 58 | Review | Review the whole on-ramp; weekly note; rest | Weekly note 8 |
| 59 | Buffer | Finish anything late | Nothing left over from the on-ramp |
| 60 | Month gate | Re-run Z1, Z2 and Z4 cold; write the month report | Month report 2; Z1–Z4 all ticked |

### Track hour, month 2

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Software engineering | Basic: Git beyond the first commit: branches, merges and rebases (*Pro Git*) | A merge conflict made on purpose, and resolved |
| Week 2 | Software engineering | Basic: reading other people's code: one small open-source Python project, read and summarised file by file | A one-page map of someone else's code |
| Week 3 | Software engineering | Basic: unit tests, first with `assert` and then with pytest, for three of your Z2 programs | Tests that fail when you plant a bug |
| Week 4 | Software engineering | Basic: writing a README: what the program does, how to run it and how to test it | A README for every Z2 program that a stranger could follow |

---

## 7. Month 3: computing from zero, then mathematics for machine learning

**Goal:** from a NAND gate to a working CPU, the bits of integers and floats, and the start of the
mathematics behind every model. **Gate this month:** F0.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 61 | F0 | Finish Petzold's *Code*, from logic gates to a working computer | A one-page map from a switch to a CPU |
| 62 | F0 | Digital logic: gates and truth tables, combinational against sequential blocks, and the clock. Nand2Tetris Part I: the Boolean-logic project, every gate built from NAND | Every chip passes its test script |
| 63 | F0 | Nand2Tetris: the Boolean-arithmetic project, adders and the ALU | The ALU passes its tests |
| 64 | F0 | Nand2Tetris: the memory project, from flip-flops to RAM | Every memory chip passes its tests |
| 65 | F0 | Nand2Tetris: the machine-language project | Two assembly programs running on the CPU emulator |
| 66 | F0 | Computer organisation: registers, memory and the fetch–decode–execute cycle. Nand2Tetris: the computer-architecture project, the CPU and the whole computer | Your computer runs the test programs |
| 67 | Review | Explain the fetch–decode–execute cycle on your own CPU, from memory; weekly note; rest | Weekly note 9 |
| 68 | F0 | Nand2Tetris: the assembler, written in Python | The assembler translates every test program |
| 69 | F0 | CS:APP chapter 2: unsigned and two's-complement integers, overflow, shifts, masks and endianness | Check yourself 1 answered |
| 70 | F0 | IEEE-754 floating point: sign, biased exponent and a mantissa with an implicit leading one; normal and subnormal numbers, ±0, ±∞ and NaN; round-to-nearest-even, machine epsilon and the ULP; addition that is not associative (CS:APP chapter 2; the opening sections of Goldberg's paper) | 0.1 encoded by hand; Check yourself 2–3 answered |
| 71 | F0 | C and its memory model: pointers, arrays, structs, alignment and undefined behaviour. Build 2: `floatbits` in C | `floatbits` classifies `0.1`, `1e-40f`, `FLT_MAX` and `NAN` |
| 72 | F0 | Tooling: the Linux shell, git, a build tool, a debugger and Compiler Explorer. CS:APP chapter 3: instruction encoding, calling conventions, and stack against heap, read with `gcc -S` and `objdump -d` | `c = a + b` traced for an integer and for a float |
| 73 | F0 | Build 3: sum ten million random floats forwards, backwards, pairwise and with Kahan summation | Four results against a `double` reference; Check yourself 4 answered |
| 74 | Review | Redo Check yourself 1–4 cold; weekly note; rest | Weekly note 10 |
| 75 | F0 | Operating systems: processes against threads; page tables, the TLB and page faults; system calls, context switches and scheduling; `mmap` and file I/O (the virtualisation part of *OSTEP*) | Check yourself 5–6 answered |
| 76 | F0 | F0's exit test: trace `c = a + b` to the ALU and the FPU, and explain summation order from your Build 3 numbers | F0 **Done when** passed |
| 77 | F1 | The Week 1 textbook in this repository, on linear algebra; *Essence of Linear Algebra* again, now with the mathematics | Matmul written three ways on paper |
| 78 | F1 | Build 1: matmul in NumPy as a triple loop, as dot products and as outer products | Agreement within tolerance, and a timing table; Check yourself 1 answered |
| 79 | F1 | *Mathematics for Machine Learning*, linear algebra: rank, orthogonality, norms, and why you never form an explicit inverse | 15 problems |
| 80 | F1 | Eigendecomposition, SVD and low-rank approximation, with MIT 18.06 lectures as needed | A low-rank approximation of an image, with its error against rank |
| 81 | Review | Redo the linear-algebra problems you missed; weekly note; rest | Weekly note 11 |
| 82 | F1 | *Mathematics for Machine Learning*, vector calculus: partial derivatives, gradients and Jacobians | The Jacobians of five functions |
| 83 | F1 | The vector–Jacobian product, and reverse-mode autodiff worked on paper | Check yourself 2 answered |
| 84 | F1 | Build 3, part 1: a 2-layer MLP, forward and backward, derived by hand | The derivation on paper |
| 85 | F1 | Build 3, part 2: implement it and check it against finite differences in FP64 | A passing gradient check; Check yourself 6 answered |
| 86 | F1 | Probability and statistics: random variables, expectation and variance; the Bernoulli, categorical and Gaussian distributions (Blitzstein & Hwang) | 15 problems |
| 87 | F1 | Maximum likelihood and Bayes' rule; for measurement, median against mean, percentiles, confidence intervals and the bootstrap | A bootstrap confidence interval computed in NumPy |
| 88 | Review | Redo the derivation of Build 3 from memory; weekly note; rest | Weekly note 12 |
| 89 | Buffer | Finish anything late | Nothing left over from month 3 |
| 90 | Month gate | Re-run F0 cold; write the month report | Month report 3; F0 ticked |

### Track hour, month 3

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Software engineering | Intermediate: code review and pull requests; test design (unit, integration and golden-file); continuous integration and pre-commit hooks; semantic versioning; debugging by bisection with `git bisect` (*Software Engineering at Google*) | A bug found with `git bisect` in your own history |
| Week 2 | Software engineering | Advanced: API design and backwards compatibility; design documents; property-based and fuzz testing; reproducible builds (Ousterhout, *A Philosophy of Software Design*) | A one-page design document for `floatbits` |
| Week 3 | Computer architecture, as software sees it | Intermediate: instruction sets and assembly; pipelining and hazards; caches, lines and associativity; virtual memory and the TLB; the latency of each level of the hierarchy (CS:APP; Patterson & Hennessy) | A table of latencies, from a register to a disk |
| Week 4 | Computer architecture, as software sees it | Advanced: out-of-order execution and branch prediction; SIMD; multicore coherence and memory ordering; NUMA; PCIe; your own machine read with `lscpu` and `lstopo` | A diagram of your machine's cores, caches and NUMA nodes |

---

## 8. Month 4: optimisation and numerics, then C, a shell and an allocator

**Goal:** finish the mathematics, then write C that talks to the operating system: a shell and a
memory allocator. **Gate this month:** F1.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 91 | F1 | Optimisation: gradient descent, SGD, momentum, Adam and AdamW, warm-up and decay, with the *Understanding Deep Learning* notebook on Adam | Adam written from its equations, matching a library optimiser on a toy problem |
| 92 | F1 | Information theory: entropy, cross-entropy, KL divergence and perplexity | The perplexity of a unigram model, computed in Python |
| 93 | F1 | Numerical analysis: conditioning against stability, catastrophic cancellation, overflow and underflow, with Trefethen & Bau as needed | Check yourself 5 answered, with an example of each |
| 94 | F1 | Build 2: naive and stable softmax and log-sum-exp; find where the naive version overflows in FP32 and in FP16 | The overflow thresholds, measured; Check yourself 3 answered |
| 95 | F1 | Kahan summation, and why accumulation precision matters more than storage precision | FP16 against FP32 accumulation of a million values, measured |
| 96 | F1 | Cost arithmetic: 2·M·N·K FLOPs, the minimum bytes moved, and arithmetic intensity | Check yourself 4 answered for a 4096³ GEMM |
| 97 | Review | Redo the week's derivations cold; weekly note; rest | Weekly note 13 |
| 98 | F1 | Build 4: a FLOP-and-byte counter for matmul, softmax and LayerNorm | A table of arithmetic intensity across sizes |
| 99 | F1 | Convexity (KNOW) and duality, with Boyd & Vandenberghe as needed; the MIT 18.065 lectures on matrix methods for machine learning | Notes connecting the SVD, least squares and gradient descent |
| 100 | F1 | Check yourself 1–6, cold, in writing | Every answer checked against the Learn list |
| 101 | F1 | F1's exit test: MLP backprop derived on paper, and a BF16 GEMM's FLOPs, bytes and intensity stated without notes | F1 **Done when** passed |
| 102 | F2 | C, the language: types, sizes and integer promotions; pointers, pointer arithmetic and arrays; strings (Kernighan & Ritchie, doing the exercises, compiled with `-Wall -Wextra` and every warning read) | The K&R exercises on pointers and strings |
| 103 | F2 | `struct`, `union` and `enum`; function pointers; `const`, `static` and linkage; the preprocessor and header files; variadic functions; bit manipulation | A generic sort that takes a comparison function |
| 104 | Review | Redo the pointer exercises you got wrong; weekly note; rest | Weekly note 14 |
| 105 | F2 | C and memory: the process layout; `malloc`, `free` and `realloc`; Valgrind on a leak, a double free and a use-after-free that you plant | Three Valgrind reports, each explained |
| 106 | F2 | Linking, with CS:APP chapter 7: multi-file programs and `make`, symbols, static and shared libraries, `nm`, `objdump`, `readelf` and `LD_PRELOAD`; the System V AMD64 calling convention (KNOW) | A library function replaced through `LD_PRELOAD`; Check yourself 8 answered |
| 107 | F2 | POSIX system programming: `fork`, `exec` and `wait`; file descriptors, pipes and `dup2`; `errno` (CS:APP chapter 8) | A C program that pipes `ls` into `wc`; Check yourself 7 answered |
| 108 | F2 | Build 1, part 1: the shell parses a command line, forks, runs the program and waits for it | Single commands run |
| 109 | F2 | Build 1, part 2: pipelines, and `<` and `>` redirection | A three-stage pipeline with redirection runs |
| 110 | F2 | Signals and async-signal safety; Build 1, part 3: background jobs and Ctrl-C | Ctrl-C stops the pipeline but not the shell; Check yourself 9 answered |
| 111 | Review | Walk through your shell's code aloud; weekly note; rest | Weekly note 15 |
| 112 | F2 | Virtual memory and dynamic allocation, with CS:APP chapter 9: `brk`, `mmap` and free lists | A design note for your allocator |
| 113 | F2 | Build 2, part 1: `malloc` and `free` with an implicit free list | A simple trace runs |
| 114 | F2 | Build 2, part 2: explicit free lists, coalescing and `realloc`, with a heap-consistency check after every call | The checker passes after every call |
| 115 | F2 | Build 2, part 3: a random stress trace; throughput and memory utilisation against the system allocator | A comparison table |
| 116 | F2 | Build 2, part 4: run a real program on your allocator through `LD_PRELOAD` | A real program running on your `malloc` |
| 117 | F2 | Data structures and algorithms, first pass: Big-O and what it hides (constants and caches); dynamic arrays, linked lists, stacks and queues, written in C | Each structure, with tests |
| 118 | Review | Redo Check yourself 7–9 cold; weekly note; rest | Weekly note 16 |
| 119 | Buffer | Finish anything late | Nothing left over from month 4 |
| 120 | Month gate | Re-run F1 cold; re-run the shell and allocator tests; write the month report | Month report 4; F1 ticked |

### Track hour, month 4

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Classical machine learning | Basic: supervised against unsupervised learning; train, validation and test splits; linear and logistic regression; k-nearest neighbours; accuracy, precision, recall and ROC curves (*An Introduction to Statistical Learning*; scikit-learn) | A logistic regression with its ROC curve, on a real dataset |
| Week 2 | Classical machine learning | Intermediate: regularisation; the bias–variance trade-off; cross-validation | A regularisation strength chosen by cross-validation |
| Week 3 | Classical machine learning | Intermediate: decision trees, random forests and gradient boosting, with XGBoost or LightGBM | Three tree models compared on one dataset |
| Week 4 | Classical machine learning | Intermediate: SVMs and kernels; k-means and PCA; feature engineering with pandas or Polars | A PCA plot and a k-means clustering of the same data |

---

## 9. Month 5: data structures, Python, modern C++ and concurrency

**Goal:** the data structures under every system, production Python and C++, sanitizers, bindings
and threads. **Gate this month:** F2.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 121 | F2 | Hash tables. Build 3, part 1: open addressing with resizing, in C, tested against a reference | A hash table with passing tests |
| 122 | F2 | Build 3, part 2: benchmark it against `std::unordered_map` | A benchmark table; Check yourself 10 answered |
| 123 | F2 | Heaps and priority queues; binary search and its off-by-one traps; merge sort and quicksort, with their worst cases (Cormen et al. or Skiena) | Each in C, with tests |
| 124 | F2 | Trees: binary search trees, balanced trees (KNOW) and tries | A binary search tree with tests |
| 125 | F2 | Graphs: BFS, DFS and topological sort | Each one run on a small graph you built |
| 126 | F2 | Shortest paths and dynamic programming | 10 algorithm problems solved |
| 127 | Review | Re-implement one structure from memory; weekly note; rest | Weekly note 17 |
| 128 | F2 | Python in depth with *Fluent Python*: the data model, iterators and generators | A generator pipeline over a large file |
| 129 | F2 | Decorators, context managers, classes and dataclasses, type hints, packaging and virtual environments with uv or pip; ruff and mypy; the GIL; `cProfile` and `py-spy` | A small package with a command-line tool, installed in a virtual environment; Check yourself 1 answered |
| 130 | F2 | NumPy's memory model: dtype, shape, strides, views and copies, broadcasting and contiguity | Check yourself 2 answered, and checked in code |
| 131 | F2 | Modern C++ with *A Tour of C++*: value semantics, RAII, the rule of zero, three and five, references and smart pointers | A resource-owning class that leaks nothing under Valgrind |
| 132 | F2 | Move semantics, templates, `constexpr` and lambdas, with *Effective Modern C++*; template metaprogramming, concepts and exception safety (KNOW) | Check yourself 4 answered |
| 133 | F2 | The STL and the cost of each container; the five classes of undefined behaviour; `volatile` and `restrict` in C; the ABI and name mangling (KNOW) | One planted example of each class, caught by a sanitizer; Check yourself 3 answered |
| 134 | Review | Redo the undefined-behaviour examples from memory; weekly note; rest | Weekly note 18 |
| 135 | F2 | Build systems: CMake targets and `PUBLIC`/`PRIVATE` propagation, optimisation and debug flags, and static against shared libraries | A CMake skeleton for the matrix library |
| 136 | F2 | Build 4, part 1: a matrix type with strided views | Views that share storage, with tests |
| 137 | F2 | Build 4, part 2: matmul, and a GoogleTest suite | The suite passes |
| 138 | F2 | Build 4, part 3: CI jobs under ASan with UBSan, and under TSan, with clang-tidy and clang-format in the same pipeline | CI green under both jobs |
| 139 | F2 | Crossing the boundary: pybind11 bindings, the buffer protocol and releasing the GIL in native code. Build 4, part 4: zero-copy NumPy interop, tested from pytest against NumPy | The bindings match NumPy within tolerance |
| 140 | F2 | Debugging: gdb or lldb and core dumps, beside the three sanitizers: debug a crash that you plant in an optimised build | A written post-mortem from a core dump |
| 141 | Review | Rebuild the library from a clean checkout; weekly note; rest | Weekly note 19 |
| 142 | F2 | Threads, mutexes and condition variables, with *C++ Concurrency in Action* | A bounded queue built on condition variables |
| 143 | F2 | Atomics and memory ordering: relaxed, acquire, release and sequentially consistent | The message-passing example, with the outcome that relaxed ordering allows; Check yourself 5 answered |
| 144 | F2 | Build 5: a racy counter that TSan reports, fixed once with an atomic and once with a mutex, both measured under contention | Build 5 committed |
| 145 | F2 | False sharing; SIMD (KNOW): auto-vectorisation, the compiler's vectorisation reports and intrinsics, with the *Performance Ninja* labs | Before-and-after timings; Check yourself 6 answered |
| 146 | F2 | `asyncio` (KNOW): the event loop, and why one blocking call stalls every request; property-based testing (KNOW) | A stalled event loop, shown and then fixed |
| 147 | F2 | F2's exit test: the shell pipeline, the allocator's stress trace, the sanitizer-clean library and its bindings, and acquire/release explained | F2 **Done when** passed |
| 148 | Review | Redo all ten Check yourself questions cold; weekly note; rest | Weekly note 20 |
| 149 | Buffer | Finish anything late | Nothing left over from month 5 |
| 150 | Month gate | Re-run F2 cold; write the month report | Month report 5; F2 ticked |

### Track hour, month 5

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Classical machine learning | Advanced: probabilistic models and the EM algorithm; Gaussian processes; calibration (Bishop; Murphy) | EM fitted to a mixture of two Gaussians |
| Week 2 | Classical machine learning | Advanced: imbalanced data; the basics of causal inference; time-series forecasting with statsmodels; Stanford CS229 as needed | A calibrated classifier on an imbalanced dataset |
| Week 3 | Classical machine learning | Projects: the programme's Week 3–4 artefacts, and part 1 of a tabular problem solved with gradient boosting | A gradient-boosting baseline with its validation score |
| Week 4 | Data structures and algorithms | Advanced: balanced trees and B-trees, tries, union–find, shortest paths and spanning trees, and amortised analysis (Sedgewick & Wayne) | Union–find and a minimum spanning tree in C, with tests |

---

## 10. Month 6: deep learning, from autograd to your own GPT

**Goal:** build every piece of a language model yourself, from a scalar autograd engine to a GPT
with your own tokenizer. **Gate this month:** F3.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 151 | F3 | ML foundations: splits, bias and variance, regularisation and data leakage (*Dive into Deep Learning* as needed) | A train/validation/test split, with the leak you avoided written down |
| 152 | F3 | *Zero to Hero*: micrograd. Build 1, part 1: a scalar autograd engine | Addition, multiplication, tanh and backward, working |
| 153 | F3 | Build 1, part 2: train a small MLP with your engine | A falling loss curve; Check yourself 1 answered |
| 154 | F3 | makemore: the bigram model, and the training loop | A trained bigram model that samples names |
| 155 | F3 | Layers: linear layers; ReLU, GELU and SiLU; embeddings. makemore: an MLP language model | Validation loss below the bigram model's |
| 156 | F3 | makemore: activations, gradients and BatchNorm; Xavier and Kaiming initialisation | Plots of activation statistics before and after a fix |
| 157 | Review | Re-derive backprop through tanh and a linear layer from memory; weekly note; rest | Weekly note 21 |
| 158 | F3 | makemore: manual backpropagation. Build 2: tensor-level backprop through an MLP with a normalisation layer, without `loss.backward()` | Your gradients match autograd |
| 159 | F3 | makemore: a WaveNet-style model; convolution, recurrent networks and LSTMs (KNOW) | A deeper model trained |
| 160 | F3 | Softmax fused with cross-entropy | Check yourself 2 answered, and checked numerically |
| 161 | F3 | "Let's build the GPT Tokenizer": byte-pair encoding. Write your own tokenizer | A tokenizer that round-trips text; Check yourself 6 answered |
| 162 | F3 | The transformer block, read whole: "Attention Is All You Need" beside *The Annotated Transformer* | Every tensor shape in the model, written down |
| 163 | F3 | "Let's build GPT", part 1: scaled dot-product attention, the causal mask and multi-head attention | Attention that passes a causal-mask test; Check yourself 3 answered |
| 164 | Review | Draw a decoder block from memory, with every shape; weekly note; rest | Weekly note 22 |
| 165 | F3 | Build 3: the block's MLP (GELU and SwiGLU), residual stream and pre-norm; LayerNorm against RMSNorm; weight tying | A complete block, shape-checked; Check yourself 4 answered |
| 166 | F3 | Positional information: sinusoidal, learned and RoPE; MQA and GQA (KNOW) | RoPE implemented and tested; Check yourself 5 answered |
| 167 | F3 | Build 3: the training loop, with batching, AdamW, a learning-rate schedule, gradient clipping, checkpointing and evaluation | A training run on a small corpus |
| 168 | F3 | Build 3: train, sample, and compare with a unigram baseline | Validation loss well below the unigram baseline |
| 169 | F3 | Build 4: a finite-difference gradient check of your attention block in FP64 | The check passes |
| 170 | F3 | Beyond language models (KNOW): CNNs, vision transformers (with `timm`), diffusion, recommendation and speech models, with *Understanding Deep Learning* | One page comparing their bottlenecks with an LLM's |
| 171 | Review | Train your GPT again from a clean checkout; weekly note; rest | Weekly note 23 |
| 172 | F3 | *Understanding Deep Learning* on initialisation, normalisation and optimisation; transfer learning; selected CS231n and CS224n lectures | Notes on three things you would now change in your GPT |
| 173 | F3 | Check yourself 1–6, cold, in writing | Every answer checked |
| 174 | F3 | A shapes drill: every tensor shape through a GQA decoder block, from memory | The drill passes without notes |
| 175 | F3 | F3's exit test: every shape from memory, and your GPT's loss and gradient check | F3 **Done when** passed |
| 176 | F4 | "Transformer Math 101": training compute and memory | C ≈ 6PD and about 16 bytes per parameter, derived; Check yourself 2–3 answered |
| 177 | F4 | kipply's "Transformer Inference Arithmetic": the KV cache and the decode bound | The KV-bytes-per-token formula; Check yourself 4 answered |
| 178 | Review | Recompute every F4 number so far without notes; weekly note; rest | Weekly note 24 |
| 179 | Buffer | Finish anything late | Nothing left over from month 6 |
| 180 | Month gate | Re-run F3 cold; write the month report | Month report 6; F3 ticked |

### Track hour, month 6

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Generative models beyond LLMs | Basic and Intermediate: what a generative model does; autoencoders; sampling; VAEs; GANs (*Understanding Deep Learning*, the generative chapters) | A VAE trained on a toy dataset, and sampled |
| Week 2 | Generative models beyond LLMs | Intermediate: diffusion models and denoising; conditioning on text (the Diffusers documentation) | A small diffusion model trained on a toy dataset |
| Week 3 | Generative models beyond LLMs | Advanced: latent diffusion; classifier-free guidance; flow matching; vision–language models; speech models | One page on why diffusion costs many steps per request where an LLM costs many tokens |
| Week 4 | Classical machine learning | Projects, part 2: the same tabular problem with your own neural network, and the reason gradient boosting wins | The comparison, with its reason written down |

---

## 11. Month 7: LLM arithmetic, then your first GPU kernels

**Goal:** count everything an LLM costs, then write HIP kernels and predict their bound before you
profile them. **Gates this month:** F4 and F5.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 181 | F4 | Architecture variants: dense models; mixture-of-experts (router, top-k selection, capacity factor and load-balancing loss); RoPE scaling (KNOW); multi-head latent attention (AWARE) | A one-page comparison of a dense and an MoE block |
| 182 | F4 | Scaling laws: Kaplan et al., and Chinchilla's D ≈ 20P, which is optimal for training cost only | Check yourself 6 answered |
| 183 | F4 | *How to Scale Your Model* chapter 4, and the CS336 lectures on architectures and scaling | The chapter's worked problems redone |
| 184 | F4 | Build: `llm_calc.py`, part 1: parameters by component, training FLOPs and training memory | Check yourself 1 answered with the calculator |
| 185 | F4 | Build, part 2: KV bytes per token and per sequence, and a lower bound on decode latency. Validate the parameter count against a real checkpoint | An exact match, to the integer; Check yourself 5 answered |
| 186 | F4 | Tokenisation and sampling (KNOW); Post-training (KNOW): SFT, RLHF and DPO, and how RL post-training puts inference inside the training loop. Then F4's exit test on a config you have not seen | F4 **Done when** passed |
| 187 | Review | Recompute the week's numbers without notes; weekly note; rest | Weekly note 25 |
| 188 | F5 | Set up the AMD GPU as in roadmap #2 §3B: `rocminfo`, `amd-smi version` and PyTorch for ROCm, with every version recorded | `torch.cuda.is_available()` prints `True` |
| 189 | F5 | Scaling laws of parallelism: Amdahl's and Gustafson's laws, strong and weak scaling; CPU parallelism: SIMD lanes, multicore, caches and coherence, and NUMA, with *Programming Massively Parallel Processors* (PMPP) | Five scaling problems solved |
| 190 | F5 | The GPU execution model (PMPP; GPU MODE lectures 1–3); AMD-GPU-PATH §4–§5, doing every "See it yourself" block | A diagram of grid, workgroup, wavefront and lane on your GPU |
| 191 | F5 | Build 1: vector add in HIP; achieved GB/s against peak bandwidth | The achieved fraction of peak; Check yourself 1 answered |
| 192 | F5 | The memory hierarchy; Access patterns: coalescing, LDS bank conflicts and padding, vectorised loads and alignment (AMD-GPU-PATH §6; GPU MODE lectures 4–6) | Check yourself 5 answered |
| 193 | F5 | Build 2, part 1: a reduction with global atomics, then with an LDS tree | GB/s at each step |
| 194 | Review | Explain coalescing and bank conflicts aloud, with a drawing; weekly note; rest | Weekly note 26 |
| 195 | F5 | Build 2, part 2: a wavefront-level reduction, then several elements per thread | The whole reduction ladder, measured |
| 196 | F5 | Divergence; Occupancy and latency hiding: what limits occupancy (VGPRs, SGPRs, LDS and workgroup size), bytes in flight = latency × bandwidth, and why maximum occupancy is not the goal | Check yourself 3–4 answered |
| 197 | F5 | Synchronisation: barriers, atomics, streams, events and pinned memory | Check yourself 6 answered |
| 198 | F5 | Build 3: a tiled matmul in LDS at several tile sizes | GFLOP/s for each tile size |
| 199 | F5 | The Roofline paper; place each matmul on the roofline by its arithmetic intensity | Check yourself 2 answered |
| 200 | F5 | Build 4, part 1: bandwidth and FMA-throughput microbenchmarks | A measured roofline for your GPU |
| 201 | Review | Predict five kernels' bounds from memory; weekly note; rest | Weekly note 27 |
| 202 | F5 | Build 4, part 2: compare with the roofline from `rocprof-compute` (AMD-GPU-PATH §9), and read a `rocprofv3 --kernel-trace` | Your roofline and the tool's, side by side |
| 203 | F5 | Horace He's "Making Deep Learning Go Brrrr"; GPU MODE lectures 7–9 | Notes on the three regimes: compute-bound, memory-bound and overhead-bound |
| 204 | F5 | Exercises from the Aalto course *Programming Parallel Computers* | Two exercises passing their tests |
| 205 | F5 | A predict-then-profile drill on every kernel of this stage | A table of predictions against counters |
| 206 | F5 | Work and span (KNOW), from the CS149 or CMU 15-418/618 lectures | Notes |
| 207 | F5 | F5's exit test: every bound predicted before profiling and confirmed by counters, and the roofline within your stated margin | F5 **Done when** passed |
| 208 | Review | Re-run your kernels from a clean build; weekly note; rest | Weekly note 28 |
| 209 | Buffer | Finish anything late | Nothing left over from month 7 |
| 210 | Month gate | Re-run F4 and F5 cold; write the month report | Month report 7; F4 and F5 ticked |

### Track hour, month 7

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Large language models | Tools: Hugging Face Transformers, PEFT, TRL and Datasets on a small open model; Raschka's *Build a Large Language Model (From Scratch)* as a second pass; Jurafsky & Martin as a reference | A small model loaded, fine-tuned for a few steps and evaluated |
| Week 2 | GPU and accelerator programming | CUDA (KNOW): NVIDIA's *CUDA C++ Programming Guide* read beside HIP, name for name | A table that maps CUDA's names to HIP's |
| Week 3 | Databases and storage engines | Basic and Intermediate: tables, keys and SQL; transactions; indexes and query plans; normalisation; ACID and isolation levels (CMU 15-445/645; PostgreSQL, SQLite and Redis) | One query made fast with an index, and its plan explained |
| Week 4 | Databases and storage engines | Intermediate: window functions and CTEs; OLTP against OLAP | Five analytical queries over your own F1 and F4 results |

---

## 12. Month 8: measurement, operating systems and networks

**Goal:** benchmarks that survive review, a kernel you have changed yourself, and a server whose
latency you can predict. **Gate this month:** F6.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 211 | F6 | Benchmark design: warm-up, enough repetitions, the median and p95/p99 with the spread, fixed inputs and seeds (Gregg's *Systems Performance* on methodology); The performance report: the question, setup, method, results with uncertainty, bottleneck analysis, and what was not tested | Check yourself 1 answered |
| 212 | F6 | Sources of noise, and timing correctly: device events, host timers and where to synchronise | Check yourself 2–3 answered |
| 213 | F6 | Profiling: sampling against instrumentation; `perf`, flame graphs and counters for caches, the TLB, branch prediction and false sharing; top-down microarchitecture analysis, on your F2 code with *Performance Ninja* | A flame graph of your allocator's stress trace |
| 214 | F6 | `rocprofv3` and ROCm Compute Profiler on your F5 kernels; the PyTorch profiler, read in Perfetto | Check yourself 5 answered |
| 215 | F6 | Comparing runs: distributions rather than single numbers, the smallest change your noise lets you detect, and change-point detection (AWARE). Build: the `bench/` harness: a warm-up, N timed repetitions, a JSON record of samples and environment, and a comparator that respects the noise band; `hyperfine` for command-line timings | The harness, with its tests; Check yourself 4 answered |
| 216 | F6 | Plant a regression; show that it is flagged and an unchanged re-run is not. Then F6's exit test | F6 **Done when** passed |
| 217 | Review | Write a one-page report on one F5 kernel in the F6 format; weekly note; rest | Weekly note 29 |
| 218 | F7 | Operating-system internals: the kernel boundary, user and kernel mode, traps, interrupts and exceptions, and the path of a system call (the concurrency and persistence parts of *OSTEP*) | Notes on the path of one system call |
| 219 | F7 | The xv6 book; set up QEMU and the RISC-V toolchain for MIT 6.1810, then its first lab | xv6 boots, and the first lab passes |
| 220 | F7 | The system-call lab | Its grading tests pass |
| 221 | F7 | Multi-level page tables and the TLB; the page-table lab, part 1 | Part 1 working |
| 222 | F7 | The page-table lab, part 2 | Its grading tests pass |
| 223 | F7 | The copy-on-write `fork` lab | Its grading tests pass; Check yourself 7 answered |
| 224 | Review | Explain a page fault on xv6 step by step, from memory; weekly note; rest | Weekly note 30 |
| 225 | F7 | Scheduling (round-robin, priorities, multi-level feedback queues, CFS and EEVDF); spinlocks, sleeping locks and futexes; drivers, DMA and the IOMMU; inodes, the buffer cache and journaling; `epoll` and `io_uring`; KVM, SR-IOV and PCIe passthrough (KNOW); eBPF (AWARE) | Check yourself 8 answered |
| 226 | F7 | Networking from the socket up: layers, addresses and the socket API (Beej's guide); TCP's handshake, flow and congestion control, head-of-line blocking, and Nagle against `TCP_NODELAY`; UDP, DNS and TLS; HTTP/1.1 against HTTP/2, and QUIC (AWARE); gRPC and SSE (Kurose & Ross as needed) | An echo server; Check yourself 3 answered |
| 227 | F7 | Build 2, part 1: a socket server that streams tokens over SSE | Tokens streaming to `curl` |
| 228 | F7 | Build 2, part 2: an open-loop load generator; p50 and p99 latency against offered load | The latency curve, with its knee |
| 229 | F7 | Queueing: Little's law, the M/M/1 intuition, open and closed loops, and fan-out tails. Predict the knee from your measured service time | Prediction against measurement; Check yourself 1–2 answered |
| 230 | F7 | Latency literacy with `iperf3`; load balancing, from L4 and L7 to consistent hashing | Your own table of latency orders of magnitude |
| 231 | Review | Re-derive Little's law and the knee from memory; weekly note; rest | Weekly note 31 |
| 232 | F7 | Go basics, for the 6.5840 labs | Two small Go programs with goroutines and channels |
| 233 | F7 | The 6.5840 lectures; Lab 1 (MapReduce), part 1 | The coordinator and the workers talking |
| 234 | F7 | Lab 1, part 2 | The MapReduce tests pass |
| 235 | F7 | Distributed-systems fundamentals: failure models and partial failure; timeouts chosen from a latency percentile, capped backoff with jitter, retry budgets and idempotency (the AWS Builders' Library article) | Check yourself 5 answered |
| 236 | F7 | Build 4: a client that causes a retry storm with naive retries, then one that does not | Both runs plotted |
| 237 | F7 | The Raft paper and site: leader election, the log and safety | A one-page summary; Check yourself 4 answered |
| 238 | Review | Explain Raft's election and log rules from memory; weekly note; rest | Weekly note 32 |
| 239 | Buffer | Finish anything late | Nothing left over from month 8 |
| 240 | Month gate | Re-run F6 cold; re-run the xv6 grading; write the month report | Month report 8; F6 ticked |

### Track hour, month 8

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Databases and storage engines | Advanced: B-trees against LSM-trees; write-ahead logging and recovery; MVCC; query optimisation; columnar storage and vectorised execution; replication and sharding (Petrov, *Database Internals*) | A design for a key/value store with a write-ahead log |
| Week 2 | Databases and storage engines | Projects: that key/value store, with a write-ahead log and a B-tree or LSM-tree index, surviving a kill in the middle of a write | Recovery after a planted crash, tested |
| Week 3 | Operating systems and Linux | Advanced: a container built by hand from namespaces and cgroups; huge pages; tracing with `strace` and `bpftrace`; `vmstat`, `iostat`, `numactl` and `taskset` (Gregg, *BPF Performance Tools*) | A process held to a cgroup limit you set, and traced |
| Week 4 | Generative models beyond LLMs | Projects: one Diffusers pipeline profiled on your GPU with your F6 harness | The pipeline's time per step, and its hottest kernel |

---

## 13. Month 9: consensus and storage, then the GEMM ladder

**Goal:** finish the foundation with Raft and the storage stack, then climb the GEMM ladder to the
matrix cores. **Gate this month:** F7.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 241 | F7 | The 6.5840 Raft lab: leader election | The election tests pass |
| 242 | F7 | Raft: log replication | The log tests pass |
| 243 | F7 | Raft: persistence | The persistence tests pass |
| 244 | F7 | Raft: log compaction. Then run the whole suite many times, unreliable-network tests included | Repeated clean passes |
| 245 | F7 | The 6.5840 key/value server lab | Its tests pass |
| 246 | F7 | Replication, partitioning and consistency with *Designing Data-Intensive Applications*; logical clocks; CAP and PACELC (KNOW) | Notes placing etcd on the consistency spectrum |
| 247 | Review | Re-run the Raft suite and read one failure log closely; weekly note; rest | Weekly note 33 |
| 248 | F7 | The storage stack: block, file and object storage; throughput, IOPS and latency; the page cache, `O_DIRECT` and `fsync` | Check yourself 6 answered |
| 249 | F7 | Build 5: a fio study on one NVMe drive: sequential and random, small and large blocks, buffered and `direct=1`, with and without `fsync` | Every number explained |
| 250 | F7 | Linux isolation: namespaces (namespaces(7)) and cgroups v2; run a process in its own PID and mount namespaces | Notes on what a container is made of |
| 251 | F7 | "The Tail at Scale"; load shedding, backpressure and circuit breakers; etcd and ZooKeeper (KNOW) | A one-page summary |
| 252 | F7 | Advanced, as time allows: the fault-tolerant key/value lab, built on your Raft | Progress recorded |
| 253 | F7 | F7's exit test: xv6 grading, the predicted knee, repeated Raft passes and the fio explanation | F7 **Done when** passed; the foundation is complete |
| 254 | Review | Review the F0–F7 flashcards; weekly note; rest | Weekly note 34 |
| 255 | P1 | The GEMM ladder, nine rungs from naive to autotuned: Boehm's matmul worklog, translated to HIP with AMD-GPU-PATH §7 and §11; rungs 1 and 2, naive and coalesced | Two rungs, each with a measured delta and the counter that explains it |
| 256 | P1 | Rung 3: LDS tiling | Rung 3 and its counter; Check yourself 2 answered |
| 257 | P1 | Rung 4: 1-D, then 2-D, register blocking; Occupancy vs ILP (KNOW): more work per thread at lower occupancy often wins (Volkov) | Rung 4 and its counter |
| 258 | P1 | Rungs 5 and 6: vectorised loads and wavefront-level tiling | Rungs 5 and 6, each with its counter |
| 259 | P1 | Rung 7: double-buffering (software pipelining) | Rung 7 and its counter |
| 260 | P1 | Matrix cores: MFMA on CDNA (AMD-GPU-PATH §7) or WMMA on RDNA (AMD-AI-STACK §5B), with the AMD Matrix Instruction Calculator | The operand and accumulator layouts, drawn |
| 261 | Review | Rebuild every rung from a clean checkout and re-measure; weekly note; rest | Weekly note 35 |
| 262 | P1 | Rungs 8 and 9: the matrix cores, then autotuning | The ladder complete; Check yourself 1 answered |
| 263 | P1 | Compare against hipBLASLt at the same shapes, including skinny decode shapes | The fraction of hipBLASLt, stated with its shapes |
| 264 | P1 | Reading the ISA: keep the intermediate files with `-save-temps`, then find the global and LDS loads, the `s_waitcnt` waits, MFMA issue, the VGPR count and any spills to scratch. Build 3: annotate your best GEMM's inner loop | The annotated AMDGCN; Check yourself 3 answered |
| 265 | P1 | The Triton tutorials: vector add, fused softmax and matmul | Each one run and timed |
| 266 | P1 | Memory-bound kernels: fused elementwise ops, reductions, online softmax, LayerNorm and RMSNorm, fused residual-add plus norm, and rotary embeddings (the online-softmax paper; Triton's layer-norm tutorial). Build 2: fused softmax and fused RMSNorm with residual, validated against PyTorch | Both kernels within a tolerance stated per dtype; Check yourself 4 answered |
| 267 | P1 | The FlashAttention paper; GPU MODE lectures 12 and 14 | FlashAttention's tiling and recomputation, written out; Check yourself 5 answered |
| 268 | Review | Explain every rung's counter from memory; weekly note; rest | Weekly note 36 |
| 269 | Buffer | Finish anything late | Nothing left over from month 9 |
| 270 | Month gate | Re-run F7 cold; write the month report | Month report 9; F7 ticked, and every foundation stage passed |

### Track hour, month 9

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Networking | Intermediate and Advanced: REST, load balancers, NAT and firewalls; WebSockets; kernel bypass and zero-copy (KNOW); `dig`, `ss`, `tcpdump`, Wireshark, `mtr`, `grpcurl` and Envoy (Stevens, *UNIX Network Programming*) | One of your SSE streams captured and read in Wireshark |
| Week 2 | Networking | Projects: a chat server in C built on `epoll` | Many clients chatting through one thread |
| Week 3 | Distributed systems | Advanced: Paxos; two-phase commit and sagas; quorums; gossip and failure detection; CRDTs; stream processing (Kleppmann; van Steen & Tanenbaum) | A one-page comparison of Raft and Paxos |
| Week 4 | Distributed systems | The papers that 6.5840 assigns beyond Raft (MapReduce, GFS, ZooKeeper and Spanner), then its sharded key/value lab as far as time allows | Notes on each paper; progress on the sharded lab recorded |

---

## 14. Month 10: kernels and compilers, on the GPU and on the NPU

**Goal:** finish the kernel craft on the GPU, repeat it on the device's iGPU and NPU, then learn
what generates kernels, both just in time and ahead of time. **Gates this month:** P1, P1 edge, P2
and P2 edge.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 271 | P1 | Build 2: a Triton FlashAttention forward pass, validated against PyTorch | Output within tolerance |
| 272 | P1 | Benchmark it across sequence lengths, against its I/O analysis | Scaling that matches the prediction |
| 273 | P1 | GEMM variants (KNOW): split-K, stream-K, persistent kernels, grouped GEMM and epilogue fusion; FlashAttention-2 and -3 | Check yourself 6 answered |
| 274 | P1 | The libraries (KNOW): hipBLASLt, rocBLAS, Composable Kernel, rocWMMA and AITER (AMD-AI-STACK §9–§10); GPU MODE lectures 25 and 29 | A map of which library you would call for which shape |
| 275 | P1 | Debugging GPU code: reference comparisons, tail shapes, `AMD_SERIALIZE_KERNEL`, `AMD_LOG_LEVEL` and `rocgdb` | A planted missing-mask bug, found; Check yourself 7 answered |
| 276 | P1 | P1's exit test: a counter behind every rung, your GEMM's fraction of hipBLASLt, and FlashAttention validated | P1 **Done when** passed |
| 277 | Review | Explain one FlashAttention tile from memory; weekly note; rest | Weekly note 37 |
| 278 | P1 edge | Set up the edge device: ONNX Runtime with its NPU execution provider (AMD-AI-STACK §13; QUALCOMM-AI-STACK §8) | A small model running on the NPU |
| 279 | P1 edge | The NPU's programming model: XDNA's tiles and IRON (AMD-AI-STACK §6); Hexagon's HVX, HMX and VTCM (QUALCOMM-AI-STACK §6) | A one-page comparison with the GPU's execution model |
| 280 | P1 edge | The integrated GPU: HIP where ROCm supports the iGPU (the Ryzen AI Max APUs, `gfx1151`), WMMA and wave32 on RDNA, and Adreno through OpenCL. Build 1: your fused RMSNorm or softmax on the iGPU, on a roofline built from the device's measured memory bandwidth | The kernel's fraction of the shared bandwidth |
| 281 | P1 edge | Build 1 again, while another engine streams memory | The fraction under interference |
| 282 | P1 edge | The cliffs: a matrix type that HMX lacks falls back to HVX, and a small operator can cost 8–22× more to dispatch than to run. Build 2: one normalisation layer exported fused and as a chain of primitive operators, both run through the NPU's execution provider | Partitions and latency for both |
| 283 | P1 edge | The edge side's exit test | P1 edge **Done when** passed |
| 284 | Review | Compare the GPU and NPU results side by side; weekly note; rest | Weekly note 38 |
| 285 | P2 | PyTorch internals with Yang's posts: storage, sizes, strides and the dispatcher | A diagram of one call's path through the dispatcher |
| 286 | P2 | Custom operators: `torch.library`, fake kernels and autograd formulas. Build 1: your P1 RMSNorm registered as an operator | `opcheck` passes; Check yourself 3 answered |
| 287 | P2 | `torch.compile`: TorchDynamo, guards and graph breaks; AOTAutograd; Inductor, read with `TORCH_COMPILE_DEBUG` and `TORCH_LOGS` | Check yourself 1, 2, 4 and 6 answered |
| 288 | P2 | Build 2: compile a small transformer, find a missed fusion or a graph break, fix it and measure the result | The fix and its measured gain |
| 289 | P2 | Compiler foundations; the MLIR paper; the Toy tutorial, chapters 1–3 | Toy parses and emits its dialect |
| 290 | P2 | The Toy tutorial, chapters 4–6 (Build 3) | Toy lowered to LLVM |
| 291 | Review | Explain a graph break and a guard failure from memory; weekly note; rest | Weekly note 39 |
| 292 | P2 | Build 4: dump Triton's IR stages for your P1 softmax, and find the layout decisions in TTGIR | Check yourself 5 answered |
| 293 | P2 | JAX and XLA (KNOW); Scheduling languages: Halide's separation of algorithm and schedule, TVM, and search-based autotuning; then P2's exit test | P2 **Done when** passed |
| 294 | P2 edge | Export at fixed shapes (`torch.export`, then ONNX); partitioners, including ExecuTorch's `QnnPartitioner`; Built for one chip: a QNN context binary loads only on the SoC it was built for, while a DLC stays portable | Your transformer exported at one fixed length |
| 295 | P2 edge | Build: variable-length input in buckets. Compile a few fixed lengths, pad each input to the next, and measure the padding waste and latency of each bucket | A bucket table |
| 296 | P2 edge | Build: compare with `torch.compile` on the GPU for compile time, first-call time, steady-state time and an unseen shape | The comparison table |
| 297 | P2 edge | Graph surgery: Gen AI Builder's steps and the four-step rewrite (QUALCOMM-AI-STACK §6B, §9); then the edge side's exit test | P2 edge **Done when** passed |
| 298 | Review | Explain what ahead-of-time compilation buys and costs, from memory; weekly note; rest | Weekly note 40 |
| 299 | Buffer | Finish anything late | Nothing left over from month 10 |
| 300 | Month gate | Re-run P1, P1 edge, P2 and P2 edge cold; write the month report | Month report 10; four gates ticked |

### Track hour, month 10

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Compilers, linkers and runtimes | Intermediate: lexing, parsing and abstract syntax trees, with the tree-walk interpreter of Nystrom's *Crafting Interpreters*: its scanner and parser | An interpreter that parses expressions and statements |
| Week 2 | Compilers, linkers and runtimes | Intermediate: evaluation, environments and closures, and the interpreter finished | Your interpreter running a recursive Fibonacci |
| Week 3 | Compilers, linkers and runtimes | Intermediate and Advanced: intermediate representations and SSA form; inlining, constant propagation, dead-code elimination and loop-invariant code motion; LLVM IR and its pass pipeline, through LLVM's Kaleidoscope tutorial with `clang`, `opt` and `llc` | Kaleidoscope emitting LLVM IR, with passes applied by `opt` |
| Week 4 | Compilers, linkers and runtimes | Advanced: instruction selection and register allocation; vectorisation; JIT compilation, with Kaleidoscope's JIT (Cooper & Torczon, *Engineering a Compiler*) | Kaleidoscope compiled just in time |

---

## 15. Month 11: distributed training and serving at scale

**Goal:** train across GPUs with predicted step times, train for devices, then serve under an SLO
with engines and general-purpose model servers. **Gates this month:** P3, P3 edge and P4.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 301 | P3 | *The Ultra-Scale Playbook*; the collectives; the α–β model; ring against tree algorithms | Check yourself 1 answered |
| 302 | P3 | Build 1: your own ring all-reduce on `torch.distributed` point-to-point operations, validated against the library collective, with α and B fitted | The fitted bandwidth curve |
| 303 | P3 | Data parallelism: DDP bucketing and overlap, global batch size and gradient accumulation; Sharded data parallelism: ZeRO stages 1–3 and FSDP ("Transformer Math 101" on memory under ZeRO) | Check yourself 2 answered |
| 304 | P3 | Rent the multi-GPU node. Build 3: predict step time from `llm_calc.py` and the α–β model. Then Build 2: a DDP run of your GPT | Predicted and measured step time |
| 305 | P3 | Build 2: the FSDP run, with memory per GPU, tokens/s, MFU and a trace that shows the overlap | The FSDP row of your table; Check yourself 5 answered |
| 306 | P3 | Tensor parallelism: Megatron's column and row splits. Build 2: the tensor-parallel run | The tensor-parallel row; Check yourself 3 answered |
| 307 | Review | Re-derive the ring's traffic and the pipeline bubble; weekly note; rest | Weekly note 41 |
| 308 | P3 | Pipeline parallelism: GPipe and 1F1B. A pipeline-parallel run if you have four or more GPUs | Check yourself 4 answered |
| 309 | P3 | Context and expert parallelism (KNOW); Memory techniques: full and selective activation recomputation, BF16 compute with FP32 master weights, and offload (AWARE); Metrics: MFU against HFU, tokens/s per GPU, and the step-time breakdown | The MFU of every run, computed with the right FLOP count |
| 310 | P3 | Reliability at scale; trace the collectives with `rocprofv3 --rccl-trace` (AMD-AI-STACK §15); read how torchtitan, Megatron-LM and DeepSpeed configure the layouts you ran | A trace that shows where communication is exposed |
| 311 | P3 | Fine-tuning and post-training workloads (KNOW): LoRA, QLoRA, DPO and HybridFlow; the optional Build 4, a LoRA fine-tune on one GPU | Check yourself 6–7 answered |
| 312 | P3 | Attribute the residual between prediction and measurement; then P3's exit test | P3 **Done when** passed |
| 313 | P3 edge | Distillation (Hinton, Vinyals & Dean); Quantisation-aware training, which AIMET keeps for last; Adapters on the device: a LoRA per task or per user, built into the device model by Gen AI Builder. Size the student from the device's memory budget with `llm_calc.py` | A memory budget stated before training |
| 314 | Review | Explain every row of your parallelism table from memory; weekly note; rest | Weekly note 42 |
| 315 | P3 edge | Build: distil your GPT or an open model into the student, and report its quality against the teacher and its memory against the budget | The student, measured |
| 316 | P3 edge | Federated learning: rounds, averaging weighted by data, clients whose data differs, and drop-outs; secure aggregation and Flower (AWARE). Build: simulate federated averaging with 20 or more clients; then the edge side's exit test | P3 edge **Done when** passed |
| 317 | P4 | The two phases: prefill compute-bound, decode bandwidth-bound, and the F4 crossover; KV-cache management: fragmentation and block tables, prefix caching and RadixAttention, KV-cache quantisation (KNOW) and offload (AWARE) (kipply; *How to Scale Your Model* chapter 7; the PagedAttention paper) | Check yourself 1–2 answered |
| 318 | P4 | Engines: vLLM and SGLang on AMD with AITER, and llama.cpp; TensorRT-LLM, TGI and NVIDIA Dynamo (AWARE). The vLLM documentation on scheduling, prefix caching and speculative decoding; the Orca and SGLang papers | Check yourself 3 answered |
| 319 | P4 | Metrics: TTFT, ITL and end-to-end latency at p50 and p99, goodput under an SLO, and cost per million tokens. Build 1: vLLM on ROCm (AMD-AI-STACK §12); sweep the request rate, and plot TTFT and ITL against throughput | The highest throughput that meets your SLO; Check yourself 5 answered |
| 320 | P4 | Build 2: decode on your F5 roofline, with bytes per token against achieved bandwidth | The gap, explained |
| 321 | Review | Re-derive the speculative-decoding formula; weekly note; rest | Weekly note 43 |
| 322 | P4 | Build 3: speculative decoding, with the acceptance rate and speed-up compared with the formula | Check yourself 4 answered |
| 323 | P4 | Launch overhead: HIP graphs for the decode loop; Parallelism for serving: TP for latency, DP and PP for throughput, EP for MoE. Build 4: toggle one attention-backend or AITER option, and attribute the change with a profile | The attribution |
| 324 | P4 | The API layer: OpenAI-compatible endpoints, SSE streaming, cancellation, structured outputs and multi-LoRA serving | A streaming client whose disconnect cancels the work on the server |
| 325 | P4 | General-purpose model servers: embedders, re-rankers, classifiers and vision models, and what a framework automates (validation, batching, concurrency, health checks and metrics). Build 5, part 1: an embedding model behind a hand-written FastAPI service | The service under open-loop load |
| 326 | P4 | Build 5, part 2: the same model in BentoML, and in Triton Inference Server or Ray Serve, at one batch policy; TorchServe, TensorFlow Serving, Seldon Core and OpenVINO (AWARE) | Throughput and p99 for all three; Check yourself 7–8 answered |
| 327 | P4 | Disaggregated serving: DistServe and Splitwise. Then P4's exit test | P4 **Done when** passed; Check yourself 6 answered |
| 328 | Review | Explain goodput and your three-server results from memory; weekly note; rest | Weekly note 44 |
| 329 | Buffer | Finish anything late; stop every rented GPU | Nothing left over from month 11 |
| 330 | Month gate | Re-run P3, P3 edge and P4 cold; write the month report | Month report 11; three gates ticked |

### Track hour, month 11

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | ML frameworks and compilers | CMU *Deep Learning Systems*: the lectures on automatic differentiation and hardware acceleration, and the first assignments of its Needle framework | Needle's automatic differentiation passing its tests |
| Week 2 | DevOps and platform engineering | Basic and Intermediate: Linux administration and shell scripting; Dockerfiles and multi-stage builds; Docker Compose; Docker or Podman | Your FastAPI service in a multi-stage image, run with Compose |
| Week 3 | DevOps and platform engineering | Intermediate: CI/CD with GitHub Actions; a local cluster with kind or k3d; pods, deployments and services with `kubectl`; Helm and Kustomize (*Kubernetes: Up and Running*) | The service deployed to a local cluster from CI |
| Week 4 | DevOps and platform engineering | Advanced: GitOps with Argo CD or Flux; operators and custom resources; secrets management; policy as code with Kyverno or OPA Gatekeeper (AWARE) (*The DevOps Handbook*) | The local cluster kept in sync with git by Argo CD |

---

## 16. Month 12: serving on a device, quantisation and data engineering

**Goal:** serve one user well on a device, quantise for both sides with an accuracy number beside
every speed number, and build a corpus you can reproduce byte for byte. **Gates this month:** P4
edge, P5, P5 edge and P6.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 331 | P4 edge | Device runtimes: OGA and Lemonade, or llama.cpp or Ollama on the iGPU (AMD-AI-STACK §13), or Genie (QUALCOMM-AI-STACK §9); context limits (AMD-AI-STACK §13B) | A small open model answering on the device |
| 332 | P4 edge | Batch-size-one arithmetic: decode tokens/s ≈ achieved bandwidth ÷ bytes read per token, the weights plus the KV cache so far. Predict the decode rate, then measure TTFT and tokens/s at two prompt lengths | Prediction against measurement |
| 333 | P4 edge | Sustained against burst: ten-minute runs on mains power and on battery, thermal throttling, and performance modes such as QNN's `burst` and `sustained_high_performance` | Sustained and burst figures |
| 334 | P4 edge | Phases on different engines: AMD's hybrid mode against NPU-only, and the NPU as a separate lane; Speculative decoding on a device: look-ahead, self-speculative and EAGLE-style decoding (QUALCOMM-AI-STACK §9). Two modes compared phase by phase; then the edge side's exit test | P4 edge **Done when** passed |
| 335 | P5 | Formats: FP32 and TF32, FP16 against BF16, FP8 E4M3 and E5M2, INT8 and INT4, and the MX formats; FP8 is not one format: FNUZ on MI300 and OCP on MI350, not portable between them (AMD-AI-STACK §5, §19) | Check yourself 1, 4 and 5 answered |
| 336 | P5 | Low-precision training (KNOW): loss scaling, FP32 master weights, and per-tensor against fine-grained FP8 scaling as in DeepSeek-V3 ("Mixed Precision Training"; "FP8 Formats for Deep Learning"); accumulation, and how error grows with K | Check yourself 2 answered |
| 337 | Review | Write every format's bit layout from memory; weekly note; rest | Weekly note 45 |
| 338 | P5 | Build 2: an FP8 GEMM emulator in PyTorch; plot the error against K and against the scaling granularity | Both plots |
| 339 | P5 | Post-training quantisation: GPTQ, AWQ, SmoothQuant and LLM.int8(); pruning and distillation (KNOW); bitsandbytes; MIT 6.5940 as needed | Check yourself 3 answered |
| 340 | P5 | Tooling on AMD: AMD Quark, and vLLM's support for quantised models (AMD-AI-STACK §14). Build 1, part 1: one model in FP8, and in INT4 weight-only with AWQ or GPTQ | Two quantised checkpoints |
| 341 | P5 | Build 1, part 2: MXFP4 where the hardware supports it; perplexity, a task score, memory and throughput at your P4 SLO | The three-way table |
| 342 | P5 | Validation at three levels, against tolerances set in advance; then P5's exit test | P5 **Done when** passed; Check yourself 6 answered |
| 343 | P5 edge | What each engine accepts; INT8 QDQ, done carefully: per-channel weights, calibration data that matches the device, and AIMET's order of AutoQuant, cross-layer equalisation, AdaRound and BatchNorm re-estimation, with quantisation-aware training last | A calibration set drawn from the device's real inputs |
| 344 | Review | Explain why the engine, not you, often picks the format on a device; weekly note; rest | Weekly note 46 |
| 345 | P5 edge | LLM weights on a device: 4, 5 and 8 bits, blocks of 32 to 256, activations at 16 bits and biases at 32. Build: a vision model in INT8 QDQ with matched and with mismatched calibration, and a small LLM in two weight formats of different block size | Four quantised models, measured |
| 346 | P5 edge | One tool, both sides: AMD Quark for the Ryzen AI NPU and, through vLLM, for Instinct GPUs. Add every edge result to your cloud table; then the edge side's exit test | P5 edge **Done when** passed |
| 347 | P6 | SQL and data modelling: joins, aggregation, window functions, CTEs, `EXPLAIN` and indexes, fact and dimension tables (DuckDB; programme Week 2 Part F); Columnar formats: Arrow in memory, and Parquet's row groups, column chunks, pages, encodings, statistics and footer; predicate pushdown and column pruning on a real dataset | A query plan that shows the pushdown; Check yourself 1 answered |
| 348 | P6 | Table formats (Iceberg): snapshots, time travel and schema evolution; batch processing with Spark, and Ray Data (AWARE); Stream processing: Kafka's partitioned log, consumer groups, offsets and delivery guarantees, and Flink (AWARE); orchestration with Airflow or Dagster; Quality, lineage and versioning: checks as code, data contracts and lineage | Notes on delivery guarantees and idempotent tasks |
| 349 | P6 | Building a pretraining corpus: FineWeb's pipeline (trafilatura extraction from WARC files, a URL blocklist, a fastText language score, the Gopher filters, MinHash within each snapshot, C4's filters, custom filters and anonymisation), then decontamination, tokenisation, sharding, packing and the mixture. Build 1, part 1: a DataTrove pipeline over a Common Crawl sample | Text extracted and filtered, with drop counts |
| 350 | P6 | A frontier-scale pipeline (KNOW): Llama 3's deduplication at three levels, its quality classifiers and its data mix; FineWeb-Edu, DCLM and Dolma. Build 1, part 2: MinHash deduplication within each snapshot, and the quality filters. Build 4: the pipeline's metadata as Parquet, queried with DuckDB | Every filter's drop count; Check yourself 2–3 answered |
| 351 | Review | Explain from memory how MinHash finds near-duplicates; weekly note; rest | Weekly note 47 |
| 352 | P6 | Build 2: plant verbatim and paraphrased evaluation items, catch them, and measure the false-positive rate on clean data | The contamination report |
| 353 | P6 | The input pipeline: WebDataset, MosaicML Streaming and `StatefulDataLoader`. Build 3, part 1: small files against shards, locally and on object storage | Check yourself 4 answered |
| 354 | P6 | Build 3, part 2: kill a run mid-epoch, resume it, and prove that the sample order is identical | Check yourself 5 answered |
| 355 | P6 | Checkpoints as data: PyTorch Distributed Checkpoint and `async_save` | Check yourself 6 answered |
| 356 | P6 | Retrieval data and Faiss (the optional Build 5); Features for classical ML: Feast, point-in-time-correct joins and training/serving skew; Post-training data: SFT and preference data, synthetic data and the chat template; data governance | Check yourself 7 answered |
| 357 | P6 | P6's exit test: reproducible from a snapshot, every drop counted, contamination caught, no input stall and an identical resume | P6 **Done when** passed |
| 358 | Review | Rebuild the corpus from its configuration and compare hashes; weekly note; rest | Weekly note 48 |
| 359 | Buffer | Finish anything late; request GPU quota for month 13 | Nothing left over from month 12 |
| 360 | Month gate | Re-run P4 edge, P5, P5 edge and P6 cold; write the month report | Month report 12; four gates ticked |

### Track hour, month 12

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Cloud computing | Basic: regions and zones; virtual machines; object storage; networks and security groups; IAM users and roles; billing, all through one provider's command-line tool | A VM created and destroyed from the command line, and its bill read |
| Week 2 | Cloud computing | Intermediate: managed Kubernetes (EKS, AKS or GKE); GPU instances and quotas; block against file against object storage; network design; spot and reserved capacity | A GPU quota request filed for month 13 |
| Week 3 | Cloud computing | Advanced: multi-account landing zones; workload identity; private networking; back-end networks for GPUs; managed ML platforms (Amazon SageMaker, Azure Machine Learning and Google Vertex AI); the provider's well-architected framework | One page on when a managed platform beats your own stack |
| Week 4 | Data engineering | Intermediate and Advanced: Polars, dbt, Great Expectations and DVC; an Airflow or Dagster pipeline; Iceberg and Delta Lake (Reis & Housley, *Fundamentals of Data Engineering*; Akidau et al., *Streaming Systems*) | Your P6 metadata job as an orchestrated, tested pipeline |

---

## 17. Month 13: device telemetry, cloud deployment and operations

**Goal:** a telemetry pipeline for devices, a GPU deployment rebuilt from code with a canary and
autoscaling, a build farm and update service for devices, and a registry guarded by CI gates.
**Gates this month:** P6 edge, P7, P7 edge and P8.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 361 | P6 edge | Data born on the device: Device-matched datasets; Telemetry pipelines that expect late, duplicate and old-schema uploads; Privacy by construction (aggregates, minimum counts, and consent and retention in code); The feedback loop from the field back into training. Then a telemetry design for a simulated fleet (roadmap #2 §3H) | An event schema with an ID, a schema version and the time each event happened |
| 362 | P6 edge | Build: simulated devices upload batches late and twice; a cloud job lands them in Parquet and reports latency by device class; a CI check refuses free-text fields. Then the edge side's exit test | P6 edge **Done when** passed |
| 363 | P7 | Cloud fundamentals: regions, zones and the shared-responsibility model; Read a GPU instance like a datasheet: the Azure ND MI300X v5 (eight MI300X, local NVMe against capped remote disks, Infinity Fabric, 400 Gb/s InfiniBand per GPU, and no live migration); the Twelve-Factor App | Check yourself 5 answered |
| 364 | P7 | Infrastructure as code: providers, modules, state and drift; GitOps with Argo CD or Flux (KNOW). Build 1: an environment in Terraform or OpenTofu (network, GPU nodes, storage and identity); destroy it, recreate it, and set a budget alert | Check yourself 7 answered |
| 365 | P7 | Containers: layers, multi-stage builds, digest pins, `/dev/kfd` and `/dev/dri`, non-root users and read-only root file systems; Model artefacts in deployment: safetensors outside the image, cached near the GPU, a cold-start budget, and many LoRA adapters on one base (KNOW). Build 2: a pinned, non-root ROCm serving image; measure its cold start, then cut it by a factor you stated in advance | The cold start, before and after |
| 366 | P7 | Kubernetes for GPUs: Pods, Deployments, Services and Jobs; requests and limits; labels, taints and tolerations; `amd.com/gpu` in `limits` (the "Schedule GPUs" page), on a local cluster | Check yourself 1 answered |
| 367 | Review | Recreate the environment from code once more, without notes; weekly note; rest | Weekly note 49 |
| 368 | P7 | The AMD GPU Operator and its device plugin. Build 3, part 1: your P4 server on Kubernetes | The server answering on a GPU node |
| 369 | P7 | Build 3, part 2: readiness gating, and KEDA autoscaling on a serving metric | Check yourself 2–3 answered |
| 370 | P7 | Safe rollouts: startup, readiness and liveness probes; blue/green and canary releases; shadow traffic for a new model. Build 3, part 3: a canary that rolls back a planted regression automatically and promotes a clean change | Both outcomes recorded |
| 371 | P7 | Kueue and LeaderWorkerSet; Slurm for training: partitions, `sbatch` and `srun`, GRES and `AutoDetect=rsmi`, requeue, and sharding without fencing; Ray and KubeRay (AWARE). Build 4: your P3 job gang-scheduled, preempted and resumed from its checkpoint | Check yourself 4 answered |
| 372 | P7 | KServe, llm-d and the Gateway API Inference Extension (KNOW and AWARE); Surviving failures: zones, regions, RPO and RTO, and GPU capacity shortages; FinOps: from $/GPU-hour to $/million tokens, on-demand, reserved and spot, idle time, egress and storage. Build 5: a cost report, with the prices and the date you read them | Check yourself 6 answered |
| 373 | P7 | P7's exit test: rebuilt from code, the canary rolls back and promotes, the SLO holds through a step in load, and the cost is derived | P7 **Done when** passed |
| 374 | Review | Tear the cluster down and list every manual step you still needed; weekly note; rest | Weekly note 50 |
| 375 | P7 edge | A build farm with one job per target; Artefacts and manifests: version, target, hash, signature and the oldest application version that can load it (QUALCOMM-AI-STACK §4, §9) | A manifest format with version, target, hash, signature and minimum application version |
| 376 | P7 edge | Build: CI builds your model for two targets and publishes each artefact with its manifest | Two artefacts, rebuilt from code |
| 377 | P7 edge | Build: an update service with a staged-rollout percentage, a pause and a rollback | A rollout paused and rolled back from code |
| 378 | P7 edge | Testing on real devices: Qualcomm AI Hub's hosted devices, and commercial device farms (AWARE); Who pays: the user for the device, and the operator for builds, downloads and cascaded requests; edge servers and gateways (AWARE); then the edge side's exit test | P7 edge **Done when** passed |
| 379 | P8 | Why ML systems rot: entanglement, undeclared consumers, data dependencies and feedback loops (Sculley et al.), and the ML Test Score (Breck et al.); lineage and the model registry, with MLflow or Weights & Biases | Check yourself 1 answered |
| 380 | P8 | Build 1, part 1: a registry entry with the full lineage: code, data snapshot, image digest, configuration, tokenizer, chat template and serving flags | A model that traces to its inputs in one step |
| 381 | Review | Trace one deployed model back to its data, from memory; weekly note; rest | Weekly note 51 |
| 382 | P8 | CI/CD for models: quality, performance and cost gates; continuous training, and when retraining on a schedule is the wrong answer (KNOW). Build 1, part 2: CI gates for quality, performance (your F6 harness) and cost | Three planted regressions blocked, and an unchanged build passing |
| 383 | P8 | Evaluating LLMs: lm-evaluation-harness against your own endpoint; HELM; confidence intervals and contamination. LLM application patterns and their serving cost: RAG, tool calls, agents, structured output and guardrail models | Check yourself 2 answered |
| 384 | P8 | Online experiments: A/B tests, guardrail metrics, and why an offline win can be an online loss (Kohavi et al.). Build 2: an evaluation report, with an LLM judge calibrated against a set that you labelled yourself | Check yourself 3 and 6 answered |
| 385 | P8 | Observability: Prometheus, Grafana and OpenTelemetry; `amd-smi` and the Device Metrics Exporter | Dashboards for your P7 deployment |
| 386 | P8 | Reliability engineering: SLIs, SLOs and error budgets, multi-window burn-rate alerts, incident command, blameless postmortems, capacity planning and hedged requests. Build 3: burn-rate alerts; inject three faults: kill a replica, saturate the queue and fill the KV cache | Every fault alerts; Check yourself 4–5 answered |
| 387 | P8 | A postmortem for one fault; Training reliability at scale: `rccl-tests` burn-in, straggler detection, automatic restart from the latest checkpoint, and the NCCL flight recorder of Llama 3; then P8's exit test | P8 **Done when** passed |
| 388 | Review | Re-read your postmortem as a hostile reviewer; weekly note; rest | Weekly note 52 |
| 389 | Buffer | Finish anything late; stop idle cloud resources | Nothing left over from month 13 |
| 390 | Month gate | Re-run P6 edge, P7, P7 edge and P8 cold; write the month report | Month report 13; four gates ticked |

### Track hour, month 13

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | MLOps and LLMOps | Intermediate and Advanced: ML pipelines with Kubeflow Pipelines, Metaflow or ZenML; data and model drift with Evidently; feature stores with Feast; batch against online inference; versioning prompts and models (Huyen, *Designing Machine Learning Systems*; *Made With ML*) | A drift report on your P6 data |
| Week 2 | Observability and SRE | Intermediate and Advanced: structured logging; logs in Loki and traces in Jaeger through OpenTelemetry; capacity planning (Google's *Site Reliability Engineering*) | One request traced from the client to the GPU |
| Week 3 | LLM applications and agents | Basic and Intermediate: calling a model API; prompt design; structured output as JSON; retrieval-augmented generation, with chunking, embeddings, vector search and re-ranking (Lewis et al.); a vector store from P6 (Faiss, pgvector, Milvus or Qdrant) | A RAG service on your P4 endpoint |
| Week 4 | LLM applications and agents | Intermediate: tool and function calling; conversation state; a latency budget for the whole request, measured end to end | The RAG service meeting its latency budget |

---

## 18. Month 14: security, and the edge application with its cloud side

**Goal:** operate the device fleet, secure both sides, then ship the edge application and size the
cloud behind it. **Gates this month:** P8 edge, P9, P9 edge, P10 and P10 cloud.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 391 | P8 edge | Fleet signals: crash-free sessions, latency by device class, fallback and cascade rates, and thermal and battery events. One registry for both sides, with the device lineage, and one evaluation harness run on the device | The device model scored on the cloud model's golden set |
| 392 | P8 edge | Regressions on one chip: release gates per device class; Incidents you cannot redeploy: a kill switch and a rollback. Build: a release gate for device builds that blocks a planted accuracy regression and a planted on-device latency regression, and a kill switch flipped on a simulated device. Then the edge side's exit test | P8 edge **Done when** passed |
| 393 | P9 | Threat modelling for ML systems: assets, trust boundaries, attackers and their goals, mapped to MITRE ATLAS and the OWASP Top 10 for LLM applications. Build 1: a threat model for your P7 deployment | At least three ATLAS techniques covered; Check yourself 5 answered |
| 394 | P9 | The software supply chain: hashes and lock files, SBOMs, cosign with Rekor, SLSA provenance, typosquatting and poisoned repositories; Secrets and identity: none in code, images, logs or prompts, a secret manager, workload identity, scanning and rotation. Build 2: an admission policy that refuses unsigned images | An unsigned image refused; Check yourself 2 and 6 answered |
| 395 | P9 | Model artefacts: pickle against safetensors; Isolation and multi-tenancy: what containers isolate, and why GPU sharing is not isolation; Memorisation and extraction: Carlini et al., with poisoning, backdoors and membership inference (AWARE). Build 3: a harmless pickle payload that `weights_only=True` refuses | Check yourself 1 answered |
| 396 | P9 | LLM application security; Privacy: PII detection and redaction, retention limits, and DP-SGD (AWARE); Governance: model cards and datasheets, the NIST AI RMF and the EU AI Act (AWARE). Build 4: indirect injections planted in your RAG application's documents, measured, mitigated and measured again. Then P9's exit test | P9 **Done when** passed; Check yourself 3–4 answered |
| 397 | Review | Re-read your threat model as the attacker would; weekly note; rest | Weekly note 53 |
| 398 | P9 edge | An attacker who owns the device; roots of trust on the device; extraction and tampering | The device added to your threat model |
| 399 | P9 edge | Verified models and a guarded key: every model file signed and verified before it loads, with the signing key in a key-management service or a hardware token, never in CI. Build: the verifying library that P10's application will call, checking hash and signature against the trusted keys | Tampered and unsigned files refused |
| 400 | P9 edge | Build: rotate the signing key, and revoke the old one | The new key accepted, and the old one refused after revocation |
| 401 | P9 edge | Local prompt injection: an assistant that reads files, mail or web pages, and least privilege for its tools (Greshake et al.); Privacy on the device: no prompts in local logs, and consent for what the model may read. An injection test against the device application; then the edge side's exit test | P9 edge **Done when** passed |
| 402 | P10 | Fitting the model: choosing or distilling a small model, and the memory arithmetic of weights, activations and the KV cache on a device; Formats and runtimes: ONNX Runtime and its execution providers, the Vitis AI execution provider and Qualcomm's backends, with ExecuTorch, LiteRT, Core ML and OpenVINO (AWARE); NPU quantisation: INT8 QDQ graphs, per-channel weights and calibration; partitioning (AMD-AI-STACK §13, §13B; QUALCOMM-AI-STACK §5, §6B) | A memory budget for your device model |
| 403 | P10 | NPU architectures: XDNA and Hexagon; Constraints: thermal throttling, shared memory bandwidth, and the compilation and caching behind the first inference; On-device LLMs: OGA and Lemonade, Genie and llama.cpp. Build 1, part 1: a vision model and a small LLM on the NPU and the iGPU, with every CPU fallback listed and explained | The fallback report; Check yourself 1–2 answered |
| 404 | Review | Explain every fallback from memory; weekly note; rest | Weekly note 54 |
| 405 | P10 | Build 1, part 2: remove at least one fallback by rewriting, re-quantising or re-exporting, and measure latency and power before and after | Check yourself 3, 4 and 7 answered |
| 406 | P10 | Application integration: load the compiled model once and reuse it, pre- and post-processing, inference off the user-interface thread, and a fallback path; Android and iOS through ExecuTorch and Core ML (AWARE). Build 2: the application, falling back to the CPU when it must | A working application |
| 407 | P10 | Shipping and updating models: versioned files, hash and signature checks before loading, staged rollouts, rollback and version compatibility. Build 3: updates through the P9 verifying library, with a tampered file refused and a rollback | Check yourself 5 answered |
| 408 | P10 | Cloud cascades: send the request to the cloud on low confidence or a large input; Field monitoring: crash reports and private aggregates, with federated learning and TinyML (AWARE). Build 4: a cascade to your P7 deployment, with quality, p50 and p99 latency, and cost for device-only, cloud-only and cascaded serving | Check yourself 6 answered |
| 409 | P10 | P10's exit test: every fallback explained and one removed, the tampered update refused and the rollback working, and the cascade measured | P10 **Done when** passed |
| 410 | P10 cloud | Connect the application to every service behind it: Training for the device (your P3 edge-side student); Device telemetry (P6 edge side); The build farm and the update service (P7 edge side); One registry, one harness and a kill switch (P8 edge side); The signing key, its rotation and the verifying library (P9 edge side) | The application running against every service |
| 411 | Review | Draw the whole system, device and cloud, from memory; weekly note; rest | Weekly note 55 |
| 412 | P10 cloud | Capacity for the cascade: devices × requests per device × the measured cascade rate, with replicas and autoscaling set from your P4 measurements | A capacity plan with every input sourced |
| 413 | P10 cloud | Load-test the cloud end of the cascade at the planned rate | The SLO, measured at the planned rate |
| 414 | P10 cloud | Double the cascade rate, as a lower threshold in a new release would; then test a kill-switch surge | Where the SLO holds, and where it breaks |
| 415 | P10 cloud | The cloud side's exit test | P10 cloud **Done when** passed |
| 416 | P11 | Choose the capstone model and write its plan, with the parity tolerance chosen before you see any result | The capstone plan |
| 417 | P11 | Porting with HIPIFY, and what it cannot fix (AMD-AI-STACK §8); golden outputs from the PyTorch reference | Golden outputs saved; Check yourself 3 answered |
| 418 | Review | Read the postings in roadmap #2 §1 line by line against your repository; weekly note; rest | Weekly note 56 |
| 419 | Buffer | Finish anything late; book the capstone's GPUs | Nothing left over from month 14 |
| 420 | Month gate | Re-run P8 edge, P9, P9 edge, P10 and P10 cloud cold; write the month report | Month report 14; five gates ticked |

### Track hour, month 14

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Security for AI systems | Intermediate and Advanced: OAuth 2.0 and OpenID Connect; container security; dependency and secret scanning with Trivy, Syft, Grype and gitleaks; model scanning with ModelScan (Anderson, *Security Engineering*; Adkins et al., *Building Secure and Reliable Systems*) | Your serving image scanned, and every finding triaged |
| Week 2 | LLM applications and agents | Advanced: agents that plan and call tools; evaluating RAG and agents; guardrails; caching; cost and latency budgets; the Model Context Protocol; LangChain, LlamaIndex or DSPy; tracing with Langfuse or Arize Phoenix (Huyen, *AI Engineering*) | An agent over your RAG service, traced call by call |
| Week 3 | Responsible AI and governance | Basic and Intermediate: bias in data; fairness and fairness metrics, with Fairlearn; privacy and PII; explainability with SHAP and LIME; model cards and datasheets (Mitchell et al.; Gebru et al.) | A fairness report and a SHAP explanation for one of your models |
| Week 4 | Responsible AI and governance | Advanced: differential privacy; red-teaming for harms and safety evaluation, with garak and PyRIT; the EU AI Act and the NIST AI RMF (the resources of programme Week 9 Part C) | A harm red-team of your RAG service, with its findings |

---

## 19. Month 15: the capstone, in the cloud and on a device

**Goal:** bring up a model that you have not used before, end to end and on both sides, and prove
every claim to a stranger. **Gates this month:** P11, and every line of roadmap #2 §23.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 421 | P11 | Parity testing: golden outputs and per-layer diffs against the PyTorch reference, tolerances per dtype chosen before you look, ULP metrics and determinism controls | Per-layer parity; Check yourself 1 answered |
| 422 | P11 | Parity on end tasks; bisect any divergence to the first layer and operator that differ | Deliverable 1, the parity report; Check yourself 2 answered |
| 423 | P11 | An optimised AMD serving configuration, with the dominant kernels placed on the roofline | Deliverable 2 |
| 424 | P11 | The cross-layer root cause of the top bottleneck: Python, framework, compiler, kernel, ISA and counters, bisecting driver and ROCm versions if needed | A written root cause |
| 425 | P11 | Deliverable 3, part 1: a kernel or compiler fix of your own for that bottleneck | The fix, measured |
| 426 | P11 | Deliverable 3, part 2: its tests and benchmarks | A change ready for review |
| 427 | Review | Re-read the parity report as a hostile reviewer; weekly note; rest | Weekly note 57 |
| 428 | P11 | Upstreaming: read the project's contribution guide, keep the change small, and open the pull request with its test and benchmark | Deliverable 3, submitted upstream |
| 429 | P11 | A throughput and cost-per-token report, backed by an SLO | Deliverable 4 |
| 430 | P11 | A reproducible data pipeline for any calibration or fine-tuning data (P6) | Deliverable 5 |
| 431 | P11 | The deployment, built from code on cloud GPUs, with autoscaling and a canary (P7) | Deliverable 6 |
| 432 | P11 | CI gates for quality, performance and cost, with the dashboards and alerts that watch the service (P8) | Deliverable 7 |
| 433 | P11 | A threat model, and a signed and scanned serving image (P9) | Deliverable 8 |
| 434 | Review | Check deliverables 1–8 against P11's list in roadmap #2; weekly note; rest | Weekly note 58 |
| 435 | P11 | The edge build, part 1: a smaller or quantised model of the same family on the NPU or iGPU, with its fallback report (P10) | The device build running |
| 436 | P11 | The edge build, part 2: signed updates, and a cascade to your cloud deployment | Deliverable 9 |
| 437 | P11 | Benchmark rules: MLPerf Training and Inference, and why the rules exist; Readiness reporting: a report with parity, performance in the F6 format, known issues and residual risk | Check yourself 5 answered |
| 438 | P11 | A one-command reproduction script that pins everything it needs | Deliverable 10; Check yourself 4 answered |
| 439 | P11 | Answer the upstream review comments, and iterate | Every comment answered |
| 440 | P11 | The stranger test, part 1: a peer reproduces your headline numbers from the repository alone | Their numbers, beside yours |
| 441 | Review | Fix what the stranger found; weekly note; rest | Weekly note 59 |
| 442 | P11 | The stranger test, part 2: a peer tears the deployment down and recreates it from code, and the device build refuses a tampered update | Both done by someone else |
| 443 | P11 | P11's exit test, including a cloud and an edge artefact for every domain in roadmap #2 §3H | P11 **Done when** passed |
| 444 | Portfolio | The repository's README: the headline numbers, how to reproduce each one, and every stage report | A portfolio that a stranger can navigate |
| 445 | Career | Place yourself on the ladder in roadmap #2 §3G, and plan the skills that no exit test checks. Write a talk about your capstone | A self-assessment and a talk |
| 446 | Career | Interview practice: coding with the F2 data structures, ML system design, and deep dives into your own projects | Three mock interviews, with notes |
| 447 | Next | Roadmap #1: pass its prerequisites cold (roadmap #1 §3), and read its §3B–§3E before month 16 | Every prerequisite passed, and the lab for month 16 listed |
| 448 | Review | Re-read your month 1 report beside today's repository; weekly note; rest | Weekly note 60 |
| 449 | Buffer | Finish anything late; stop every rented resource | Nothing left over |
| 450 | Month gate | Re-run P11 cold; tick every line of roadmap #2 §23, cloud and edge; write the roadmap #2 report | Month report 15; the whole of roadmap #2, done on both sides |

### Track hour, month 15

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Responsible AI and governance | Projects: a model card and a datasheet for the model you bring up in P11 | Both documents, published with the capstone |
| Week 2 | Software engineering | Expert: leading a design review; contributing upstream to a large project, through your P11 pull request; owning a subsystem's reliability | Your upstream review answered, and what it taught you written down |
| Week 3 | Skills no exit test checks | Estimation, writing, presenting and collaboration (roadmap #2 §3G): estimate a task before you start it and compare; explain your capstone to an engineer, a manager and an executive | An estimate checked against the truth, and three versions of one explanation |
| Week 4 | Skills no exit test checks | Product and business sense, ethics, teaching and career craft (roadmap #2 §3G): what your capstone is worth and costs, who it could harm, a talk given, and your portfolio made public | A talk given, and a public portfolio |

---

## 20. Month 16: logic, RTL and silicon, then the quantitative method

**Goal:** set up the architect's lab, build a systolic array from gates to a placed layout, price
its energy for a device, and start computer architecture. **Gates this month:** A1 and A1 edge.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 451 | Lab | The architect's lab (roadmap #1 §3B): the OSS CAD Suite on your `PATH`, `perf stat` reading real counters, and an `assumptions.md` register in your repository (roadmap #1 §3C) | Tool versions recorded; one counter reading; the register started |
| 452 | A1 | Combinational logic: Boolean algebra; muxes, decoders and comparators, each written in SystemVerilog and linted with Verilator as you go (Harris & Harris) | Five combinational modules, lint-clean |
| 453 | A1 | Combinational logic, continued: ripple-carry adders, then carry-lookahead and prefix adders (KNOW), with Weste & Harris and Mutlu's Digital Design lectures | An 8-bit adder with a testbench; Check yourself 1 answered |
| 454 | A1 | Combinational logic, continued: the array multiplier; Booth encoding and Wallace and Dadda trees (KNOW) | A 4 × 4 array multiplier, simulated |
| 455 | A1 | Sequential logic: latches against flip-flops, registers, Moore and Mealy FSMs, counters and FIFOs | A counter, an FSM and a synchronous FIFO, simulated |
| 456 | A1 | SystemVerilog for design: `always_ff` against `always_comb`, non-blocking against blocking assignment, avoiding inferred latches, parameterised modules and the synthesizable subset | A latch planted and then removed; Check yourself 3 answered |
| 457 | Review | Draw a full adder and a Moore FSM from memory; weekly note; rest | Weekly note 61 |
| 458 | A1 | Timing: clock period, setup and hold, and the critical path; pipelining to raise frequency, and what it costs in latency, area and power; retiming (AWARE) | Check yourself 2 answered |
| 459 | A1 | Verification: self-checking testbenches against a reference model in Python; SystemVerilog assertions, functional coverage, constrained-random stimulus and cocotb (KNOW), with Spear & Tumbush | A cocotb testbench that checks the adder by itself |
| 460 | A1 | Build, part 1: the MAC processing element (INT8 operands, an INT32 accumulator), then a parameterised N × N output-stationary array of them | The array computing a small GEMM in simulation |
| 461 | A1 | Build, part 2: a self-checking testbench against a NumPy GEMM, with non-square and tail shapes | Every shape passing |
| 462 | A1 | Clock-domain crossing (KNOW): metastability, two-flop synchronisers, and asynchronous FIFOs with Gray-coded pointers. Build, part 3: the array clean under `verilator --lint-only` | A lint-clean array; Check yourself 4 answered |
| 463 | A1 | Implementation (KNOW): synthesis and technology mapping, place-and-route, static timing analysis, PPA, SRAM macros against flip-flop arrays, dynamic against leakage power, and clock gating. Open tools: Yosys `synth`, mapped to the example CMOS cell library in its sources | Cell counts at 4 × 4 and 8 × 8; Check yourself 6 answered |
| 464 | Review | Explain setup and hold, and the latch you removed, from memory; weekly note; rest | Weekly note 62 |
| 465 | A1 | Build, part 4: peak MACs per cycle, edge operands per cycle, and fill and drain latency at each size | The scaling table: N², about 2N and the cell count; Check yourself 5 answered |
| 466 | A1 | FPGAs (KNOW): LUTs, DSP slices and block RAM for prototyping. Read the systolic-array RTL example in SCALE-Sim line by line, beside your own | A written comparison of the two designs |
| 467 | A1 | Static timing with OpenSTA on the synthesised array: constraints, slack and the critical path (Bhasker & Chadha) | The critical path of the 4 × 4 array, named |
| 468 | A1 | The array through OpenROAD or OpenLane with an open PDK, SkyWater SKY130 or ASAP7: floorplan, placement, clock tree and routing (Kahng et al.) | A placed and routed 4 × 4 array |
| 469 | A1 | Area, timing and power after place-and-route, set against the cell-count proxy of day 463 | How far the proxy was from the layout, measured |
| 470 | A1 | A1's exit test: the scaling of MACs per cycle, edge bandwidth and cell count from your own numbers, and the idle fraction of a larger array at a small M, fill and drain included | A1 **Done when** passed |
| 471 | Review | Rebuild the array from a clean checkout and re-run every test; weekly note; rest | Weekly note 63 |
| 472 | A1 edge | Logic for a power budget: Clock gating and power gating; Voltage and frequency, with dynamic power ∝ C·V²·f; Switching activity, which follows the data; always-on islands and several voltage domains (AWARE) | What each technique saves and what it costs, written down |
| 473 | A1 edge | Build: dump waveforms for an M = 1 GEMM and for a prefill-shaped one, and count toggles per useful MAC | Relative activity per useful MAC for both shapes |
| 474 | A1 edge | Estimate what clock-gating the idle PEs saves at M = 1, and name what a toggle count leaves out. Then the edge side's exit test | A1 edge **Done when** passed |
| 475 | A2 | Quantitative principles: execution time = instructions × CPI × cycle time, and Amdahl's law for hardware; dynamic power ∝ C·V²·f, the end of Dennard scaling and dark silicon (KNOW) (Hennessy & Patterson chapter 1) | Check yourself 1–2 answered |
| 476 | A2 | ISA design (KNOW): RISC against CISC, instruction encoding and predication; RISC-V V (AWARE). Pipelining: structural, data and control hazards, forwarding and stalls, and branch prediction (bimodal, gshare and TAGE, AWARE) | A five-stage pipeline with every hazard marked |
| 477 | A2 | Out-of-order execution (KNOW): register renaming, the reorder buffer, issue queues, load/store queues, memory disambiguation and the limits of ILP (Hennessy & Patterson chapter 3) | Renaming worked by hand for a short loop |
| 478 | Review | Redo Check yourself 1–2 cold; weekly note; rest | Weekly note 64 |
| 479 | Buffer | Finish anything late | Nothing left over from month 16 |
| 480 | Month gate | Re-run A1 and A1 edge cold; write the month report | Month report 16; A1 and A1 edge ticked in roadmap #1 §15 |

### Track hour, month 16

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Digital logic and circuits | Advanced: adder and multiplier architectures (carry-lookahead, Booth encoding and Wallace trees), SRAM cells, clock distribution, metastability and clock-domain crossing (Weste & Harris; Rabaey, Chandrakasan & Nikolić) | A 4-bit Wallace tree drawn and checked by hand |
| Week 2 | Verification | Intermediate: constrained-random stimulus, scoreboards and reference models, functional and code coverage, and cocotb tests in Python (the cocotb documentation) | Coverage numbers for your array's testbench |
| Week 3 | Verification | Advanced: UVM (KNOW), SystemVerilog assertions, formal property checking with SymbiYosys, and equivalence checking (Seligman, Schubert & Kumar); VCS, Xcelium and Questa (AWARE) | One property of your FIFO proved with SymbiYosys |
| Week 4 | RTL design | Advanced: pipelined datapaths with valid/ready handshakes, FIFOs, synchronisers, arbiters and memory macros; Verible for linting (Sutherland, Davidmann & Flake; Cummings's papers) | A valid/ready pipeline stage, verified |

---

## 21. Month 17: caches, memory and the cost of silicon, then the GPU from the inside

**Goal:** a cache simulator that agrees with the hardware, the economics of chiplets, a device's
shared memory, and the start of a model of your own GPU. **Gates this month:** A2 and A2 edge.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 481 | A2 | Caches: sets, ways and lines; LRU and pseudo-LRU; write-back against write-through; the three Cs; inclusion, MSHRs, non-blocking caches and prefetchers (KNOW) | Check yourself 3–4 answered |
| 482 | A2 | Build 1, part 1: a trace-driven cache simulator, with its size, associativity, line size and replacement policy configurable, and two or more levels | The simulator, with unit tests |
| 483 | A2 | Build 1, part 2: drive it with the address streams of a CPU matmul at several tile sizes, predicting each change of miss rate first | Predictions beside simulated miss rates |
| 484 | A2 | Build 1, part 3: validate the miss counts against `perf stat` on the same loop, allowing for the prefetchers; one configuration cross-checked with gem5 (optional) | Agreement within an error you stated |
| 485 | A2 | Virtual-memory hardware (KNOW): TLBs, page walks and large pages, on CPUs and on GPUs. Coherence and consistency (KNOW): MSI, MESI and MOESI, snooping against directories, false sharing, SC, TSO and relaxed models, fences, and scoped GPU memory models (AWARE) (Nagarajan et al.) | Check yourself 5 answered |
| 486 | A2 | DRAM and HBM (KNOW): channels, ranks, banks and rows; row-buffer hits and misses; refresh; timing parameters and controller scheduling (AWARE); HBM stacks and pseudo-channels (Jacob, Ng & Wang) | Check yourself 6 answered |
| 487 | Review | Draw the MESI states and a DRAM access from memory; weekly note; rest | Weekly note 65 |
| 488 | A2 | On-chip networks (KNOW): crossbars, rings and meshes, bisection bandwidth, routing and flow control. Multicore, chiplets and packaging (KNOW): shared last-level caches, NUMA and die-to-die links; 2.5-D interposers and 3-D stacking (AWARE) | A ring and a mesh compared by bisection bandwidth |
| 489 | A2 | Silicon economics (KNOW): cost per good die, the Poisson yield model and Hennessy & Patterson's refinement, the reticle limit, and chiplets on different processes (AMD-AI-STACK §5). Energy (KNOW): per operation against per byte moved | Check yourself 7 answered |
| 490 | A2 | Build 2: the die-cost model: one large die against four quarter-size chiplets, with stated wafer, packaging and link costs; sweep the defect density | The crossover defect density |
| 491 | A2 | A DRAM bandwidth microbenchmark against the datasheet; DRAMSim3 or Ramulator 2 (KNOW); CACTI for a cache's area and energy (AWARE) | Measured against datasheet bandwidth, with the gap explained |
| 492 | A2 | Optional build: a pipelined RISC-V core in RTL, part 1: the RV32I datapath, with Spike as the reference (Patterson & Hennessy, RISC-V edition) | Single instructions matching Spike |
| 493 | A2 | The RISC-V core, part 2: hazards and forwarding, then a test program run against Spike | A small program running on your core |
| 494 | Review | Explain the die-cost crossover and how packaging moves it, from memory; weekly note; rest | Weekly note 66 |
| 495 | A2 | "A New Golden Age for Computer Architecture"; Hennessy & Patterson chapters 5 and 7; Mutlu's lectures as needed; Check yourself 1–7 cold | Every answer checked |
| 496 | A2 | A2's exit test: miss-rate trends predicted before each run, the simulator within its stated error, and the die-cost crossover explained | A2 **Done when** passed |
| 497 | A2 edge | The memory system of a device: Unified memory, with no copies but one shared ceiling; Interference, 3.3% against 69% on Strix Halo; Effective against theoretical bandwidth, about 158–170 against 256 GB/s; performance and efficiency cores (AWARE) (AMD-AI-STACK §13B) | Predictions written before any run |
| 498 | A2 edge | Build: a bandwidth-bound loop alone, then while the iGPU or a second group of cores streams memory, each run predicted from the measured shared bandwidth | Measured slowdowns beside the predictions |
| 499 | A2 edge | What an SoC architect could change to reduce the slowdown; then the edge side's exit test | A2 edge **Done when** passed |
| 500 | A3 | The compute unit: SIMD units and wavefront schedulers, instruction issue and arbitration, SGPRs and VGPRs, and register-file banking (KNOW) (AMD-GPU-PATH §4–§7; Aamodt, Fung & Rogers) | A diagram of one compute unit of your GPU |
| 501 | Review | Re-read your A2 stage report as a hostile reviewer; weekly note; rest | Weekly note 67 |
| 502 | A3 | Latency hiding: waves and ILP against a memory latency (Little's law), and Volkov's result on occupancy against ILP; the method of Jia et al.'s microbenchmarking paper | Check yourself 1 answered |
| 503 | A3 | The memory system: LDS banking, the L1 path and coalescing, L2 slices and the fabric, the Infinity Cache, memory controllers, HBM stacks and channel interleaving (AMD-AI-STACK §5) | Your GPU's hierarchy, with the numbers still to measure |
| 504 | A3 | Build 1, part 1: pointer-chase latency per memory level, with a randomised chase | Latency per level; Check yourself 2 answered |
| 505 | A3 | Build 1, part 2: bandwidth per level, and the LDS bank-conflict penalty against stride | Two measured curves |
| 506 | A3 | Matrix engines: MFMA shapes, data types and cycle counts from the Matrix Instruction Calculator (AMD-GPU-PATH §7), the `v_smfmac_*` family, and FLOPs per cycle. Build 1, part 3: MFMA throughput per instruction and type | Measured against computed throughput; Check yourself 3 answered |
| 507 | A3 | Chiplets: XCDs over IODs, an L2 per XCD, non-uniform access and the partitioning modes (AMD-GPU-PATH §6). The front end: the command processor, AQL packets, hardware queues and dispatch (AMD-GPU-PATH §4). Build 1, part 4: kernel-launch overhead | Launch overhead measured; Check yourself 4 answered |
| 508 | Review | Explain every microbenchmark's method from memory; weekly note; rest | Weekly note 68 |
| 509 | Buffer | Finish anything late | Nothing left over from month 17 |
| 510 | Month gate | Re-run A2 and A2 edge cold; write the month report | Month report 17; A2 and A2 edge ticked |

### Track hour, month 17

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Synthesis, timing and physical design | Advanced: floorplanning, placement, clock-tree synthesis and routing; power analysis; design rule checks; process design kits, all on your A1 array in OpenROAD (the OpenROAD documentation) | The array's clock tree and routing reports, read and explained |
| Week 2 | Processor architecture | Intermediate and Advanced: RISC-V as the teaching ISA; branch prediction; out-of-order execution; superscalar issue; SIMD and vector ISAs; multithreading; prefetching; Spike and ChampSim (Shen & Lipasti; Mutlu's lectures) | Two branch predictors compared on a ChampSim trace |
| Week 3 | Memory systems and coherence | Advanced: MESI and directories, memory consistency models, HBM stacks and their interfaces, memory controllers and request scheduling, and NUMA | A litmus test that shows an outcome TSO allows |
| Week 4 | GPU architecture | Advanced: chiplets (XCDs and IODs), the cache hierarchy and Infinity Cache, register-file and LDS trade-offs, and partitioning modes (AMD's CDNA white papers and ISA reference guides) | Your GPU's hierarchy annotated with the white paper's numbers |

---

## 22. Month 18: a model of your GPU, then accelerators and dataflow

**Goal:** predict your own GPU kernels from first principles, recalibrate for a client GPU, then
choose dataflows for LLM operators in the datacenter and on an NPU. **Gates this month:** A3, A3
edge, A4 and A4 edge.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 511 | A3 | Power management: clocks, power caps, and sustained against boost clocks; the sustained clock recorded beside every benchmark | Check yourself 5 answered |
| 512 | A3 | Build 2, part 1: an analytical model in Python, built from your measured parameters | The model, with every parameter traced to a measurement |
| 513 | A3 | Build 2, part 2: predict every rung of your P1 GEMM ladder and your P1 softmax, with the error stated in advance | Predictions beside measurements |
| 514 | A3 | Simulation (KNOW): Accel-Sim, trace-driven and validated against NVIDIA hardware on GPGPU-Sim, and its AccelWattch power model (AWARE); where an analytical model is the practical tool on AMD | Notes on what a simulator adds to your model |
| 515 | A3 | Competitive literacy: Hopper and Blackwell (the Tensor Memory Accelerator, asynchronous warp-group MMA, and thread-block clusters with distributed shared memory) beside CDNA and the TPU; NVIDIA's whitepapers | Check yourself 6 answered |
| 516 | A3 | Name the mechanism behind every miss (GPU MODE lecture 37); then A3's exit test | A3 **Done when** passed |
| 517 | Review | Explain your model's worst miss from memory; weekly note; rest | Weekly note 69 |
| 518 | A3 edge | The client GPU, seen by an architect: CDNA against RDNA; What RDNA 4 changed (twice the FP16 and BF16 and four times the INT8 matrix throughput per CU, FP8 and BF8, 4:2 sparsity, a new register layout); Bandwidth is the gap, 640 GB/s against 8.0 TB/s; Adreno (AWARE) (AMD-AI-STACK §5B) | The parameters you expect to change, written down |
| 519 | A3 edge | Build: the bandwidth, matrix-throughput and launch-overhead benchmarks on an RDNA GPU that ROCm supports, discrete or integrated | The client GPU's measured parameters |
| 520 | A3 edge | Recalibrate the model and predict one of your portable, pre-MFMA GEMM rungs on the client GPU | Prediction against measurement |
| 521 | A3 edge | Explain each parameter that differs from CDNA by the design goal behind it; then the edge side's exit test | A3 edge **Done when** passed |
| 522 | A4 | Loop nests: GEMM, convolution and attention written as loop nests; tiling, loop order, and temporal against spatial reuse (Sze et al.; MIT 6.5930) | Check yourself 1 answered |
| 523 | A4 | Dataflows: weight-, output- and input-stationary; row-stationary, as in Eyeriss (KNOW); systolic arrays against spatial arrays on a network-on-chip | Check yourself 2–3 answered |
| 524 | Review | Write a GEMM loop nest and mark each operand's reuse, from memory; weekly note; rest | Weekly note 70 |
| 525 | A4 | Buffer hierarchies (KNOW): register files, local and global buffers and DRAM, with the energy of an access at each level (Horowitz, ISSCC 2014) | Check yourself 4 answered |
| 526 | A4 | Mapping and mapspace search (KNOW): Timeloop's mapper, MAESTRO's data-centric model, SCALE-Sim and Accelergy. Install Timeloop with Docker and work its tutorial exercises | The first tutorial exercises passing |
| 527 | A4 | Sparsity (KNOW): structured (N:M) against unstructured, compressed formats, when sparsity pays in hardware, and RDNA 4's 4:2 | Check yourself 5 answered |
| 528 | A4 | Case studies (KNOW): TPU v1 and v4, Eyeriss, XDNA (AMD-AI-STACK §6) and Hexagon (QUALCOMM-AI-STACK §6); wafer-scale and dataflow start-ups (AWARE); Processing-in-memory and near-memory compute (AWARE) | A one-page comparison of four designs |
| 529 | A4 | Build, part 1: the QKV projection at prefill and decode shapes, on two dataflows | Utilisation, DRAM traffic and energy for one operator |
| 530 | A4 | Build, part 2: attention, QKᵀ and PV | The second operator |
| 531 | Review | Explain why decode reuses each weight once, from memory; weekly note; rest | Weekly note 71 |
| 532 | A4 | Build, part 3: the MLP up and down projections, and a check that a compiler could produce the best mapping the mapper found | All three operators; Check yourself 6 answered |
| 533 | A4 | A4's exit test: the dataflow and buffer sizes for prefill and for decode, justified by your numbers, and what each choice costs the other phase | A4 **Done when** passed |
| 534 | A4 edge | Two edge dataflow designs: XDNA 2 (32 compute tiles in 8 columns by 4 rows, 64 KB of L1 each, a 512 KB memory tile per column and shim tiles, all managed by software); Hexagon (HVX and HMX fed by DMA from about 8 MB of VTCM); Coverage is architecture | The array's parameters, ready to model |
| 535 | A4 edge | Build: an XDNA-like array in Timeloop or SCALE-Sim for the prefill and decode GEMMs of a small on-device LLM | Utilisation and DRAM traffic beside your datacenter results |
| 536 | A4 edge | Which buffer level limits on-device decode, and what doubling the memory tile would change; then the edge side's exit test | A4 edge **Done when** passed |
| 537 | A5 | Arithmetic hardware (KNOW): an array multiplier's area grows with the square of the significand width; a floating-point multiply is a significand multiply, an exponent add, normalisation and rounding; a floating-point add needs alignment (Muller et al.) | Check yourself 1–2 answered |
| 538 | Review | Compare your datacenter and edge dataflow results aloud; weekly note; rest | Weekly note 72 |
| 539 | Buffer | Finish anything late | Nothing left over from month 18 |
| 540 | Month gate | Re-run A3, A3 edge, A4 and A4 edge cold; write the month report | Month report 18; four gates ticked |

### Track hour, month 18

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | FPGAs and emulation | Basic and Intermediate: LUTs, flip-flops and block RAM; the FPGA flow of synthesis, place and route and bitstream; DSP blocks; timing constraints; on-chip logic analysers (Yosys with nextpnr, or AMD Vivado) | Your A1 array through an FPGA flow, with its timing report |
| Week 2 | FPGAs and emulation | Advanced: high-bandwidth memory on FPGAs, partial reconfiguration, and high-level synthesis with Vitis HLS; the array on a board and measured, if you have one | A board measurement, or one PE written in HLS |
| Week 3 | Accelerators and dataflow | Advanced: searching the mapping space, sparsity support, on-chip buffers and networks, and energy per access (Stanford CS217) | Two mappings of one operator, ranked by energy |
| Week 4 | Edge SoCs and NPUs | Intermediate and Advanced: power and thermal budgets in watts, memory shared by every engine, NPU microarchitecture, operator coverage and scheduling across engines (AMD-AI-STACK §13B; QUALCOMM-AI-STACK §6B; MIT 6.5940) | Your P10 fallback report read as architecture evidence: the missing operator or format that cost the most |

---

## 23. Month 19: number formats in silicon, then performance modelling

**Goal:** price every number format in accuracy and in area, on both sides, then build the
end-to-end model that ranks hardware levers. **Gates this month:** A5, A5 edge and A6.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 541 | A5 | The format zoo: significand widths from FP32's 24 bits to FP4 E2M1's 2; exponent bits buy range and significand bits precision; OCP against FNUZ FP8; TF32 moved to software emulation on MI350 (AMD-AI-STACK §5) | Check yourself 4 answered |
| 542 | A5 | Block scaling: a shared scale with its own format; block size against scale overhead and outlier isolation; per-tensor, per-channel and per-block granularity; CDNA 4's MXFP8, MXFP6 and MXFP4 with an E8M0 scale over 32 elements (the OCP MX specification; Rouhani et al.) | Check yourself 3 answered |
| 543 | A5 | Accumulation: accumulator width against K, error growth, and partial sums promoted to higher precision; DeepSeek-V3's report and its ISCA '25 follow-up. Rounding (KNOW): round-to-nearest-even, stochastic rounding, and saturation against overflow in FP8 | Check yourself 5 answered |
| 544 | A5 | Subnormals and flush-to-zero (KNOW); Conversion hardware (KNOW): quantise and dequantise units, amax scale computation and where they sit in the pipeline; Low-precision training stability (KNOW): what breaks at FP8 and FP4, and what fixes it | Notes on each failure and its fix |
| 545 | A5 | Build 1, part 1: FP8 E4M3 and E5M2 GEMMs emulated in PyTorch on real LLM weight and activation tensors, against an FP32 reference | Error against K for both formats |
| 546 | A5 | Build 1, part 2: MXFP4 GEMMs; the error plotted against K, block size and scaling granularity | Check yourself 6 answered |
| 547 | Review | Write every format's bit layout and bits per element from memory; weekly note; rest | Weekly note 73 |
| 548 | A5 | Build 2, part 1: INT8 and INT4 multipliers and an FP8 significand multiplier with an exponent adder, in SystemVerilog | Three multipliers, verified |
| 549 | A5 | Build 2, part 2: all three synthesised with Yosys, then an FP32 accumulator added and its share of the total measured | Relative cell counts, accumulator included |
| 550 | A5 | GPU MODE lectures 69 and 84; then A5's exit test: a format and block size recommended for a named tensor class, with accuracy and relative area side by side | A5 **Done when** passed |
| 551 | A5 edge | Formats for an NPU: integer-first engines (XDNA's int8, int16, bf16 and block-FP16; HMX's INT4, INT8, INT16 and FP16); Weight-only against full quantisation; Block size on a device, with the scales counted; The cliff to HVX, roughly 300× slower (QUALCOMM-AI-STACK §6, §9) | The formats your target's matrix unit supports, listed |
| 552 | A5 edge | Build, part 1: the emulator extended to 8-bit weights with 16-bit activations, and to 4-bit weights at block sizes of 32 and 128, on a small on-device LLM's real weights | Accuracy per format, scales counted |
| 553 | A5 edge | Build, part 2: INT8 × INT16 and INT4 × INT16 multipliers synthesised beside your INT8 and INT4 ones; then the edge side's exit test | A5 edge **Done when** passed |
| 554 | Review | Explain why a missing format is a cliff and not a slope, from memory; weekly note; rest | Weekly note 74 |
| 555 | A6 | Model types (KNOW): analytical (roofline and hierarchical roofline), queueing, trace-driven and cycle-level, and what each costs in accuracy, speed and effort; the Roofline paper | Check yourself 1 answered |
| 556 | A6 | Hierarchical roofline: one roof per memory level and per interconnect, and each operator placed at each level (*How to Scale Your Model* chapter 1, its problems worked) | Your P1 kernels on a hierarchical roofline |
| 557 | A6 | Communication models: the α–β model; LogP and LogGP (KNOW); the cost of each collective on ring, tree and hierarchical algorithms | Check yourself 2 answered |
| 558 | A6 | Queueing (KNOW): Little's law, and why latency climbs near full utilisation, as in your P4 tails. End-to-end LLM models: a training step as compute plus exposed communication plus bubbles; inference as prefill plus decode with KV growth, batching and SLOs (chapters 4, 5 and 7) | Both models written as equations |
| 559 | A6 | Workload characterisation: operator mix, shapes and intensity across dense, MoE and long-context models, and across recommendation and diffusion; the three operator classes of "Data Movement Is All You Need"; the trends two to three years out | An intensity histogram of one workload |
| 560 | A6 | Simulators (KNOW): ASTRA-sim with MLCommons Chakra traces, Timeloop and Accelergy, Accel-Sim and SCALE-Sim, and the question each one answers; one Chakra trace run through ASTRA-sim | A simulated step beside your own estimate |
| 561 | Review | Re-derive the ring all-reduce's α–β cost from memory; weekly note; rest | Weekly note 75 |
| 562 | A6 | Build, part 1: a Python model covering TP, PP, DP and EP, with FLOP/s per format, HBM capacity and bandwidth, and scale-up and scale-out bandwidth and latency | The model's structure |
| 563 | A6 | Build, part 2: calibrate it on your P3 and P4 measurements | Every calibrated parameter traced to a run |
| 564 | A6 | Validation: held-out configurations that you did not calibrate on, and the whole error distribution. Build, part 3: the held-out runs | Check yourself 3–4 answered |
| 565 | A6 | Sensitivity analysis: partial derivatives of step time and cost per token, tornado charts and Pareto frontiers. Build, part 4: 2× HBM bandwidth, 2× matrix FLOP/s and 2× scale-up bandwidth, on dense training, MoE training and long-context decode | The levers ranked per workload; Check yourself 5 answered |
| 566 | A6 | Where models fail: overlap assumed to be perfect, and efficiency that depends on shape; the OpenAI performance-modelling posting of roadmap #1 §1, read as a checklist | Check yourself 6 answered |
| 567 | A6 | A6's exit test: validated within a stated error on held-out runs, with the levers ranked per workload and the sensitivities behind the ranking | A6 **Done when** passed |
| 568 | Review | Present your tornado chart to someone outside the field; weekly note; rest | Weekly note 76 |
| 569 | Buffer | Finish anything late | Nothing left over from month 19 |
| 570 | Month gate | Re-run A5, A5 edge and A6 cold; write the month report | Month report 19; three gates ticked |

### Track hour, month 19

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Computer arithmetic and number formats | Advanced: FP8 variants, block-scaled formats, stochastic rounding, and how a multiplier's area and energy grow with significand width (Ercegovac & Lang, *Digital Arithmetic*; Muller et al.) | A stochastic-rounding experiment on your A5 emulator |
| Week 2 | Performance modelling and simulation | Advanced: trace-driven against cycle-level simulation, and validation on held-out data (Harchol-Balter; the ASTRA-sim papers); gem5 run on one of your A2 loops | gem5's miss counts beside your cache simulator's |
| Week 3 | Interconnects and networks | Intermediate: PCIe; scale-up links (Infinity Fabric and NVLink); scale-out networks (InfiniBand and RoCE); on-chip network basics (Jerger, Krishna & Peh, *On-Chip Networks*) | Every link of the ND MI300X v5, with its bandwidth in each direction |
| Week 4 | Interconnects and networks | Advanced: fat-tree, torus and dragonfly; routing and congestion control; collectives mapped to a topology; BookSim 2 and gem5's Garnet, and UCIe (AWARE) (Dally & Towles) | One topology's bisection bandwidth computed by hand |

---

## 24. Month 20: the device model, the cluster and its facility

**Goal:** a validated model of your device, a 1,024-accelerator cluster in which every number
traces to evidence, the energy and cost of the cloud against the device, and the start of storage.
**Gates this month:** A6 edge, A7 and A7 edge.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 571 | A6 edge | Modelling a device: Terms per phase and per engine over one shared bandwidth; Thermal limits, so sustained clocks rather than burst ones (QUALCOMM-AI-STACK §6B); Energy per token as power × time ÷ tokens, on mains and on battery | The device model's equations |
| 572 | A6 edge | Build, part 1: the model extended to your device and calibrated on your P4 edge-side measurements | The calibrated device model |
| 573 | A6 edge | Build, part 2: validation on a held-out prompt length | The device model's error |
| 574 | A6 edge | Rank 2× memory bandwidth, 2× NPU throughput and 2× on-chip memory for prefill and for decode; then the edge side's exit test | A6 edge **Done when** passed |
| 575 | A7 | Scale-up fabrics (KNOW): NVLink and NVSwitch, AMD Infinity Fabric (AMD-AI-STACK §5), load/store semantics, bandwidth per GPU and domain size; UALink (AWARE), reported rather than shipped (AMD-AI-STACK §20) | A table of scale-up domains |
| 576 | A7 | Scale-out networks (KNOW): InfiniBand and RoCE v2, Ultra Ethernet (AWARE), NICs, RDMA and GPU peer-to-peer transfers (Guo et al.; Gangidi et al.) | Notes on what RoCE needs from the network |
| 577 | Review | Draw a rail-optimised fat-tree from memory; weekly note; rest | Weekly note 77 |
| 578 | A7 | Topologies (KNOW): fat-tree (Clos), rail-optimised, torus and dragonfly; bisection bandwidth, oversubscription and diameter (Dally & Towles) | Check yourself 1 answered |
| 579 | A7 | Congestion and load balancing (KNOW): ECMP and flow collisions; PFC, with its head-of-line blocking and deadlock; DCQCN and packet spraying (AWARE); multi-plane networks, as in DeepSeek-V3's ISCA '25 paper | Check yourself 3–4 answered |
| 580 | A7 | Mapping collectives to topology: hierarchical all-reduce, all-to-all on fat-trees against tori, and TP, PP, DP and EP placed on the physical hierarchy. Host and memory interconnect (KNOW): PCIe generations, storage and checkpoint bandwidth, and CXL (AWARE) | Check yourself 6 answered |
| 581 | A7 | The facility (KNOW): rack power density, liquid cooling, power delivery, failure rates and MTBF, and Young's checkpoint interval. Total cost of ownership: capital plus operating cost, $/token and performance per watt (*The Datacenter as a Computer*) | Check yourself 2 and 7 answered |
| 582 | A7 | An ASTRA-sim what-if: one collective on two topologies, with the difference explained | A simulated comparison of two networks |
| 583 | A7 | Bandwidth directions: kipply shows that an A100's "600 GB/s" is 300 GB/s each way. Build, part 1: the scale-up domain, scale-out topology, oversubscription and NICs per accelerator of a 1,024-accelerator cluster for a named model (Alibaba HPN; the Llama 3 infrastructure sections; TPU v4's optical network) | The fabric designed; Check yourself 5 answered |
| 584 | Review | Re-read the cluster design as the network team would; weekly note; rest | Weekly note 78 |
| 585 | A7 | Build, part 2: where each parallelism group goes, and the step time predicted by your A6 model | The step time, predicted |
| 586 | A7 | Build, part 3: the failure and checkpoint policy, rack power and cooling, and TCO per training run, each number sourced or tagged as an assumption | The design complete |
| 587 | A7 | Change one assumption, such as MoE instead of dense, and quantify what it does; then A7's exit test | A7 **Done when** passed |
| 588 | A7 edge | The device as a system: The on-chip path (XDNA's shim tiles; the remote procedure call into Snapdragon's DSP, QUALCOMM-AI-STACK §3B); The thermal envelope; Cloud against device, in energy and cost per token (roadmap #2 P10) | The comparison's inclusions and exclusions, written first |
| 589 | A7 edge | Build: one workload served cloud-only, device-only and cascaded, from your device measurements and your cluster design | Energy and cost per token, three ways |
| 590 | A7 edge | Name the assumption that would reverse the result; then the edge side's exit test | A7 edge **Done when** passed |
| 591 | Review | Explain Young's interval and the TCO formula from memory; weekly note; rest | Weekly note 79 |
| 592 | A8 | The capacity hierarchy (KNOW): HBM, host DRAM, local NVMe, a parallel file system and an object store, with capacity, bandwidth, latency and cost per byte; CXL memory as a tier (AWARE) | The hierarchy tabulated for your A7 cluster |
| 593 | A8 | Checkpoint sizing: 12–14 bytes per parameter for mixed-precision AdamW; Llama 3's Tectonic figures and its bursty checkpoint writes; sizing for the burst; asynchronous, multi-tier checkpointing with DCP's `async_save` | Check yourself 1–2 answered |
| 594 | A8 | Ingestion as a hardware requirement: host CPU cores and memory, the CPU-to-accelerator ratio, the Meta ingestion study and tf.data; text against images, video and recommendation features | Check yourself 3 answered |
| 595 | A8 | Data paths (KNOW): direct storage-to-GPU transfers against bounce buffers; front-end against back-end networks, and the ND MI300X v5's ratio of 40 | Check yourself 4 answered |
| 596 | A8 | The KV cache as a storage tier (KNOW): Mooncake's disaggregated design, its KV pooling and its early rejection; LMCache (AWARE) | Check yourself 5 answered |
| 597 | A8 | Recommendation and retrieval (KNOW): DLRM's model-parallel embeddings and data-parallel MLPs, Gupta et al. on inference latency, and Faiss's index trade-offs. Fleet profiling as evidence (KNOW): Google-Wide Profiling, Kanev et al. and Chakra traces | Check yourself 6 answered |
| 598 | Review | Size a checkpoint burst for a model you have not seen, from memory; weekly note; rest | Weekly note 80 |
| 599 | Buffer | Finish anything late | Nothing left over from month 20 |
| 600 | Month gate | Re-run A6 edge, A7 and A7 edge cold; write the month report | Month report 20; three gates ticked |

### Track hour, month 20

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Packaging, power and thermal | Intermediate: cost per good die, chiplets against monolithic dies, 2.5-D packaging on interposers, HBM integration and thermal design power | Your A2 die-cost model extended with an interposer |
| Week 2 | Packaging, power and thermal | Advanced: 3-D stacking and hybrid bonding, power delivery, DVFS, liquid cooling and power capping; McPAT and CACTI for power estimates | A CACTI estimate for one cache of your A2 simulator |
| Week 3 | Storage and memory at system scale | Advanced: the KV cache as a storage tier, CXL memory pooling, and embedding tables in recommendation models (the Mooncake and DLRM papers) | One page sizing a CXL tier for a KV cache |
| Week 4 | Datacenters and fleets | Intermediate and Advanced: failure rates and checkpoint intervals, cluster scheduling and utilisation, fleet traces, fragmentation, RAS and silent data corruption, power oversubscription and carbon accounting (*The Datacenter as a Computer*) | A TCO spreadsheet for your A7 cluster, every input sourced |

---

## 25. Month 21: storage and the fleet, on both sides

**Goal:** a storage design checked against your own measurements, a device's capacity limits, a
trace study and a fleet-health plan, and the fleet of devices. **Gates this month:** A8, A8 edge,
A9 and A9 edge.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 601 | A8 | Build 1, part 1: checkpoint size, frequency, burst bandwidth and first landing tier for your A7 cluster | The checkpoint plan |
| 602 | A8 | Build 1, part 2: input-pipeline CPU cores and host memory per accelerator for a text model and for one vision or recommendation model; KV-cache capacity per tier for a stated load and hit rate | The ingestion and KV-cache plans |
| 603 | A8 | Build 1, part 3: every rate validated against your F7 fio study, a P3 checkpoint and a P4 sweep; one input doubled and carried through the design | The doubled input, quantified |
| 604 | A8 | Build 2: your P3 and P4 profiler traces converted to Parquet, and ranked with DuckDB by time, bytes moved and intensity | The ranking, matching the profiler |
| 605 | A8 | A8's exit test | A8 **Done when** passed |
| 606 | A8 edge | Capacity on a device: The memory budget (weights, KV cache, runtime and activations; Token Fusion's 16K cap and `genai_config.json`, AMD-AI-STACK §13B); Load time, and QNN context binaries (QUALCOMM-AI-STACK §4); Download size | A memory budget for a named model |
| 607 | Review | Explain the three parts of a cold start from memory; weekly note; rest | Weekly note 81 |
| 608 | A8 edge | Build, part 1: cold start with the model read from flash and from the page cache, and first inference with and without a cached compiled artefact | Cold start split into reading, compiling and warming up |
| 609 | A8 edge | Build, part 2: predict the longest context that fits your device's budget, then confirm it; then the edge side's exit test | A8 edge **Done when** passed |
| 610 | A9 | Cluster scheduling (KNOW): Borg-style cluster management and Kubernetes, gang scheduling, fragmentation and queueing delay (the Borg paper; "Borg, Omega, and Kubernetes") | Check yourself 2 answered |
| 611 | A9 | Reading real traces: the Philly traces (install Git LFS first; 0.98 GB unpacks to 6.6 GB) and Alibaba's `gpu-v2020`, `gpu-v2023`, `gpu-v2025` and `gpu-v2026` | The trace loaded, and its parsing notebook run; Check yourself 3 answered |
| 612 | A9 | Sharing and partitioning (KNOW): MI300X partitioning modes, MIG, time-slicing and SR-IOV; sharing is not isolation, as Slurm's GPU sharding shows | Notes on what each mode strands |
| 613 | A9 | Reliability, availability and serviceability (RAS): ECC, poison and page retirement, health checks, burn-in and failure domains; silent data corruption (Dixit et al.; Hochschild et al.); Llama 3's 466 interruptions in 54 days | Check yourself 1 and 4 answered |
| 614 | Review | Explain why silent data corruption needs software defences, from memory; weekly note; rest | Weekly note 82 |
| 615 | A9 | Security architecture (KNOW): roots of trust, measured boot and attestation; Caliptra; confidential VMs such as AMD SEV-SNP, and GPU trusted execution environments (AWARE) | Check yourself 5 answered |
| 616 | A9 | A threat model for an accelerator in a multi-tenant cloud, with a root of trust, secure firmware update and isolation between tenants (the Caliptra specification; Anderson, *Security Engineering*) | The threat model |
| 617 | A9 | Power at fleet scale (KNOW): capping and oversubscription (Fan et al.), tens of megawatts swinging at once, and a diurnal throughput variation of 1–2%. Carbon (KNOW): "Chasing Carbon", and Patterson et al. | Check yourself 6–7 answered |
| 618 | A9 | Heterogeneous fleets (KNOW): mixed generations and memory sizes, Splitwise's split of prefill and decode, and a cloud instance's ratios read as its designer's assumptions (roadmap #2 P7) | Notes |
| 619 | A9 | Build 1, part 1: one published statistic reproduced from the trace | The statistic, reproduced |
| 620 | A9 | Build 1, part 2: one change simulated, such as a packing policy or GPU partitioning, and a one-page recommendation on queueing delay and utilisation | The recommendation, backed by the simulation |
| 621 | Review | Re-read your recommendation as the scheduling team would; weekly note; rest | Weekly note 83 |
| 622 | A9 | Build 2: a fleet-health plan for your A7 cluster: burn-in, periodic checks, screening for silent data corruption, the expected interruption rate and the goodput it costs, and one hardware feature that would reduce the cost | The plan, with sourced failure rates |
| 623 | A9 | A9's exit test | A9 **Done when** passed |
| 624 | A9 edge | The device fleet: The support matrix (AMD's OGA flow supports Strix and Krackan Point but not Phoenix or Hawk Point, AMD-AI-STACK §13B); Staged rollouts and halt criteria (roadmap #2 P8); Security across the fleet; Carbon over a device's life | A support matrix for your P10 application |
| 625 | A9 edge | Build: a fleet plan for your P10 application across a mixed device population, each class with its engine, fallback, rollout stages and halt criteria | The fleet plan |
| 626 | A9 edge | The cloud capacity for classes without an NPU, derived from measured fallback and cascade rates; then the edge side's exit test | A9 edge **Done when** passed |
| 627 | A10 | From trend to requirement: MoE, long context, low precision, MLA, speculative decoding and RL post-training, each turned into FLOP/s per format, bytes/s, capacity, scale-up domain size and latency | A table of requirements |
| 628 | Review | List the evidence in your repository that a proposal could use; weekly note; rest | Weekly note 84 |
| 629 | Buffer | Finish anything late | Nothing left over from month 21 |
| 630 | Month gate | Re-run A8, A8 edge, A9 and A9 edge cold; write the month report | Month report 21; four gates ticked |

### Track hour, month 21

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Hardware security | Basic and Intermediate: why hardware must be trusted; secure boot; roots of trust; measured boot and attestation; signed firmware (Bhunia & Tehranipoor, *Hardware Security*) | The boot chain of one accelerator, drawn |
| Week 2 | Hardware security | Advanced: trusted execution environments and confidential VMs, isolation on shared GPUs, and side channels and fault attacks | One side channel explained, with the defence that closes it |
| Week 3 | The software a feature must pass through | Basic to Advanced: the framework, compiler, library, runtime and driver; which layer a new instruction, format or memory feature must change; the cost of exploiting it (AMD-GPU-PATH; roadmap #2 P1 and P2) | The software path of one CDNA 4 feature, traced layer by layer |
| Week 4 | Workloads and trends | Basic to Advanced: dense transformers, mixture-of-experts, diffusion and recommendation; operator mixes; long context, low precision, speculative decoding and RL-trained reasoning; MLPerf results ("Insights into DeepSeek-V3") | The three trends your proposal will bet on, with evidence |

---

## 26. Month 22: the hardware proposal

**Goal:** a ten-page hardware proposal that survives hostile review, whose key figure a stranger
rebuilds with one command, and the start of a specialisation. **Gate this month:** A10, and every
line of roadmap #1 §15.

| Day | Stage | Today | You finish with |
| --- | --- | --- | --- |
| 631 | A10 | The two-to-three-year bet, and programmability as its hedge (*How to Scale Your Model*, the introduction and its co-design footnote); The hardware lottery (KNOW) (Hooker) | Check yourself 2 and 6 answered |
| 632 | A10 | Case studies (KNOW): the TPU, FlashAttention, MoE, DeepSeek-V3's hardware requests, and CDNA 4's changes, each read as a bet (AMD-AI-STACK §5) | Check yourself 1 answered |
| 633 | A10 | Benchmark design (KNOW): representative workloads and MLPerf's rules. Vendor evaluation (KNOW): datasheet against sustained numbers, and acceptance tests | Check yourself 5 answered |
| 634 | A10 | Fleet impact (KNOW), through A7–A9; Communication: the proposal's structure, a one-page executive summary, and disagreeing with data | Check yourself 3–4 answered |
| 635 | A10 | Choose the proposal's topic from your own evidence, such as native MXFP4 with wider accumulation, a larger LDS or a larger scale-up domain, and write its falsifier before anything else | The topic and its falsifier |
| 636 | A10 | Section 1: the workload evidence, from your own P-stage measurements | Section 1 |
| 637 | Review | Try to break your falsifier; weekly note; rest | Weekly note 85 |
| 638 | A10 | Section 2: the proposed change, specified | Section 2 |
| 639 | A10 | Section 3: its benefit, modelled in A6 with its sensitivity | Section 3 |
| 640 | A10 | Section 4, part 1: its area cost, from RTL of the proposed block synthesised as in A1 and A5 | The area estimate, with its method |
| 641 | A10 | Section 4, part 2: its power cost, with its method stated | Section 4 |
| 642 | A10 | Section 5: its effects on the fleet: storage, scheduling, reliability, power and carbon (A8, A9) | Section 5 |
| 643 | A10 | Section 6: the software work it needs: compiler support (roadmap #2 P2) and kernels (roadmap #2 P1) | Section 6 |
| 644 | Review | Read sections 1–6 as a hostile reviewer; weekly note; rest | Weekly note 86 |
| 645 | A10 | Section 7: the alternatives you considered, and why each lost | Section 7 |
| 646 | A10 | Section 8: the risks, and the measurement that would prove the proposal wrong | Section 8 |
| 647 | A10 | Section 9: its effect on the other side of the product line (roadmap #1 §3E) | Section 9 |
| 648 | A10 | The script that rebuilds the key figure with one command | The key figure, rebuilt from a clean checkout |
| 649 | A10 | The one-page executive summary | The summary |
| 650 | A10 | A design review with peers, run as a hostile review | Every objection recorded |
| 651 | Review | Sort the objections into fixed, answered and open; weekly note; rest | Weekly note 87 |
| 652 | A10 | Revise the proposal to answer the review | The revised proposal |
| 653 | A10 | A stranger rebuilds the key figure from your repository alone | Their figure, beside yours |
| 654 | A10 | A10's exit test: every benefit traced, the cost method stated, the key figure reproduced and the other side addressed | A10 **Done when** passed |
| 655 | Portfolio | The repository's README for roadmap #1: the proposal, the models, the RTL and every stage report | A portfolio a hardware team can navigate |
| 656 | Career | Place yourself on the ladder in roadmap #2 §3G at staff, principal and architect level, and plan the evidence that only work will give you | A self-assessment |
| 657 | Career | Interview practice for architect roles: performance modelling, microarchitecture and system design, and deep dives into your proposal | Three mock interviews, with notes |
| 658 | Review | Re-read your month 1 report beside today's repository; weekly note; rest | Weekly note 88 |
| 659 | Buffer | Finish anything late; stop every rented resource | Nothing left over |
| 660 | Final gate | Tick every line of roadmap #1 §15 and roadmap #2 §23; write the final report | Both roadmaps done, on both sides |

### Track hour, month 22

| Week | Track | Concepts and work | You finish with |
| --- | --- | --- | --- |
| Week 1 | Technical influence | Basic and Intermediate: clear writing; presenting data honestly; design documents and reviews; disagreeing with data | Your A6 report rewritten for a reader outside your field |
| Week 2 | Technical influence | Advanced: architecture proposals with alternatives, costs and a falsifier; executive summaries (Hooker, "The Hardware Lottery") | A one-page summary that a manager could decide from |
| Week 3 | Expert tracks | Choose two tracks from §28, and write a 12-week plan for each | Two 12-week plans |
| Week 4 | Skills no exit test checks | At staff and principal level (roadmap #2 §3G): technical direction, cross-team designs, strategy papers and mentoring | A talk on your proposal, given to an audience |

---

## 27. The syllabus index: every subject, every level, its days

Every subject of both syllabi, roadmap #2 §3D and roadmap #1 §3D, with the days on which it
reaches each of its four levels. "Track hour, month N" is a row of that month's track-hour table,
and §28 is the Expert track that continues the subject. Each subject's Tools, Projects and books
are in its roadmap, and the rows named here use them.

### Roadmap #2's syllabus: software, systems, ML and production

| Subject | Basic | Intermediate | Advanced | Expert |
| --- | --- | --- | --- | --- |
| Mathematics for AI | Days 2–54 (Z1) | Days 77–92 (F1) | Days 82–99 (F1) | Day 338 (P5); §28 |
| C programming | Days 57, 71 and 102 | Days 103–107 | Days 107–110, 133 and 143 | Days 113–116, 140 and 264; §28 |
| C++ | Day 131 | Days 131–137 | Days 132–133, 139 and 142–143 | Day 274 (P1); §28 |
| Python | Days 2–55 (Z2) | Days 128–129 | Days 129, 139 and 146 | §28 |
| Data structures and algorithms | Days 117 and 123 | Days 121–126 | Days 124–126; track hour, month 5 | Day 356 (P6); §28 |
| Computer architecture, as software sees it | Days 42–45 and 61–66 | Days 72 and 75; track hour, month 3 | Days 145 and 189–207; track hour, month 3 | Days 213 and 264; days 475–516 (A2, A3); §28 |
| Operating systems and Linux | Days 4 and 12 (Z3) | Days 75, 107–110 and 218–225 | Days 221–225 and 250; track hour, month 8 | §28 |
| Compilers, linkers and runtimes | Day 106 | Day 106; track hour, month 10 | Days 285–292; track hour, month 10 | §28 |
| Software engineering | Days 9, 17 and 27; track hour, month 2 | Days 137–138; track hour, month 3 | Days 215–216; track hour, month 3 | Day 428; track hour, month 15; §28 |
| Networking | Day 226 | Days 226–230; track hour, month 9 | Days 227 and 302; track hour, month 9 | Days 575–583 (A7); §28 |
| Distributed systems | Day 235 | Days 230–246 | Days 241–246 and 301–312; track hour, month 9 | §28 |
| Databases and storage engines | Day 347; track hour, month 7 | Track hour, month 7 | Day 348; track hour, month 8 | Days 348 and 356; §28 |
| Classical machine learning | Day 151; track hour, month 4 | Track hour, month 4 | Track hour, month 5 | §28 |
| Deep learning | Days 151–155 | Days 156–167 | Days 162–170 and 181–182 | §28 |
| Large language models | Days 161 and 186 | Days 176–185; track hour, month 7 | Days 181–182, 311, 352 and 383 | Days 313–316 and 349–350; §28 |
| Generative models beyond LLMs | Track hour, month 6 | Track hour, month 6 | Day 170; track hour, month 6 | Track hour, month 8; §28 |
| LLM applications and agents | Track hour, month 13 | Track hour, month 13 | Track hour, month 14 | Day 396; §28 |
| GPU and accelerator programming | Days 188–191 | Days 192–207; track hour, month 7 | Days 255–276 | Days 262–264 and 274; §28 |
| ML frameworks and compilers | Day 285 | Days 285–287 and 294 | Days 287–293; track hour, month 11 | §28 |
| Distributed training | Day 301 | Days 302–305 | Days 306–312 | Day 387; days 562–567 (A6); §28 |
| Inference and model serving | Day 325 | Days 325–326 | Days 317–324 | Days 327 and 372; §28 |
| Quantisation and compression | Day 335 | Days 339–340 | Days 336–342 | Days 313 and 341; §28 |
| Performance engineering | Day 211 | Days 212–215 | Days 199–202 and 213–216 | Days 229 and 437; §28 |
| Edge and on-device AI | Day 278 | Days 282 and 343 | Days 279–283, 331–334 and 402–409 | Days 294–297; §28 |
| Data engineering | Day 347 | Day 348; track hour, month 12 | Days 348–350; track hour, month 12 | §28 |
| Cloud computing | Track hour, month 12 | Day 363; track hour, month 12 | Track hour, month 12 | Days 372 and 412; §28 |
| DevOps and platform engineering | Track hour, month 11 | Track hour, month 11 | Days 364 and 368–371; track hour, month 11 | §28 |
| MLOps and LLMOps | Day 379 | Days 380–382; track hour, month 13 | Days 383–384; track hour, month 13 | §28 |
| Observability and SRE | Day 385 | Day 385; track hour, month 13 | Days 386–387 | §28 |
| Security for AI systems | Day 1 | Day 393; track hour, month 14 | Days 394–396 | §28 |
| Responsible AI and governance | Track hour, month 14 | Track hour, month 14 | Track hour, month 14 | Track hour, month 15; §28 |

### Roadmap #1's syllabus: silicon, architecture, systems and co-design

| Subject | Basic | Intermediate | Advanced | Expert |
| --- | --- | --- | --- | --- |
| Digital logic and circuits | Days 42–43 and 62–64 | Days 452–458 | Days 453–454 and 462; track hour, month 16 | Days 472–474 (A1 edge); §28 |
| RTL design | Day 456 | Days 455–456 | Days 460–462; track hour, month 16 | Days 460–469; §28 |
| Verification | Day 459 | Day 461; track hour, month 16 | Track hour, month 16 | §28 |
| Synthesis, timing and physical design | Day 463 | Days 458 and 467 | Days 468–469; track hour, month 17 | §28 |
| FPGAs and emulation | Day 466; track hour, month 18 | Track hour, month 18 | Track hour, month 18 | §28 |
| Processor architecture | Days 65–66 and 475–476 | Days 476–477 | Days 477 and 492–493; track hour, month 17 | §28 |
| Memory systems and coherence | Day 481 | Days 481–486 | Days 485–486 and 491; track hour, month 17 | Days 592–597 (A8); §28 |
| GPU architecture | Day 500 | Days 502–507 | Day 507; track hour, month 17 | Days 511–516; §28 |
| Accelerators and dataflow | Days 460 and 522 | Days 522–525 | Days 526–528; track hour, month 18 | Days 529–533; §28 |
| Edge SoCs and NPUs | Day 278 | Days 497–499 | Days 534–536; track hour, month 18 | Days 551–553 and 571–574; §28 |
| Computer arithmetic and number formats | Days 69–70 | Days 335–336 | Days 541–544; track hour, month 19 | Days 545–550; §28 |
| Performance modelling and simulation | Days 199 and 229 | Days 555–558 | Days 560–566; track hour, month 19 | Day 567; §28 |
| Interconnects and networks | Day 575 | Days 575–576; track hour, month 19 | Days 578–582; track hour, month 19 | Days 583–587; §28 |
| Packaging, power and thermal | Day 489 | Days 488–490; track hour, month 20 | Track hour, month 20 | Day 586; §28 |
| Storage and memory at system scale | Day 592 | Days 593–595 | Days 596–597; track hour, month 20 | Days 601–605; §28 |
| Datacenters and fleets | Day 581 | Days 610–613 | Days 611–617; track hour, month 20 | Days 622–626; §28 |
| Hardware security | Day 615; track hour, month 21 | Day 615; track hour, month 21 | Track hour, month 21 | Day 616; §28 |
| The software a feature must pass through | Days 285–287 | Day 643; track hour, month 21 | Day 643; track hour, month 21 | §28 |
| Workloads and trends | Days 170 and 181 | Day 559 | Day 627; track hour, month 21 | Days 627 and 631; §28 |
| Technical influence | Day 211 | Track hour, month 22 | Days 635–654; track hour, month 22 | §28 |

---

## 28. Expert tracks, after day 660

Expert level is where people specialise, and nobody holds it in every subject. Each track below is
one subject's Expert level from its roadmap's syllabus. Take one or two at a time, in blocks of
twelve weeks at the same daily routine: weeks 1–4 to read the primary work, weeks 5–10 to build
the artefact, and weeks 11–12 to write it up and put it where others can check it. That rhythm is
planning judgement, not a promise that twelve weeks make an expert.

| Subject | The Expert level | Starts from | An artefact that proves it |
| --- | --- | --- | --- |
| Mathematics for AI | Randomised linear algebra; the theory of adaptive and second-order optimisers; the mathematics of scaling laws; the numerical analysis of low-precision training | F1, F4 and P5 | A randomised SVD with its error measured against the exact one, and one scaling-law fit derived and checked |
| C programming | Your own allocator; lock-free structures in C11 atomics; SIMD intrinsics; reading compiler output; core dumps from optimised builds | F2 | A lock-free queue in C11 atomics, clean under TSan and a stress test |
| C++ | Lock-free structures; custom allocators; the compile-time template kernels of CUTLASS and Composable Kernel; coroutines | F2 and P1 | A templated GEMM in the style of Composable Kernel, benchmarked against your P1 ladder |
| Python | CPython's bytecode, reference counting and garbage collector; the free-threaded build (AWARE); a library with a stable public API | F2 | A C extension that releases the GIL, published as a versioned package |
| Data structures and algorithms | Cache-aware and cache-oblivious algorithms; concurrent and lock-free structures; Bloom filters, HyperLogLog and count-min sketches; approximate nearest-neighbour search | F2 and P6 | A Bloom filter and a count-min sketch in C, benchmarked against exact structures |
| Computer architecture, as software sees it | Tuning at the microarchitecture level with hardware counters; vendor ISA manuals; the design of CDNA and RDNA | F5, P1, A2 and A3 | One kernel tuned from counter evidence to a stated fraction of peak |
| Operating systems and Linux | Kernel development and debugging; the Linux scheduler and memory manager; eBPF tracing; the `amdgpu` driver and its KFD interface; tuning for low latency | F7 | A merged kernel patch, or an eBPF tool that explains a real latency problem |
| Compilers, linkers and runtimes | An LLVM pass or an MLIR dialect; polyhedral loop transformation; autotuning and cost models; the AMDGPU back end and its code objects | P2 | A compiler pass that speeds up one of your kernels, with its tests |
| Software engineering | Leading design reviews; upstream work on large projects; owning a subsystem's reliability; writing for decision-makers | P11 and A10 | A subsystem you own, with its design review and reliability record |
| Networking | Congestion control for AI collectives; datacenter topologies; tuning with `tcpdump` and eBPF; programmable networks | F7 and A7 | One collective measured under two network settings, with the difference explained |
| Distributed systems | TLA+ specifications; fault injection in the style of Jepsen; Byzantine fault tolerance; Spanner and TrueTime; elastic training on thousands of GPUs | F7, P3 and P8 | Your Raft specified in TLA+ and model-checked, or a Jepsen-style test that finds a bug |
| Databases and storage engines | A storage engine of your own; distributed SQL; vector databases and ANN indexes at scale; lakehouse table formats | F7 and P6 | Your key/value store grown into an engine with transactions and recovery tests |
| Classical machine learning | Learning theory; Bayesian methods at scale; ranking and recommendation; online learning and bandits | The track hours of months 4–6 | A bandit or ranking system, evaluated offline and online |
| Deep learning | Training stability at scale; optimiser design; interpretability; architectures beyond the transformer, such as state-space models | F3 and P3 | One paper on stability, optimisers or state-space models, reproduced with its code |
| Large language models | Pre-training at scale; reasoning models trained with reinforcement learning; distillation; data mixtures and synthetic data; serving at frontier scale | F4, P3, P4, P6 and P7 | A pre-training or RL run whose design choices are ablated and written up |
| Generative models beyond LLMs | Video generation; multimodal pre-training; the serving cost of diffusion against LLMs | The track hours of months 6 and 8 | A diffusion pipeline served under an SLO, with its cost per image |
| LLM applications and agents | Multi-agent systems; agent reliability and safety; production tracing of LLM applications; prompt-injection defence in depth | The track hours of months 13–14, and P9 | An agent with measured reliability, and a red-team report against it |
| GPU and accelerator programming | Kernels at the ISA level; CUTLASS, CuTe and Composable Kernel; kernels that communicate across GPUs from inside the kernel; autotuning; new number formats | P1 and P5 | A kernel merged upstream into a library you used |
| ML frameworks and compilers | Compiler passes; a PyTorch back end for a new accelerator; kernel and compiler co-design | P2 and A10 | A compiler fix merged upstream, with its benchmark |
| Distributed training | Fault tolerance, stragglers and elastic restarts on thousands of GPUs; collectives tuned to a topology; a parallelism plan for a new model | P3, P8, A6 and A7 | A parallelism plan for a new model, predicted and then measured |
| Inference and model serving | Disaggregated prefill and decode; KV offload and cache-aware routing; multi-LoRA serving; KServe and Seldon Core; cost per million tokens at an SLO | P4 and P7 | A disaggregated deployment whose goodput beats your P4 baseline, measured |
| Quantisation and compression | Microscaling formats; quantisation-aware training; the numerics of low-precision training; which formats get hardware | P5 and A5 | A low-precision training run with its accuracy parity report |
| Performance engineering | Models that predict before you measure; fleet-wide profiling; benchmark design that survives review | F6, P3, P4 and A6 | A benchmark that others adopt, with its rules and its reproduction script |
| Edge and on-device AI | Compiler back ends for NPUs; power- and thermal-aware scheduling | P10, A4 and A6 | An NPU compiler change, or a scheduler that keeps a device inside its thermal budget |
| Data engineering | Corpus pipelines at petabyte scale; exactly-once streaming; data platforms for an organisation; data for post-training | P6 | A pipeline reproducible byte for byte at a size that no single machine holds |
| Cloud computing | Multi-region design and disaster recovery; FinOps at scale; capacity planning for GPU fleets | P7 and A9 | A disaster-recovery drill run end to end, with its RPO and RTO measured |
| DevOps and platform engineering | An internal developer platform; multi-cluster fleets; policy as code; Kubernetes at thousands of GPU nodes | P7 | A platform that another team deploys through |
| MLOps and LLMOps | An ML platform for many teams; evaluation infrastructure for frontier models; the policy that decides when a model may ship | P8 | A release policy with its gates, used for a real release |
| Observability and SRE | Reliability of training on thousands of GPUs; tail-latency engineering; SRE practice across an organisation | P8 | A tail-latency fix, with p99 before and after and its postmortem |
| Security for AI systems | Red-teaming AI systems; confidential computing and attestation; the security architecture of an AI platform | P9 and A9 | A red-team report whose findings are fixed and verified |
| Responsible AI and governance | Governance programmes for an organisation; safety cases for frontier models | P9, and the track hours of months 14–15 | A safety case for your capstone model |
| Digital logic and circuits | Energy per operation at the circuit level; process variation; low-power and near-threshold design | A1 and A1 edge | A circuit-level energy estimate for your MAC, with its assumptions |
| RTL design | A block micro-architected for area, timing and power together; high-level synthesis and Chisel; a matrix engine | A1 and A4 | A matrix engine that closes timing, with its PPA against your A1 array |
| Verification | A verification plan for a full IP block; formal proofs of protocol properties; emulation of full workloads | A1, and the track hour of month 16 | A verification plan executed to its coverage goals |
| Synthesis, timing and physical design | Timing closure on a large block; PPA trade-offs at a process node; design-technology co-optimisation | A1, and the track hour of month 17 | A block closed on timing with OpenROAD, its trade-offs written up |
| FPGAs and emulation | A full accelerator emulated to run real workloads before tape-out | The track hour of month 18 | Your array running a real GEMM workload on an FPGA |
| Processor architecture | A core designed against a workload; top-down analysis with counters; microarchitectural side channels | A2, and the track hour of month 17 | Your RISC-V core extended and measured on a workload |
| Memory systems and coherence | A memory hierarchy for an accelerator; processing in memory; CXL tiers; memory RAS | A2 and A8 | A memory-hierarchy proposal with its simulator results |
| GPU architecture | Predicting a new GPU's performance from microbenchmarks; proposing a change to one | A3 and A10 | A prediction for a new GPU, published before its benchmarks and then checked |
| Accelerators and dataflow | Accelerators for prefill against decode; hardware for attention and mixture-of-experts | A4 | A dataflow design for attention, modelled and priced |
| Edge SoCs and NPUs | An NPU for on-device LLMs within a power budget; the memory and formats that on-device decode needs; the compiler support each feature requires | The edge sides of A1–A9 | An NPU proposal in the A10 format |
| Computer arithmetic and number formats | Choosing a future accelerator's formats from accuracy, area and energy together | A5 and A10 | A format proposal with accuracy, area and energy side by side |
| Performance modelling and simulation | Models that choose between hardware designs years before the silicon exists | A6 | A model whose prediction a later measurement confirms |
| Interconnects and networks | A scale-up domain and a cluster network designed for a model; collectives and hardware co-designed | A7 | A network design whose collectives are simulated and costed |
| Packaging, power and thermal | Package-level co-design of compute, memory and I/O; power and cooling budgets for a rack | A2 and A7 | A rack's power and cooling budget, every number sourced |
| Storage and memory at system scale | The storage and memory tiers of a whole AI cluster | A8 | A tiering design validated against traces |
| Datacenters and fleets | A fleet's hardware roadmap: generations, SKUs and partitioning | A9 | A fleet roadmap with its TCO over three generations |
| Hardware security | An accelerator's security architecture: a root of trust such as Caliptra, secure firmware update and isolation between tenants | A9, and the track hours of month 21 | A security architecture reviewed against its threat model |
| The software a feature must pass through | Planning the software for hardware that does not exist yet | A10 | The software plan for your A10 proposal's feature |
| Workloads and trends | Forecasting the workloads of the next two to three years | A6 and A10 | A forecast written down, then checked a year later |
| Technical influence | Changing a product roadmap across organisations | A10 | A decision that changed because of your evidence |

---

## 29. After day 660

- **The job.** The levels above senior in roadmap #2 §3G are earned with scope and years: leading
  incidents, mentoring, and designs that other people build on. Study cannot replace them.
- **Specialise.** Take the Expert tracks of §28 one or two at a time, in the order your work needs.
- **The habits that keep you there.** A paper a week, with one reproduced now and then; an upstream
  fix whenever your work finds a bug; the F6 harness on everything you ship; and both roadmaps
  re-read each year, because the field moves.

---

## 30. Verification status

### From this repository

- Every stage, build, exit test, tool and resource named in this plan is taken from the two
  roadmaps: roadmap #2's stages Z1–P11 with their edge and cloud sides, its §3B, §3D and §3H, and
  roadmap #1's stages A1–A10 with their edge sides, its §3B, §3D and §3E. Each keeps the
  verification status given in roadmap #2 §24 or roadmap #1 §16.
- The concept labels in the rows are the Learn topics of the two roadmaps, copied from their text,
  and the track-hour rows use the levels, tools, projects and books of the two syllabi.
- The hardware notes in §4 come from roadmap #2 §3B (the GPU families at ROCm 10.0.0), from
  roadmap #1 §3B (the architect's lab), and from AMD-AI-STACK §13B (the processors that AMD's OGA
  flow supports).

### Checked when this plan was written

- On 2026-09-25 a script outside this repository checked that every Learn topic of both roadmaps
  (244 in roadmap #2 and 113 in roadmap #1) is named in a row of its own stage, that all 51
  subjects of the two syllabi appear in §27 with all four levels placed and in §28, and that every
  track-hour month cited in §27 teaches that subject. It also checked the calendar: 660 days in
  order, every review, buffer and gate day in its place, and every gate passed exactly once.

### Derived here, not quoted from a source

- The schedule: the days given to each stage, the order of the work inside each stage, the daily
  routine, the track hour and what each month's track covers, and the review, buffer and gate
  days. These are planning judgement.
- The hours: 360 study days × 8 hours = 2,880 hours for roadmap #2, and 168 × 8 = 1,344 for
  roadmap #1. At four hours a day the whole plan takes about 44 months.
- Seven months for roadmap #1. This day-level plan replaces the earlier rough estimate of a year.
- The level each day reaches in §27, the artefacts in §28, and the twelve-week rhythm of a track.

### From memory: standard, but not re-fetched here

- The order and topics of the *Neural Networks: Zero to Hero* lectures, the six projects of
  Nand2Tetris Part I, the parts of the 6.5840 Raft lab, CS50x's week numbering, and Kaggle Learn's
  pandas course.
- The contents of the books and tutorials the track hours name without a link, such as the
  tree-walk interpreter of *Crafting Interpreters*, the chapters of LLVM's Kaleidoscope tutorial and
  the assignments of CMU's Needle framework.
- That spaced review and rest improve how much you retain, which is the idea behind the course
  that Z3 in roadmap #2 recommends.

---

## Primary sources

This plan adds no new sources. Every resource it names is listed, with its link where one exists,
in the stage references and Primary sources of
[`ROADMAP-AI-PERFORMANCE-ENGINEER.md`](ROADMAP-AI-PERFORMANCE-ENGINEER.md) and
[`ROADMAP-AI-SYSTEMS-ARCHITECT.md`](ROADMAP-AI-SYSTEMS-ARCHITECT.md).
