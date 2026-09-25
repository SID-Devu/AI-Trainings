# AI-Trainings

Self-directed AI / Machine Learning / Deep Learning engineering programme.

## Contents

| File | What it is |
| --- | --- |
| [`AI-ML-DL-COMPLETE-ROADMAP.md`](AI-ML-DL-COMPLETE-ROADMAP.md) | The full programme specification — 10 weekly modules, plus the conversion phase and the model-to-hardware specialisation track. 19 portfolio artefacts. |
| [`textbook/WEEK-01-MATHEMATICS-FOUNDATIONS.md`](textbook/WEEK-01-MATHEMATICS-FOUNDATIONS.md) | Week 1 textbook, written from zero. 126 concepts: Python, NumPy, linear algebra, calculus, optimisation, information theory. |
| [`reference/QUALCOMM-AI-STACK.md`](reference/QUALCOMM-AI-STACK.md) | The Qualcomm AI stack from model to hardware, explained for a beginner. Every layer diagrammed, the offline toolchain, graph partitioning, Hexagon NPU internals, heterogeneous CPU/GPU/NPU execution with measured evidence, Genie and Gen AI Builder, speculative decoding, and the datacenter branch. |
| [`reference/AMD-AI-STACK.md`](reference/AMD-AI-STACK.md) | The AMD AI stack from model to hardware — **the map**. ROCm and HIP, CDNA datacenter GPUs, RDNA client GPUs and WMMA, the XDNA client NPU, AITER, vLLM on ROCm, Ryzen AI, Quark, NPU + iGPU hybrid execution, the CUDA porting hazards, and a head-to-head of AMD's strategy versus Qualcomm's. |
| [`reference/AMD-GPU-PATH.md`](reference/AMD-GPU-PATH.md) | The AMD **GPU** path from `model.py` to electrons — **the deep dive**. Ten layers with a "see it yourself" command block each: PyTorch dispatch, HIP-to-`hsaco` compilation, AQL kernel dispatch, the execution model, the memory hierarchy, the verified CDNA 3 MFMA instruction set, Triton internals, the roofline workflow, an optimisation ladder, and a staged learning curriculum. |
| [`reference/ROADMAP-AI-SYSTEMS-ARCHITECT.md`](reference/ROADMAP-AI-SYSTEMS-ARCHITECT.md) | Role roadmap #1 — **AI Systems Architect** (hardware/software co-design), the role that changes the hardware to fit the model. Ten gated stages, A1–A10: digital logic and RTL, computer architecture, GPU microarchitecture, accelerators and dataflow, number formats in silicon, performance modelling, interconnect and the datacenter, storage and data systems, the fleet (scheduling, reliability, security and carbon), and a co-design proposal as the capstone, plus a 20-subject hardware syllabus from basic to expert (§3D). Every stage from A1 to A9 decides for a datacenter part and, in its Edge side, for an edge part such as a laptop NPU, each with its own gate (§3E). Its prerequisites are roadmap #2's F0–F7 and P1–P5 exit tests. |
| [`reference/ROADMAP-AI-PERFORMANCE-ENGINEER.md`](reference/ROADMAP-AI-PERFORMANCE-ENGINEER.md) | Role roadmap #2 — **Full-Stack AI Performance Engineer**, the role that changes the software to fit the hardware. Learn it first. It starts from zero, with an on-ramp for someone just out of class 10 (§3E, Z1–Z4). A 31-subject syllabus from basic to expert (§3D) covers C, operating systems, distributed systems, ML, GPUs, model serving from FastAPI and BentoML to vLLM, cloud, MLOps and security; §3F walks AI in the cloud and AI at the edge end to end; §3G is the career ladder from AI systems engineer to systems architect. Foundation stages F0–F7 (computing from zero, C and C++, up to operating systems, networks and distributed systems), then P1–P11: GPU kernels, frameworks and compilers, distributed training, inference and serving, quantisation, data engineering, cloud infrastructure and deployment, operations (MLOps, LLM evaluation and SRE), security, edge and on-device AI, and a capstone that brings a model up end to end in the cloud and on a device. Every stage from P1 to P10 is worked on both sides, cloud and edge, with a separate build and gate for each (§3H), so every domain is learned twice. Every stage ends in a pass/fail exit test. |
| [`reference/PLAN-15-MONTHS.md`](reference/PLAN-15-MONTHS.md) | The **15-month plan, then seven months to architect**, day by day: 660 days from class 10 through both roadmaps, cloud and edge. Days 1–450 are roadmap #2 and days 451–660 are roadmap #1. Every Learn topic of every stage is named on its day; a daily track hour covers the parts of both syllabi that no stage teaches; and an index gives the days on which each of the 51 syllabus subjects reaches Basic, Intermediate, Advanced and Expert, with the Expert levels laid out as specialisation tracks. Each month has its tech stack and its gates, and a table says what hardware and accounts you need, and from which day. The pace is full-time (about eight hours a day, six days a week), or about 44 months at half that. |

