# AI-Trainings

Self-directed AI / Machine Learning / Deep Learning engineering programme.

## Contents


| File                                                                                         | What it is                                                                                                                                              |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`AI-ML-DL-COMPLETE-ROADMAP.md`](AI-ML-DL-COMPLETE-ROADMAP.md)                               | The full programme specification — 10 weekly modules, plus the conversion phase and the model-to-hardware specialisation track. 19 portfolio artefacts. |
| [`textbook/WEEK-01-MATHEMATICS-FOUNDATIONS.md`](textbook/WEEK-01-MATHEMATICS-FOUNDATIONS.md) | Week 1 textbook, written from zero. 126 concepts: Python, NumPy, linear algebra, calculus, optimisation, information theory.                            |
| [`reference/QUALCOMM-AI-STACK.md`](reference/QUALCOMM-AI-STACK.md)                           | The Qualcomm AI stack from model to hardware, explained for a beginner. Every layer diagrammed, the offline toolchain, graph partitioning, Hexagon NPU internals, heterogeneous CPU/GPU/NPU execution with measured evidence, Genie and Gen AI Builder, speculative decoding, and the datacenter branch. |
| [`reference/AMD-AI-STACK.md`](reference/AMD-AI-STACK.md)                                     | The AMD AI stack from model to hardware. ROCm and HIP, CDNA datacenter GPUs, **RDNA client GPUs and WMMA**, the XDNA client NPU, AITER, vLLM on ROCm, Ryzen AI, Quark, **NPU + iGPU hybrid execution**, the CUDA porting hazards, and **a head-to-head of AMD's strategy versus Qualcomm's**. |


## Structure

```
AI-Trainings/
├── AI-ML-DL-COMPLETE-ROADMAP.md    # the plan
├── textbook/
│   └── WEEK-01-MATHEMATICS-FOUNDATIONS.md
├── reference/
│   ├── QUALCOMM-AI-STACK.md        # vendor stack deep-dive (model -> hardware)
│   └── AMD-AI-STACK.md             # vendor stack deep-dive (model -> hardware)
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
|---|---|
| **T** | **The baseline** — what ML actually is, the training loop, the vocabulary, why these four maths branches, the ten-week arc, the standard, your starting scorecard |
| **S** | How to read the maths — Greek letters, `Σ`, indices, set notation, logarithms from scratch |
| **R** | Class 10 refresher + a 12-question prerequisite check |
| **0–7** | Setup · Python · NumPy · Linear algebra · Calculus · Optimisation · Information theory · Advanced |

There is an hour-blocked **5-day plan** at the top of the file (~12–13 hrs/day), with 8-day and
15-day alternatives at lower intensity. Nothing is cut at any pace — only the calendar changes.

| Day | Covers |
|---|---|
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
|---|---|
| §2.17 NumPy | 25 |
| §3.40 Linear algebra | 30 |
| §4.17 Calculus | 30 |
| §5.15 Optimisation | 25 |
| §6.9 Information theory | 22 |
| §3.41 + §6.10 quizzes | 90 questions |

Remaining work is listed in "What is still being added" at the end of the textbook.