## Structure

```text
AI-Trainings/
├── AI-ML-DL-COMPLETE-ROADMAP.md    # the plan
├── textbook/
│   └── WEEK-01-MATHEMATICS-FOUNDATIONS.md
├── reference/
│   ├── QUALCOMM-AI-STACK.md        # vendor stack: model -> hardware
│   ├── AMD-AI-STACK.md             # vendor stack: the map (GPU + NPU, all layers named)
│   ├── AMD-GPU-PATH.md             # GPU deep dive: compiler, dispatch, MFMA, roofline
│   ├── PLAN-15-MONTHS.md           # the 660-day calendar: roadmap #2, then roadmap #1, day by day
│   ├── ROADMAP-AI-SYSTEMS-ARCHITECT.md     # role roadmap #1: hardware/software co-design (A1–A10)
│   └── ROADMAP-AI-PERFORMANCE-ENGINEER.md  # role roadmap #2: performance engineering (Z1–Z4, F0–F7, P1–P11); learn first
└── week01/                          # my code and deliverables (to come)
```

## The roadmap in one table

| Week | Module                                                                                    |
| ---- | ----------------------------------------------------------------------------------------- |
| 1.   | Mathematics: linear algebra, calculus, optimisation, information theory *(double weight)* |
| 2.   | Probability, statistics, experimentation, data handling, SQL                              |
| 3.   | ML foundations and supervised learning                                                    |
| 4.   | Unsupervised learning, model selection, tuning                                            |
| 5.   | Neural networks and PyTorch                                                               |
| 6.   | Training techniques, optimisers, CNNs                                                     |
| 7.   | Sequence models and transformers                                                          |
| 8.   | Specialisations: NLP, vision, generative AI, ranking, RL                                  |
| 9.   | MLOps, deployment, data engineering, system design, ethics                                |
| 10.  | Systems, GPU performance, inference optimisation, career conversion                       |

Continuous throughout: data structures and algorithms, computer science fundamentals,
research literacy.

## Week 1 deliverables

- [ ] 1 — PCA explainer with visual output
- [ ] 2 — linear regression via the normal equation, with `pytest`
- [ ] 3 — gradient descent from first principles, three learning rates
- [ ] 4 — entropy, cross-entropy and KL divergence, verified against SciPy

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install numpy scipy matplotlib pytest
```

## How to read the Week 1 textbook

It is one file, read in this order:

| Part | What it does |
| --- | --- |
| **T** | **The baseline** — what ML actually is, the training loop, the vocabulary, why these four maths branches, the ten-week arc, the standard, your starting scorecard |
| **S** | How to read the maths — Greek letters, `Σ`, indices, set notation, logarithms from scratch |
| **R** | Class 10 refresher + a 12-question prerequisite check |
| **0–7** | Setup · Python · NumPy · Linear algebra · Calculus · Optimisation · Information theory · Advanced |

There is an hour-blocked **5-day plan** at the top of the file (~12–13 hrs/day), with 8-day and
15-day alternatives at lower intensity. Nothing is cut at any pace — only the calendar changes.

| Day | Covers |
| --- | --- |
| 1 | Theory baseline, notation, refresher, setup, Python core |
| 2 | Python advanced, all of NumPy, 35 exercises |
| 3 | Linear algebra complete + deliverables 1 and 2 |
| 4 | Calculus + optimisation + deliverable 3 |
| 5 | Information theory + deliverable 4 + completion gate |

## Status

**Week 1 textbook: ~7,000 lines.** 126 concepts · **132 problems** · **90 quiz questions** ·
35 exercises · 4 deliverables. Every problem has a worked solution, and every code output in the
file was executed before being written.

| Bank | Problems |
| --- | --- |
| §2.17 NumPy | 25 |
| §3.40 Linear algebra | 30 |
| §4.17 Calculus | 30 |
| §5.15 Optimisation | 25 |
| §6.9 Information theory | 22 |
| §3.41 + §6.10 quizzes | 90 questions |

Remaining work is listed in "What is still being added" at the end of the textbook.
