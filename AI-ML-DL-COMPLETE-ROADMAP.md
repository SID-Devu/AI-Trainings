# AI / Machine Learning / Deep Learning Engineering Programme

## A Complete Ten-Week Structured Curriculum

**Document type:** Training curriculum specification
**Duration:** 10 weekly modules (approximately 2.5 months), plus a defined post-programme conversion
phase (Section 10.16) and an optional model-to-hardware specialisation track (Section 10.17)
**Delivery mode:** Self-paced or cohort-based
**Prerequisite:** Working knowledge of Python syntax
**Target:** Undergraduate entry to machine learning roles at large technology and semiconductor
organisations
**Version:** 2.2 · 2026-08-30

---

### Revision log — version 2.2 (structure)

**This revision moved content; it did not remove any.** The document was flattened from sixteen
top-level Parts into **four top-level sections** — Title, Contents, Overview, Weekly Modules — and
the curriculum was consolidated from eleven weekly modules to **ten**.

| Change | Detail |
|---|---|
| **Four top-level sections** | Everything now sits under Title, Contents, Overview or Weekly Modules |
| **Overview** | Absorbs the former Parts 0, 1, 3, 4, 11 and 12 as sections A–F |
| **Eleven weeks → ten** | The two mathematics modules merged into **Week 1**, which is therefore double weight. Old Weeks 3–11 became Weeks 2–10, one for one |
| **Reference Parts folded into weeks** | Advanced mathematics → 1.18 · research literacy → 7.9 · ethics reference → 9.9 · interview preparation → 10.13 · career tracks → 10.14 · professional skills → 10.15 · conversion phase → 10.16 · model-to-hardware track → 10.17 · programme close → 10.18 |
| **Cross-references updated** | All week references, section references and Part references were remapped to the new structure |

**Nothing was deleted.** Line-for-line, every topic, resource, table, assessment question, artefact
and caveat present before this revision is present after it. The restructure was performed by moving
blocks rather than by retyping them, so no content could be lost in transit.

Sections 10.13 to 10.17 keep their original internal numbering (8.x, 9.x, 13.x, 14.x), because those
numbers are referenced extensively inside those blocks. See the note at the end of the Contents.

---

### Revision log — version 2.0

Version 1.0 was audited in full against the stated target. The audit found six internal defects and
five structural content gaps. All are resolved in this version, within the original 11-week
envelope; the room was created by demoting lower-value material rather than by extending the
timeline. Changes are summarised in Section 0.7.

**Link verification status.** Two links were fetched and checked during this revision:
`coursera.org/learn/machine-learning` (confirmed live, but it resolves to *Supervised Machine
Learning: Regression and Classification* — course 1 of 3 in the Machine Learning Specialization, not
the original standalone course; the label has been corrected) and `arxiv-sanity.com` (**did not
respond**; flagged in Overview E). All other links in this document are carried over or added without
individual verification and should be treated as unverified.

### About this document

This curriculum consolidates a complete Artificial Intelligence, Machine Learning and Deep Learning
engineering pathway into a single specification, covering foundations through advanced production
and performance engineering.

Content has been consolidated from the following sources:

1. *30-Week AI/ML Engineer Roadmap (4 Hours Daily)* — mahi community, 102 pages. All topics,
   subtopics, learning resources, practice tasks, assessment questions and projects from this source
   are preserved in full within this document.
2. A GPU performance, profiling and inference-optimisation track, added because the source material
   does not address it and it represents a primary hiring criterion at hardware, semiconductor and
   AI-infrastructure organisations.
3. An MLOps and deployment module, added to close a structural gap in the source material
   (see Section 0.6).
4. A continuous data structures and algorithms track, added because the source lists coding
   interviews as a requirement without providing preparation for them.
5. A recommender systems and ranking track (Week 8, Track D), added because ranking and retrieval
   are the largest single machine learning application area at consumer-scale technology
   organisations and were absent entirely.
6. Reinforcement learning foundations (Week 8, Track C), added because the source names RLHF and DPO
   without the underlying material required to understand either.
7. A continuous computer science fundamentals track (operating systems and computer architecture),
   added because Section 10.13 assessed these topics without teaching them anywhere.
8. An ML system design track with written deliverables (Week 9, Part D), added because system
   design is a distinct interview round and the source treated it as a four-line list.

Every module concludes with a **Real-World Applications and Industry Use Cases** section mapping the
material to production systems, commercial outcomes and the engineering roles that depend on it.

---

# CONTENTS

The document has four sections: **Title**, **Contents**, **Overview**, and **Weekly Modules**.
Everything the programme contains lives in one of them. Nothing is stored outside this structure.

## OVERVIEW — programme-level material

| | Section | Contains |
|---|---|---|
| **A** | Programme scoping, depth tiers and target lanes | Time budget · depth tiers ([BUILD] / [KNOW] / [AWARE]) · daily structure · operating principles · learning outcomes · source-material gaps · version audit · the two target lanes |
| **B** | Environment setup and continuous tracks (Week 0) | Philosophy · environment configuration · accounts · compute · tooling · repository structure · the three continuous tracks (algorithms, CS fundamentals, research literacy) |
| **C** | Project catalogue and portfolio artefacts | Beginner, intermediate and advanced practice projects · the register of all 19 portfolio artefacts and their priority order by lane |
| **D** | Tools and libraries | The full stack, by category |
| **E** | Master resource index | Courses, texts, channels, documentation, datasets, research sources |
| **F** | Assessment and tracking | Weekly progress record · artefact register · depth-tier audit · coverage checklist · readiness gate |

## WEEKLY MODULES — the ten-week curriculum

| Wk | Module | Sections |
|---|---|---|
| **1** | **Mathematics Foundations** *(double weight — merged module)* | 1.1–1.8 linear algebra, NumPy, Python engineering · **1.9–1.17** calculus, optimisation, information theory · **1.18** advanced mathematics (research tier) |
| **2** | Probability, Statistics, Discrete Mathematics and Data Handling | 2.1–2.8 · includes experimentation and A/B testing, graph theory, pandas, SQL foundations |
| **3** | Machine Learning Foundations and Supervised Learning | 3.1–3.7 |
| **4** | Unsupervised Learning, Model Selection and Tuning | 4.1–4.7 |
| **5** | Neural Network Fundamentals and PyTorch | 5.1–5.7 |
| **6** | Training Techniques, Optimisers and Convolutional Networks | 6.1–6.7 |
| **7** | Sequence Models and Transformer Architectures | 7.1–7.8 · **7.9** research literacy |
| **8** | Specialisation Tracks: NLP, Vision, Generative AI, Ranking, RL | 8.1–8.8 · Tracks A–D |
| **9** | MLOps, Deployment, Data Engineering, System Design and Responsible AI | 9.1–9.8 · **9.9** ethics expanded reference |
| **10** | **Systems, GPU Performance, Inference Optimisation and Career Conversion** | 10.1–10.12 systems and GPU performance · **10.13** interview preparation · **10.14** career tracks · **10.15** professional skills · **10.16** conversion phase · **10.17** model-to-hardware track (Stages 1–6) · **10.18** programme close |

**Two notes on reading this document.**

*Weeks 1 and 10 are the heavy modules.* Week 1 merges the two mathematics modules; Week 10 carries
the systems material plus everything that follows the taught curriculum. Weeks 2–9 map one-to-one
onto a single week of work.

*Sections 10.13 to 10.17 retain their own internal numbering* (8.x, 9.x, 13.x, 14.x) from before the
consolidation, because those numbers are referenced extensively within and between those blocks.
Section 10.17, for example, contains Stages numbered 14.1 to 14.9. The parent number tells you where
the block sits; the internal numbers are self-consistent within it.

---

# OVERVIEW

## A. Programme scoping, depth tiers and target lanes

### 0.1 Time budget and honest scoping

| Commitment | Total hours over 10 weeks |
|---|---|
| 4 hours/day, 7 days/week | 280 hours |
| 6 hours/day, 7 days/week | 420 hours |
| 8 hours/day, 7 days/week (full-time) | 560 hours |
| Original 30-week source plan at 4 hrs/day | 840 hours |

The compression from 840 hours to 280–560 is real and is addressed explicitly rather than concealed.
No topic from the source material has been removed. Instead, every topic is assigned a **depth tier**
that governs how deeply it is treated within the 10-week window. Topics assigned the lowest tier
remain fully documented here, with their resources, and form the post-programme backlog.

> **Note on Week 1 (v2.2).** The programme was consolidated from eleven modules to ten by merging
> the two mathematics modules — linear algebra and calculus/optimisation/information theory — into a
> single **Week 1**. No content was removed in that merge; Week 1 is therefore a **double-weight
> module** and should be expected to take roughly two weeks at 4 hrs/day, or one week at
> full-time intensity. Its two halves are marked in the module itself. Every other module maps
> one-to-one onto its predecessor.

A curriculum claiming complete mastery of this scope in 10 weeks would not survive contact with a
technical interview. This one does not make that claim. Section 0.5 states the realistic outcome.

**The 10-week boundary and what lies beyond it.** Ten weeks is sufficient to build the knowledge
and the portfolio. It is arithmetically insufficient to also complete the interview volume required
by large technology organisations — principally the algorithmic problem count, which cannot be
compressed below roughly 150 problems without accepting a materially lower pass rate. This version
therefore separates two things the source material conflated:

| Phase | Duration | Purpose | Location |
|---|---|---|---|
| **Programme** | 10 weeks | Knowledge and portfolio construction | Overview + Weekly Modules |
| **Conversion** | 4–6 weeks | Interview execution and applications | **Section 10.16** |

The conversion phase is not optional padding. For a candidate whose objective is an offer rather
than a certificate, it is the phase in which the offer is actually won, and it is scheduled here
rather than left as the source material's undefined "intensively thereafter".

### 0.2 Depth tiers

| Tier | Definition | Completion test |
|---|---|---|
| **[BUILD]** | Implemented from first principles in code, and working | Can be reproduced on a blank page |
| **[KNOW]** | Mechanism understood; explainable in interview; library usage fluent | Can be taught to a peer in five minutes |
| **[AWARE]** | Term recognised; the problem it solves and its relevance understood | Will not cause a blind spot in technical discussion |

A **[BUILD]** topic is not complete without working code. A **[KNOW]** topic is not complete because
a video was watched.

### 0.3 Daily structure

| Block | 4 hr/day | 6 hr/day | Purpose |
|---|---|---|---|
| Theory | 0.5 hr | 1.0 hr | Video, book, documentation |
| **Implementation** | 2.0 hr | 3.5 hr | Writing code — the primary learning mechanism |
| **Data structures and algorithms** | 1.0 hr | 1.0 hr | Eight to ten problems per week |
| Review, notes, CS fundamentals | 0.5 hr | 0.5 hr | Restating concepts; operating systems and architecture reading |

Where time is constrained, the theory block is reduced. The implementation block is not.

**Revised in version 2.0.** The algorithms block was previously 0.5 hr/day at three to five problems
per week, which yields 33–55 problems across the programme against a stated target of 150–200 — a
shortfall of roughly three to four times, silently deferred to an unscheduled period. The block is
now 1.0 hr/day at eight to ten problems per week, delivering approximately 110 problems within the
programme, with the balance scheduled explicitly in Section 10.16. The additional half-hour was taken from
the theory block in both columns, consistent with Operating Principle 1. Total daily hours are
unchanged.

### 0.4 Operating principles

1. **Implementation over consumption.** A tutorial watched is not a skill acquired.
2. **Public delivery each week.** Work not committed to a public repository does not constitute
   evidence.
3. **Restatement in plain language.** A concept that cannot be explained simply is not understood.
4. **Measurement over assertion.** Performance claims require numbers and a reproducible method.
5. **Depth over breadth.** One thoroughly understood project outweighs ten tutorials.
6. **Sequential completion.** Partial understanding compounds into confusion downstream.
7. **Time-boxed debugging.** After 45 minutes without progress, change approach — read the source,
   search the error, escalate.

### 0.5 Learning outcomes

On completion, a participant will be able to:

- Derive and implement backpropagation without a framework
- Build, train and evaluate convolutional and transformer architectures from published papers
- Apply classical machine learning to tabular problems with statistically honest evaluation
- Build a two-stage retrieval-and-ranking system and evaluate it with ranking metrics
- Explain the reinforcement learning formulation underlying RLHF and DPO
- Fine-tune and serve large language models, including retrieval-augmented pipelines
- Containerise, deploy, monitor and document a model in production form
- Produce a written ML system design under interview conditions
- Profile a model, identify the bottleneck class, and optimise inference with measured evidence
- Present **eleven portfolio artefacts** with reproducible results, plus a merged open-source
  contribution

**Realistic positioning:** internship-ready and junior-engineer-ready. This programme does not
produce senior engineers and does not represent itself as doing so.

**A necessary distinction.** Completing the 10 weeks produces a *qualified candidate*. Converting
that into an offer at a large technology or semiconductor organisation additionally requires the
algorithmic volume, system design repetitions, mock interviews and application timing set out in
Section 10.16. Candidates who complete the Overview and Weekly Modules and skip Section 10.16 are, in the author's assessment, the
most common failure profile: strong portfolio, failed coding screen.

### 0.6 Gaps identified in source material

Established by reading all 102 pages of the source document.

> **Verification notice (added in v2.0).** The 102-page source document is not distributed with this
> curriculum and was not available for re-inspection during the version 2.0 audit. The four claims
> in the table below are therefore **UNVERIFIED** as of this revision: they are carried over from
> version 1.0 in good faith but cannot be independently confirmed from the materials at hand.
> The resolutions listed in the right-hand column *are* verifiable, because they exist in this
> document.

| Gap | Evidence (unverified) | Resolution (verifiable) |
|---|---|---|
| **Week 23 absent** | The document sequences Week 22 directly to Week 24. "Stage 5 — MLOps" appears in the final checklist without a corresponding module. | Addressed in Week 9 |
| **No GPU or performance content** | No coverage of profiling, roofline analysis, memory bandwidth, kernel authoring, quantisation, ONNX, TensorRT or MLPerf anywhere in the document | Addressed in Week 10 |
| **No DSA preparation** | Coding interviews listed as a requirement in Week 25 without supporting material | Addressed as a continuous track, and scheduled in Section 10.16 |
| **No code or deliverables** | The document enumerates topics but does not specify what is to be built | Every module now terminates in a deliverable |

### 0.7 Version 2.0 audit — defects corrected and gaps closed

The version 1.0 document was audited line by line against its stated target. Findings and
resolutions:

#### Internal defects corrected

| # | Defect in v1.0 | Correction |
|---|---|---|
| 1 | Week 10 was headed "Portfolio artefacts 7 and 8" but listed **three** deliverables; the profiling study appeared in neither artefact register | Week 10 now declares artefacts 9, 10 and 11, and the profiling study appears in both registers |
| 2 | "Eight portfolio artefacts" was asserted in three places while the registers numbered nine rows and the weekly modules produced ten items — the count did not close | Artefact count is now stated once, consistently: **eleven weekly artefacts plus one open-source contribution** |
| 3 | Mixed precision was stated as delivering "approx. 2× throughput" as a flat fact, contradicting the roofline material later in the same document | Claim now qualified by bottleneck class and hardware, and cross-referenced to Week 10 |
| 4 | The Andrew Ng resource was labelled "Machine Learning"; the link resolves to course 1 of 3 of the Machine Learning Specialization (verified by fetch) | Label corrected; course 3, which covers reinforcement learning and recommenders, is now linked separately |
| 5 | Section 0.6 asserted specific facts about a source document not available for inspection | Marked UNVERIFIED above |
| 6 | arXiv Sanity was listed as a working resource; it did not respond when fetched | Flagged as unverified in Overview E |

#### Structural gaps closed

| Gap in v1.0 | Consequence for the stated target | Resolution |
|---|---|---|
| **Algorithms volume under-scheduled 3–4×** | The highest-variance filter for an undergraduate candidate was deferred to an undefined period | Section 0.3 rebalanced; Section 10.13.1 rewritten; Section 10.16 added |
| **Recommender systems and ranking absent** | No two-tower retrieval, learning-to-rank, ranking metrics, calibration or position bias — the largest ML application area at consumer-scale organisations | **Week 8, Track D** added, with a portfolio artefact |
| **Reinforcement learning absent** | RLHF and DPO were named without MDPs, policy gradients or PPO, making the claimed understanding unsupportable | **Week 8, Track C** extended with RL foundations |
| **ML system design had no depth and no artefact** | A dedicated interview round was covered in four lines, and *Designing Machine Learning Systems* was listed but never assigned | **Week 9, Part D** added, with written design deliverables |
| **CS fundamentals assessed but never taught** | Section 10.13 required operating systems and architecture; no resource for either appeared in the document | **Continuous track** added in Section 1.7 |
| **AMD/ROCm and C++ under-specified** | CUDA was taught "at concept level" with no HIP, ROCm libraries or reading-level C++, narrowing the accessible role surface | **Week 10, Parts B, E and H** extended |
| **Inference topics missing from the differentiating module** | No speculative decoding, GQA/MQA, MoE, or online-softmax numerics — the last being required by the Triton kernel the module asks for | **Week 10, Parts B and D** extended |
| **Experimentation, LLM security, GNNs, early SQL** | Assessed or production-relevant topics with no coverage | Added to Weeks 2, 8 and 9 |

### 0.8 Two target lanes — routing decision

*Added in v2.1, after the target was specified as **both** large consumer technology organisations
**and** semiconductor organisations, spanning model through to hardware.*

These two targets share a foundation and then diverge sharply. They are not the same preparation, and
attempting both at equal depth produces a candidate who is competitive for neither. The shared core is
substantial — Weeks 1 through 7 and the continuous tracks are common to both — after which the lanes
separate.

| | **Lane A — Product and applied ML** | **Lane B — Model-to-hardware / framework** |
|---|---|---|
| **Typical employers** | Large consumer technology and platform organisations | Semiconductor vendors, accelerator and cloud-infrastructure providers, framework teams |
| **Representative roles** | ML Engineer, Ranking/Search Engineer, Applied Scientist, MLOps Engineer | Model Enablement Engineer, Framework Integration Engineer, Inference/Performance Engineer, Kernel Engineer, ML Systems Engineer |
| **The question you are hired to answer** | "Does this model improve the product, and can we prove it?" | "Does this model run correctly and fast on this silicon, and can you prove it?" |
| **Shared core** | Weeks 1–7, continuous tracks (Section 1.7), Section 10.13, Section 10.16 | Identical |
| **Lane-specific depth** | Week 8 Track D (ranking) · Week 2 Part B2 (experimentation) · Week 9 Parts A–D (MLOps and system design) | **Week 10 in full** · **Section 10.17 in full** (framework internals, compiler stack, ROCm/HIP, distributed training, model bring-up, edge and NPU) |
| **Differentiating artefacts** | 1, 5, 6, 7, 8 | **9, 10, 11, and 12–19** |
| **Language** | Python throughout | Python primary, **reading-level C++ required**, HIP/CUDA reading required |
| **The rare skill** | Honest evaluation and offline/online reasoning | Diagnosing where in the stack a problem lives, and fixing it at the right layer |

**Lane B has two sub-paths**, and they are worth distinguishing because they need different hardware
and lead to different teams:

| | **B1 — Datacentre** | **B2 — Client, edge and NPU** |
|---|---|---|
| **Silicon** | Datacentre GPUs and accelerators | NPUs and integrated GPUs in laptops, phones, vehicles, embedded devices |
| **Stack** | ROCm, HIP, distributed training, serving at scale | ONNX Runtime execution providers, LiteRT, ExecuTorch, vendor NPU toolchains |
| **Binding constraint** | Throughput and cost per token | Power, thermal envelope, and whether the graph fits the accelerator at all |
| **Section 10.17 stages** | 1, 2, **3, 4**, 5 | 1, 2, **6**, and 5's methodology |
| **Artefacts** | 14, 15, 16, 17 | **18, 19** |
| **Hardware barrier** | High — needs real datacentre parts | **Low — a laptop, a phone, or a hosted device service** |

Both AMD and Qualcomm staff substantial organisations on the B2 side. **If accelerator access is your
constraint, start at B2**: artefact 18 requires only hardware you already own, and every skill in
Stage 6 — execution providers, partitioning, quantisation, disciplined measurement — transfers
directly upward into B1.

#### How to use the two lanes

**Both lanes complete Weeks 1–10.** The difference is the weighting, and what happens after Week 10.

- **Lane A** treats Week 10 at the depth written (profiling, one Triton kernel, one inference study)
  and does not enter Section 10.17. This is sufficient: product ML roles assess performance awareness, not
  performance engineering.
- **Lane B** treats Week 8 Tracks A, B and D at [KNOW] rather than [BUILD] — survey them, build none
  of them — and reinvests that time in Week 10 and then in **Section 10.17**, which is the lane's real
  content and does not fit inside ten weeks.
- **A candidate genuinely pursuing both** should complete the shared core, then Lane B, then add
  artefact 6 (ranking) from Lane A. Lane B's material is harder to acquire independently and is held
  by far fewer applicants, so it is the correct thing to be deep in if you can only be deep in one.
  Ranking can be added on top; the reverse is much harder.

**Honest scoping for Lane B.** Section 10.17 is a further eight to twelve weeks of work beyond the
programme. It is presented as a distinct Part rather than compressed into Week 10 because pretending
otherwise would repeat exactly the defect this document's own audit identified in Section 0.7 — a
requirement stated without a schedule attached to it.

#### Content demoted to create room

The additions above were funded, not appended. The following were compressed or demoted, on the
grounds of low return against the stated target: research-tier advanced mathematics (Section 1.18), set
theory and Boolean algebra (Week 2, Part C), low-tier calculus topics (Week 1, Part A), the tutorial
tier of the project catalogue (Overview C), duplicated ethics reference material (Section 9.9), leadership and
Agile process content (Section 10.15), historical CNN architectures, recurrent network gate-level detail,
classical NLP and image-processing techniques, and second-framework (TensorFlow/Keras) coverage.
Nothing was deleted outright; demoted material retains its tier marking and its resources.

---

## B. Environment setup and continuous tracks (Week 0)

Completed before Week 1. Estimated duration: three to four hours. A defective environment surfaces
as lost time in Week 5.

### 1.1 Programme philosophy

The source document opens with an observation worth preserving:

> Most students fail not because AI is hard. They fail because they start the wrong way — following
> courses without clarity or direction, accumulating certificates in place of understanding.

The corrective principle underpinning this curriculum: **advance past a topic only once it is
genuinely understood**, and demonstrate that understanding by building something that works.

### 1.2 Environment configuration

```bash
# Python 3.11+ recommended (3.13 supported; some ML libraries lag the newest release)
python --version

# Virtual environment — one per project, without exception
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

# Core stack
pip install numpy pandas matplotlib seaborn scikit-learn jupyter pytest
pip install torch torchvision            # select the CUDA/ROCm build at pytorch.org
pip install xgboost lightgbm
pip install transformers datasets peft accelerate
pip install opencv-python nltk spacy
pip install fastapi uvicorn streamlit
```

### 1.3 Required accounts

GitHub · Kaggle · Hugging Face · Google Colab · Weights & Biases · LeetCode · LinkedIn ·
Medium or Hashnode. All free tier.

### 1.4 Compute provisioning

| Option | Cost | Applicable modules |
|---|---|---|
| Local CPU | Free | Weeks 1–4, all classical machine learning |
| Google Colab | Free tier with GPU | Weeks 5–8, majority of deep learning |
| Kaggle Notebooks | Free, 30 GPU hours/week | Deep learning training, competitions |
| Cloud spot instances | Approx. $0.20–1.00/hour | Week 10 profiling, extended training runs |

Dedicated GPU hardware is not a prerequisite for completing this programme.

### 1.5 Engineering tooling

- **Git** — commit, branch, merge, rebase, pull request workflow
- **Linux CLI** — ssh, shell fundamentals, file operations, `htop`, `nvidia-smi` / `rocm-smi`
- **Docker** — image build and run. All production ML deployment is containerised.
- **IDE** — integrated debugger in place of print-statement debugging, notebook integration

### 1.6 Repository structure

```
ai-engineering-programme/
├── README.md          # public progress log, updated weekly
├── week01/ ... week11/
├── projects/
└── notes/
```

This repository constitutes the participant's portfolio. It begins empty and concludes as the
primary hiring artefact.

### 1.7 Continuous tracks

Three tracks run in parallel with the weekly modules from Week 1 to Week 10. They are not modules
and have no single week; they are habits with weekly quotas, audited in the Overview F progress record.

#### Track 1 — Data structures and algorithms — [BUILD]

Eight to ten problems per week, one hour per day. Full topic sequence and weekly allocation in
Section 10.13.1. This is the single highest-weight interview component for an undergraduate candidate and
the one most commonly under-resourced.

#### Track 2 — Computer science fundamentals — [KNOW]

*Added in v2.0. Section 10.13.5 previously assessed these topics without any module or resource teaching
them.*

Thirty minutes per day, within the review block. Two texts, read in parallel with the modules rather
than ahead of them:

| Area | Topics | Resource |
|---|---|---|
| **Operating systems** | Processes versus threads · scheduling · virtual memory and paging · concurrency, locks and race conditions · file systems · I/O | *Operating Systems: Three Easy Pieces* (Arpaci-Dusseau), free: https://pages.cs.wisc.edu/~remzi/OSTEP/ |
| **Computer architecture and systems** | Memory hierarchy and cache behaviour · locality · instruction-level parallelism · linking and loading · numerical representation · performance measurement | *Computer Systems: A Programmer's Perspective* (Bryant and O'Hallaron): https://csapp.cs.cmu.edu |
| **Networking** — [AWARE] | TCP versus UDP · HTTP and gRPC · latency versus bandwidth · load balancing | Any standard introduction; depth is not required |

**Why this track exists for this target.** Cache behaviour and the memory hierarchy are the
conceptual prerequisites for the roofline model in Week 10 — a candidate who has not internalised
why locality matters on a CPU will not reason correctly about it on a GPU. Concurrency and the
process/thread distinction are assessed directly in interviews at semiconductor and infrastructure
organisations. The recommended reading order is CS:APP chapters on the memory hierarchy **before**
Week 10, and OSTEP concurrency **before** Week 9.

**Completion test.** Explain, without notes, why a strided array traversal can be an order of
magnitude slower than a contiguous one, and what changes if the stride exceeds a cache line.

#### Track 3 — Research literacy — [KNOW]

One publication per week from Week 5 onward, methodology in Section 7.9. Reading list in Section 7.9.

---

## C. Project catalogue and portfolio artefacts

> **Compressed in v2.0.** Sections 3.1 to 3.3 are **optional practice**, not portfolio material.
> Version 1.0 presented them alongside the artefact list with equal prominence, which invites a
> genuine strategic error: these are tutorial-tier projects with thousands of near-identical public
> implementations, and a reviewer assigns them close to zero weight. The document's own standard,
> stated at the end of this Part, is the correct one — *a project without measured results is a
> tutorial*.
>
> **The eleven artefacts in Section 3.4 are the portfolio.** Use 3.1–3.3 only to practise a technique
> in isolation, or where an artefact prerequisite needs rehearsal. Do not substitute them for an
> artefact, and do not list them on a CV above the artefacts.

### 3.1 Beginner projects

| Project | Algorithms | Concept focus | Industry parallel |
|---|---|---|---|
| **House Price Prediction** | Linear Regression | Regression, feature selection, MSE and R² | Property valuation, mortgage underwriting |
| **Titanic Survival Prediction** | Logistic Regression, Decision Tree | Classification, feature importance | Risk scoring, triage prioritisation |
| **MNIST Digit Classification** | MLP, CNN | Image classification, neural network workflow | Cheque processing, form digitisation, postal automation |
| **Spam Email Classifier** | TF-IDF, Logistic Regression | Text features, binary classification | Email security, content moderation |

### 3.2 Intermediate projects

| Project | Technology | Concept focus | Industry parallel |
|---|---|---|---|
| **Face Recognition System** | CNN, OpenCV | Feature extraction, detection versus recognition | Access control, device authentication |
| **Chatbot System** | RNN, Transformer | Sequence processing, contextual response | Customer support automation |
| **Movie Recommendation** | Collaborative filtering, cosine similarity | User and item similarity | Streaming and e-commerce personalisation |
| **Sentiment Analysis** | Word embeddings, LSTM | Text representation, sequence learning | Brand monitoring, review analytics |

### 3.3 Advanced projects

| Project | Deep learning applied | Concept focus | Industry parallel |
|---|---|---|---|
| **Image Caption Generator** | CNN + LSTM | Vision-language combination | Accessibility tooling, media asset tagging |
| **Object Detection** | YOLO, SSD | Localisation, bounding boxes, real-time inference | Autonomous systems, retail analytics, safety monitoring |
| **Text Summarisation** | Transformer, BART, T5 | Sequence-to-sequence, context modelling | Legal review, clinical documentation, news aggregation |
| **Fake News Detection** | BERT, DistilBERT | Contextual understanding, transfer learning | Platform integrity, information verification |
| **Time Series Forecasting** | LSTM, ARIMA | Sequential prediction, trend and seasonality | Demand planning, energy load forecasting, capacity management |

### 3.4 Portfolio artefacts

**Eleven weekly artefacts, plus one open-source contribution.** *Corrected and extended in v2.0: the
v1.0 catalogue numbered nine rows while the modules produced ten items, and the Week 10 profiling
study was absent. Two artefacts were added (ranking system, system design portfolio).*

| # | Artefact | Module | Demonstrates | Compute cost |
|---|---|---|---|---|
| 1 | End-to-end tabular ML project | Week 4 | Applied ML judgement and honest evaluation | Low |
| 2 | NumPy backpropagation with PyTorch port | Week 5 | Foundational understanding beyond API usage | Low |
| 3 | ResNet reproduced from publication | Week 6 | Research-to-implementation capability | Medium |
| 4 | Mini-GPT from scratch | Week 7 | Command of the dominant architecture | Medium |
| 5 | LoRA fine-tune with RAG pipeline | Week 8 | Contemporary LLM engineering | Medium |
| **6** | **Two-stage retrieval and ranking system** *(new in v2.0)* | Week 8 | The dominant industrial ML application, evaluated honestly | Low |
| 7 | Deployed containerised API | Week 9 | Production delivery capability | Low |
| **8** | **ML system design portfolio (three designs)** *(new in v2.0)* | Week 9 | Structured design reasoning under a time limit | None |
| **9** | **Profiling study** *(previously unnumbered)* | Week 10 | Diagnostic capability on a real bottleneck | Low |
| 10 | Triton kernel with roofline benchmark | Week 10 | Systems and performance engineering | Low |
| 11 | Multi-backend inference study | Week 10 | Measurement discipline and optimisation judgement | Medium |
| — | Merged open-source contribution | Any | Peer-reviewed professional credibility | None |

#### Lane B artefacts — Section 10.17 *(added in v2.1)*

Not part of the ten-week programme. Required only for the model-to-hardware lane (Section 0.8).

| # | Artefact | Stage | Demonstrates | Hardware needed |
|---|---|---|---|---|
| 12 | Custom operator with full framework integration | 14.1 | You can extend a framework, not only use one | Any GPU |
| 13 | Compiler investigation report | 14.2 | You can explain and influence what the compiler did | Any GPU |
| 14 | Cross-vendor kernel port (CUDA → HIP) | 14.3 | Portability engineering; the core enablement skill | AMD preferred |
| 15 | AMD profiling and optimisation study | 14.3 | Vendor-stack fluency and measurement discipline | **AMD required** |
| 16 | Distributed training study (DDP versus FSDP) | 14.4 | Scaling measured honestly, with efficiency reported | Multi-GPU |
| 17 | **Model enablement report** | 14.5 | The job itself: bring-up, parity, coverage, attribution | **AMD required** |
| 18 | Cross-runtime edge deployment study | 14.6 | Runtime breadth and partitioning literacy | **Laptop and phone only** |
| 19 | **NPU quantisation and partitioning study** | 14.6 | Client AI engineering: accuracy under quantisation, NPU residency | NPU (Ryzen AI laptop or hosted Snapdragon) |

**Artefact 17 is the flagship of Lane B's datacentre path; artefact 19 is the flagship of its client
path.** Both are rare. Note the hardware column: **artefact 18 needs nothing you do not already own**,
which makes it the correct first Section 10.17 artefact for anyone without accelerator access.

**Documentation standard for every artefact:**
Problem → Data → Approach → Results (tabulated) → Alternatives considered → Reproduction instructions.

A project without measured results is a tutorial. A project with them is evidence.

**If time is short, this is the priority order.** The two additions in v2.0 are not filler; artefact 6
is the closest match to what consumer-scale organisations actually build, and artefact 8 is the
cheapest artefact in the list by compute while being the most directly predictive of a specific
interview round.

| Priority | Lane A — product and applied ML | Lane B1 — datacentre | Lane B2 — client, edge and NPU |
|---|---|---|---|
| **Essential** | 4, 6, 11 | 4, 11, **17** | 4, 11, **18, 19** |
| **High** | 1, 5, 8, 9 | 9, 10, **12, 14, 15** | 9, **12, 13** |
| **Valuable** | 2, 3, 7, 10 | 2, 3, **13, 16** | 2, 3, 7, **15** |
| **Survey only** | 12–19 not required | 1, 5, 6, 7, 8 at reduced depth | 1, 5, 6, 8, and Stages 3–4 |
| **Differentiating** | Open-source contribution | Open-source contribution — **weighted higher**, since reviewers in these projects are frequently employed by the target organisations | As B1; ONNX Runtime and the on-device runtimes are unusually approachable projects to contribute to |

Artefact 4 (mini-GPT from scratch) appears as essential in both lanes: for Lane A it demonstrates
command of the dominant architecture, and for Lane B it is the model every subsequent profiling,
compilation and enablement exercise is performed against.

---

## D. Tools and libraries

**Language** — Python

**Machine Learning and Deep Learning** — scikit-learn · XGBoost · LightGBM · **PyTorch** ·
TensorFlow and Keras [AWARE — *demoted in v2.0*]
*Learn one deep learning framework properly. PyTorch is the correct choice for this target: it is
dominant in research, in the LLM ecosystem, and in the semiconductor enablement work Week 10
addresses. Recognise TensorFlow and Keras syntax so that legacy code and older tutorials are
readable; do not divide implementation time between two frameworks.*

**Data Processing** — pandas · NumPy · Polars [AWARE] · SQL

**Visualisation** — Matplotlib · Seaborn · Plotly

**Computer Vision and NLP** — OpenCV · NLTK · spaCy · Hugging Face Transformers · datasets · tokenizers

**LLM and Generative AI** — peft · accelerate · bitsandbytes · vLLM · LangChain · LangGraph · FAISS · ChromaDB

**Deployment** — Flask · FastAPI · Docker · Streamlit · Gradio · ONNX Runtime · TensorRT

**Cloud and MLOps** — AWS and GCP · MLflow · Kubernetes · Weights & Biases · DVC · GitHub Actions

**Recommendation and ranking** *(added in v2.0)* — implicit · LightFM · FAISS · ScaNN [AWARE] ·
`torchrec` [AWARE]

**Performance** *(added)* — torch.profiler · Nsight Systems and Compute · rocprof · Omniperf ·
Triton · torch.compile

**Edge, client and NPU deployment** *(added in v2.1)* — ONNX Runtime and its execution providers
(VitisAI, QNN, MIGraphX, ROCm, OpenVINO, CoreML, DirectML, XNNPACK) · LiteRT · ExecuTorch ·
Windows ML · AMD Ryzen AI and AMD Quark · Qualcomm QAIRT/QNN and Qualcomm AI Hub · Netron
(graph inspection — indispensable for partitioning work)

**Engineering hygiene** *(added)* — git · pytest · ruff or black · pre-commit

**Databases** *(added in v2.0)* — SQLite or PostgreSQL for the Week 2 SQL track

#### Assessment questions
- Why does Python dominate the AI ecosystem?
- What distinguishes scikit-learn from PyTorch in application?
- Why do deployment tools matter? Why does experiment tracking matter?

#### Exercise
Produce a personal tool stack specification: selected ML framework, deployment stack and experiment
tracking tool, each with a one-sentence justification.

---

## E. Master resource index

### Primary courses and texts

| Resource | URL | Application |
|---|---|---|
| Andrej Karpathy — Zero to Hero | https://www.youtube.com/c/AndrejKarpathy | Deep learning from first principles |
| Dive into Deep Learning | https://d2l.ai | Comprehensive text with PyTorch implementations |
| Stanford CS231n | https://cs231n.stanford.edu | Computer vision |
| Stanford CS224n | https://web.stanford.edu/class/cs224n | Natural language processing |
| fast.ai | https://course.fast.ai | Applied deep learning, top-down |
| Hugging Face courses | https://huggingface.co/learn | NLP, LLM, diffusion |
| Mathematics for Machine Learning | https://mml-book.github.io | Mathematical foundations |
| Google ML Crash Course | https://developers.google.com/machine-learning/crash-course | Rapid ML introduction |
| Kaggle Learn | https://www.kaggle.com/learn | Applied practical modules |
| MIT OpenCourseWare | https://ocw.mit.edu | 18.06, 18.01, 18.05 |
| Khan Academy | https://www.khanacademy.org | Mathematical fundamentals |
| Andrew Ng — ML Specialization, course 1 | https://www.coursera.org/learn/machine-learning | **Verified by fetch.** Supervised learning only — linear and logistic regression. This is *not* the original standalone course, despite the URL |
| Andrew Ng — ML Specialization, course 3 | https://www.coursera.org/learn/unsupervised-learning-recommenders-reinforcement-learning | **Recommenders and reinforcement learning** — closes two v1.0 omissions; assigned in Week 8 |
| *Operating Systems: Three Easy Pieces* | https://pages.cs.wisc.edu/~remzi/OSTEP/ | **Added in v2.0** — Section 1.7 Track 2 |
| *Computer Systems: A Programmer's Perspective* | https://csapp.cs.cmu.edu | **Added in v2.0** — memory hierarchy, prerequisite for Week 10 |
| Google Rules of Machine Learning | https://developers.google.com/machine-learning/guides/rules-of-ml | **Added in v2.0** — applied ML judgement, ranking, experimentation |
| Google Recommendation Systems course | https://developers.google.com/machine-learning/recommendation | **Added in v2.0** — Week 8 Track D |
| OpenAI Spinning Up in Deep RL | https://spinningup.openai.com | **Added in v2.0** — Week 8 Track C |
| *Reinforcement Learning: An Introduction* | http://incompleteideas.net/book/the-book.html | **Added in v2.0** — chapters 1–3, 6, 13 only |
| ROCm documentation | https://rocm.docs.amd.com | **Added in v2.0** — Week 10 Section 10.3a |
| OWASP Top 10 for LLM Applications | https://owasp.org/www-project-top-10-for-large-language-model-applications/ | **Added in v2.0** — Week 8 Track C Topic 12 |
| NeetCode | https://neetcode.io | **Added in v2.0** — algorithm pattern lists, Section 10.13.1 |

### Video channels
3Blue1Brown · StatQuest · Andrej Karpathy · Yannic Kilcher · Krish Naik · freeCodeCamp · sentdex ·
Hugging Face · LangChain · Full Stack Deep Learning · DataTalksClub · TechWorld with Nana ·
NVIDIA Developer · AI Coffee Break · Two Minute Papers · Data Professor · Tina Huang ·
William Fiset · Neso Academy · IBM Technology

### Documentation
PyTorch https://pytorch.org/docs · scikit-learn https://scikit-learn.org ·
TensorFlow https://www.tensorflow.org · Hugging Face https://huggingface.co · NumPy · pandas ·
OpenCV https://opencv.org · NLTK https://www.nltk.org · spaCy https://spacy.io ·
LangChain https://docs.langchain.com · FAISS https://faiss.ai ·
OpenAI https://platform.openai.com/docs · Triton https://triton-lang.org ·
NVIDIA CUDA https://developer.nvidia.com/cuda-zone

### Practice and datasets
Kaggle https://www.kaggle.com · UCI ML Repository https://archive.ics.uci.edu ·
Google Colab https://colab.research.google.com · LeetCode https://leetcode.com ·
Devpost https://devpost.com · Zindi https://zindi.africa · StrataScratch · Codeforces

**Graded ML implementation practice** *(added in v2.3 — this closed a real gap)*

Until now this document had LeetCode for algorithms and Kaggle for end-to-end projects, but **no
source of graded, test-checked ML implementation exercises** — "implement scaled dot-product
attention and pass the tests." That is a distinct skill from both, and it was unresourced.

**TensorTonic** — https://www.tensortonic.com/study-plans (pricing verified 2026-09-02)

| Tier | Cost | What it gives |
|---|---|---|
| **Free** | $0 | 300+ core ML problems · **all 35 CUDA/GPU kernel problems** · 13 research-paper implementations · theory per problem · interactive visualisations · unlimited submissions · Discord |
| Pro | ~$8.33/mo, $100/yr | The structured study plans · 700+ problems · 500+ quiz questions · mock interviews |
| Plus | ~$14/mo, $168/yr | 850+ problems · modern LLM architectures in PyTorch · ML system design with a design canvas |

**How its plans map onto this programme:**

| Their plan | Problems | Our module |
|---|---|---|
| Linear Algebra · Calculus for ML · Optimization | 30 · 30 · 25 | **Week 1** (Parts 3, 4, 5) |
| NumPy Sheet | 25 | Week 1 Part 2 |
| Probability & Statistics · Pandas · SQL | 30 · 25 · 25 | **Week 2** |
| Cracking ML | 35 | Weeks 3–4 |
| PyTorch Sheet · Build Micrograd from Scratch | 30 · 25 | **Week 5** — the roadmap already names Karpathy's micrograd as the highest-value exercise in that module |
| Cracking Deep Learning · Cracking CV | 35 · 35 | Weeks 6, 8 |
| Build LLM from Scratch | 62 | Weeks 7–8 |
| Cracking NLP · Cracking RL | 35 · 30 | Week 8 Tracks A and C |
| **CUDA Kernels · Triton Kernels · Inference Engineering** | 35 · 30 · 30 | **Week 10 and Section 10.17** |
| ML System Design (Plus tier) | — | Week 9 Part D |
| Mock interview assessments | — | Section 10.16 |

**Guidance on using it.**

1. **It is practice, not teaching.** Attempting problems before understanding the material produces
   copied solutions and false confidence. Work the module first, then use the problems as a
   second pass — solve without notes to *verify* understanding.
2. **Do not pay early.** The free tier's 300+ problems exceed what you can consume before Week 5.
   Revisit the paid tiers only when the free problems genuinely run out, and decide with evidence
   that the platform suits you.
3. **The 35 free GPU/CUDA kernel problems are the standout item.** Practice material for kernel
   authoring is scarce, and this is the hardest part of Section 10.17 to rehearse. Note it now; use
   it at Week 10.
4. **It does not replace the artefacts.** A platform profile is invisible to a reviewer. The 19
   artefacts in Overview C are the hiring signal, because they are yours and they carry measured
   results. Solving 300 problems on a website is worth nothing you can point at.
5. **It does not replace the algorithms track.** Part 8.1's 150+ problems are data structures and
   algorithms — a different assessment, still required.

### Research
arXiv https://arxiv.org · Papers With Code https://paperswithcode.com ·
Distill.pub https://distill.pub ·
The Illustrated Transformer https://jalammar.github.io/illustrated-transformer/

> **arXiv Sanity** (`http://www.arxiv-sanity.com`) was listed in v1.0. It **did not respond** when
> fetched during the v2.0 audit. It is removed from the active list; a maintained successor may exist
> under a different address, but that has not been verified here. Papers With Code and arXiv's own
> subject feeds cover the same function.

### Commercial texts

| Text | Assigned to |
|---|---|
| *Hands-On Machine Learning* (Aurélien Géron) | Weeks 3–4, chapters 1–7 |
| *Designing Machine Learning Systems* (Chip Huyen) | **Weeks 9–10 — assigned in v2.0**; listed but never assigned in v1.0 |
| *Machine Learning System Design Interview* (Aminian and Xu) | Week 9, Part D |
| *Trustworthy Online Controlled Experiments* (Kohavi, Tang and Xu) | Week 2, Part B2 |
| *Operating Systems: Three Easy Pieces* (Arpaci-Dusseau) | Section 1.7, Track 2 |
| *Computer Systems: A Programmer's Perspective* (Bryant and O'Hallaron) | Section 1.7, Track 2 |
| *Reinforcement Learning: An Introduction* (Sutton and Barto) | Week 8, Track C — partial |
| Andrew Ng ML and Deep Learning Specialisations (Coursera) | Weeks 3, 5, 8 |

> **Link verification.** Two links in this document were fetched and checked during the v2.0 audit
> (Section "Revision log"). Every other link is **unverified**. Resource locations change over time;
> where a link fails, the exact title will generally locate the current address. Do not cite a link
> from this document as confirmed working without checking it.

---

## F. Assessment and tracking

### 12.1 Weekly progress record

*Extended in v2.0 with the DSA target column (the v1.0 record tracked problems solved without a
target to compare against, which is not a control) and the continuous-track columns.*

| Wk | Dates | Topics completed | Artefact delivered | DSA solved / target | CS fundamentals | Paper read | Mock | Blockers |
|---|---|---|---|---|---|---|---|---|
| **1a** | | | | / 8–10 | | — | — | |
| **1b** | | | | / 8–10 | | — | — | |
| 2 | | | EDA report | / 8–10 | | — | — | |
| 3 | | | Algorithm comparison | / 8–10 | | — | — | |
| 4 | | | Artefact 1 | / 8–10 | | — | — | |
| 5 | | | Artefact 2 | / 8–10 | | ☐ | — | |
| 6 | | | Artefact 3 | / 8–10 | | ☐ | — | |
| 7 | | | Artefact 4 | / 8–10 | | ☐ | ☐ | |
| 8 | | | Artefacts 5, 6 | / 8–10 | | ☐ | ☐ | |
| 9 | | | Artefacts 7, 8 | / 8–10 | | ☐ | ☐ | |
| 10 | | | Artefacts 9, 10, 11 | / 8–10 | | ☐ | ☐ | |
| **Programme total** | | | **11 artefacts** | **/ ≈110** | | **6** | **4** | |

*Week 1 is tracked as two rows (**1a** linear algebra, **1b** calculus and information theory)
because it is the merged double-weight module described in Section 0.1. The problem target is
per tracked row, so the cumulative figure is unchanged at approximately 110.*

### 12.2 Portfolio artefact register

*Corrected in v2.0: the v1.0 register omitted the Week 10 profiling study entirely, and its numbering
did not match the Week 10 module heading.*

| # | Artefact | Module | Status | Repository | Headline measured result |
|---|---|---|---|---|---|
| 1 | End-to-end tabular ML | 5 | ☐ | | |
| 2 | NumPy backpropagation with PyTorch port | 6 | ☐ | | |
| 3 | ResNet from publication | 7 | ☐ | | |
| 4 | Mini-GPT from scratch | 8 | ☐ | | |
| 5 | LoRA fine-tune with RAG | 9 | ☐ | | |
| **6** | **Two-stage retrieval and ranking system** | **9** | ☐ | | |
| 7 | Deployed containerised API | 10 | ☐ | | |
| **8** | **ML system design portfolio (three designs)** | **10** | ☐ | | |
| **9** | **Profiling study** | **11** | ☐ | | |
| 10 | Triton kernel with benchmark | 11 | ☐ | | |
| 11 | Multi-backend inference study | 11 | ☐ | | |
| — | Merged open-source contribution | Any | ☐ | | |

**Lane B additions — Section 10.17** *(v2.1; required for the model-to-hardware lane only)*

| # | Artefact | Stage | Status | Repository | Headline measured result |
|---|---|---|---|---|---|
| 12 | Custom operator with framework integration | 14.1 | ☐ | | |
| 13 | Compiler investigation report | 14.2 | ☐ | | |
| 14 | Cross-vendor kernel port (CUDA → HIP) | 14.3 | ☐ | | |
| 15 | AMD profiling and optimisation study | 14.3 | ☐ | | |
| 16 | Distributed training study (DDP vs FSDP) | 14.4 | ☐ | | |
| 17 | **Model enablement report** | 14.5 | ☐ | | |
| 18 | Cross-runtime edge deployment study | 14.6 | ☐ | | |
| 19 | **NPU quantisation and partitioning study** | 14.6 | ☐ | | |

The final column is not decorative. An artefact with no number attached to it is not finished, and
the number is what gets quoted in an interview. For artefacts 14 through 17, the column must also
record the **hardware and software configuration** the number was obtained on — an unattributed
performance figure is not a result (Section 14.5.4). For artefacts 18 and 19 this extends to device
model, driver and SDK version, thermal and power state, and whether the figure is cold or warm
(Section 14.6.8).

### 12.3 Depth tier audit (conducted at Week 10 close)

For each **[BUILD]** topic: does working, self-authored code exist?
For each **[KNOW]** topic: can it be explained to a peer in five minutes without reference?
For each **[AWARE]** topic: is the problem it addresses understood?

Topics failing their assigned tier constitute the post-programme backlog, which forms the basis of
the subsequent three to six months of development.

### 12.4 Curriculum coverage checklist

| Stage | Area | Complete |
|---|---|---|
| 1 | Classical Machine Learning | ☐ |
| 2 | Deep Learning | ☐ |
| 3 | Project Building | ☐ |
| 4 | NLP, Computer Vision, LLM or Generative AI specialisation | ☐ |
| 5 | MLOps — deployment, monitoring, scaling | ☐ |
| 6 | Competitive profile — Kaggle, GitHub, publication | ☐ |
| 7 | Interview and System Design | ☐ |
| 8 | Data Engineering | ☐ |
| 9 | Ethics, Bias, Privacy, Explainability | ☐ |
| 10 | Paper Reading and Research | ☐ |
| 11 | Advanced Mathematics (optional) | ☐ |
| 12 | Prompt Engineering and LLMOps | ☐ |
| 13 | ML Systems and Infrastructure Design | ☐ |
| 14 | Professional skills and domain knowledge | ☐ |
| **15** | **GPU performance, profiling, inference optimisation** *(added in v1.0 revision)* | ☐ |
| **16** | **Recommender systems, retrieval and ranking** *(added in v2.0)* | ☐ |
| **17** | **Reinforcement learning foundations and RLHF/DPO** *(added in v2.0)* | ☐ |
| **18** | **Online experimentation and A/B testing** *(added in v2.0)* | ☐ |
| **19** | **Computer science fundamentals — OS and architecture** *(added in v2.0)* | ☐ |
| **20** | **ML system design — written and presented** *(added in v2.0)* | ☐ |
| **21** | **Algorithms — 150+ problems and mock interviews** *(added in v2.0)* | ☐ |
| **22** | **Application mechanics — submitted within the window** *(added in v2.0)* | ☐ |

**Lane B additions — Section 10.17** *(v2.1)*

| Stage | Area | Complete |
|---|---|---|
| **23** | **Framework internals — dispatcher, autograd, allocator, streams** | ☐ |
| **24** | **Compiler and graph layer — capture, fusion, codegen, IR** | ☐ |
| **25** | **HIP and cross-vendor portability** | ☐ |
| **26** | **ROCm library stack and PyTorch-on-ROCm** | ☐ |
| **27** | **CDNA execution model and AMD profiling workflow** | ☐ |
| **28** | **Distributed training and collective communication** | ☐ |
| **29** | **Numerical parity, operator coverage, benchmarking discipline** | ☐ |
| **30** | **Model bring-up and enablement, end to end** | ☐ |
| **31** | **Merged upstream contribution to a framework or vendor repository** | ☐ |
| **32** | **ONNX Runtime execution providers and graph partitioning** | ☐ |
| **33** | **On-device runtimes — LiteRT, ExecuTorch, Windows ML** | ☐ |
| **34** | **NPU quantisation — QDQ, calibration, accuracy recovery** | ☐ |
| **35** | **Vendor client stacks — AMD Ryzen AI and Qualcomm QAIRT/QNN** | ☐ |
| **36** | **Client measurement — power, thermal, sustained, cold versus warm** | ☐ |

### 12.5 Readiness gate — before applying

*Added in v2.0.* The programme is complete when the Overview and Weekly Modules are done. **Readiness to interview is a
separate test**, and these are its criteria:

| Criterion | Threshold |
|---|---|
| Artefacts complete with measured results | 8 of 11 minimum, including artefacts 4, 6 and 11 |
| Algorithm problems solved | 110 minimum, with the pattern log complete |
| Medium problems solved in under 25 minutes while narrating | 8 in 10 |
| Mock interviews completed | 4 minimum |
| System designs presented aloud within 45 minutes | 3 minimum |
| Every artefact defensible in both 2-minute and 10-minute form | All |
| Each artefact has one honest weakness you can state unprompted | All |
| CV built on artefacts and numbers, not course completions | Yes |

**Lane B additions** *(v2.1)* — required only when targeting semiconductor, accelerator or framework
organisations:

| Criterion | Threshold |
|---|---|
| Descent map traced without notes, Python to hardware | Yes |
| Section 10.17 artefacts complete | 4 of 6 minimum, including artefact 17 |
| ROCm component names and NVIDIA counterparts recalled | All in the Section 10.3a table |
| Reading-level C++: can read a kernel and state what it does | Yes |
| Every performance number accompanied by full configuration disclosure | All |
| Merged upstream contribution | 1 minimum — weighted heavily in this lane |

Failing this gate does not mean not applying — application windows do not wait, and Section 10.16 exists to
be run in parallel with a live process. It means knowing accurately which part of the loop is the
current weakness, rather than discovering it during the loop.

---

# WEEKLY MODULES

| Wk | Module | Primary deliverable | Also contains |
|---|---|---|---|
| **1** | Mathematics: Linear Algebra, NumPy, Python Engineering **+** Calculus, Optimisation, Information Theory *(double weight)* | Linear regression in pure NumPy; gradient descent from first principles | Advanced mathematics (research tier) |
| 2 | Probability, Statistics, Discrete Mathematics, Data Handling, Experimentation, SQL | Statistical EDA report with pre-registered experiment design | — |
| 3 | ML Foundations and Supervised Learning | Seven-algorithm comparison study | — |
| 4 | Unsupervised Learning, Model Selection, Tuning | End-to-end tabular ML project *(artefact 1)* | — |
| 5 | Neural Network Fundamentals and PyTorch | NumPy backpropagation with PyTorch port *(artefact 2)* | — |
| 6 | Training Techniques, Optimisers, CNNs | ResNet reproduced from publication *(artefact 3)* | — |
| 7 | Sequence Models and Transformers | Mini-GPT implemented from scratch *(artefact 4)* | Research literacy |
| 8 | Specialisations: NLP, Vision, Generative AI, **Ranking**, **RL** | LoRA fine-tune with RAG; two-stage ranking system *(artefacts 5, 6)* | — |
| 9 | MLOps, Deployment, Data Engineering, **System Design**, Ethics | Containerised monitored API; written design portfolio *(artefacts 7, 8)* | Ethics expanded reference |
| **10** | Systems, GPU Performance, Inference, Career | Profiling study, kernel benchmark, inference study *(artefacts 9, 10, 11)* | Interview preparation · career tracks · professional skills · conversion phase · **model-to-hardware track (artefacts 12–19)** · programme close |

Continuous throughout: data structures and algorithms, computer science fundamentals, research
literacy (Section 1.7).

**Weeks 1 and 10 are the two heavy modules.** Week 1 carries the merged mathematics load; Week 10
carries the systems material plus everything that follows the taught curriculum — interview
preparation, career conversion, and the optional model-to-hardware specialisation track. Both are
signposted internally so the boundaries are clear.

---

## WEEK 1 — Mathematics Foundations: Linear Algebra, Calculus, Optimisation and Information Theory

### 1.1 Module objective

Establish complete conceptual and visual understanding of linear algebra, expressed throughout in
NumPy. Tensor shape reasoning is developed to fluency at this stage, as shape errors constitute the
majority of downstream deep learning defects.

### 1.2 Topics and subtopics

**1. Scalars, Vectors, Matrices, Tensors** — [BUILD]
Notation · Dimensions · Representation · Broadcasting concept

**2. Vector Operations** — [BUILD]
Addition · Subtraction · Scalar multiplication · Dot product · Cross product [AWARE — *demoted in
v2.0; near-zero relevance to machine learning practice*]

**3. Matrix Operations** — [BUILD]
Matrix addition · Matrix multiplication · Transpose · Identity matrix

**4. Matrix Inverses and Determinants** — [KNOW]
Inverse of matrix · Singular versus non-singular matrices · Determinant properties

**5. Linear Independence** — [KNOW]
Rank · Null space · Column space

**6. Systems of Linear Equations** — [AWARE — *demoted in v2.0*]
Gaussian elimination · Consistency of equations. Solve with `numpy.linalg.solve`; the hand method is
not assessed and consumes disproportionate time.

**7. Span and Basis** — [KNOW]
Basis vectors · Vector spaces

**8. Orthogonality** — [KNOW]
Orthogonal vectors · Vector projection · Gram-Schmidt process [AWARE]

**9. Eigenvalues and Eigenvectors** — [KNOW]
Eigendecomposition · Diagonalisation

**10. Matrix Factorisation** — [AWARE]
LU Decomposition · QR Decomposition. Recognition only.

**11. Singular Value Decomposition (SVD)** — [KNOW]
Concept · Low-rank approximation — *the mathematical basis of LoRA, revisited in Week 8*

**12. Principal Component Analysis (PCA)** — [BUILD]
Covariance matrix · Eigenvectors as principal axes

**Concurrent — Python engineering** — [BUILD]
Data model (`__init__`, `__call__`, `__getitem__`, `__iter__`) · decorators · generators ·
comprehensions · context managers · dataclasses · type hints · virtual environments · `pytest` ·
debugger-based diagnosis · `cProfile` and `timeit`

**Concurrent — NumPy** — [BUILD]
Arrays · dtypes · shape and reshape · broadcasting · indexing and slicing · views versus copies ·
vectorisation · `einsum` · axis semantics · seeded randomness

### 1.3 Learning resources

- 3Blue1Brown — *Essence of Linear Algebra*: https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
- Khan Academy — Linear Algebra: https://www.khanacademy.org/math/linear-algebra
- MIT OpenCourseWare 18.06: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- MIT practice problems: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/assignments/
- *Mathematics for Machine Learning*: https://mml-book.github.io

### 1.4 Practice tasks

- Identify scalars, vectors and matrices from worked examples
- Perform vector addition and dot product manually, then verify in NumPy
- Multiply matrices by hand step-by-step, then verify programmatically
- Observe matrix transformations visually
- **Shape-reasoning drill** *(added in v2.0)* — for twenty randomly generated shape pairs, state
  whether the operation broadcasts, matrix-multiplies, or raises, and why, before running the code.
  Repeat until the error rate is zero. Shape errors are the highest-frequency defect in Weeks 5–8.
- Produce written notes for each topic

### 1.5 Assessment questions

- What distinguishes a vector from a matrix?
- Why is the dot product significant in AI systems?
- Under what conditions is a matrix invertible?
- What information does rank convey?
- Why are eigenvalues central to PCA?
- How does linear algebra enable AI systems to process data?
- Given `A.shape == (32, 512)` and `B.shape == (512, 128)`, what is the shape of `A @ B`, and what
  fails if B is `(128, 512)`?

### 1.6 Deliverables

1. **Visual PCA explainer** — demonstrating data point transformation, eigenvector interpretation,
   and a written explanation in plain language.
2. **Linear regression via the normal equation** — `θ = (XᵀX)⁻¹Xᵀy` implemented in pure NumPy with
   no scikit-learn dependency, accompanied by `pytest` coverage.

### 1.7 REAL-WORLD APPLICATIONS AND INDUSTRY USE CASES

| Industry | Application | Role of this module's material |
|---|---|---|
| **Search and e-commerce** | Semantic product search, query matching | Vector embeddings with cosine and dot-product similarity form the core retrieval primitive. Every "similar items" feature reduces to a dot product over normalised vectors |
| **Streaming and media** | Recommendation engines | Matrix factorisation decomposes a sparse user–item interaction matrix into latent factors. SVD and low-rank approximation are the foundational technique |
| **Financial services** | Risk modelling, portfolio construction | Covariance matrices, eigendecomposition and PCA reduce hundreds of correlated instruments to a small number of orthogonal risk factors |
| **Computer vision and imaging** | Compression, denoising, feature extraction | Images are tensors. Convolution, colour-space transformation and compression are matrix operations; low-rank approximation underlies lossy compression |
| **Genomics and healthcare analytics** | Dimensionality reduction over high-dimensional assays | PCA reduces tens of thousands of gene-expression features to interpretable components before modelling |
| **Large language models** | Parameter-efficient fine-tuning (LoRA) | LoRA expresses weight updates as a product of two low-rank matrices — a direct application of Topic 11. It reduces trainable parameters by orders of magnitude and is why enterprise fine-tuning is economically viable |
| **Manufacturing and IoT** | Sensor fusion, anomaly detection | Projection and orthogonality separate signal subspaces from noise subspaces in multi-sensor telemetry |

**Commercial significance.** Every matrix multiplication in a production model consumes compute
budget. Understanding rank, sparsity and low-rank structure is what enables engineers to reduce
model size and inference cost without accuracy loss — a directly measurable saving at scale.

**Roles dependent on this module:** Machine Learning Engineer · Data Scientist · Computer Vision
Engineer · Quantitative Analyst · Search and Relevance Engineer · AI Performance Engineer

### 1.8 Completion criteria

Confident manipulation of vectors and matrices · ability to solve foundational linear algebra
problems · conceptual explanation of eigenvalues · understanding of dimensionality reduction via
PCA · established foundation for machine learning.

---

### 1.9 SECOND HALF — Calculus, Optimisation and Information Theory

### 1.10 Module objective

Establish how models learn. Backpropagation is an application of the chain rule; optimisers govern
descent; cross-entropy provides the scoring mechanism. These three constitute the learning loop of
every model in the remainder of the programme.

### 1.11 Topics and subtopics

**PART A — Calculus**

**1. Differentiation** — [BUILD] · Power rule · Product rule · Quotient rule · **Chain rule**
**2. Partial Derivatives** — [BUILD] · Multivariable functions · ∂f/∂x, ∂f/∂y
**3. Gradient Vectors** — [BUILD] · Gradient meaning · Direction of steepest ascent
**4. Jacobian and Hessian Matrices** — [KNOW] · First-order · Second-order · Curvature
**5. Backpropagation Algorithm** — [BUILD] · Chain rule application · Error minimisation logic
**6. Vector-Jacobian products** — [KNOW] *(added in v2.0)* · Why reverse-mode automatic
differentiation computes `vᵀJ` rather than materialising `J` · why this makes backpropagation
tractable for wide layers — *the mechanism behind `torch.autograd`, revisited in Week 5*

**Compressed in v2.0 — [AWARE], recognition only.** Limits and continuity · directional derivatives ·
Taylor series expansions · integration and area under curves. These consumed four numbered topic
slots in v1.0 at the lowest depth tier; they are grouped here to release time to the algorithms
track. Resources below still cover them.

**PART B — Optimisation**

**1. Objective and Loss Functions** — [BUILD]
Mean Squared Error (MSE) · Mean Absolute Error (MAE) · Cross-Entropy Loss · Hinge Loss

**2. Gradient Descent** — [BUILD]
Batch Gradient Descent · Stochastic Gradient Descent (SGD) · Mini-batch Gradient Descent · Momentum

**3. Learning Rate** — [BUILD] · Learning rate concept · Scheduling · Annealing
**4. Convex Functions** — [KNOW] · Global versus local minima · Convex optimisation basics
**5. Constrained Optimisation** — [AWARE] · Lagrange multipliers
**6. Stochastic Optimisation** — [KNOW] · SGD · Adam · RMSprop · Adagrad
**7. Second-order Optimisation** — [AWARE] · Newton's Method · Hessian Matrix · BFGS
**8. Regularisation Techniques** — [KNOW] · L1 (Lasso) · L2 (Ridge) · Dropout

**PART C — Information Theory**

**1. Entropy** — [BUILD] · Information content · Uncertainty measurement
**2. Cross Entropy** — [BUILD] · Classification loss function · Relation to entropy
**3. Kullback-Leibler (KL) Divergence** — [BUILD] · Difference between distributions
**4. Mutual Information** — [KNOW] · Shared information between variables
**5. Bits, Encoding and Compression** — [AWARE] · Shannon entropy · Huffman coding
**6. Perplexity** — [KNOW] · Language model evaluation metric

### 1.12 Learning resources

- 3Blue1Brown — *Essence of Calculus*: https://www.youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6
- Khan Academy — Calculus: https://www.khanacademy.org/math/calculus-1
- MIT OpenCourseWare 18.01: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/
- Paul's Online Math Notes: https://tutorial.math.lamar.edu
- StatQuest — Gradient Descent and Optimisation: https://www.youtube.com/c/joshstarmer
- Distill.pub — visual optimisation guides: https://distill.pub
- Google ML Crash Course: https://developers.google.com/machine-learning/crash-course

### 1.13 Practice tasks

- Differentiate elementary functions; apply chain rule problems
- Compute partial derivatives; visualise gradient direction
- Compare loss functions; visualise gradient descent trajectories
- Assess the effect of learning rate; distinguish convex from non-convex objectives
- Calculate entropy for simple distributions; compare distributions via KL divergence
- Interpret mutual information examples

### 1.14 Assessment questions

- What does the gradient represent?
- What distinguishes the Jacobian from the Hessian?
- How does backpropagation apply calculus?
- What is the function of a loss function?
- How does learning rate affect convergence?
- What distinguishes SGD from Adam? Why is regularisation necessary?
- What does entropy measure? Why is cross-entropy used for classification?
- What is KL divergence used for? How does perplexity evaluate language models?

### 1.15 Deliverables

1. **Gradient descent implemented from first principles** in NumPy, with loss curves plotted for
   three learning rates (insufficient, appropriate, divergent) and an explanation of each.
2. **Hand-implemented `entropy`, `cross_entropy` and `kl_divergence`**, verified against
   `scipy.stats`.
3. Visual explainer demonstrating stepwise error reduction under gradient descent.

### 1.16 REAL-WORLD APPLICATIONS AND INDUSTRY USE CASES

| Industry | Application | Role of this module's material |
|---|---|---|
| **All AI organisations** | Every production model training run | Gradient descent and its variants are the mechanism by which every deployed model was fitted. Optimiser and schedule selection routinely determine whether a multi-week training run converges or is wasted |
| **Advertising and marketing technology** | Click-through rate prediction, bid optimisation | Cross-entropy loss across billions of daily impressions. Calibration of predicted probabilities translates directly into revenue |
| **Logistics and operations research** | Route planning, warehouse allocation, scheduling | Constrained optimisation and Lagrange multipliers formalise capacity and cost constraints |
| **Energy and utilities** | Load forecasting, grid dispatch optimisation | Objective function design encodes the operational trade-off between cost, reliability and emissions |
| **Language model providers** | Pre-training and evaluation | Next-token prediction is cross-entropy minimisation. Perplexity is the standard reported quality metric in every LLM technical report |
| **Data compression and networking** | Codec design, transmission efficiency | Shannon entropy establishes the theoretical bound on compression; Huffman coding is its practical realisation |
| **Generative modelling** | Variational autoencoders, diffusion models, distillation | KL divergence is the regularisation term in variational objectives and the distillation loss transferring capability from large models to small ones |
| **Recommendation and ranking** | Feature selection, redundancy elimination | Mutual information quantifies the information a candidate feature adds beyond the existing feature set |

**Commercial significance.** Training compute is among the largest line items in an AI budget. An
optimiser and schedule converging in 40% fewer steps yields a proportional reduction in cost and
time-to-market. Loss function design is where business objectives are translated into mathematics —
a mis-specified loss produces a model that optimises the wrong outcome flawlessly.

**Roles dependent on this module:** Deep Learning Engineer · Research Engineer · Applied Scientist ·
Optimisation Engineer · LLM Training Engineer

### 1.17 Completion criteria

Confident handling of derivatives · gradient interpretation · clear articulation of gradient
descent · loss function interpretation · distribution comparison · a coherent account of how models
learn.

---

### 1.18 Advanced mathematics (research tier)

> **Compressed in v2.0.** [AWARE] throughout, and **out of scope for the target of this programme.**
> This Part is a signpost for a doctoral or frontier-research trajectory, not a study list. Version
> 1.0 gave each item a paragraph and a resource block, which over-represented its importance: none of
> it is assessed in industry interviews for the roles in Section 10.14.2, and time spent here is time not
> spent on the algorithms track, ranking, or Week 10 — all of which are assessed. The Section 1.18
> information theory entry also duplicated Week 1, Part C, which is where the applicable material
> lives.

| Area | Core idea | Where it is actually required |
|---|---|---|
| Numerical optimisation | Convexity · Newton's method · convergence guarantees | Optimiser research |
| Functional analysis | Function spaces · convergence of function sequences | Neural network theory |
| Topology and manifold learning | Manifold hypothesis · representation geometry | Representation learning research (the applied surface — t-SNE and UMAP — is in Week 4) |
| Riemannian geometry | Optimisation on curved spaces | Optimisation research |
| Measure theory | Probability in continuous and infinite-dimensional spaces | Probabilistic ML theory |

*Information theory has been removed from this Part as a duplicate; KL divergence, mutual information
and entropy are covered at working depth in Week 1, Part C.*

*Resources, if pursued:* MIT OCW https://ocw.mit.edu · 3Blue1Brown https://www.youtube.com/c/3blue1brown ·
Distill.pub https://distill.pub · arXiv https://arxiv.org

**Honest guidance.** If the objective is an offer at a large technology or semiconductor
organisation, read this table once and return to Section 10.13. If the objective is a doctorate, this Part
becomes a curriculum in its own right and this document is not the right guide to it.

---

## WEEK 2 — Probability, Statistics, Discrete Mathematics and Data Handling

### 2.1 Module objective

Develop the capacity to reason under uncertainty, evaluate models without self-deception, and
manipulate real-world data at scale.

### 2.2 Topics and subtopics

**PART A — Probability Theory**

**1. Sample Space and Events** — [KNOW] · Set theory basics · Outcomes · Venn diagrams
**2. Probability Axioms** — [KNOW] · Addition rule · Multiplication rule
**3. Conditional Probability** — [BUILD] · P(A|B) · Applied examples
**4. Bayes' Theorem** — [BUILD] · Prior · Likelihood · Posterior
**5. Independence** — [KNOW] · Independent events · Dependent events
**6. Random Variables** — [KNOW] · Discrete versus continuous · Outcome-to-number mapping
**7. Probability Distributions** — [BUILD]
- *Discrete:* Bernoulli · Binomial · Poisson
- *Continuous:* Uniform · Normal (Gaussian) · Exponential

**8. Expectation and Variance** — [BUILD] · Mean (E[X]) · Variance · Standard deviation
**9. Covariance and Correlation** — [KNOW] · Inter-variable relationships
**10. Law of Large Numbers** — [KNOW] · Empirical versus theoretical probability
**11. Central Limit Theorem** — [KNOW] · Normal distribution behaviour

**PART B — Statistics**

**1. Descriptive Statistics** — [BUILD]
Mean · Median · Mode · Variance · Skewness · Kurtosis

**2. Inferential Statistics** — [KNOW] · Estimation · Confidence intervals
**3. Sampling Techniques** — [KNOW] · Random sampling · Stratified sampling
**4. Hypothesis Testing** — [BUILD — *promoted in v2.0*] · Null versus alternate hypothesis ·
p-value · z-test · t-test · Type I and Type II error
**5. Correlation versus Causation** — [BUILD] · Pearson correlation · Spearman correlation
**6. Maximum Likelihood Estimation (MLE)** — [KNOW] · Parameter estimation
**7. Bayesian Inference** — [AWARE] · Prior · Posterior · Marginalisation
**8. Bias–Variance Tradeoff** — [BUILD] · Underfitting · Overfitting · Generalisation
**9. Confidence Intervals** — [KNOW] · Interpretation of parameter bounds
**10. Outlier Detection** — [BUILD] · IQR method · Z-score method

**PART B2 — Online experimentation and A/B testing** — [BUILD]
*Added in v2.0. Version 1.0 referenced A/B testing only as an industry application, with no
supporting material. Experimentation is assessed directly in machine learning and data science
interviews at consumer-scale technology organisations, and is the mechanism by which model changes
are actually approved for release.*

**1. Experiment design** — [BUILD]
Randomisation unit · treatment and control · the difference between a metric moving and a metric
moving *because of the treatment*

**2. Power and sample size** — [BUILD]
Minimum detectable effect · statistical power · why an underpowered test that "shows no effect"
demonstrates nothing · computing required sample size before launch, not after

**3. Metric design** — [KNOW]
Primary, secondary and guardrail metrics · proxy metrics and their failure modes ·
**offline versus online metric divergence** — why an offline accuracy gain frequently does not
reproduce as an online engagement gain

**4. Multiple comparisons and peeking** — [BUILD]
Family-wise error · why inspecting a running experiment and stopping when it reaches significance
inflates the false-positive rate · sequential testing as the correct remedy

**5. Variance reduction** — [AWARE]
Stratification · CUPED (pre-experiment covariate adjustment)

**6. Interference and violated assumptions** — [KNOW]
Network effects between treatment and control units · cannibalisation · seasonality ·
novelty and primacy effects

*Resources:* *Trustworthy Online Controlled Experiments* (Kohavi, Tang and Xu) ·
Google Rules of Machine Learning https://developers.google.com/machine-learning/guides/rules-of-ml

**PART C — Set Theory and Logic** — [AWARE — *compressed in v2.0*]

Set operations (union, intersection, difference, complement) · functions and relations (one-to-one,
onto) · propositional logic and truth tables · Boolean algebra and logic gates · quantifiers (∀, ∃).

*Rationale for demotion:* these five topics occupied full numbered slots in v1.0. Set operations
recur usefully in SQL and in de-duplication reasoning, and quantifier notation must be readable in
papers; the remainder does not repay dedicated study time against this target. Retained here with
resources for participants who want them.

**PART D — Graph Theory**
*Concurrently establishes the foundation for the algorithms track.*

**1. Graphs** — [BUILD] · Nodes · Edges · Directed and undirected · Adjacency matrix
**2. Trees and DAGs** — [BUILD] · Tree structures · **Directed Acyclic Graphs** · Decision trees
**3. Graph Traversals** — [BUILD] · Breadth-First Search · Depth-First Search
**4. Shortest Path Algorithms** — [KNOW] · Dijkstra · A*
**5. Connectivity** — [KNOW] · Connected components · Spanning trees

**PART E — Data handling and visualisation** — [BUILD]
pandas: Series and DataFrame · `loc`/`iloc` · filtering · `groupby` · joins · pivot · missing data ·
dtypes · vectorised operations · CSV, JSON and Parquet ingestion
Matplotlib and Seaborn: line, scatter, histogram, box plot, heatmap, confusion matrix

**PART F — SQL foundations** — [BUILD]
*Moved forward from Week 9 in v2.0. Version 1.0 placed SQL in Week 9 of 11 while simultaneously
observing that "SQL is assessed in interview considerably more often than is generally anticipated" —
an internal contradiction. SQL screens occur early in application processes, so the material must
land early.*

`SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY` · all four join types and what each does to row
count · aggregate functions · `NULL` semantics and why `NULL != NULL` · subqueries.
Every pandas operation in Part E is to be reproduced in SQL against the same dataset, and the results
compared. Advanced SQL — window functions and common table expressions — remains in Week 9, Part B.

*Resources:* StrataScratch · Mode SQL tutorial · SQLZoo. Practise against a real database file
(SQLite is sufficient), not a browser sandbox.

### 2.3 Learning resources

- StatQuest: https://www.youtube.com/c/joshstarmer
- Khan Academy — Statistics and Probability: https://www.khanacademy.org/math/statistics-probability
- MIT OpenCourseWare 18.05: https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/
- ProbabilityCourse.com: https://www.probabilitycourse.com
- Statistics How To: https://www.statisticshowto.com
- Neso Academy — Discrete Mathematics: https://www.youtube.com/c/NesoAcademy
- Brilliant.org — Logic and Sets: https://brilliant.org
- William Fiset — Graph Theory: https://www.youtube.com/c/WilliamFiset-videos
- freeCodeCamp — Graph Data Structures: https://www.youtube.com/c/Freecodecamp
- Visualgo: https://visualgo.net
- GeeksforGeeks — Graph Theory: https://www.geeksforgeeks.org/graph-data-structure-and-algorithms

### 2.4 Practice tasks

- Identify sample spaces; solve conditional probability problems; apply Bayes' theorem
- Plot distributions; compute mean and variance; interpret correlation coefficients
- Compute descriptive statistics; interpret confidence intervals; perform hypothesis tests
- Detect outliers via IQR; solve set operations
- Represent graphs as adjacency matrices; execute BFS and DFS manually; solve shortest-path problems
- **Compute the sample size required to detect a two percent relative change at 80% power**, then
  state what conclusion is and is not available if the observed effect is smaller *(added in v2.0)*
- **Reproduce five pandas `groupby` results as SQL queries** and reconcile any differences

### 2.5 Assessment questions

- What is conditional probability? How does Bayes' theorem update belief?
- Why is the normal distribution significant in AI?
- What distinguishes descriptive from inferential statistics? What does a p-value indicate?
- What is the bias–variance tradeoff? How do outliers affect models?
- When is BFS preferred to DFS? What is a DAG and why is it useful?
- An experiment shows a 1.5% lift with p = 0.04. The team wants to ship. What do you ask first?
- A model improves offline AUC by three points but produces no online metric movement. Give three
  distinct explanations, and state how you would distinguish between them.
- Why does stopping an experiment as soon as it reaches significance inflate false positives?
- What does a `LEFT JOIN` do to row count when the right table has duplicate keys?

### 2.6 Deliverable

**Complete statistical exploratory data analysis report** on a public dataset: descriptive
statistics, distribution analysis, outlier detection by two methods, correlation matrix, one
hypothesis test, and written findings. *Added in v2.0:* include a **pre-registered experiment
design** for a hypothetical intervention on the same data — randomisation unit, primary and guardrail
metrics, minimum detectable effect, and required sample size computed before any analysis.

### 2.7 REAL-WORLD APPLICATIONS AND INDUSTRY USE CASES

| Industry | Application | Role of this module's material |
|---|---|---|
| **Technology platforms** | A/B testing and experimentation | Hypothesis testing, p-values and confidence intervals govern product decisions. Organisations run thousands of concurrent experiments; flawed statistical reasoning ships harmful features |
| **Healthcare and pharmaceuticals** | Clinical trial analysis, diagnostic screening | Bayes' theorem explains why a highly accurate test for a rare condition still produces mostly false positives — a foundational result for diagnostic AI deployment and regulatory approval |
| **Insurance and actuarial** | Premium pricing, claims reserving, catastrophe modelling | Distribution fitting, expectation and variance are the discipline's core mathematics; the Poisson distribution models claim frequency directly |
| **Banking and fraud prevention** | Transaction anomaly detection | Outlier detection via z-score and IQR provides the first-line filter before ML models are invoked; extreme-value reasoning governs threshold placement |
| **Manufacturing** | Statistical process control, yield analysis | Control charts, sampling strategy and CLT-based confidence bounds determine when a production line is halted |
| **Logistics and navigation** | Route optimisation, delivery planning | Dijkstra and A* are the operative algorithms in mapping and fleet-routing products |
| **Social platforms and trust & safety** | Network analysis, community detection, fraud ring identification | Graph connectivity and traversal identify coordinated inauthentic behaviour and collusion networks |
| **Deep learning frameworks** | Automatic differentiation | The computation graph in PyTorch and TensorFlow is a DAG; the backward pass is a reverse topological traversal — Topic D2 applied directly |
| **Knowledge systems and search** | Knowledge graphs, entity resolution | Graph representation underpins entity linking and relationship inference in search and enterprise data products |

**Commercial significance.** Statistical illiteracy is expensive in a specific, recurring pattern:
teams ship models that appear to improve a metric, and the improvement is noise. Correct
experimental design and honest confidence reporting are the controls preventing this. Separately,
correlation-versus-causation discipline prevents deployment against a spurious relationship that
fails as soon as conditions shift.

**Roles dependent on this module:** Data Scientist · Machine Learning Engineer · Experimentation
Engineer · Risk Analyst · Quantitative Researcher · Fraud Analyst · Data Engineer

---

## WEEK 3 — Machine Learning Foundations and Supervised Learning

### 3.1 Module objective

Establish how data is prepared for modelling and how supervised algorithms learn from labelled
examples.

### 3.2 Topics and subtopics

**PART A — Machine Learning Foundations**

**1. What is Machine Learning** — [KNOW]
Definition of ML · Types of ML: Supervised · Unsupervised · Semi-Supervised · Reinforcement Learning

**2. Data Preprocessing** — [BUILD]
Handling missing data · Data scaling · Encoding (Label, One-Hot) · Data normalisation

**3. Feature Engineering** — [BUILD]
Feature selection · Feature extraction · Polynomial features
*Added:* **data leakage** — the predominant silent failure mode in applied ML. Transformations are
fitted on training data exclusively.

**4. Evaluation Metrics** — [BUILD]
Accuracy · Precision · Recall · F1 Score · ROC Curve · AUC Score · Confusion Matrix
*Added:* PR-AUC for imbalanced problems · MSE, MAE and R² for regression

**PART B — Supervised Learning Algorithms**

**1. Linear Regression** — [BUILD] · Cost function (MSE) · Gradient descent · Overfitting
**2. Logistic Regression** — [BUILD] · Sigmoid function · Probability output · Cross-entropy loss
**3. K-Nearest Neighbours (KNN)** — [BUILD] · Euclidean distance · Optimal K · Distance-based prediction
**4. Decision Trees** — [BUILD] · Gini impurity · Entropy · Information gain · Overfitting in trees
**5. Random Forest** — [BUILD] · Ensemble learning · Bagging · Multiple-tree voting
**6. Support Vector Machines (SVM)** — [KNOW] · Hyperplanes · Margin maximisation · Kernel trick
**7. Gradient Boosting** — [BUILD] *(added — absent from source material despite dominating tabular
problems and appearing consistently in technical interviews)*
Boosting versus bagging · XGBoost · LightGBM · early stopping

### 3.3 Learning resources

- StatQuest — ML algorithms: https://www.youtube.com/c/joshstarmer
- Andrew Ng — **Machine Learning Specialization**, course 1 of 3: *Supervised Machine Learning:
  Regression and Classification*: https://www.coursera.org/learn/machine-learning
  *(Corrected in v2.0: this link was labelled "Machine Learning" in v1.0, implying the original
  standalone course. It was fetched and verified to resolve to course 1 of 3 of the Specialization,
  which covers linear and logistic regression only. Course 3 —* Unsupervised Learning, Recommenders,
  Reinforcement Learning *— covers two topics v1.0 omitted entirely and is assigned in Week 8.)*
- Krish Naik — practical ML: https://www.youtube.com/c/KrishNaik
- Google ML Crash Course: https://developers.google.com/machine-learning/crash-course
- scikit-learn documentation: https://scikit-learn.org
- Kaggle Learn: https://www.kaggle.com/learn
- *Hands-On Machine Learning* (Géron), chapters 1–7

### 3.4 Practice tasks

- Classify real-world problems by ML type; practise data cleaning
- Distinguish scaling from normalisation; compare evaluation metrics; interpret confusion matrices
- Distinguish regression from classification problems; trace the prediction logic of each algorithm
- Compare algorithmic use cases; work through bias–variance examples

### 3.5 Assessment questions

- What distinguishes supervised from unsupervised learning? Why does preprocessing matter?
- When is precision preferred to recall? What does the ROC curve show?
- What distinguishes linear from logistic regression? Why does K matter in KNN?
- Why do decision trees overfit? How does Random Forest mitigate this?
- Why do SVMs employ kernels?
- A fraud detection model reports 99% accuracy. Explain why this may be worthless.

### 3.6 Deliverable

Using a single dataset: implement **linear and logistic regression from first principles in NumPy**,
then train all seven algorithms via scikit-learn and XGBoost. Produce a comparison table covering
accuracy, precision, recall, F1, AUC and training time, with a written recommendation and
justification.

### 3.7 REAL-WORLD APPLICATIONS AND INDUSTRY USE CASES

| Industry | Application | Role of this module's material |
|---|---|---|
| **Banking and lending** | Credit scoring, default prediction | Logistic regression remains dominant because regulators require explainable, auditable decisions. Coefficient interpretability is a legal requirement rather than a preference |
| **Insurance** | Claim likelihood, premium setting, churn prediction | Gradient boosting over tabular policyholder data is the industry standard; XGBoost and LightGBM outperform deep learning on this data shape |
| **Retail and e-commerce** | Demand forecasting, price elasticity, churn | Regression and tree ensembles drive inventory and pricing decisions with direct margin impact |
| **Healthcare** | Readmission risk, triage prioritisation, diagnostic support | Precision and recall trade-offs are life-critical. A false negative in cancer screening carries a fundamentally different cost to a false positive, making threshold selection a clinical decision |
| **Telecommunications** | Subscriber churn, network fault classification | Feature engineering over usage telemetry; retention campaigns are targeted using model output |
| **Cybersecurity** | Intrusion detection, malware classification | Extreme class imbalance makes PR-AUC the meaningful metric; accuracy is actively misleading |
| **Human resources technology** | CV screening, attrition modelling | A domain where bias auditing is legally mandated and where naive feature selection reproduces historical discrimination |
| **Agriculture** | Yield prediction, disease classification | Sensor and satellite features combined through tree ensembles for field-level recommendations |
| **Energy** | Consumption forecasting, predictive maintenance | Regression over sensor histories; failure classification triggers maintenance scheduling |

**Commercial significance.** Classical machine learning, not deep learning, remains the production
technology for the majority of tabular business problems — faster to train, cheaper to serve, easier
to explain to regulators, and frequently more accurate on structured data. Data leakage is the most
common cause of a model performing excellently in validation and failing in production; recognising
it is a core professional competency.

**Roles dependent on this module:** Machine Learning Engineer · Data Scientist · Risk Modeller ·
Credit Analyst · Business Intelligence Engineer · Applied Scientist

---

## WEEK 4 — Unsupervised Learning, Model Selection and Tuning

### 4.1 Module objective

Discover latent structure in unlabelled data, and select and tune models under statistically sound
validation.

### 4.2 Topics and subtopics

**PART A — Unsupervised Learning**

**1. K-Means Clustering** — [BUILD] · Centroids · Cluster formation · Inertia · Elbow method
**2. Hierarchical Clustering** — [KNOW] · Agglomerative clustering · Dendrograms · Linkage criteria
**3. DBSCAN** — [KNOW] · Density-based clustering · Epsilon (ε) · MinPts · Noise and outlier detection
**4. PCA (Dimensionality Reduction)** — [BUILD] · Covariance matrix · Eigen decomposition · Explained variance
**5. t-SNE and UMAP** — [AWARE] · Nonlinear dimensionality reduction

**PART B — Model Selection and Tuning**

**1. Cross Validation** — [BUILD] · K-Fold · Stratified K-Fold
**2. Hyperparameter Tuning** — [BUILD] · Grid Search · Random Search · Bayesian optimisation [AWARE]
**3. Bias–Variance Tradeoff** — [BUILD] · Underfitting · Overfitting · Generalisation
**4. Learning Curves** — [BUILD] · Training versus validation performance · Diagnosing over- and underfitting
**5. Pipelines** — [BUILD] *(added)* · `Pipeline` · `ColumnTransformer` — structural defence against leakage
**6. Class Imbalance** — [KNOW] *(added)* · Class weights · Resampling · SMOTE · Threshold tuning

### 4.3 Learning resources

- StatQuest — Clustering, PCA, Bias/Variance, Cross Validation: https://www.youtube.com/c/joshstarmer
- Krish Naik — Unsupervised Learning, Hyperparameter Tuning: https://www.youtube.com/c/KrishNaik
- 3Blue1Brown — PCA intuition: https://www.youtube.com/c/3blue1brown
- scikit-learn model selection guide: https://scikit-learn.org
- Kaggle Learn — Model Validation: https://www.kaggle.com/learn

### 4.4 Practice tasks

- Identify clustering problems in operational contexts; distinguish K-Means from DBSCAN
- Interpret dendrogram structure; assess how PCA reduces dimensionality
- Compare Grid Search with Random Search; interpret learning curves
- Diagnose overfitting versus underfitting from curve shape

### 4.5 Assessment questions

- Why is clustering used? When does DBSCAN outperform K-Means?
- Why apply PCA before modelling? What is explained variance?
- Why is cross-validation necessary? When is Stratified K-Fold required?
- What causes overfitting? How do learning curves inform tuning decisions?

### 4.6 Deliverable — Portfolio artefact 1

**End-to-end tabular machine learning project.** Public dataset. Exploratory analysis, cleaning,
feature engineering, `Pipeline` construction, five or more models, cross-validated evaluation,
hyperparameter tuning, metric selection justified against the problem, error analysis, and a README
containing a results table and stated next steps.

### 4.7 REAL-WORLD APPLICATIONS AND INDUSTRY USE CASES

| Industry | Application | Role of this module's material |
|---|---|---|
| **Retail and consumer goods** | Customer segmentation, market basket analysis | K-Means over purchase behaviour produces the segments driving campaign targeting, store layout and assortment decisions |
| **Banking** | Anti-money-laundering, transaction clustering | DBSCAN identifies dense clusters of coordinated activity and flags points belonging to no cluster — precisely the AML signal of interest |
| **Telecommunications** | Network traffic profiling, cell-site optimisation | Clustering usage patterns informs capacity planning and infrastructure investment |
| **Bioinformatics** | Gene expression clustering, single-cell analysis | Hierarchical clustering and dendrograms are the standard presentation format in published genomics research |
| **Cybersecurity** | Novel and zero-day threat detection | Unsupervised methods detect deviation from established baselines without requiring labelled examples of attacks that have not yet occurred |
| **Manufacturing** | Failure mode discovery | Clustering sensor signatures reveals previously uncharacterised failure modes before any labelled dataset exists |
| **Recommendation systems** | Cold-start handling, content grouping | Clustering provides recommendations for users with no interaction history |
| **All ML organisations** | Pre-release model validation | Cross-validation and learning-curve analysis are the gate controls determining production approval |
| **Search and NLP** | Embedding space inspection | t-SNE and UMAP projections are the standard method for visually auditing whether an embedding space has learned meaningful structure |

**Commercial significance.** Unsupervised methods apply wherever labels are unavailable,
prohibitively expensive, or where the objective is discovery rather than prediction — which
describes a large proportion of real commercial data. This module also contains the professional
discipline distinguishing reliable engineers: rigorous validation. A model tuned against the test
set yields a number that is not real, and the failure surfaces only after deployment.

**Roles dependent on this module:** Data Scientist · Machine Learning Engineer · Customer Analytics
Lead · Security Analyst · Bioinformatician · Marketing Analyst

---

## WEEK 5 — Neural Network Fundamentals and PyTorch

### 5.1 Module objective

Establish how neural networks learn by constructing one without a framework, then translate that
understanding into idiomatic PyTorch.

### 5.2 Topics and subtopics

**PART A — Neural network fundamentals**

**1. Perceptron** — [BUILD] · Neuron concept · Input → Weight → Output
**2. Activation Functions** — [BUILD]
ReLU · Sigmoid · Tanh · Rationale for non-linearity (absent it, N layers collapse to one)
*Added:* GELU · Softmax · Leaky ReLU

**3. Neural Network Architecture** — [BUILD] · Input layer · Hidden layer · Output layer · Connectivity
**4. Forward Propagation** — [BUILD] · Weighted sum · Activation output · Signal flow
**5. Backpropagation** — [BUILD] · Chain rule application · Gradient computation · Error reduction
**6. Loss Functions** — [BUILD] · MSE · Cross-Entropy · Hinge Loss

**PART B — PyTorch** — [BUILD]

Tensors, dtypes, device placement, broadcasting · **Autograd**: computation graph, `backward()`,
`.grad`, `no_grad()`, `detach()` · `nn.Module`, `nn.Parameter`, `nn.Sequential`, `state_dict`,
checkpointing · `Dataset`, `DataLoader`, `collate_fn`, worker processes, pinned memory ·
the canonical training loop (`zero_grad → forward → loss → backward → step`) ·
train, validation and test discipline · `model.train()` versus `model.eval()` · reproducibility and
seeding · diagnosis of shape errors, NaN loss and device mismatches

### 5.3 Learning resources

- **Andrej Karpathy — *Neural Networks: Zero to Hero*: https://www.youtube.com/c/AndrejKarpathy**
  The `micrograd` construction is the single highest-value exercise in this module.
- 3Blue1Brown — Neural Networks: https://www.youtube.com/c/3blue1brown
- StatQuest — Neural Network basics: https://www.youtube.com/c/joshstarmer
- Andrew Ng — Deep Learning Specialisation: https://www.coursera.org/specializations/deep-learning
- PyTorch tutorials: https://pytorch.org/tutorials
- Dive into Deep Learning: https://d2l.ai
- DeepLearning.ai: https://www.deeplearning.ai

### 5.4 Practice tasks

- Draw a neural network diagram; identify input, hidden and output layers
- Interpret activation function curves; distinguish forward from backward flow
- Compare loss functions; trace a gradient by hand through two layers

### 5.5 Assessment questions

- What is a perceptron? Why do neural networks require activation functions?
- What occurs during forward propagation? Why is backpropagation necessary?
- How do loss functions influence learning?
- What does `optimizer.zero_grad()` do, and what fails if it is omitted?
- Why is `no_grad()` used at inference time?

### 5.6 Deliverable — Portfolio artefact 2

1. **Two-layer neural network with hand-derived backpropagation in pure NumPy**, trained on MNIST,
   with no framework dependency.
2. **Equivalent implementation in PyTorch**, with matching loss curves and a written account of the
   abstractions PyTorch provides.

### 5.7 REAL-WORLD APPLICATIONS AND INDUSTRY USE CASES

| Industry | Application | Role of this module's material |
|---|---|---|
| **Financial services** | Real-time transaction fraud scoring | Feed-forward networks score transactions within millisecond budgets at payment-network scale; architecture depth is bounded by latency SLA |
| **Postal, logistics and banking** | Handwriting and document digitisation | MNIST is the canonical teaching problem precisely because cheque, form and address digitisation was among the first commercially deployed neural network applications |
| **Advertising technology** | Click-through and conversion prediction | Deep networks over sparse categorical features; embedding layers are the production mechanism for high-cardinality identifiers |
| **Energy and utilities** | Demand forecasting, grid telemetry anomaly detection | Regression networks over multivariate sensor streams |
| **Gaming and simulation** | Behaviour models, procedural systems | Lightweight networks operating under strict per-frame compute budgets |
| **All deep learning organisations** | Framework-level defect diagnosis | The most frequent production defect class — silent device mismatch, omitted `eval()` mode, un-zeroed gradients, NaN propagation — is diagnosed using precisely this module's material |

**Commercial significance.** Understanding backpropagation from first principles distinguishes an
engineer who can diagnose a failing training run from one who can only restart it with different
hyperparameters. When a model produces NaN loss at hour nine of a twelve-hour run, the cost of that
distinction is measured directly in compute spend and delivery schedule.

**Roles dependent on this module:** Deep Learning Engineer · Machine Learning Engineer ·
Applied Scientist · Research Engineer · AI Platform Engineer

---

## WEEK 6 — Training Techniques, Optimisers and Convolutional Networks

### 6.1 Module objective

Train deep networks that converge reliably, and develop working command of convolutional
architectures for visual data.

### 6.2 Topics and subtopics

**PART A — Training techniques**

**1. Gradient Descent Variants** — [BUILD] · Batch · Stochastic (SGD) · Mini-Batch
**2. Weight Initialisation** — [KNOW] · Significance of initialisation · Xavier · He
**3. Training Stabilisation** — [BUILD] · Dropout · Batch Normalisation · Layer Normalisation [KNOW]
**4. Training Process Terms** — [BUILD] · Epochs · Iterations · Batch size
**5. Overfitting and Regularisation** — [BUILD] · L1 · L2 · Early stopping · Data augmentation

**PART B — Optimisers**

**1. SGD** — [BUILD] · Update noise · Speed versus stability characteristics
**2. Adam** — [BUILD] · Adaptive learning rates · Momentum combined with RMSprop
*Added:* **AdamW** — decoupled weight decay; the operative default for transformer training
**3. RMSprop** — [KNOW] · Per-parameter adaptive learning rate
**4. Learning Rate Schedulers** — [BUILD] · Step decay · Exponential decay · Reduce-on-plateau ·
Warm-up · Cosine annealing [KNOW]
**5. Gradient Clipping** — [BUILD] · Exploding gradient mitigation
**6. Mixed Precision (`torch.amp`)** — [BUILD] *(added)* · FP16 and BF16 · GradScaler · reduced
memory footprint, permitting larger batches
*Corrected in v2.0:* v1.0 stated "approx. 2× throughput" as a flat fact. The realised speedup depends
on the hardware and on the bottleneck class: it approaches the arithmetic ratio only for
compute-bound layers on accelerators with tensor or matrix cores, and can be negligible for a
workload that is dataloader-bound or memory-bandwidth-bound. **Measure it; do not assume it.** The
diagnostic framework is Week 10, Part B (roofline analysis) — this is the first point in the
programme where a performance claim must be earned with a number.
**7. Gradient Accumulation** — [KNOW] *(added)* · Emulating large batches under memory constraint

**PART C — Convolutional Neural Networks**

**1. Convolution Operation** — [BUILD] · Filters and kernels · Strides · Padding
**2. Pooling** — [BUILD] · Max pooling · Average pooling
**3. Receptive Field** — [KNOW] *(added)*
**4. CNN Architectures** — [BUILD] (**ResNet**) / [AWARE] (historical lineage)
LeNet → AlexNet → VGG → **ResNet** (residual connections) → EfficientNet
*Demoted in v2.0:* LeNet, AlexNet and VGG are historical context, not working knowledge. Know what
each contributed in one sentence. ResNet is built; the residual connection is the transferable idea
and it reappears in every transformer block in Week 7.
**5. Transfer Learning and Fine-Tuning** — [BUILD] *(added)*

### 6.3 Learning resources

- StatQuest — GD variants, regularisation, optimisers: https://www.youtube.com/c/joshstarmer
- DeepLearning.ai — Training Deep Networks: https://www.coursera.org/specializations/deep-learning
- Krish Naik — deep learning training: https://www.youtube.com/c/KrishNaik
- PyTorch tutorials: https://pytorch.org/tutorials
- TensorFlow training guide: https://www.tensorflow.org
- Stanford CS231n: https://cs231n.stanford.edu
- Dive into Deep Learning — CNN chapters: https://d2l.ai

### 6.4 Practice tasks

- Compare batch, stochastic and mini-batch descent; assess batch size effects
- Examine dropout behaviour; explain why normalisation stabilises training
- Compare L1 and L2; distinguish SGD, Adam and RMSprop
- Assess learning rate scheduling effects; characterise the exploding gradient problem
- Distinguish convolutional from fully-connected architectures

### 6.5 Assessment questions

- Why mini-batch rather than full-batch descent? Why does initialisation matter?
- How does dropout reduce overfitting? What problem does batch normalisation address?
- Why is Adam the common default? When is SGD preferable?
- Why is learning rate scheduling required? What does gradient clipping solve?
- Why are CNNs suited to images? How did ResNet enable deeper networks?
- How does BatchNorm behave differently in training and evaluation modes, and what fails if the mode
  is not switched?

### 6.6 Deliverable — Portfolio artefact 3

**ResNet reproduced from the original publication** (not from a tutorial) and trained on CIFAR-10,
incorporating a learning rate schedule, augmentation and mixed precision. Repeat using transfer
learning from pretrained weights and present a comparative analysis with training curves and final
metrics.

### 6.7 REAL-WORLD APPLICATIONS AND INDUSTRY USE CASES

| Industry | Application | Role of this module's material |
|---|---|---|
| **Medical imaging** | Radiology triage, pathology slide analysis, retinal screening | CNN architectures classify and localise findings in X-ray, CT, MRI and histopathology. Transfer learning from natural-image pretraining is standard practice because annotated medical data is scarce and expensive |
| **Automotive** | Advanced driver assistance, autonomous perception | Convolutional backbones process camera feeds under hard real-time constraints; architecture selection is governed by latency and power envelope |
| **Manufacturing** | Automated visual inspection, defect detection | CNNs replace manual inspection on production lines, operating continuously at line speed with measurable scrap-rate reduction |
| **Agriculture** | Crop disease identification, yield estimation | Drone and satellite imagery classified at field scale to direct intervention |
| **Retail** | Checkout-free stores, shelf monitoring, visual search | Detection and classification pipelines executing on in-store edge hardware |
| **Security and critical infrastructure** | Surveillance analytics, perimeter monitoring, industrial safety | Real-time video analysis where false-positive rate directly determines operational viability |
| **Insurance** | Automated damage assessment from photographs | Vehicle and property damage classified for claims triage, compressing settlement cycle time |
| **Satellite and geospatial** | Land use classification, disaster response mapping | Segmentation models over multispectral imagery |
| **Consumer electronics** | On-device photography enhancement, biometric unlock | Efficient architectures selected against power and thermal constraints on mobile silicon |

**Commercial significance.** Transfer learning is the economic foundation of applied computer
vision: it reduces the labelled data requirement from millions of examples to hundreds, converting
projects that would be commercially unviable into ones delivering within a quarter. Mixed precision
training approximately halves training cost, which at production scale is a material budget line.

**Roles dependent on this module:** Computer Vision Engineer · Deep Learning Engineer ·
Medical Imaging AI Engineer · Autonomous Systems Engineer · Edge AI Engineer

---

## WEEK 7 — Sequence Models and Transformer Architectures

### 7.1 Module objective

Develop working command of the architecture underpinning contemporary artificial intelligence.

### 7.2 Topics and subtopics

**PART A — Sequence models**

**1. Recurrent Neural Networks (RNN)** — [KNOW]
Sequence modelling · Time-step processing · Vanishing gradient problem · why the sequential
dependency prevents parallel training — *the specific limitation transformers remove*

**2. LSTM and GRU** — [AWARE — *demoted in v2.0*]
Long-term dependency handling · gating as a learned mechanism for retaining or discarding state.
*Gate-by-gate derivation is no longer required.* Know what problem gating solves and that GRU is a
cheaper variant. The interview question is why gating helps, not what the forget gate's equation is.

**3. BiRNN** — [AWARE] · Bidirectional processing

**PART B — Transformers**

**1. Attention Mechanism** — [BUILD] · Query · Key · Value · Dot-product attention · Scaling · Softmax
**2. Self-Attention** — [BUILD] · Multi-head attention · Rationale for multiple heads
**3. Positional Encoding** — [BUILD] · Sinusoidal · Learned [KNOW] · RoPE [AWARE]
**4. Encoder–Decoder Architecture** — [KNOW]
Encoder-only (BERT) · Decoder-only (GPT) · Encoder-decoder (T5)
**5. Causal Masking** — [BUILD] *(added)* · Enforcing the autoregressive constraint
**6. KV Cache** — [KNOW] *(added)* · Why generation is memory-bandwidth-bound — foundation for Week 10
**7. Parallel Processing Advantage** — [KNOW] · Absence of sequential dependency during training
**8. Residual Connections and LayerNorm** — [BUILD] *(added)* · Pre-norm versus post-norm

**9. Attention variants that reduce KV-cache cost** — [KNOW] *(added in v2.0)*
Multi-head attention (MHA) → **multi-query attention (MQA)** → **grouped-query attention (GQA)**.
Key and value heads are shared across query heads, which cuts the per-token KV-cache footprint
proportionally. Because decode is bandwidth-bound (Topic 6), this translates directly into
achievable batch size and serving cost. GQA is standard in current open-weight model families, so
this is not an exotic topic — it is what the checkpoint you download is actually using.
*Reference:* *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints*
(Ainslie et al., 2023).

**10. Numerical stability of softmax** — [BUILD] *(added in v2.0)*
The max-subtraction trick · the log-sum-exp identity · why a naive `exp` over unbounded logits
overflows in FP16 · **online (streaming) softmax**, which computes the normaliser in a single pass
without materialising all scores.
*This is a prerequisite, not an aside:* the fused-softmax Triton kernel required in Week 10, Part E
cannot be written correctly without it, and it is the core idea FlashAttention generalises. Version
1.0 asked for that kernel without ever teaching this.

**11. Mixture of Experts (MoE)** — [AWARE] *(added in v2.0)*
Sparse routing: a router selects a small subset of expert feed-forward blocks per token, so total
parameter count and per-token compute decouple. The consequence worth carrying forward is that an
MoE model has high memory capacity requirements with comparatively low arithmetic per token, which
shifts it further into the bandwidth-bound regime and complicates serving.

**12. Long-context mechanisms** — [AWARE] *(added in v2.0)*
Sliding-window and local attention · why full attention cost is quadratic in sequence length and
linear in the KV cache · context-length extension by positional-encoding modification.

**PART C — Generative foundations** — [KNOW]
Autoencoders · Variational autoencoders · GANs (generator and discriminator, mode collapse) ·
Diffusion models (developed in Week 8)

### 7.3 Learning resources

- **Andrej Karpathy — *Let's build GPT* and nanoGPT: https://www.youtube.com/c/AndrejKarpathy**
- **The Illustrated Transformer: https://jalammar.github.io/illustrated-transformer/**
- Yannic Kilcher — Transformers explained: https://www.youtube.com/c/YannicKilcher
- StatQuest — CNN and RNN basics: https://www.youtube.com/c/joshstarmer
- Stanford CS224n: https://web.stanford.edu/class/cs224n
- Publication: *Attention Is All You Need*
- PyTorch tutorials: https://pytorch.org/tutorials

### 7.4 Practice tasks

- Trace RNN sequence processing; establish why LSTM addresses vanishing gradients
- Trace the attention mechanism step-by-step; compare CNN and transformer applicability
- Hand-compute attention for a three-token sequence with two-dimensional embeddings

### 7.5 Assessment questions

- Why do RNNs degrade on long sequences? How does LSTM address the memory problem?
- Why did transformers displace RNNs in natural language processing?
- How does attention enable selective focus on relevant information?
- Reproduce scaled dot-product attention from memory. Why is the scaling factor √d_k applied?
- What effect does the causal mask have on the attention matrix?
- Why does subtracting the row maximum before exponentiating leave the softmax output unchanged?
- A model is switched from MHA to GQA with eight query heads per key-value head. What happens to the
  KV-cache size, and what does that permit at serving time?
- An MoE model has 8× the parameters of a dense model at similar per-token compute. Which resource
  becomes the binding constraint when serving it, and why?

### 7.6 Deliverable — Portfolio artefact 4

**Mini-GPT implemented from scratch in PyTorch**: tokeniser, embeddings, positional encoding,
multi-head causal self-attention, feed-forward blocks, residual connections and normalisation,
training loop, and text generation. Trained on a small corpus, with generated samples and
architectural documentation.

*Extended in v2.0 — two additions, both small and both load-bearing later:*
- Implement the softmax with explicit max-subtraction, and demonstrate the overflow that occurs
  without it by forcing large logits in FP16.
- Implement a KV cache for generation, and measure tokens per second with and without it. This
  measurement is the input to the Week 10 profiling study, so record it.

### 7.7 REAL-WORLD APPLICATIONS AND INDUSTRY USE CASES

| Industry | Application | Role of this module's material |
|---|---|---|
| **Software engineering** | Code completion and generation assistants | Decoder-only transformers trained on source corpora, now embedded in the daily workflow of a substantial proportion of professional developers |
| **Customer operations** | Support automation, intent classification, response drafting | Transformer models handle first-line contact at volumes that materially change support cost structures |
| **Legal and professional services** | Contract review, clause extraction, discovery | Long-context transformer models process document sets at a scale infeasible for manual review |
| **Healthcare** | Clinical note summarisation, coding assistance | Sequence-to-sequence summarisation over unstructured clinical text, reducing documentation burden |
| **Financial services** | Sentiment analysis over filings and news, report generation | Transformer encoders extract structured signal from unstructured market text |
| **Search engines** | Query understanding, semantic ranking, direct answers | Transformer-based relevance ranking displaced keyword matching as the dominant retrieval paradigm |
| **Media and localisation** | Machine translation, subtitling, transcription | Encoder-decoder architectures are the production standard for translation systems |
| **Bioinformatics** | Protein structure and sequence modelling | Attention over amino acid sequences underpins the current generation of structure prediction systems |
| **Industrial and time series** | Forecasting, predictive maintenance | Transformer variants increasingly displace LSTM for long-horizon multivariate forecasting |
| **Speech and audio** | Transcription, voice interfaces, audio generation | Transformer-based speech models are the current production standard |

**Commercial significance.** The transformer is the highest-leverage architecture in contemporary
AI, and the KV cache introduced here is the direct link to inference economics: during generation
the binding constraint is memory bandwidth rather than arithmetic throughput. This single fact
determines serving cost, achievable batch size and hardware selection for every deployed language
model, and is the point at which this module connects to Week 10.

**Roles dependent on this module:** NLP Engineer · LLM Engineer · Applied Scientist ·
Research Engineer · Conversational AI Engineer · Speech Engineer

---

### 7.9 Research literacy

**Reading methodology** — Problem → Method → Results → Limitations. Abstract first, then figures,
then results, then method. Related work is deferred to a second pass.

**Reproduction** — Concept-level implementation · study of official repositories · simplified
reimplementation in PyTorch

**Tools** — Papers With Code https://paperswithcode.com · arXiv https://arxiv.org ·
arXiv Sanity http://www.arxiv-sanity.com

##### Foundational reading list

| Area | Publication |
|---|---|
| Transformers | *Attention Is All You Need* |
| Vision | *ResNet — Deep Residual Learning* |
| Language models | *BERT — Pre-training of Deep Bidirectional Transformers* |
| Generative AI | DALL·E · Stable Diffusion |
| Scientific AI | AlphaFold · AlphaGo |
| Vision foundation models | Segment Anything |
| *Added — systems* | FlashAttention · LoRA · GPT-3 (*Language Models are Few-Shot Learners*) |

*Resources:* Yannic Kilcher https://www.youtube.com/c/YannicKilcher ·
AI Coffee Break https://www.youtube.com/c/AICoffeeBreak · Two Minute Papers

**Cadence** — one publication per week, sustained indefinitely.

**Assessment:** Can the publication be explained in plain language? Why does the method work? What
advantages does it hold over prior approaches? What are its stated limitations?

**Real-world relevance.** Applied research roles, frontier product teams and any organisation
adopting techniques ahead of their appearance in library documentation depend on this capability.
The practical commercial value is time-to-adoption: an organisation able to read and implement a
publication within weeks of release holds a durable advantage over one waiting for a library release.

---

## WEEK 8 — Specialisation Tracks: NLP, Computer Vision, Generative AI

### 8.1 Module objective

Establish working knowledge across the specialisation tracks, with implementation-level depth in the
track selected by the participant.

**Revised in v2.0.** Version 1.0 offered three tracks (NLP, computer vision, generative AI). Two
have been added — **Track D, recommender systems and ranking**, and **reinforcement learning
foundations** within Track C — because both were absent from v1.0 and both are directly relevant to
the stated target. Room was created by demoting the pre-transformer material in Tracks A and B,
which retains historical and interview-vocabulary value but no longer repays implementation time.

**Track selection.** Tracks A, B and D are surveyed at [KNOW]; **one** is taken to [BUILD]. Track C
is [BUILD] for all participants. Candidates targeting consumer-scale technology organisations should
weight **Track D**; candidates targeting semiconductor and infrastructure organisations should weight
Week 10 over any Week 8 track.

### 8.2 TRACK A — Natural Language Processing

**1. Text Preprocessing** — [BUILD] (subword) / [AWARE] (classical)
**Subword tokenisation and Byte-Pair Encoding** — the mechanism used by modern LLMs — is built.
Stemming, lemmatisation and stop-word removal are [AWARE]: *demoted in v2.0*, as they are largely
obsolete in transformer pipelines and are worth recognising rather than implementing.

**2. Feature Extraction** — [KNOW — *demoted*] · Bag of Words (BoW) · TF-IDF
Still a legitimate strong baseline on small text corpora, and TF-IDF appears in interviews as a
contrast to learned embeddings. Implement once; do not dwell.

**3. Word Embeddings** — [BUILD] (Word2Vec) / [AWARE] (GloVe, FastText)
Word2Vec is built because the skip-gram objective and negative sampling recur in Track D's
two-tower retrieval. Contextual embeddings [KNOW].

**4. Sequence Models** — [AWARE — *demoted*] · RNN · BiRNN · LSTM (see Week 7)
**5. Transformers** — [BUILD] · BERT · GPT · Attention mechanism
**6. NLP Tasks** — [BUILD] (select two) / [KNOW] (remainder)
Text classification · Named Entity Recognition · Text summarisation · Machine translation ·
Question Answering

*Resources:* Hugging Face NLP Course https://huggingface.co/learn · NLTK https://www.nltk.org ·
spaCy https://spacy.io · Krish Naik NLP playlist https://www.youtube.com/c/KrishNaik ·
Hugging Face https://www.youtube.com/c/HuggingFace · Stanford CS224n

### 8.3 TRACK B — Computer Vision

**1. Image Basics** — [BUILD] · Pixels · Colour channels (RGB, greyscale) · Formats (JPEG, PNG)
**2. Image Processing Techniques** — [AWARE — *demoted in v2.0*] · Thresholding · Edge detection ·
Morphological operations. Classical techniques, largely superseded for recognition tasks; retained
for vocabulary and for preprocessing work where they remain the right tool.
**3. CNN Architectures** — [AWARE] (historical) / see Week 6 for ResNet · EfficientNet
**4. Object Detection** — [KNOW] · YOLO · SSD · Faster-RCNN · Anchor boxes, IoU, NMS, mAP
**5. Image Segmentation** — [KNOW] · Semantic · Instance · U-Net · Mask-RCNN
**6. Modern Vision** — [KNOW] *(added)* · **Vision Transformers** · **CLIP** and contrastive
image-text training · vision-language models · Segment Anything
*Weighted upward in v2.0:* CLIP-style contrastive training is the shared mechanism behind
multimodal retrieval and Track D's two-tower architecture, making it the highest-value item in this
track.

*Resources:* OpenCV https://opencv.org · PyTorch Vision https://pytorch.org/tutorials ·
Papers With Code https://paperswithcode.com · freeCodeCamp Computer Vision course ·
Krish Naik CV playlist · Stanford CS231n

### 8.4 TRACK C — Generative AI and Large Language Models

**1. LLM Basics** — [BUILD] · Tokenisation · Embeddings · Transformer blocks
**2. GPT Architecture** — [BUILD] · Decoder-only · Causal attention · Autoregressive generation
**3. Training LLMs** — [KNOW] · Masked Language Modelling · Next token prediction
*Added:* the pretraining → supervised fine-tuning → RLHF/DPO pipeline

**3a. Reinforcement learning foundations** — [KNOW] *(added in v2.0)*

*Version 1.0 named RLHF and DPO while listing reinforcement learning only as a word in a taxonomy.
That is not a supportable position: a candidate asked "what is the reward model optimising against,
and why is a KL penalty applied?" cannot answer it from the RLHF acronym alone. This subsection
supplies the minimum foundation. It is [KNOW], not [BUILD] — the objective is to be able to reason
about post-training, not to become a reinforcement learning specialist.*

**Formulation** — Agent, environment, state, action, reward · policy · the Markov Decision Process ·
discounting and the return · why the delayed-reward credit assignment problem is what makes this
different from supervised learning

**Value and policy** — State-value and action-value functions · the Bellman equation as a
consistency condition · Q-learning [AWARE] · exploration versus exploitation

**Policy gradient methods** — The policy gradient theorem at concept level · REINFORCE · why
variance is the central practical problem · baselines and advantage estimation · actor-critic
structure

**PPO** — Why unconstrained policy updates collapse · the clipped surrogate objective as a
trust-region approximation · this is the algorithm in the original RLHF pipeline

**Applied to language models** — [BUILD-adjacent]
Reward modelling from pairwise human preference · the KL penalty against the reference policy and
what it prevents · **reward hacking** as the characteristic failure mode ·
**DPO** — why a closed-form preference objective removes the need for an explicit reward model and a
sampling loop, and what is given up in exchange · GRPO-style group-relative variants and their use in
reasoning-model post-training [AWARE]

**Multi-armed bandits** — [KNOW]
ε-greedy · upper confidence bound · Thompson sampling [AWARE] · **why this matters here:** bandits
are the production mechanism for the explore/exploit problem in ranking and recommendation
(Track D) and are the bridge between the experimentation material in Week 2 and online learning.

*Resources:* *Reinforcement Learning: An Introduction* (Sutton and Barto), free:
http://incompleteideas.net/book/the-book.html — chapters 1–3, 6 and 13 only ·
OpenAI Spinning Up in Deep RL: https://spinningup.openai.com ·
Andrew Ng Machine Learning Specialization, **course 3**: *Unsupervised Learning, Recommenders,
Reinforcement Learning* — https://www.coursera.org/learn/unsupervised-learning-recommenders-reinforcement-learning
*(this course covers both v1.0 omissions — reinforcement learning and recommenders — and is the
single most efficient way to close them)*

**Completion test.** Explain the RLHF pipeline end to end at a whiteboard, name the objective at each
of the three stages, and state what the KL term is protecting against.

**4. Fine-Tuning Techniques** — [BUILD] · **LoRA** · **QLoRA** · **PEFT** · Adapter layers
*Direct application of Week 1, Topic 11 — low-rank approximation.*

**5. Prompt Engineering** — [BUILD]
Zero-shot · Few-shot · Chain-of-Thought (CoT) · ReAct (Reason and Act) · Instruction tuning

**6. Diffusion Models** — [KNOW] · Denoising process · Latent diffusion · Stable Diffusion
**7. Retrieval-Augmented Generation (RAG)** — [BUILD]
Vector databases · FAISS · ChromaDB · LangChain RAG pipelines
*Added:* chunking strategy, embedding model selection, retrieval quality, reranking

**8. LLM Agents** — [KNOW] · LangGraph · CrewAI · AutoGen · Multi-agent workflows
**9. LLM APIs and Ecosystem** — [KNOW] · OpenAI · Claude · Cohere · Gemini · Mistral
**10. Serving LLMs** — [KNOW] *(developed further in Week 10)* · vLLM · Triton Inference Server ·
High-throughput inference
**11. LLM Evaluation** — [BUILD] · Perplexity · BLEU · BERTScore · Human evaluation
*Added:* LLM-as-judge methodology, benchmark contamination, the intrinsic difficulty of LLM evaluation

**12. LLM application security** — [KNOW] *(added in v2.0)*
*Version 1.0 covered ethics, privacy and compliance but contained no security material. These are
different disciplines: a compliant system can still be trivially exploitable.*

**Prompt injection** — direct and indirect · why a retrieval-augmented system is an injection
surface, since retrieved documents are untrusted input reaching the model as instructions ·
**why input filtering is not a solution**
**Jailbreaking** — instruction-hierarchy violation · the practical limits of alignment training
**Data exfiltration** — leakage of retrieved context, system prompts, and other tenants' data in
shared-index designs
**Insecure tool use** — an agent with tool access is an agent with an attack surface; the blast
radius of a compromised agent equals the permissions granted to it
**Mitigations** — least-privilege tool scoping · output validation over input filtering ·
human confirmation gates on irreversible actions · treating model output as untrusted

*Resource:* OWASP Top 10 for Large Language Model Applications:
https://owasp.org/www-project-top-10-for-large-language-model-applications/

**Why this is in scope for the target.** Any candidate presenting a RAG or agent artefact should
expect to be asked how it fails adversarially. "I did not consider that" is a poor answer for a
system in a portfolio.

*Resources:* Hugging Face LLM Course https://huggingface.co/learn ·
LangChain https://docs.langchain.com · FAISS https://faiss.ai ·
OpenAI https://platform.openai.com/docs · Stability AI https://stability.ai ·
LangChain channel https://www.youtube.com/c/LangChain

### 8.5 TRACK D — Recommender Systems, Retrieval and Ranking

> **Added in its entirety in v2.0.** Version 1.0 contained no ranking material: no two-stage
> architecture, no learning-to-rank, no ranking metrics, no calibration, no position bias, and no
> sparse-embedding models. Its only related content was a single tutorial-tier project row
> ("Movie Recommendation | Collaborative filtering").
>
> This is the most consequential omission in the original document relative to its stated target.
> Feed ranking, ads ranking, search ranking and recommendation are the largest machine learning
> application area at consumer-scale technology organisations, employ a large share of their machine
> learning engineers, and are the default subject of their ML system design interviews. A candidate
> who can fine-tune a language model but cannot describe a candidate-generation-and-ranking pipeline
> is prepared for the wrong interview.

**1. The recommendation problem** — [KNOW]
Explicit versus implicit feedback · why implicit feedback dominates in practice and what biases it
carries · the absence of negatives — every unobserved item is not a negative · cold start for users,
items and both · popularity bias and feedback loops

**2. Classical approaches** — [BUILD]
User-based and item-based collaborative filtering · matrix factorisation via alternating least
squares · **implicit-feedback weighting** · *direct application of Week 1, Topic 11 — this is
low-rank approximation of a sparse interaction matrix*

**3. The two-stage architecture** — [BUILD]
The central design pattern in production ranking, and the thing to reach for in an interview:

| Stage | Corpus size | Latency budget | Model class | Objective |
|---|---|---|---|---|
| **Retrieval / candidate generation** | Millions to billions | Single-digit milliseconds | Two-tower, approximate nearest neighbour, heuristics | High recall, cheap |
| **Ranking** | Hundreds | Tens of milliseconds | Heavy feature-rich model | High precision at the top |
| **Re-ranking** | Tens | Low | Rules and business logic | Diversity, freshness, policy |

Why one model cannot do both: the retrieval stage cannot afford per-item scoring against the full
corpus, and the ranking stage can afford features the retrieval stage cannot compute.

**4. Two-tower retrieval** — [BUILD]
Separate query and item encoders producing a shared embedding space · the requirement that scoring
factorise into a dot product so item embeddings can be precomputed and indexed · in-batch negatives
and sampled softmax · **negative sampling strategy as the dominant quality lever** · hard negative
mining · embedding index refresh and staleness.
*Contrast with cross-encoders,* which score query and item jointly for higher accuracy at
prohibitive cost — hence their use in re-ranking only.

**5. Approximate nearest neighbour search** — [KNOW]
Exact versus approximate search · inverted file indexes · HNSW graphs · product quantisation ·
the recall-versus-latency-versus-memory trade-off · *connects to the vector database material in
Week 10, Part A*

**6. Ranking models over sparse features** — [BUILD]
High-cardinality categorical features · **embedding tables** as the production mechanism for
identifiers · hashing tricks and collision behaviour · why embedding tables dominate model memory
while the dense layers dominate arithmetic — *and why this makes recommendation models a distinct
systems problem from language models* · feature crosses · **DLRM-style architecture**
*Reference:* *Deep Learning Recommendation Model for Personalization and Recommendation Systems*
(Naumov et al., 2019) · *Deep Neural Networks for YouTube Recommendations* (Covington et al., 2016)

**7. Learning-to-rank** — [KNOW]
Pointwise, pairwise and listwise formulations · why pointwise regression on clicks optimises the
wrong objective when the goal is ordering · BPR and pairwise logistic loss · LambdaRank [AWARE]

**8. Ranking metrics** — [BUILD]
Precision@k and recall@k · mean average precision · **NDCG** and the role of the position discount ·
mean reciprocal rank · coverage and diversity · *why accuracy and AUC are inadequate: both are
insensitive to where in the ordering an error occurs, and only the top positions are seen*

**9. Calibration** — [BUILD]
The distinction between ranking correctly and predicting probability correctly · reliability
diagrams · Platt scaling and isotonic regression · **why calibration is mandatory when the score
enters an economic calculation** — an advertising auction multiplies predicted click probability by a
bid, so a systematically inflated probability produces systematically mispriced inventory.
*Version 1.0 mentioned calibration once, in passing, inside an industry table.*

**10. Position and selection bias** — [KNOW]
Users click higher-ranked items because they are higher-ranked · the model trains on logs produced by
the previous model, so the feedback loop is closed and self-confirming · inverse propensity weighting
· randomised exploration traffic as the source of unbiased data · **why offline evaluation on logged
data systematically overestimates a new ranker**

**11. Serving considerations** — [KNOW]
Feature stores and **training/serving skew** as the characteristic production defect · online versus
offline feature computation · embedding refresh cadence · retraining frequency ·
real-time versus batch candidate generation

**12. Graph neural networks** — [AWARE] *(added in v2.0)*
Message passing and neighbourhood aggregation · GraphSAGE-style sampling for large graphs ·
applications to recommendation over user-item graphs and to fraud and abuse detection.
Recognition level: know what problem they solve and why sampling is necessary at scale.

*Resources:* Andrew Ng Machine Learning Specialization course 3 (recommenders section) ·
Google Recommendation Systems course
https://developers.google.com/machine-learning/recommendation ·
*Designing Machine Learning Systems* (Chip Huyen) · Google Rules of Machine Learning
https://developers.google.com/machine-learning/guides/rules-of-ml ·
RecSys conference proceedings · Papers With Code recommendation section

### 8.6 Assessment questions

- Why does text preprocessing matter? What distinguishes TF-IDF from learned embeddings?
- Why are transformers the current standard in NLP? When is LSTM still appropriate?
- What distinguishes object detection from segmentation? Why is YOLO selected for real-time systems?
- How does GPT generate text stepwise? Why is fine-tuning required?
- Why is RAG preferred to pure prompting? Why does parameter-efficient fine-tuning matter?
- Why is LLM evaluation harder than conventional ML evaluation?

*Added in v2.0 — reinforcement learning:*
- What is the reward model in RLHF trained on, and why is a KL penalty applied against the reference
  policy? What happens without it?
- What does DPO remove from the RLHF pipeline, and what is traded away?
- Describe reward hacking with a concrete example.

*Added in v2.0 — ranking and retrieval:*
- Why does production ranking use two stages rather than one model over the full corpus?
- Why must a two-tower model's scoring function factorise into a dot product? What breaks if it does
  not?
- A ranking model achieves 0.85 AUC and ranks badly. How is that possible, and which metric would
  have revealed it?
- A model ranks well but its predicted probabilities are inflated by 30%. For which applications does
  this matter, and for which does it not?
- Your new ranker beats the incumbent on logged data and loses in an online experiment. Give the most
  likely cause.
- Where does the memory footprint of a large recommendation model actually sit, and how does that
  differ from a language model of similar parameter count?

### 8.7 Deliverables — Portfolio artefacts 5 and 6

**Artefact 5 — Fine-tune an open-weight language model using LoRA or QLoRA on a domain dataset,
integrated into a retrieval-augmented generation pipeline.** Includes dataset preparation, training
configuration, before-and-after evaluation, retrieval design, and a working demonstration published
to Hugging Face. *Added in v2.0:* include an adversarial section — attempt indirect prompt injection
through a retrieved document and document the outcome and mitigation.

**Artefact 6 — Two-stage retrieval and ranking system** *(added in v2.0)*.
On a public interaction dataset (MovieLens, an e-commerce or news click log, or comparable):

1. **Retrieval** — a two-tower model with an approximate nearest neighbour index over item
   embeddings. Report recall@k against a held-out set. Compare at least two negative-sampling
   strategies and explain the difference in results.
2. **Ranking** — a feature-rich second-stage model (gradient boosting is acceptable and often
   correct) over retrieval candidates. Report NDCG@k and MAP against a popularity baseline and a
   random baseline.
3. **Calibration** — a reliability diagram for the ranker's scores, before and after calibration.
4. **Honest evaluation** — a temporal split, not a random one, with a written explanation of why a
   random split leaks; and a written statement of which biases the offline evaluation cannot remove.
5. **Serving sketch** — latency budget per stage, what is precomputed versus computed at request
   time, and the retraining and index-refresh cadence.

*This artefact is deliberately weighted toward evaluation honesty rather than model complexity. A
simple ranker evaluated correctly is a stronger signal than a complex one evaluated with a leaking
split, and the second is a common and immediately visible failure in candidate portfolios.*

### 8.8 REAL-WORLD APPLICATIONS AND INDUSTRY USE CASES

| Industry | Application | Role of this module's material |
|---|---|---|
| **Enterprise knowledge management** | Internal documentation assistants, policy question answering | RAG is the dominant enterprise LLM pattern: it grounds responses in proprietary documents without retraining and provides source citation for auditability |
| **Financial services** | Research summarisation, regulatory monitoring, KYC document processing | Domain fine-tuning adapts general models to specialised terminology; retrieval anchors outputs to current regulation |
| **Healthcare** | Clinical documentation, literature review, patient communication drafting | Fine-tuned models over clinical corpora with retrieval across current guidelines to control factual drift |
| **Legal** | Contract analysis, precedent retrieval, due diligence | Retrieval over case and contract repositories; hallucination control is a professional liability requirement |
| **E-commerce** | Product description generation, visual search, review summarisation | Combined vision-language pipelines; CLIP-class models enable natural-language image search |
| **Media and creative industries** | Image and video generation, localisation, asset production | Diffusion models in commercial content pipelines; latent diffusion made this economically viable |
| **Customer experience** | Multilingual support agents, intent routing, quality analysis | Agent frameworks orchestrate retrieval, tool invocation and escalation |
| **Manufacturing and field service** | Maintenance manual assistants, diagnostic support | RAG over technical documentation delivered to field technicians on mobile devices |
| **Insurance** | Claims document extraction, damage assessment from imagery | Combined NLP and vision pipelines processing mixed-modality claim submissions |
| **Public sector** | Citizen service automation, document digitisation, accessibility | Translation, summarisation and OCR pipelines at population scale |
| **Social platforms** *(v2.0)* | Feed ranking, connection recommendation, notification targeting | Two-stage retrieval and ranking over sparse identifier embeddings. This is the largest single deployment of machine learning by engineer headcount at consumer-scale organisations |
| **Advertising** *(v2.0)* | Ads retrieval, click and conversion prediction, auction pricing | Ranking plus **calibration**: the auction multiplies predicted probability by bid, so an uncalibrated model misprices inventory directly. Position bias correction determines whether the model learns preference or learns rank order |
| **Search and marketplaces** *(v2.0)* | Query-to-item retrieval, relevance ranking, sponsored placement | Two-tower retrieval with approximate nearest neighbour indexes, then cross-encoder re-ranking of the shortlist |
| **Streaming and short-form video** *(v2.0)* | Candidate generation and watch-time ranking | Real-time candidate generation with explore/exploit via bandits; feedback loops and popularity bias are the central engineering problem |
| **Trust and safety** *(v2.0)* | Abuse, spam and fraud ranking | Graph neural networks over user-interaction graphs; extreme class imbalance makes ranking metrics the only meaningful evaluation |

**Commercial significance.** LoRA and QLoRA are the reason enterprise LLM customisation is
affordable: full fine-tuning of a large model requires substantial multi-accelerator
infrastructure, whereas low-rank adaptation trains a small fraction of the parameters and often runs
on a single device. RAG addresses the two principal enterprise objections to LLM adoption — factual
reliability and the inability to incorporate proprietary or current data — which is why it appears
in the majority of production enterprise deployments.

**Commercial significance of Track D** *(added in v2.0)*. Ranking quality converts to revenue more
directly than almost any other machine learning output: a single-digit percentage improvement in a
ranking metric on a large platform is a material revenue figure, which is why these teams are large,
well-resourced and continuously hiring. The corresponding professional risk is equally direct — an
uncalibrated or bias-confirming ranker degrades the product while reporting improved offline
numbers, and the offline/online divergence problem is the reason experimentation discipline (Week 2,
Part B2) and ranking engineering are inseparable skills.

**Roles dependent on this module:** LLM and Generative AI Engineer · NLP Engineer · Computer Vision
Engineer · **Recommendation and Ranking Engineer** · **Search and Relevance Engineer** ·
**Ads Machine Learning Engineer** · AI Solutions Architect · Applied Scientist ·
Conversational AI Engineer

---

## WEEK 9 — MLOps, Deployment, Data Engineering and Responsible AI

> **This module addresses the structural gap in the source material, which sequences Week 22
> directly to Week 24, leaving "Stage 5 — MLOps" referenced in the final checklist without a
> corresponding module.**

### 9.1 Module objective

Transition a model from notebook to production system, operating reliably and responsibly.

### 9.2 PART A — MLOps and deployment — [BUILD]

- **Serialisation** — `state_dict`, TorchScript, ONNX export
- **Service layer** — Flask · FastAPI · request and response schemas · asynchronous handling · batching
- **Demonstration interfaces** — Streamlit · Gradio
- **Containerisation** — Dockerfile authoring, layer caching, image size, non-root execution,
  Docker Compose
- **Experiment tracking** — MLflow · Weights & Biases · run comparison · artefact management
- **Model versioning and registry** · model cards
- **CI/CD** — GitHub Actions: test, lint and build on push
- **Monitoring** — latency, error rate, **data drift**, **model drift**, alerting
- **Release strategy** — canary deployment · A/B testing · rollback procedures
- **Cloud platforms** — AWS and GCP fundamentals · Kubernetes [AWARE]
- **Cost management** — accelerator-hour accounting, inference cost per thousand requests

### 9.3 PART B — Data Engineering Foundations

**1. Data Pipelines** — [BUILD]
ETL (Extract, Transform, Load) · ELT workflows · Data ingestion systems · Batch versus scheduled

**2. Data Warehousing** — [KNOW]
Snowflake · Google BigQuery · AWS Redshift · Analytical storage concepts

**3. Batch versus Stream Processing** — [KNOW]
Batch (offline) · Stream (real-time) · Kafka · Apache Beam · Spark Streaming

**4. Querying and Data Access — advanced** — [BUILD]
Window functions · Common Table Expressions (CTEs) · query plans and why an index changes one
*SQL is assessed in interview considerably more often than is generally anticipated — which is why
v2.0 moved the foundations forward to Week 2, Part F rather than introducing SQL for the first time
in Week 9 of 11. Joins and aggregation are assumed here.*

**5. Data Versioning** — [KNOW] · DVC (Data Version Control) · Delta Lake
**6. Data Validation and Quality** — [KNOW] · Great Expectations · Deequ · Quality check design

*Resources:* Data Engineering Zoomcamp (DataTalksClub) https://www.youtube.com/c/DataTalksClub ·
TechWorld with Nana https://www.youtube.com/c/TechWorldwithNana ·
Snowflake https://www.snowflake.com · BigQuery https://cloud.google.com/bigquery ·
Kafka https://kafka.apache.org · Delta Lake https://delta.io

### 9.4 PART C — AI Ethics, Fairness and Privacy

**Bias in AI** — [BUILD] · Dataset imbalance · Label bias and skew · Fairness metrics
**Interpretability** — [BUILD] · SHAP (feature attribution) · LIME (local explanation) ·
Attention visualisation
**Privacy** — [KNOW] · Differential privacy · PII masking · Secure data handling
**Explainable AI** — [KNOW] · Model transparency · Stakeholder trust · Decision explanation
**Legal and Compliance** — [AWARE] · GDPR · HIPAA · EU AI Act · DPDP (India)
**Security** — [KNOW] *(added in v2.0)* · Threat modelling for ML systems · training-data poisoning ·
model and prompt extraction · adversarial examples · **the distinction between compliance and
security**: a system can satisfy every documentation obligation and remain trivially exploitable.
LLM-specific attack surface is covered in Week 8, Track C, Topic 12.

*Resources:* Google Responsible AI https://ai.google/responsibilities ·
IBM AI Ethics https://www.ibm.com/ai/ethics · EU AI Act https://artificialintelligenceact.eu ·
NIST AI Risk Management Framework https://www.nist.gov/itl/ai-risk-management-framework ·
IBM Technology https://www.youtube.com/c/IBMTechnology · DeepLearning.ai https://www.deeplearning.ai

### 9.5 PART D — ML system design — [BUILD]

> **Added in v2.0.** Version 1.0 marked ML system design `[BUILD]` in Week 10 but produced no design
> artefact, and covered the topic in four lines in Section 10.13. It also listed *Designing Machine Learning
> Systems* in the resource index without ever assigning it to a week. ML system design is a distinct
> interview round with its own failure modes, and it is the round in which an otherwise strong
> candidate most often loses points for lack of structure rather than lack of knowledge.

**Assigned reading:** *Designing Machine Learning Systems* (Chip Huyen) — read during Weeks 9 and 10,
one chapter per day. Supplement: Google Rules of Machine Learning
https://developers.google.com/machine-learning/guides/rules-of-ml ·
*Machine Learning System Design Interview* (Aminian and Xu).

**The framework.** Every design answer follows the same skeleton. Memorise the skeleton; the content
varies by problem, the structure does not.

| Step | What is established | Characteristic failure |
|---|---|---|
| **1. Clarify** | Business objective, scale, latency budget, existing system | Designing before asking; solving the wrong problem elegantly |
| **2. Frame as ML** | Is ML warranted? What is the prediction target? Is it ranking, classification, regression, generation? | Accepting an ML framing that a heuristic would serve better |
| **3. Define metrics** | Offline metric, online metric, guardrails, and the expected gap between them | Naming accuracy for a ranking problem |
| **4. Data** | Sources, labels, volume, freshness, label delay, biases in collection | Assuming clean labels exist |
| **5. Features** | Feature families, computation location, **training/serving skew** | Proposing features that cannot be computed at request time |
| **6. Model** | Baseline first, then complexity, with the trade-off stated | Opening with a transformer when a baseline is undefined |
| **7. Training** | Split strategy (temporal, not random), retraining cadence, compute | Random splits on temporal data — an instant credibility loss |
| **8. Evaluation** | Offline protocol, online experiment design, ramp plan | No plan for validating the change in production |
| **9. Serving** | Architecture, latency budget per component, batching, caching, precomputation | Ignoring the latency budget declared in step 1 |
| **10. Monitoring** | Drift, degradation, alerting, rollback, feedback loops | Treating deployment as the end of the problem |
| **11. Trade-offs and scale** | Bottlenecks, cost, failure modes, what breaks at 10× | Presenting a design with no acknowledged weakness |

**The eight canonical problems.** Written up in full, one per sitting, timed at 45 minutes to
simulate interview conditions. These cover the great majority of what is actually asked:

1. **Feed ranking** for a social platform
2. **Video or content recommendation** with watch-time as the objective
3. **Ad click-through prediction** with auction pricing and calibration requirements
4. **Search ranking** for a marketplace or document corpus
5. **Abuse, spam or fraud detection** under extreme class imbalance and adversarial adaptation
6. **ETA or demand prediction** for a logistics or ride-hailing product
7. **A retrieval-augmented enterprise assistant**, including grounding, evaluation and injection risk
8. **An inference serving platform** for a large language model, with cost per token as the objective
   *(this is the design problem most relevant to semiconductor and infrastructure organisations, and
   it depends on Week 10)*

**Method.** Write the design as a document, then present it aloud against a timer without reading
from it. The written form builds the reasoning; the spoken form is what is assessed. Problems 1–4
depend on Week 8, Track D; problem 8 depends on Week 10.

**Completion test.** Given an unfamiliar prompt, produce a structured whiteboard design in 45 minutes
that reaches serving and monitoring — not one that runs out of time at feature engineering, which is
the most common way this round is failed.

### 9.6 Assessment questions

- Why are data pipelines critical to AI systems? What distinguishes ETL from ELT?
- When is batch processing appropriate versus streaming? Why does data versioning matter?
- Why is bias consequential in AI systems? Why is explainability required in enterprise contexts?
- How do privacy regulations constrain model design?
- A deployed model's accuracy declines eight percent over three months with no redeployment.
  Identify the cause and the monitoring that would have detected it earlier.
- What is training/serving skew, how does it arise, and what structurally prevents it?
- Why is a temporal split required for a model that will predict future events?
- A system meets every documentation and compliance obligation. Give three ways it could still be
  exploited.

### 9.7 Deliverables — Portfolio artefacts 7 and 8

**Artefact 7 — Deploy a previously built model.** FastAPI endpoint, Dockerfile, running container,
experiment tracking integration, logging and monitoring, SHAP-based prediction explanations, and a
model card documenting intended use, limitations and identified bias risks. Optional extension: a
GitHub Actions CI pipeline.

**Artefact 8 — ML system design portfolio** *(added in v2.0)*.
Three of the eight canonical problems in Part D, written up in full and committed to the repository.
Each document follows the eleven-step framework, states its latency and cost budget explicitly, and
includes an architecture diagram and a section titled "what breaks at ten times the scale".

*This artefact costs writing time rather than compute time, which is why it fits inside the existing
ten weeks. It is also the artefact most directly predictive of performance in the design round,
and reviewers read it — a candidate who has written three designs answers the fourth visibly better
than one who has written none.*

### 9.8 REAL-WORLD APPLICATIONS AND INDUSTRY USE CASES

| Industry | Application | Role of this module's material |
|---|---|---|
| **All AI-deploying organisations** | Transition from prototype to production | A large proportion of models developed never reach production. The competencies in this module are the difference between a demonstration and a system |
| **Banking and lending** | Regulated model deployment | Model cards, audit trails, explainability and versioning are supervisory requirements. SHAP and LIME outputs are used to satisfy adverse-action notification obligations |
| **Healthcare** | Clinical decision support deployment | Regulatory approval requires documented intended use, validated performance boundaries and monitoring for population drift |
| **E-commerce and streaming** | Continuously retrained recommendation systems | Feature stores, scheduled pipelines and automated retraining; drift detection triggers retraining as consumer behaviour shifts |
| **Ride-hailing and delivery** | Real-time pricing and dispatch | Streaming pipelines feed models under sub-second latency requirements; canary deployment limits the blast radius of a defective release |
| **Telecommunications** | Network operations automation | Streaming telemetry at extreme volume; batch and stream processing coexist within a single architecture |
| **Insurance and HR technology** | Fairness auditing under legal obligation | Bias measurement and mitigation are legally mandated in several jurisdictions for hiring and underwriting decisions |
| **Public sector** | Citizen-facing automated decisions | The EU AI Act imposes graduated obligations by risk classification; high-risk systems require documented risk management |
| **Any organisation handling personal data** | Privacy-preserving machine learning | GDPR, HIPAA and DPDP determine what data may be retained, for how long, and what a data subject may require to be deleted — constraints shaping architecture from the outset |

**Commercial significance.** Model drift is the defining operational risk of production machine
learning: a model degrades silently while continuing to return confident predictions. Monitoring
infrastructure converts that from an incident discovered by customers into an alert addressed by
engineers. Regulatory exposure is also increasing globally; documentation, explainability and bias
auditing have moved from optional good practice to compliance obligation across finance, healthcare,
employment and public services.

**Roles dependent on this module:** MLOps Engineer · ML Platform Engineer · Data Engineer ·
Site Reliability Engineer · AI Governance Specialist · Solutions Architect

---

### 9.9 AI ethics, fairness, privacy and explainability - expanded reference

> **Compressed in v2.0.** The topic list in v1.0 duplicated Week 9, Part C line for line. The
> substantive material — bias, interpretability via SHAP and LIME, privacy, explainability,
> compliance, and (new in v2.0) security — now lives in **Week 9, Part C**, where it is taught
> alongside the deployment work it constrains. Only the exercise, which is not duplicated, is
> retained here.

**Deployment contexts:** Enterprise AI · Healthcare AI · Financial services AI · Government systems ·
Large-scale consumer products

**Exercise.** Select one AI system — automated loan approval or CV screening. Identify bias risks,
specify an explainability approach, and define a privacy protection strategy. *Added in v2.0:* add a
fourth section identifying one way the system could be attacked rather than merely be unfair; these
are separate analyses and interviewers ask about both.

**Professional relevance.** Ethics questions appear routinely in senior technical interviews, and a
model card present in a candidate's repository signals a level of professional maturity that
distinguishes a small minority of applicants.

---

## WEEK 10 — Systems, GPU Performance, Inference Optimisation and Career Conversion

> **This module is entirely absent from the source material.** It distinguishes engineers who can
> apply models from engineers who can make them efficient, and constitutes the principal technical
> hiring criterion at semiconductor, hardware and AI-infrastructure organisations.

### 10.1 Module objective

Develop the capability to measure, optimise and evidence system performance, then convert the
programme's output into professional opportunity.

### 10.2 PART A — Systems thinking and AI infrastructure

**1. ML System Design (Production Architecture)** — [BUILD]
Model serving architecture · Model versioning · Canary deployment · Feature stores ·
Data pipelines · Monitoring systems

**2. Vector Databases** — [KNOW] · Vector search · FAISS · Pinecone · Weaviate · ChromaDB

**3. Distributed Training** — [KNOW]
Data parallelism · Model parallelism · Pipeline parallelism · Tensor parallelism ·
DistributedDataParallel (DDP) · FSDP · ZeRO and DeepSpeed · Horovod [AWARE] · Collective
communication libraries [AWARE]

**4. Hardware Awareness** — [KNOW]
Datacentre GPUs · TPUs · NPUs · Inference latency optimisation · Batch size tuning ·
Latency versus throughput · P50 and P99 characterisation

**5. The descent from model to hardware** — [KNOW] *(added in v2.1)*

*Version 2.0 taught profiling and kernel authoring but treated everything between the Python call and
the hardware as opaque. For a semiconductor or framework target that middle region is the job. This
topic establishes the map at [KNOW]; **Section 10.17** takes it to [BUILD].*

Trace one operation — `y = x @ w` — all the way down, and name each layer it passes through:

| Layer | What happens | Who owns it in industry |
|---|---|---|
| **Model code** | `torch.matmul`, an `nn.Module` call | Applied ML engineer |
| **Framework API** | Python binding into the framework's C++ core | Framework engineer |
| **Dispatcher** | Selects an implementation by device, dtype and autograd state | Framework engineer |
| **Operator library** | The registered kernel for that backend | Framework / vendor enablement |
| **Compiler (if compiled)** | Graph capture → fusion → code generation | Compiler engineer |
| **Math library** | A tuned GEMM in a vendor library | Vendor library engineer |
| **Kernel** | The launched GPU program | Kernel engineer |
| **ISA and hardware** | Matrix instructions, memory system, interconnect | Hardware / architecture |

**Why this matters as a diagnostic skill, not trivia.** Almost every real performance or correctness
problem lives at exactly one of these layers, and the fix at the wrong layer does nothing. A slow
model may be slow because of a Python-level data dependency, a dispatcher falling back to a generic
implementation, a missing fusion, an untuned library path for that shape, a poorly written kernel, or
a memory-system limit. The professional competency being hired for is **locating the layer first**.
Version 2.0 taught how to measure; this teaches where to look.

### 10.3 PART B — GPU execution model — [KNOW] → [BUILD]

- CPU versus GPU execution models · SIMT · warps and wavefronts · threads, blocks, grids
- **Memory hierarchy** — registers → shared memory and LDS → L2 → HBM
- **Why memory bandwidth, rather than arithmetic throughput, is typically the binding constraint**
- **Roofline model** · arithmetic intensity · compute-bound versus memory-bound classification
- Occupancy · memory coalescing · kernel launch overhead
- **Numerical precision** — FP32 · TF32 · FP16 · BF16 · FP8 · INT8; dynamic range versus precision
  and the failure mode of each
- Tensor Cores and Matrix Cores — operand shapes and alignment requirements
- CUDA · cuDNN · cuBLAS at concept level

### 10.3a PART B, continued — Vendor software stacks and reading-level C++ — [KNOW]

*Added in v2.0. Version 1.0 taught CUDA "at concept level (no C++ requirement)" and named no AMD
software component other than the two profilers. For a target that includes semiconductor
organisations, that is under-specified: the work in these teams is conducted against these stacks by
name.*

**The two stacks, in correspondence.** Learning one and mapping across is far more efficient than
learning either in isolation, and the mapping itself is a legitimate interview topic:

| Function | NVIDIA | AMD |
|---|---|---|
| Language and runtime | CUDA | **HIP** (source-portable; CUDA code ports mechanically in most cases) |
| Dense linear algebra | cuBLAS | rocBLAS / hipBLAS |
| Deep learning primitives | cuDNN | **MIOpen** |
| Collective communication | NCCL | **RCCL** |
| Tunable kernel templates | CUTLASS | **Composable Kernel** |
| System profiler | Nsight Systems | **rocprof** |
| Kernel profiler | Nsight Compute | **Omniperf** |
| Device query | `nvidia-smi` | `rocm-smi` |
| Datacentre architecture | Hopper / Blackwell class | **CDNA** class, with Matrix Cores |
| Python-level kernel authoring | Triton | **Triton** (same tool, both backends) |

*Resource:* ROCm documentation https://rocm.docs.amd.com

**Reading-level C++** — [KNOW], not [BUILD]
The objective is to read a kernel, a framework operator or a library header and understand what it
does; it is *not* to become a C++ engineer. Sufficient scope: types and references · headers and
compilation units · templates enough to read them · RAII · pointers and memory layout ·
`__global__` and `__device__` qualifiers · reading a launch configuration.

**Why this is worth the time.** Version 1.0 correctly noted (Section 10.14.3) that the deepest roles at
semiconductor organisations are C and C++ disciplines and that a Python-only path is a deliberate
narrowing. It then provided no means of narrowing it less. Reading-level competence is a few days of
work and materially widens the accessible role surface; write-level competence is a separate
undertaking and is out of scope here.

### 10.4 PART C — Profiling and measurement — [BUILD]

- `torch.profiler` · **`torch.cuda.synchronize()`** — asynchronous execution invalidates naive
  wall-clock timing
- NVIDIA Nsight Systems and Nsight Compute
- AMD rocprof and Omniperf
- Trace interpretation — synchronisation points, host-to-device transfers, dataloader stalls, idle gaps
- Bottleneck taxonomy — dataloader-bound · CPU-bound · memory-bound · compute-bound

### 10.5 PART D — Optimisation and inference — [BUILD]

- `torch.compile` and TorchInductor · graph breaks · operator fusion · CUDA graphs
- **FlashAttention** — the canonical memory-bound-to-tiled optimisation study
- **Quantisation** — post-training versus quantisation-aware training · per-tensor versus
  per-channel · calibration · INT8 and INT4 · GPTQ · AWQ
- Pruning · structured sparsity · knowledge distillation
- **KV cache optimisation** · paged attention · continuous batching
- **ONNX** export and ONNX Runtime · opset compatibility · graph optimisation
- **TensorRT** and TensorRT-LLM · **vLLM** · Triton Inference Server
- **MLPerf** benchmark methodology: https://mlcommons.org

**Edge, client and NPU inference** — [KNOW] *(expanded in v2.1; this was a single bullet in v2.0)*

*The datacentre is not the only deployment target, and for several major silicon vendors it is not
the primary one. Client and edge inference is a distinct engineering discipline with its own
runtimes, its own constraints and its own hiring demand. This is the in-programme survey;
**Section 10.17, Stage 6** takes it to [BUILD].*

- **Why the client is different** — no discrete accelerator memory, power and thermal envelopes as
  hard constraints rather than cost considerations, unpredictable shared hardware, and a single
  concurrent user instead of a batch. Almost every datacentre assumption inverts.
- **NPUs** — dedicated low-power inference silicon, distinct from CPU and GPU. Characteristically:
  integer-first arithmetic, restricted operator support, a preference for static shapes, and
  excellent performance per watt inside those constraints and poor performance outside them.
- **ONNX Runtime and the Execution Provider model** — the dominant cross-vendor deployment path on
  the client. An EP is a hardware backend plugged into a common runtime; the runtime partitions the
  graph and assigns subgraphs to the EP that supports them, falling back to CPU otherwise.
- **The runtime landscape** — ONNX Runtime · **LiteRT** (the renamed TensorFlow Lite) ·
  **ExecuTorch** (PyTorch's on-device runtime) · vendor SDKs beneath all of them
- **Quantisation is mandatory here, not optional** — most NPUs are integer-first, so an unquantised
  model may not execute on the accelerator at all
- **Graph partitioning as the dominant performance factor** — an unsupported operator in the middle
  of a model splits the graph and forces data movement between processors; the number of partitions
  frequently matters more than the quality of any individual kernel
- Power, thermal throttling, and sustained versus peak performance
- **MLPerf Client, Mobile and Tiny** as the benchmark suites for these targets

**Added in v2.0 — decode-side optimisations.** Version 1.0 established that decode is
memory-bandwidth-bound but omitted the principal techniques that exploit that fact. Since this module
is the differentiating one for the stated target, the omission mattered more than its size:

- **Speculative decoding** — [KNOW]. A small draft model proposes several tokens; the target model
  verifies them in a single forward pass. The insight is that verification of *k* tokens costs
  approximately one forward pass, so a bandwidth-bound decode can be converted into a
  better-utilised one at no accuracy cost, since rejected tokens are discarded. Acceptance rate is
  the governing parameter. *Reference:* *Fast Inference from Transformers via Speculative Decoding*
  (Leviathan et al.).
- **Self-speculative and multi-token prediction variants** — [AWARE].
- **GQA and MQA at serving time** — [KNOW]. The architectural side is Week 7, Topic 9; here the
  concern is the resulting KV-cache budget and the batch size it permits.
- **MoE serving** — [AWARE]. Expert placement, routing imbalance, and why a sparse model with high
  parameter count is a memory-capacity problem rather than an arithmetic one.
- **Online-softmax and tiling as a general pattern** — [BUILD]. FlashAttention is the canonical
  instance, but the pattern — restructure the computation so intermediates stay in fast memory and
  the normaliser is accumulated in a single pass — is the reusable idea, and it is what Part E asks
  you to implement. Numerical foundation: Week 7, Topic 10.
- **FlashAttention lineage** — [AWARE]. FlashAttention-2 and FlashAttention-3 improve work
  partitioning and exploit newer hardware features; know that the line exists and that kernel
  performance tracks hardware generations rather than being solved once.
- **Continuous batching in practice** — [KNOW]. Why static batching wastes capacity when sequence
  lengths differ, and how request-level scheduling recovers it.

### 10.6 PART E — Kernel authoring in Python

**OpenAI Triton** (https://triton-lang.org) enables GPU kernel authoring in Python, executing on both
NVIDIA and AMD hardware without C++.

Official tutorial sequence: vector addition → fused softmax → matrix multiplication → layer
normalisation → attention. Each kernel is benchmarked against the framework equivalent, with the
performance difference explained through roofline analysis.

**Prerequisite made explicit in v2.0.** The fused-softmax kernel requires the max-subtraction and
online-normaliser technique from Week 7, Topic 10. Version 1.0 asked for this kernel without
teaching that anywhere, which would have produced either a numerically unstable kernel or a copied
one. Confirm that material before starting.

**Cross-vendor exercise** *(added in v2.0)*. Triton compiles for both backends from identical Python.
Where two devices are accessible, run the same kernel on both and compare achieved bandwidth against
each device's specification. Where only one is accessible, state which device produced the numbers —
an unattributed benchmark is not evidence. Optional extension for candidates targeting semiconductor
organisations: express one kernel in HIP as well, to demonstrate the source-level correspondence
described in Section 10.3a.

### 10.7 PART F — Portfolio and competitive exposure

**Practice and competition**
Kaggle — competitions, real datasets, progression toward Expert: https://www.kaggle.com ·
Hackathons — Zindi https://zindi.africa · Devpost https://devpost.com · Omdena ·
LeetCode https://leetcode.com · StrataScratch · Codeforces

**Public professional profile**
- **GitHub** — project code, notebooks, deployment work, READMEs presenting measured results
- **Medium or Hashnode** — project write-ups, technical explanations
- **LinkedIn** — progress updates, project demonstrations
- **Hugging Face** — published models and demonstration Spaces

**Open source contribution** — one merged pull request to PyTorch, vLLM, Triton, ONNX Runtime,
scikit-learn or Hugging Face. Documentation, test and small-defect contributions are the appropriate
entry point.

### 10.8 PART G — Interview preparation

**1. ML System Design** — data pipelines · feature stores · serving APIs · monitoring
**2. Technical Interviews** — ML algorithms · deep learning concepts · mathematics ·
project-based questioning · model selection and trade-off reasoning
**3. Coding Interviews** — data structures · algorithms · problem-solving patterns · ML logic problems
**4. Behavioural Interviews** — STAR method · collaboration · problem-solving narratives ·
product reasoning
**5. Research Literacy** — architecture comprehension and concept-level reimplementation,
beginning with *Attention Is All You Need* and the ResNet publication

### 10.9 Learning resources

- Full Stack Deep Learning: https://www.youtube.com/c/FullStackDeepLearning
- NVIDIA Developer: https://www.youtube.com/c/NVIDIADeveloper
- NVIDIA CUDA documentation: https://developer.nvidia.com/cuda-zone
- Triton: https://triton-lang.org
- MLCommons and MLPerf: https://mlcommons.org
- Pinecone https://www.pinecone.io · Weaviate https://weaviate.io · FAISS https://faiss.ai
- DataTalksClub — ML System Design: https://www.youtube.com/c/DataTalksClub
- AI Coffee Break: https://www.youtube.com/c/AICoffeeBreak

### 10.10 Assessment questions

- Why is system design critical to production AI? When does distributed training become necessary?
- Why is GPU optimisation critical for large models? How does hardware influence model performance?
- Inference is measured at three times the expected latency. Describe the diagnostic procedure.
- Is single-batch transformer decoding compute-bound or memory-bound? Justify the answer.
- INT8 quantisation has reduced accuracy by four percent. Identify the next three remediation steps.
- Explain a machine learning project end to end, including model selection rationale.
- Why can speculative decoding produce a speedup at no cost in output quality? *(added in v2.0)*
- Mixed precision was enabled and throughput did not improve. Give three possible explanations and
  the measurement that would distinguish between them.
- Name the AMD counterpart to NCCL, cuDNN and Nsight Compute, and state what HIP is for.
- A benchmark reports a mean latency of 40 ms and a P99 of 900 ms. What is likely occurring?

### 10.11 Deliverables — Portfolio artefacts 9, 10 and 11

> **Corrected in v2.0.** Version 1.0 headed this section "Portfolio artefacts 7 and 8" while listing
> three deliverables, and the profiling study appeared in neither the Overview C.4 catalogue nor the
> Overview F.2 register. It was, in effect, an unnumbered orphan. All three items are now numbered and
> registered.

**Artefact 9 — Profiling study.** Profile the Week 7 mini-GPT, identify the three principal
bottlenecks, remediate them, and publish before-and-after measurements with supporting trace
evidence. Classify each bottleneck by type (dataloader-bound, CPU-bound, memory-bound,
compute-bound) and state how the classification was established, not merely asserted. Include the
KV-cache measurement recorded in Week 7.

**Artefact 10 — Kernel implementation and benchmark.** One Triton kernel (fused softmax or layer
normalisation) benchmarked against the framework baseline, with roofline-supported analysis. Report
achieved memory bandwidth as a percentage of the device specification, and name the device.

**Artefact 11 — Multi-backend inference study.** One model across three backends (eager PyTorch →
ONNX Runtime → TensorRT or vLLM) at two or three quantisation levels. Tabulated latency, throughput,
memory footprint and accuracy, with written explanation of each measured difference. *Added in v2.0:*
report P50 and P99 latency separately, not a mean — the mean conceals precisely the tail behaviour
that determines whether a service meets its budget.

**Artefact 11 is the highest-value item in the portfolio.** Fine-tuning capability is common among
applicants; the ability to diagnose and remediate performance is not.

### 10.12 REAL-WORLD APPLICATIONS AND INDUSTRY USE CASES

| Industry | Application | Role of this module's material |
|---|---|---|
| **Semiconductor and hardware vendors** | Model enablement, framework integration, kernel libraries, MLPerf submission | Entire engineering organisations exist to make models execute efficiently on specific silicon. Profiling, kernel authoring and quantisation constitute the daily work of these teams |
| **Cloud and AI infrastructure providers** | Inference serving platforms, capacity planning | Serving cost per token is the defining unit economic of an inference business; a 20% throughput improvement is a 20% margin improvement at constant price |
| **Language model providers** | Production serving at scale | Continuous batching, paged attention and KV-cache management determine how many concurrent users a given hardware allocation can serve |
| **Mobile and consumer electronics** | On-device inference | Aggressive quantisation to INT8 or INT4 is mandatory rather than optional; power draw and thermal envelope are hard constraints, and NPU offload is the enabling mechanism |
| **Automotive** | In-vehicle perception under real-time constraint | Inference must complete within a fixed frame budget on fixed hardware. Optimisation is a functional safety requirement, not a performance preference |
| **Healthcare imaging** | High-throughput scan processing | Batch inference over large volumes, where throughput determines whether a department can process its daily caseload |
| **Financial trading** | Low-latency inference | Tail latency (P99) is the operative metric; microsecond-level optimisation carries direct revenue consequence |
| **Robotics and industrial automation** | Embedded perception and control | Constrained compute, power and memory budgets on embedded accelerators |
| **Video platforms** | Content moderation, recommendation, transcoding at scale | Inference cost across billions of daily items makes per-item optimisation a major infrastructure line |
| **Scientific computing** | Large-scale training campaigns | Distributed training efficiency determines whether a training run completes within its allocated cluster window |

**Commercial significance.** This module addresses the point at which machine learning becomes an
economics problem. A model twice as fast costs approximately half as much to serve, supports twice
the user load on identical hardware, or enables deployment on cheaper hardware entirely. At
production scale these are the largest available cost levers. The distinguishing professional
capability is diagnostic: determining whether a workload is memory-bound or compute-bound
establishes which optimisations can possibly help, and prevents extended effort on approaches that
cannot succeed.

**Roles dependent on this module:** AI Performance Engineer · Inference Engineer · ML Systems
Engineer · GPU and Kernel Engineer · ML Infrastructure Engineer · Edge AI Engineer ·
Model Enablement Engineer

---

### 10.13 Interview preparation

#### 8.1 Data structures and algorithms — continuous from Week 1

> **Rewritten in v2.0.** Version 1.0 set a target of 150–200 problems at three to five per week,
> which delivers 30–50 problems across ten weeks — roughly a quarter of its own target — and
> deferred the remainder to an unspecified "intensively thereafter". Since the coding rounds are the
> highest-variance filter for an undergraduate candidate, an unscheduled three-quarters of the
> requirement is the single largest structural defect in the original document. The block is now
> 1.0 hr/day (Section 0.3) and the volume is scheduled, in-programme and in Section 10.16.

**Target: 150–200 problems, of which approximately 110 fall inside the programme.**

##### Weekly allocation

| Weeks | Pattern focus | Problems | Difficulty |
|---|---|---|---|
| 1a–1b | Arrays and hashing · two pointers | 16–20 | Easy, moving to medium |
| 2 | Sliding window · prefix sums | 8–10 | Easy and medium |
| 3 | Binary search (including on the answer) · sorting | 8–10 | Medium |
| 4 | Stacks · queues · monotonic stack | 8–10 | Medium |
| 5 | Linked lists · fast and slow pointers | 8–10 | Easy and medium |
| 6 | Trees · BFS and DFS · recursion | 8–10 | Medium |
| 7 | Graphs · topological sort · union-find | 8–10 | Medium |
| 8 | Heaps · intervals · greedy | 8–10 | Medium |
| 9 | Dynamic programming, part 1 — one dimension | 8–10 | Medium |
| 10 | Dynamic programming, part 2 — two dimensions · tries · backtracking | 8–10 | Medium and hard |
| **Conversion phase** | Mixed review, timed sets, weak patterns | **40–90** | Medium and hard |

Graph traversal is deliberately aligned with Week 2, Part D, where BFS, DFS and DAGs are taught
mathematically; and with Week 5, where the autograd computation graph makes the reverse topological
traversal concrete. The tracks reinforce each other where they can.

##### Method

The volume matters less than the method, and this is where most self-directed preparation fails:

1. **Twenty-five minutes, then look.** Beyond that, unassisted struggle stops teaching. Read the
   solution, understand it completely, then close it and reimplement from nothing.
2. **Re-solve, do not re-read.** A problem understood is not a problem retained. Anything that took
   help returns to the queue after 7 days and again after 21.
3. **State complexity aloud before coding**, and again after. Interviewers ask; fluency is audible.
4. **Speak while solving from Week 4 onward.** Silent solving trains a skill that is not the one
   assessed. The assessed skill is solving while narrating.
5. **Maintain a pattern log**, not a problem log — one line per pattern recording the trigger that
   identifies it. Roughly fifteen patterns cover the large majority of what is asked; recognising
   which one applies is the actual skill.
6. **Do not grind Hard problems.** Medium fluency with clean communication outperforms sporadic Hard
   solutions, and the interview distribution is weighted to medium.

##### Mock interviews

From **Week 7**, one 45-minute mock per week, escalating to two per week in Section 10.16. Speaking under
observation is a separate skill from solving, it degrades under pressure, and it cannot be acquired
in the final week. Peers, Pramp-style pairing platforms, or a recorded session reviewed afterwards
are all acceptable; solving alone in silence is not.

**Platforms:** LeetCode https://leetcode.com · NeetCode pattern lists https://neetcode.io ·
StrataScratch (SQL) · Codeforces (optional, contest practice only)

#### 8.2 ML and deep learning theory — assessed conceptually

- Explain backpropagation; derive it for a two-layer network
- Justify AdamW over SGD; identify when SGD is preferable
- Describe BatchNorm behaviour at inference versus training
- Present cases where precision and recall respectively dominate
- Describe overfitting detection and remediation
- Explain attention; justify the scaling factor and multi-head design
- Illustrate the bias–variance tradeoff from personal project experience

*Added in v2.0 — topics that were assessed but untaught in the original document:*
- Describe the two-stage retrieval-and-ranking architecture and justify why one model is insufficient
- Explain NDCG and why AUC is inadequate for a ranking problem
- Explain calibration, and name an application where ranking correctly is not sufficient
- Explain why offline ranking evaluation on logged data is optimistically biased
- Walk through the RLHF pipeline and state what the KL penalty prevents; contrast DPO
- Design an A/B test for a model change: randomisation unit, metrics, sample size, stopping rule
- Explain the difference between compute-bound and memory-bound, and how you would establish which
  applies to a given workload

#### 8.3 Python depth
Generators · decorators · the GIL · memory model · context managers · `__slots__` ·
mutable default arguments · comprehension semantics · shallow versus deep copy

#### 8.4 ML system design

**Taught in Week 9, Part D** — the eleven-step framework, the eight canonical problems, and the
written deliverable (artefact 8). *Version 1.0 covered this round in the two lines that previously
occupied this section, with no framework, no practice problems and no deliverable.*

Interview preparation here is repetition, not new material: **three additional problems from the
Part D list of eight, presented aloud against a 45-minute timer.** Six total (three written as
artefact 8, three spoken) is a defensible level of preparation for the round.

The most common failure is running out of time before reaching serving and monitoring. The remedy is
budgeting explicitly — approximately five minutes on clarification, ten on data and features, ten on
modelling, fifteen on serving and scale, five on trade-offs — and stating the budget aloud at the
start, which also demonstrates the structure to the interviewer.

#### 8.5 Computer science fundamentals

**Taught as a continuous track from Week 1** — see Section 1.7, Track 2, which supplies the operating
systems and computer architecture resources. *Version 1.0 assessed the topics in this section without
teaching them anywhere in the document; the resources now exist.*

Assessed scope: memory hierarchy and cache behaviour · threads versus processes · virtual memory and
paging · concurrency, locks and race conditions · deadlock conditions · networking at [AWARE] ·
numerical representation, including why floating-point comparison requires a tolerance.

**Weighting by target.** For semiconductor, infrastructure and performance roles this is assessed
directly and repeatedly, and Week 10 depends on it. For product-focused machine learning roles it
appears less often, but the memory hierarchy material remains the foundation of the roofline
reasoning in Week 10 and is not optional on that basis alone.

#### 8.6 Behavioural — STAR framework
Situation, Task, Action, Result. Six prepared narratives: a difficult defect, a disagreement,
a failure, a delivered system, rapid learning under pressure, and an occasion of being wrong.

#### 8.7 Project defence

For each of the eleven portfolio artefacts: the problem addressed, the rationale for the approach,
the measured results, what would be changed, and what proved unexpected.

Prepare a **two-minute** and a **ten-minute** version of each. The two-minute version is what is
actually requested; the ten-minute version is what follow-up questions extract. Every number quoted
must be one you can source, and every artefact must have at least one honest weakness you can name
before being asked — an artefact presented as flawless invites the interviewer to find the flaw.

**Preparation exercise:** one project explained end to end · five algorithmic problems solved ·
one algorithm explained in depth · one publication summarised · one system design presented aloud
against a timer.

---

### 10.14 Career tracks and specialisation lanes

#### 9.1 Specialisation domains

| Domain | Market rationale |
|---|---|
| **NLP and Large Language Models** | Currently the largest area of hiring demand |
| **Vision and Robotics** | Convergence of hardware and AI; embedded deployment |
| **Generative AI** | Image, video, audio and code generation |
| **BioAI and MedAI** | Personalised medicine, protein structure, drug discovery |
| **Autonomous Systems** | Automotive, drones, industrial autonomy |
| **FinTech AI** | Risk modelling, algorithmic trading, fraud prevention |
| **Multi-modal AI** | Combined text, image and audio understanding |
| **Agentic AI** | Autonomous agents, planning and tool use |
| **AI Systems and Performance** *(added)* | Kernel engineering, inference optimisation, ML infrastructure |

#### 9.2 Role mapping

| Role | Core competency | Modules of greatest relevance |
|---|---|---|
| Machine Learning Engineer | End-to-end pipelines, deployment | 4–5, 10 |
| Deep Learning Engineer | Architectures, training | 6–9 |
| Applied Scientist | Research and implementation | 8–9, Section 7.9 |
| MLOps and Platform Engineer | Infrastructure, CI/CD, monitoring | 10–11 |
| Data Engineer | Pipelines, warehousing, SQL | 3 Part F, 10 Part B |
| **AI Performance and Inference Engineer** | Profiling, kernels, quantisation | **11**, 14 Stages 2–3 |
| LLM and Generative AI Engineer | Fine-tuning, RAG, agents, serving | 9 Track C |
| **Recommendation, Ranking and Search Engineer** *(added in v2.0)* | Retrieval, ranking, calibration, experimentation | **9 Track D**, 3 Part B2, 10 Part D |
| AI Research Engineer | Publications, novel architectures | 8, Sections 1.18 and 7.9 |
| **Model Enablement Engineer** *(added in v2.1)* | Bring-up, numerical parity, operator coverage, vendor stack | **14 Stages 1, 3, 5**, 11 |
| **Framework Integration Engineer** *(v2.1)* | Dispatcher, backend registration, operator libraries, upstreaming | **14 Stages 1–2**, 11 |
| **GPU / Kernel Engineer** *(v2.1)* | HIP and Triton kernels, architecture-aware tuning | **11 Part E, 14 Stage 3** — *plus write-level C++ beyond this document* |
| **ML Systems / Training Infrastructure Engineer** *(v2.1)* | Distributed training, collectives, scaling efficiency | **14 Stage 4**, 11 Part A, 10 |
| **Benchmarking and Validation Engineer** *(v2.1)* | MLPerf methodology, CI matrices, regression detection | **14 Stage 5**, 11 |
| **Edge / Client AI Engineer** *(v2.1)* | On-device runtimes, execution providers, power-constrained deployment | **14 Stage 6**, 11 Part D |
| **NPU Software / Model Optimisation Engineer** *(v2.1)* | Quantisation, graph partitioning, operator coverage on fixed-function silicon | **14 Stage 6**, 14 Stage 5, 11 Part D |
| **Execution Provider / Runtime Integration Engineer** *(v2.1)* | ONNX Runtime EPs, delegates, backend partitioners | **14 Stages 2 and 6** |

#### 9.3 Semiconductor, hardware and AI-infrastructure organisations

A substantial class of Python-primary roles exists at these organisations: model enablement,
framework integration, inference and deployment engineering, quantisation tooling, MLPerf
benchmarking, applied deep learning, deep learning library validation, and Triton kernel authoring.

**The differentiating module is Week 10, not Week 8.** Fine-tuning competence is widely held. The
combined ability to profile a model, establish that decode is memory-bandwidth-bound, author a fused
kernel and evidence the speedup through roofline analysis is rare and directly hireable.

**A qualification worth stating explicitly:** the deepest roles at these organisations — driver,
compiler, kernel library and firmware engineering — are C and C++ disciplines. A Python-only
trajectory is entirely viable, but represents a deliberate narrowing.

*Revised in v2.0.* Version 1.0 asserted that reading-level C++ "approximately doubles the accessible
role surface" — a quantitative claim with no cited basis, and it is removed rather than repeated. The
defensible statement is narrower and sufficient: **a candidate who cannot read a kernel or a
framework operator is excluded from a set of roles that a few days of reading-level study would open,
and the cost of acquiring that is small relative to the rest of this programme.** Section 10.3a now
provides the scope, and Section 10.3a's stack correspondence table is what makes it efficient — one
stack learned, the other mapped.

**Also revised in v2.0.** Version 1.0 named only two AMD tools in the entire document (rocprof and
Omniperf) while positioning semiconductor organisations as a primary target. Section 10.3a now names
the ROCm stack — HIP, MIOpen, RCCL, Composable Kernel, CDNA-class Matrix Cores — against its NVIDIA
counterparts, because these teams discuss their work in those terms and a candidate who cannot is
visibly outside the conversation.

#### 9.4 Conversion strategy

- **Internships** offer the highest conversion probability to full-time employment
- **Kaggle placement** provides an externally verifiable credential
- **A merged open-source contribution** is the strongest single signal available; reviewers are
  frequently employed by target organisations
- **Public technical writing** — a published analysis of a profiling study or kernel implementation
  generates inbound visibility
- **Referrals** — earned through substantive technical engagement, once artefacts exist
- **CV structure** — built around the eleven artefacts with measured results, not course completions
- **Academic standing** — remains a filter in many campus recruitment pipelines

#### 9.5 Application mechanics and timing

> **Added in v2.0.** Version 1.0 addressed how to become qualified but not how to apply, which is a
> serious omission for an undergraduate audience. For a student, **timing is frequently the binding
> constraint rather than skill**: large organisations recruit for internships and new-graduate
> positions on fixed annual cycles, high-volume programmes close when filled rather than at a
> published deadline, and a candidate who becomes ready one month after the cycle closes waits
> approximately a year regardless of how strong the portfolio is.

**The scheduling principle.** Determine the application window for each target organisation *before*
beginning the programme, and work backwards from it. Do not begin a ten-week programme and then
discover when applications open.

| Action | When | Note |
|---|---|---|
| Identify target organisations and role families | **Before Week 1** | Determines whether to weight Week 8 Track D or Week 10 |
| Confirm each organisation's application window from its own careers page | **Before Week 1** | Cycles differ by organisation, region and programme, and change year to year — verify at source rather than relying on any summary, including this one |
| Set calendar reminders for each window opening | Week 0 | High-volume programmes frequently close early |
| CV drafted with the artefacts that exist so far | Week 5 | It is revised, not written from scratch, later |
| Referral conversations begun | Weeks 7–8 | Once two or three artefacts are presentable; a referral request backed by visible work is a different proposition from a cold one |
| Applications submitted | **When the window opens** — not when preparation feels complete | Readiness is never subjectively complete; the window is real |
| Mock interviews at two per week | Section 10.16 | Begins once applications are submitted, since the screen may arrive quickly |

**Two structural points, both commonly mishandled:**

Apply when the window opens, not when you feel ready. Screening and onsite loops are typically
separated by weeks, and that interval is usable preparation time. A submitted application with two
artefacts and four weeks of preparation before the screen beats a perfect application submitted after
the window closed.

Referral timing is a trade-off. Too early and there is nothing to show; too late and the window has
closed. Weeks 7–8 is the point at which artefacts 1 through 4 exist and the strongest ones are still
being built — a legitimate position from which to open a conversation.

**A caution on sources.** Application dates, loop formats and process details for individual
organisations are not stated in this document because they change and because stating them
unverified would be worse than omitting them. Read each organisation's own careers pages, and treat
second-hand accounts of interview processes as unverified.

#### 9.6 Continuing currency

- Weekly review of arXiv or Papers With Code
- Tracking of major research organisations' releases
- Newsletters: The Batch (Andrew Ng) · Import AI (Jack Clark) · Latent Space
- Monitoring of trending open-source repositories

> Knowledge in this field decays rapidly. Adaptation is itself a professional competency.
> Ten delivered projects outweigh ten thousand pages of theory.

---

### 10.15 Professional skills and domain knowledge

*Developed continuously rather than as a discrete module.*

> **Reweighted in v2.0.** Version 1.0 gave equal prominence to communication, documentation, Agile
> process and *leading ML teams*. For an undergraduate targeting an individual-contributor entry
> role, team leadership is not assessed and process methodology is learned on the job in days. The
> two items that *are* assessed — communication and technical writing — are retained at full weight;
> the remainder is demoted.

**Communication** — [BUILD]
Explaining models to non-technical stakeholders · business impact narrative ·
data-driven decision communication
→ *Assessed directly. Every artefact defence, every design presentation and every behavioural round
is a communication assessment wearing a technical costume.*

**Technical writing and documentation** — [BUILD]
Model cards · technical documentation · README authoring · ethical declarations · research records
→ *Assessed indirectly and continuously: reviewers read the repository before they meet the
candidate, and a README is the first writing sample submitted whether intended as one or not.*

**Domain expertise** — [KNOW]
Finance · Healthcare · Robotics and automation · Gaming · E-commerce · Consumer platforms
→ *Domain knowledge is what renders a model production-ready rather than merely accurate. Depth in
one domain is worth more than familiarity with five.*

**Project planning and execution** — [AWARE — *demoted*]
Agile methodology · Jira workflow · Scrum · Sprint planning · AI project lifecycle
→ *Recognise the vocabulary; do not study it. It is acquired in the first fortnight of employment.*

**Leadership** — [AWARE — *demoted*]
Mentoring · feature ownership · technical decision-making
→ *Not assessed for entry-level individual-contributor roles. Relevant in three to five years, at
which point this document is no longer the right guide.*

*Resources:* Atlassian Agile guides https://www.atlassian.com/agile ·
Google Model Cards https://modelcards.withgoogle.com ·
Microsoft Responsible AI https://www.microsoft.com/ai

**Exercise.** Select one domain specialisation · produce one model explanation for a non-technical
audience · produce one project documentation sample.

**Real-world relevance.** The proportion of an engineer's impact attributable to communication rises
sharply with seniority. Technical decisions are approved or rejected on the basis of how they are
presented, and a model that stakeholders do not understand does not get deployed regardless of its
measured performance.

---

### 10.16 Conversion phase - interview execution

> **Added in v2.0.** Version 1.0 ended at Week 10 and deferred the remaining interview volume to
> "intensively thereafter" — an undefined period with no schedule, no targets and no completion test,
> covering roughly three-quarters of its own stated algorithm requirement. This Part defines it.

**Duration:** four to six weeks, run **in parallel with a live application process** rather than
before it. Applications are submitted when the window opens (Section 9.5), not when this phase ends.

**Objective:** convert a qualified candidate into an offer. No new subject matter is introduced. The
work is volume, speed, and performance under observation.

#### 13.1 Weekly structure

| Block | Hours/day | Content |
|---|---|---|
| **Algorithms** | 2.0 | 10–15 problems/week, medium and hard, timed |
| **Mock interviews** | 1.0 | Two per week minimum, at least one with a person |
| **System design** | 0.5 | One problem written or presented per week |
| **Artefact defence and behavioural** | 0.5 | Rotating through the eleven artefacts and six STAR narratives |

#### 13.2 Targets

| Item | Programme total | Conversion phase | Cumulative |
|---|---|---|---|
| Algorithm problems | ≈110 | 40–90 | **150–200** |
| Mock interviews | 4 | 8–12 | **12–16** |
| System designs (written or presented) | 6 | 4–6 | **10–12** |
| Artefacts defended aloud | — | All 11, twice | — |

#### 13.3 Week-by-week

**Weeks 1–2 — Volume and diagnosis.** Timed mixed sets, two problems per 45 minutes, no topic
labels. The absence of a topic label is the point: identifying which pattern applies is the skill
being tested, and a labelled problem set does not test it. Log every failure by pattern. The output
of these two weeks is a ranked list of weak patterns.

**Weeks 3–4 — Targeted repair and design.** Attack the weak patterns from the log, not the
comfortable ones. Two mocks per week. Present two system designs aloud. Rehearse the six STAR
narratives (Section 10.13.6) aloud until they are 90 seconds rather than five minutes.

**Weeks 5–6 — Simulation and sustaining.** Full-loop simulations: two coding rounds, one design
round, one behavioural round, in a single sitting, to build the specific stamina a real loop
requires. Sustain 10 problems per week. Do not learn new material in these weeks.

#### 13.4 Behavioural preparation

The six narratives specified in Section 10.13.6 (a difficult defect, a disagreement, a failure, a delivered
system, rapid learning under pressure, and an occasion of being wrong), each rehearsed to a
90-second spoken version with a specific result attached.

The failure and the being-wrong narratives are the two most commonly under-prepared and the two most
frequently asked. A narrative in which nothing actually went wrong, or in which the fault lay
entirely with someone else, reads as evasion. Prepare a real one with a real lesson.

#### 13.5 Running a live process

- **Track every application** with the date submitted, stage reached and outcome. Pattern-match your
  own rejections: consistently failing at the coding screen is a different problem from consistently
  failing at the onsite, and the remedies share nothing.
- **Request feedback** where a process permits it; many do not.
- **Treat the gap between screen and onsite as scheduled preparation time.** It is typically weeks,
  and it is the highest-leverage preparation window available because the target is now known.
- **A rejection is one sample.** Loop outcomes at large organisations carry substantial variance from
  interviewer assignment and problem selection alone. Reapplication is usually permitted after a
  cooling-off period; treat a single rejection as information, not verdict.

#### 13.6 Completion test — Section 10.16

Two medium problems solved and explained in 45 minutes, cold, while narrating. An unfamiliar system
design taken to serving and monitoring in 45 minutes. Any of the eleven artefacts defended for ten
minutes under follow-up questioning without reference notes.

When those three are reliable, preparation is no longer the constraint — and the remaining variance
is outside your control, which is the correct point at which to stop preparing and start applying
more widely.

---

### 10.17 Model-to-hardware specialisation track

> **Added in v2.1.** This Part is **Lane B** (Section 0.8): the specialisation track for semiconductor
> vendors, accelerator and infrastructure providers, and framework teams. It is the answer to a
> specific question the earlier versions of this document could not answer — *what does a model
> enablement, framework integration or performance engineer at a silicon company actually do all
> day, and how do I become able to do it?*
>
> **Prerequisites:** Weeks 1–10 complete, including artefacts 9, 10 and 11. Reading-level C++ per
> Section 10.3a. The descent map in Week 10, Part A, Topic 5.
>
> **Duration:** eight to twelve weeks beyond the programme. It is not compressible into Week 10 and
> is not represented as being so.
>
> **Depth policy:** everything here is [BUILD] or [KNOW]. There is no [AWARE] tier in this Part —
> awareness of a stack you are being hired to work inside is not a qualification.

#### 14.0 Why this Part exists

Week 10 produces an engineer who can measure a model and optimise it from the outside. That is
genuinely rare and genuinely hireable. But the roles this Part targets require working *inside* the
stack: registering an operator, explaining why the compiler broke a graph, porting a kernel between
vendor languages, establishing that a numerical difference is tolerance and not a bug, and getting a
model to run correctly on hardware it has never run on before.

That work has a shape, and the shape is the same everywhere: **descend the stack until you find the
layer that owns the problem, fix it at that layer, and prove the fix with a number.** The five stages
below follow the descent.

| Stage | Layer | Weeks | Artefact |
|---|---|---|---|
| **1** | Framework internals — dispatcher, autograd, memory, streams | 2–3 | 12 |
| **2** | Compiler and graph — Dynamo, Inductor, XLA, ONNX, MLIR | 2 | 13 |
| **3** | Vendor stack — HIP, ROCm libraries, CDNA execution model | 2–3 | 14, 15 |
| **4** | Scale — distributed training and collective communication | 1–2 | 16 |
| **5** | The job itself — model bring-up, parity, coverage, benchmarking | 2 | 17 |
| **6** | Edge, NPU and client AI — runtimes, execution providers, vendor stacks | 2–3 | 18, 19 |

**Stages 1–5 descend the datacentre stack; Stage 6 applies the same descent to client and edge
silicon**, which is a large and separately-staffed part of what semiconductor vendors do. Both AMD
and Qualcomm ship substantial client AI software organisations, and the deployment path there —
ONNX Runtime execution providers, LiteRT, ExecuTorch, and vendor NPU toolchains — shares almost no
tooling with the ROCm datacentre path in Stage 3. Take Stage 6 if client, mobile, automotive or
embedded AI is in scope for your target; it is independent of Stages 3 and 4 and can be taken
without datacentre hardware.

**A standing accuracy warning for this Part.** Framework internals and vendor stacks change faster
than any other material in this document — APIs are renamed, tools are superseded, and file paths
move between releases. Everything here is written at the level of *mechanism and concept*, which is
stable, rather than exact signatures, which are not. **Verify every API, flag, environment variable
and tool name against the current official documentation before relying on it**, and treat any
specific name in this Part as a search term rather than a citation. This applies with particular
force to ROCm, where tool naming has changed across releases.

---

#### 14.1 STAGE 1 — Framework internals — [BUILD]

*The objective: stop treating PyTorch as an API and start treating it as a system you can open.*

##### 14.1.1 How a call becomes a kernel

Follow one operator from Python to the backend and be able to draw the path from memory:

- **The Python-to-C++ boundary** — what the Python `torch` module is actually calling into
- **ATen** — PyTorch's tensor and operator library; the operator schema and what a schema declares
- **The dispatcher** — the central mechanism. Dispatch is keyed on device (CPU, CUDA/HIP, others),
  dtype, layout and whether autograd is active. Understand that **autograd is itself a dispatch
  layer**, not a special case bolted on: the autograd key intercepts, records, and redispatches to
  the backend key.
- **Backend registration** — how a kernel is registered against a key, and therefore how a *new
  backend* is added to PyTorch. This is the single most relevant internal mechanism for a vendor
  enablement role, because it is the mechanism by which a vendor's hardware becomes usable from
  framework code.
- **Fallback behaviour** — what happens when a backend has no kernel registered for an operator, why
  a silent fallback to a generic or CPU path is a common cause of a mysteriously slow model, and how
  to detect it.
- **Composite versus explicit kernels** — why some operators need no per-backend implementation
  because they decompose into others, and the performance consequence of relying on decomposition.

##### 14.1.2 Autograd internals

- The autograd graph as a DAG built during the forward pass — *this is Week 2, Part D, Topic 2 made
  concrete, and Week 1's vector-Jacobian product made mechanical*
- `torch.autograd.Function` — writing a custom forward and backward, and the contract between them
- **`gradcheck`** — numerical verification of an analytic backward against finite differences. This
  is the standard correctness gate for a new operator and you should be fluent with it.
- Backward formula registration — where the derivative of an operator is declared
- Non-differentiable and in-place operations · why in-place operations can corrupt the graph
- `retain_graph`, `create_graph`, and double backward
- Hooks — inspecting and modifying gradients in flight, as a debugging instrument

##### 14.1.3 Memory and the allocator

- **The caching allocator** — why a framework does not call the driver allocator on every tensor, and
  what "reserved" versus "allocated" memory means in the framework's own reporting
- **Fragmentation** — how a long training run exhausts memory without a leak, and why the failure is
  intermittent and load-dependent
- Allocator configuration via environment variable (name and options: verify in current PyTorch
  documentation — this is exactly the kind of detail that changes between releases)
- Memory snapshots and the allocator's own profiling output
- Activation memory versus parameter memory versus optimiser state — and which of the three
  gradient checkpointing actually trades away
- **Pinned host memory** and why it changes host-to-device transfer behaviour
- Reading a memory profile well enough to say *which* of those four categories is the problem

##### 14.1.4 Asynchronous execution, streams and events

- **The single most common measurement error in the field:** GPU launches are asynchronous, so naive
  wall-clock timing measures launch time, not execution time. Week 10 introduced
  `torch.cuda.synchronize()`; here, understand exactly *why* it is required and what it costs.
- Streams as ordered queues · concurrency between independent streams · events for cross-stream
  dependency and for correct timing
- **Accidental synchronisation** — the operations that silently force a sync (moving a value to the
  host, printing a tensor, control flow that branches on a tensor value, `.item()`), why each
  destroys pipelining, and how to find them in a trace
- Host-side launch overhead as a bottleneck class in its own right, and why very small kernels can be
  launch-bound rather than compute- or memory-bound
- CUDA/HIP graphs as the mitigation for launch-bound workloads

##### 14.1.5 Custom operators, end to end — [BUILD]

The stage's central exercise. Implement one non-trivial operator (a fused activation, a small
normalisation variant, or a simple attention component) and take it all the way:

1. A reference implementation in Python, treated as ground truth
2. A Triton or native kernel implementation
3. Registration through the framework's custom-operator mechanism so it dispatches correctly
4. A custom backward, verified with `gradcheck`
5. `torch.compile` compatibility — confirm it does not force a graph break, and fix it if it does
6. A test suite covering dtypes, shapes including edge cases, non-contiguous inputs, and empty tensors
7. A benchmark against the composed-operator baseline, with the speedup explained by roofline

**Why this is the highest-value exercise in Section 10.17.** It is a compressed version of the actual job:
the artefact demonstrates that you can add capability to a framework rather than only consume it, and
almost no applicant at entry level has done it.

##### 14.1.6 TensorFlow, JAX and the multi-framework reality — [KNOW]

*Included because the target explicitly names TensorFlow, and because vendor enablement teams support
more than one framework whether they would prefer to or not.*

- **`tf.function` and graph mode** — the tracing model, and how it differs from PyTorch's eager
  default; what retracing is and why it silently destroys performance
- **XLA** — the compiler shared by TensorFlow and JAX; **HLO** as its intermediate representation ·
  `jit_compile` · why XLA's static-shape preference conflicts with dynamic-shape workloads
- **JAX** — functional transformation model (`jit`, `grad`, `vmap`, `pmap`) and why a
  transformation-based design is easier for a compiler to target than an imperative one
- **Keras 3 as a multi-backend layer** across TensorFlow, JAX and PyTorch
- **SavedModel and the deployment surface** · LiteRT for on-device
- The comparison that gets asked in interviews: eager-with-tracing-compiler (PyTorch) versus
  graph-first (TensorFlow) versus functional-with-compiler (JAX), and the engineering trade-off each
  represents for a hardware vendor trying to support all three

##### 14.1.7 Stage 1 assessment questions

- Trace `torch.matmul(a, b)` from the Python call to a vendor GEMM. Name every layer.
- Where does autograd sit relative to the backend dispatch, and why does that ordering matter?
- A model runs on a new backend but at one-tenth of the expected speed with no obvious hot kernel.
  Give the two mechanisms you would suspect first and how you would confirm each.
- A twelve-hour training run fails with an out-of-memory error at hour nine, having used the same
  batch size throughout. What is the most likely cause?
- Why does `print(loss)` inside a training loop degrade throughput?
- You timed a kernel at 0.1 ms and the model did not get faster. What did you measure?
- What is `gradcheck` for, and what class of bug does it not catch?
- Why is a static-shape compiler a poor fit for variable-length sequence workloads?

##### 14.1.8 Artefact 12 — Custom operator with full framework integration

Deliver Section 14.1.5 as a repository: kernel, registration, custom backward, `gradcheck` evidence,
test suite, `torch.compile` compatibility statement, benchmark table, and a written walkthrough of
the dispatch path the operator takes. The walkthrough is a substantial part of the value — it is the
document that proves you understand the mechanism rather than having followed a template.

---

#### 14.2 STAGE 2 — The compiler and graph layer — [BUILD]

*The objective: be able to explain, and influence, what the compiler did to your model.*

##### 14.2.1 Graph capture

- **Why capture at all** — an eager framework cannot fuse across operations it cannot see; capturing a
  graph is what makes fusion, layout choice and scheduling possible
- **TorchDynamo** — bytecode-level capture producing an FX graph
- **Graph breaks** — the central practical concept. Data-dependent control flow, unsupported calls and
  host-side interaction force the compiler to give up and fall back to eager for a region. Learn to
  *find* breaks with the framework's own reporting tools, understand *why* each occurred, and remove
  the ones that are removable.
- **Guards and recompilation** — what conditions the compiled artefact assumed, why violating one
  triggers recompilation, and why a model that recompiles constantly is slower than one never compiled
- **Dynamic shapes** — the tension between specialising on a shape (fast, brittle) and generalising
  over shapes (portable, slower); why variable sequence length is the hard case
- **AOTAutograd** — capturing forward *and* backward together, which is what allows the backward pass
  to be optimised rather than merely executed

##### 14.2.2 Lowering and code generation

- **TorchInductor** — the default backend compiler: lowering the captured graph, then generating
  **Triton** kernels for GPU targets and C++ for CPU. *Note the significance for Lane B: the
  compiler's GPU output is Triton, which means the kernel language from Week 10, Part E is also the
  compiler's own target language.*
- **Fusion** — vertical (elementwise chains) and its limits; why fusion is the single highest-value
  graph optimisation for memory-bound workloads, and why it barely helps compute-bound ones
- **Layout and memory format** — channels-last versus contiguous; why layout choice can matter more
  than kernel quality, and where layout conversions get inserted
- Constant folding · dead code elimination · common subexpression elimination
- **Autotuning** — how a compiler selects among candidate kernel configurations, what it costs at
  compile time, and caching of the results
- Reading generated code: open the emitted Triton kernel and confirm the fusion you expected happened

##### 14.2.3 Graph-level intermediate representations

- **FX** — PyTorch's graph representation; graph transformation as an exercise in reading and rewriting
  a DAG
- **ONNX** — the interchange format in practice: opset versioning, why export fails on dynamic control
  flow, what a "custom op" means at the ONNX boundary, and graph optimisation in ONNX Runtime.
  *Week 10 used ONNX as a backend; here you look inside the graph and modify it.*
- **HLO** (XLA) and **MLIR** at concept level — MLIR's contribution is the idea of *multiple levels*
  of IR with progressive lowering between them, which is the organising principle of most current ML
  compilers. Know why that matters: a vendor adds hardware support by implementing a lowering, not by
  rewriting a compiler.
- **Where a vendor plugs in** — the three realistic integration points are a backend for the existing
  compiler, a custom operator library, or a whole-graph replacement runtime; know the trade-off of
  each

##### 14.2.4 Stage 2 assessment questions

- What is a graph break, what causes them, and why does one in a hot loop matter more than one at
  model construction?
- Why does the same model recompile repeatedly, and what would you change?
- Fusion doubled the throughput of one model and did nothing for another. Explain both outcomes with
  the roofline model.
- Why does ONNX export fail on data-dependent control flow, and what are your options?
- What does MLIR's multi-level design buy a hardware vendor?
- `torch.compile` made a model *slower*. Give three plausible explanations.

##### 14.2.5 Artefact 13 — Compiler investigation report

Take the Week 7 mini-GPT and one third-party model. For each: enumerate every graph break with its
cause, remove those that are removable, record compilation and recompilation counts, extract and read
at least one generated kernel to confirm an expected fusion, and tabulate eager versus compiled
throughput and memory. Then explain each measured difference by mechanism — not "compilation helped",
but *which* transformation produced *which* part of the gain.

---

#### 14.3 STAGE 3 — The vendor stack: HIP, ROCm and the AMD execution model — [BUILD]

*The objective: work fluently in AMD's stack, and be able to move between vendor stacks rather than
being resident in one.*

> **Naming and versioning warning, restated because it matters most here.** ROCm component and tool
> names have changed across releases — profilers in particular have been renamed and superseded.
> Treat every name below as a **search term for the current documentation at
> https://rocm.docs.amd.com**, not as a verified current API. The concepts are stable; the names are
> not. Stating a tool invocation from memory in an interview and being wrong is worse than saying
> "there's a profiler for that, and I'd check the current name."

##### 14.3.1 Getting real hardware access

This is the practical obstacle, and it should be solved before the stage begins rather than
discovered mid-stage.

| Route | Notes |
|---|---|
| **Cloud instances with AMD accelerators** | Several providers offer them; availability and pricing change, so check current offerings. Usually the most direct route to genuine CDNA-class hardware |
| **Consumer AMD GPU with ROCm support** | Lower cost, but support is limited to specific architectures — verify your exact part against the current ROCm compatibility list before buying anything |
| **Containers** | AMD publishes ROCm and framework container images; this removes most environment setup pain and is the recommended starting point |
| **Concept-only fallback** | Stages 14.3.2 and 14.3.5 (porting and architecture) can be studied without hardware; the benchmarking work cannot. **Do not report numbers you did not measure** — an unattributed or fabricated benchmark is the fastest way to lose credibility with this audience |

**Environment fundamentals:** ROCm installation and version checking · `rocm-smi` for device, clock,
power and memory state · device visibility environment variables · the ROCm container images ·
confirming a framework build is genuinely using the accelerator rather than silently running on CPU.

##### 14.3.2 HIP and portability — [BUILD]

**HIP is the pivot skill for this lane.** It is a C++ dialect closely paralleling CUDA, which means one
kernel-programming model gets you both vendors, and the *translation between them* is itself a large
part of what enablement teams do.

- The HIP programming model — kernels, launch configuration, memory management, streams and events —
  and its correspondence to CUDA construct by construct
- **The `hipify` tooling** — source-to-source translation of CUDA to HIP. Run it on real CUDA code and
  study the output.
- **What does *not* translate mechanically**, which is the interesting part and the part interviews
  probe: warp/wavefront size assumptions, warp-level primitives, inline assembly and intrinsics,
  vendor-library calls with no direct counterpart, hardware-specific instruction usage, and
  occupancy or shared-memory sizing tuned for a different architecture
- Conditional compilation for portable source that targets both vendors
- Reading a kernel and identifying its portability hazards *before* porting it

**The exercise:** take a real CUDA kernel from an open-source project, port it with `hipify`, fix what
the tool could not, verify numerical equivalence against the original, and benchmark both if you have
access to both. Write up every manual intervention and why it was needed. **This is very close to
actual day-one work at a GPU vendor.**

##### 14.3.3 The ROCm library stack — [KNOW]

Know what each library is for, when the framework calls it, and what to do when it is the bottleneck.
The NVIDIA correspondence table in Section 10.3a is the map; this is the detail.

- **rocBLAS / hipBLAS / hipBLASLt** — dense linear algebra and GEMM. Understand that GEMM performance
  is **shape-dependent**: a library may have a well-tuned path for one matrix shape and a poor one for
  another, which is why an unusual shape can be unexpectedly slow. This is a real and frequent
  enablement finding.
- **MIOpen** — deep learning primitives (convolution and related). Algorithm selection and
  autotuning; the tuning cache and why the first run differs from later runs.
- **RCCL** — collective communication, the counterpart to NCCL. Stage 4 uses it.
- **Composable Kernel** — templated, tunable kernel building blocks; the counterpart in role to
  CUTLASS. Concept level: understand *why* a template library exists rather than hand-written kernels,
  namely that the tuning space is too large to explore by hand.
- **hipSPARSE, hipFFT, rocRAND** and the rest of the maths libraries — [KNOW] by name and purpose
- **Where the framework meets the library** — how PyTorch's backend chooses a library path, and how to
  determine which path a given operation actually took

##### 14.3.4 PyTorch on ROCm — [BUILD]

Practical specifics that surprise people coming from CUDA:

- **The `torch.cuda` namespace is used on ROCm builds.** This is deliberate for portability, and
  regularly confuses newcomers: `torch.cuda.is_available()` returning `True` on an AMD system is
  correct behaviour, not a bug.
- Identifying whether a build is a ROCm build, and which ROCm version it was built against
- Which features have full, partial or no support on the ROCm path — and, more importantly, **how to
  find out** for a given release rather than assuming parity
- Triton on the ROCm backend, including for `torch.compile`-generated kernels
- `torch.profiler` on ROCm and what appears in a trace
- Building PyTorch from source against ROCm — [KNOW]; do it once if hardware permits, because
  enablement work frequently requires a source build
- **TensorFlow on ROCm** — a ROCm-targeted build exists; verify current support status and version
  matrix in the documentation rather than assuming

##### 14.3.5 CDNA execution model and the hardware layer — [BUILD]

This is where the "hardware" half of the target is actually earned. Everything here is a *difference
that changes how you write and tune code*, not trivia.

- **Wavefront of 64 on CDNA versus a warp of 32 on NVIDIA.** The single most consequential difference
  for a ported kernel: block-size choices, occupancy arithmetic and any code with a hard-coded 32
  must all be revisited. Verify wavefront width for the specific target architecture rather than
  assuming.
- **Compute units** and their relationship to the thread-block scheduling model
- **Matrix Cores and MFMA instructions** — the matrix-multiply-accumulate hardware; supported operand
  shapes, data types and alignment requirements, and why a shape that does not map onto them falls
  back to a much slower path
- **LDS (Local Data Share)** as the counterpart to shared memory · bank conflicts · why tiling
  strategy is architecture-specific
- **Memory system** — HBM bandwidth as the usual binding constraint (Week 10's central claim, now at
  the hardware level) · cache hierarchy · Infinity Cache · coalescing requirements
- **Chiplet and multi-die organisation** on recent datacentre parts, and its consequence: a single
  logical device can have **non-uniform internal memory behaviour**, so placement and partitioning
  affect performance. Check the specific architecture's documentation for how a given part is
  organised.
- **Infinity Fabric** and inter-device interconnect — the bandwidth that determines whether a
  collective operation is cheap or expensive, which Stage 4 depends on directly
- **Precision support** — which formats the matrix hardware accelerates on the target architecture,
  including low-precision formats; and the accumulate precision, which is what actually determines
  numerical behaviour
- Reading the architecture's ISA documentation well enough to recognise instructions in a disassembly
  — [KNOW], not fluency

##### 14.3.6 AMD profiling workflow — [BUILD]

Week 10 named `rocprof` and Omniperf. Here they become a workflow rather than two names:

1. **System-level trace first** — establish where time goes at the whole-application level, and
   whether the problem is even on the accelerator. A great many "GPU performance problems" are
   dataloader or host-side problems.
2. **Kernel-level counters second** — for the specific kernel that the trace identified, collect
   hardware counters
3. **Derive, don't guess** — compute achieved bandwidth and arithmetic intensity from counters, place
   the kernel on the roofline, and *then* decide what class of optimisation can possibly help
4. **Compare against the specification** — achieved bandwidth as a percentage of the device's
   theoretical peak is the number that means something; a raw millisecond figure alone is not evidence
5. **Cross-vendor discipline** — when comparing two vendors' hardware, state both configurations
   fully: hardware, driver and ROCm/CUDA version, framework version and build, precision, batch size,
   sequence length, and warm-up policy. An underspecified cross-vendor benchmark is not a result, and
   this audience will identify that immediately.

##### 14.3.7 Stage 3 assessment questions

- What is HIP, and what does `hipify` do well and badly?
- A CUDA kernel ports cleanly and produces wrong results on AMD hardware. Name the first thing you
  would check.
- Why does a wavefront of 64 versus a warp of 32 change a kernel's block-size and occupancy tuning?
- A GEMM is fast at one matrix shape and slow at another on the same device. Explain.
- Name the AMD counterparts to cuBLAS, cuDNN, NCCL and CUTLASS, and state what each does.
- `torch.cuda.is_available()` returns `True` on an AMD system. Is that a bug?
- What are Matrix Cores, and what happens to a matrix operation whose shape does not map onto them?
- A single logical accelerator shows non-uniform memory performance internally. What would explain it?
- You measured 400 GB/s on a device. Is that good? What do you need to know to answer?

##### 14.3.8 Artefacts 14 and 15

**Artefact 14 — Cross-vendor kernel port.** Deliver Section 14.3.2: an open-source CUDA kernel ported
to HIP, with a written record of every manual intervention `hipify` could not perform and why,
numerical equivalence evidence against the original, and benchmarks on whatever hardware you actually
have — clearly attributed. If you have access to only one vendor's hardware, say so explicitly and
present the port as a correctness and portability exercise rather than a performance comparison.
Honesty here is itself the signal.

**Artefact 15 — AMD profiling and optimisation study.** Take one model, profile it on AMD hardware
using the system-then-kernel workflow in 14.3.6, identify the top three kernels by time, place each on
the roofline with achieved bandwidth as a percentage of the device peak, optimise at least one, and
report before-and-after with full configuration disclosure. State which layer of the descent map each
bottleneck lived at.

---

#### 14.4 STAGE 4 — Scale: distributed training and collective communication — [BUILD]

*Promoted from [KNOW] to [BUILD] in v2.1. Version 2.0 listed the parallelism strategies as vocabulary
in Week 10, Part A, Topic 3, with no exercise attached. For both lanes this is insufficient: at
consumer-scale organisations every serious training job is distributed, and at semiconductor
organisations the interconnect and the collective library are a primary performance surface.*

##### 14.4.1 Collective communication — the actual primitives

Parallelism strategies are usually taught as diagrams. Understand them instead as **patterns of
collective communication**, because that is what determines their cost:

| Collective | What it does | Where it appears |
|---|---|---|
| **All-reduce** | Combines values across all devices, result to all | Gradient synchronisation in data parallelism |
| **Reduce-scatter** | Combines, then distributes shards | Sharded optimiser and gradient states |
| **All-gather** | Every device receives every shard | Reconstructing sharded parameters before use |
| **Broadcast** | One device to all | Initial weight distribution |
| **All-to-all** | Full pairwise exchange | Expert routing in MoE, embedding exchange in recommendation models |

- **Ring versus tree algorithms** and why topology determines which is faster
- **Cost model** — for a given collective, how much data actually crosses the interconnect, and
  therefore how the time scales with device count and message size
- **The library** — NCCL on NVIDIA, **RCCL** on AMD. In PyTorch the `nccl` process-group backend maps
  to RCCL on ROCm builds, which again reflects the deliberate API-compatibility choice.
- **Interconnect matters more than device count.** Devices connected by a high-bandwidth fabric behave
  fundamentally differently from devices connected only over PCIe or across nodes, and a scaling curve
  is uninterpretable without knowing which case you are in.
- Bandwidth and latency microbenchmarks for collectives, run before blaming the model

##### 14.4.2 Parallelism strategies — [BUILD] for DDP and FSDP

- **Data parallelism / DDP** — replicate the model, shard the batch, all-reduce the gradients ·
  gradient bucketing and overlap of communication with backward computation, which is the mechanism
  that makes DDP efficient at all · why it fails when the model does not fit in one device's memory
- **Sharded data parallelism / FSDP and ZeRO** — shard optimiser state, then gradients, then
  parameters; understand what each successive stage buys in memory and costs in communication ·
  the all-gather-before-use, free-after-use pattern
- **Tensor parallelism** — split individual weight matrices across devices · communication *inside*
  the forward pass, which is why it demands a fast interconnect and is normally confined within a node
- **Pipeline parallelism** — split by layer · the **bubble** (idle time from pipeline fill and drain) ·
  micro-batching as the mitigation
- **Expert parallelism** — distributing MoE experts, with all-to-all as the characteristic cost
- **Composition** — real large-scale training combines several of these; be able to say which axis
  each strategy consumes and why the combination is chosen
- **Activation checkpointing** — trading recomputation for activation memory, and its interaction with
  each strategy above

##### 14.4.3 Measuring scaling honestly

- **Scaling efficiency** — achieved speedup divided by ideal speedup, reported per device count. A
  scaling claim without this number is not a claim.
- Strong versus weak scaling, and which one your measurement actually shows
- **Where scaling is lost** — communication that failed to overlap with computation, stragglers, load
  imbalance, dataloader saturation, an interconnect ceiling
- Distinguishing a communication bottleneck from a compute bottleneck in a trace
- The honesty requirement: **report the device count, interconnect type, and per-device batch size**
  with any scaling number. "It scales well" is not a result.

##### 14.4.4 Stage 4 assessment questions

- Which collective does DDP rely on, and how much data crosses the interconnect per step?
- What does each successive stage of sharding shard, and what does each cost?
- Why is tensor parallelism normally confined within a node while data parallelism is not?
- What is the pipeline bubble, and how is it reduced?
- Scaling efficiency falls from 92% at 2 devices to 55% at 8. Give three candidate causes and the
  measurement that would distinguish them.
- Why does MoE training stress the interconnect differently from dense training?
- Which AMD library provides collectives, and how does PyTorch reach it?

##### 14.4.5 Artefact 16 — Distributed training study

Train one model at one, two and (if available) four or more devices using **both** DDP and FSDP.
Report per-configuration throughput, memory per device, and **scaling efficiency**, with the hardware
and interconnect fully stated. Identify from a trace where scaling is lost and explain the mechanism.
If only one device is available, substitute a collective-communication microbenchmark study and state
the substitution plainly — a documented limitation is acceptable, an implied capability is not.

---

#### 14.5 STAGE 5 — The job itself: model bring-up and enablement — [BUILD]

*The objective: perform the actual work of a model enablement engineer, end to end, and produce the
artefact that most closely resembles it.*

This stage is deliberately last because it composes all four preceding stages. It is also the stage
that most directly answers "what would you be doing here?" in an interview.

##### 14.5.1 The bring-up workflow

The repeatable procedure for getting a model running correctly and quickly on a target it has not run
on before:

1. **Environment and baseline** — establish the toolchain, and get *something* running end to end
   before optimising anything
2. **Functional correctness** — does it run, and does it produce plausible output?
3. **Numerical parity** — does it produce output matching a trusted reference within a defensible
   tolerance? (Section 14.5.2)
4. **Operator coverage** — which operators are unimplemented, falling back, or taking a slow path?
   (Section 14.5.3)
5. **Performance baseline** — measure before optimising, and record the configuration
6. **Bottleneck attribution** — locate the owning layer using the descent map
7. **Fix at the right layer** — model code, framework registration, compiler, library call, or kernel
8. **Regression protection** — a test and a benchmark so the fix cannot silently disappear
9. **Report** — what changed, by how much, measured how, and what remains

##### 14.5.2 Numerical parity and correctness — [BUILD]

The most underestimated skill in this lane, and the one that separates a credible engineer from a
plausible one. Most reported "accuracy bugs" on new hardware are tolerance questions, and most real
bugs are found by someone who knew the difference.

- **Why bit-exactness is the wrong expectation.** Floating-point addition is not associative, so any
  change to reduction order — a different kernel, a different block size, a different device count —
  changes the result legitimately. A different number is not automatically a wrong number.
- **Choosing a tolerance** — absolute versus relative; why the appropriate tolerance depends on
  dtype, magnitude and reduction depth; why a single global epsilon is naive
- **Accumulation precision** — low-precision inputs with higher-precision accumulation is the standard
  design, and confusing storage precision with accumulation precision is a common analytical error
- **Localising a divergence** — compare layer by layer, not end to end. The end of a deep network
  amplifies any upstream difference, so the final output tells you almost nothing about the cause.
- **Distinguishing tolerance from a genuine bug** — the practical tests: does the divergence grow with
  depth or appear at one layer? Is it dtype-dependent? Shape-dependent? Reproducible across runs?
  Present in the backward but not the forward?
- **Determinism** — the framework controls for deterministic algorithms, what they cost, why some
  operations have no deterministic implementation, and why non-determinism makes debugging materially
  harder
- **The failure modes to recognise on sight** — NaN and Inf propagation, overflow in low-precision
  formats, loss-scaling failure, catastrophic cancellation, silent underflow to zero

##### 14.5.3 Operator coverage and validation — [BUILD]

- Enumerating the operators a model requires, and determining which are natively supported on the
  target versus falling back
- **Why a silent fallback is worse than a hard failure**: a hard failure is a bug report, whereas a
  fallback is a mysterious performance deficit that nobody attributes correctly for weeks
- Framework operator test suites — how a backend is validated, and how to run that validation
- Writing the test for a newly supported operator: dtypes, shapes, edge cases, non-contiguous inputs,
  empty tensors, backward correctness
- **Continuous integration for a hardware backend** — why the test matrix (framework version × ROCm
  version × architecture × dtype) is the real engineering problem in this work, and why nightly
  regression detection is a large fraction of these teams' output

##### 14.5.4 Benchmarking as a discipline — [KNOW] → [BUILD]

- **MLPerf** methodology — closed versus open divisions and why the distinction exists; what a
  submission requires; why the rules are strict about configuration disclosure
  (https://mlcommons.org)
- Warm-up, steady state, and repeated measurement; reporting distribution rather than a single number
- **P50 and P99, never a bare mean** — Week 10 established this; here it is a reporting standard
- Full configuration disclosure as a habit: hardware, driver, runtime and library versions, framework
  build, precision, batch and sequence dimensions, and warm-up policy
- Reproducibility: a benchmark that someone else cannot rerun is an anecdote

##### 14.5.5 Upstreaming and open source — [BUILD]

The strongest external signal available in this lane, and the reason Section 10.7's open-source item
is worth more here than in Lane A: **the reviewers of these projects are frequently employed by the
organisations being targeted.**

- Navigating a large framework repository: locating an operator's registration, its kernel, and its
  tests
- The contribution process — issue, discussion, pull request, review, CI, iteration
- Realistic entry points: documentation corrections, a missing test, a small operator fix, an
  architecture-specific correctness fix, a benchmark addition
- Candidate projects: **PyTorch, Triton, vLLM, ONNX Runtime, the ROCm component repositories**,
  Hugging Face libraries
- Why an accepted contribution outweighs a portfolio project: it was reviewed by someone with no
  incentive to be kind

##### 14.5.6 Stage 5 assessment questions

- A model produces different output on new hardware than on the reference. Walk me through
  establishing whether that is a bug.
- Why is bit-exact agreement the wrong requirement, and what is the right one?
- Why is a silent operator fallback more damaging than an unimplemented-operator error?
- You are given a model that has never run on this accelerator. What are your first three steps?
- What would your continuous integration matrix look like for a hardware backend, and why?
- Why does MLPerf separate closed and open divisions?
- Loss becomes NaN at step 4,000 in low precision but not in FP32. What are the candidates?
- A number differs in the fourth decimal place. Bug or tolerance? How do you decide?

##### 14.5.7 Artefact 17 — Model enablement report

**The flagship artefact of this Part, and the closest available proxy for the job.**

Select a model that is not trivially supported on your target backend. Produce a full enablement
report:

1. **Bring-up log** — what failed, what you changed, in order
2. **Operator coverage table** — supported natively, falling back, or unsupported; with the method you
   used to determine it
3. **Numerical parity analysis** — layer-wise comparison against a reference, tolerances chosen and
   justified, and a defended conclusion for each divergence: tolerance or bug
4. **Performance baseline and optimisation** — before and after, with each bottleneck attributed to a
   specific layer of the descent map
5. **Regression tests and benchmark harness** — committed and runnable
6. **A written report addressed to a hardware vendor's enablement team** — findings, remaining gaps,
   and recommended next actions

**Why this artefact is disproportionately valuable.** Applicants for these roles typically present
model training projects, which demonstrate that they can use the stack. This demonstrates that you can
*fix* the stack. Version 2.0 correctly identified artefact 11 as the rarest item in the Lane A
portfolio; artefact 17 is the equivalent for Lane B, and it is rarer still.

---

#### 14.6 STAGE 6 — Edge, NPU and client AI inference — [BUILD]

> **Added in v2.1.** Versions up to 2.0 gave the entire client and edge stack one bullet
> ("Edge and mobile — LiteRT · ExecuTorch · NPU offload"). That is a serious under-weighting for the
> stated target: client AI is a major and separately-staffed engineering area at both AMD and
> Qualcomm, and the software stack involved shares almost nothing with the datacentre path.
>
> **Verification status.** The vendor product names, execution provider names and workflow steps in
> this Stage were checked against vendor and project documentation on 2026-08-30; the sources are
> listed at the end of Section 14.6.10 and in Section 14.8. **This is the fastest-moving material in
> the entire document** — two tools that widely-cited secondary sources still present as current
> turned out to have been superseded by their own vendors. Re-verify before relying on any specific
> name, and treat version numbers as illustrative rather than current.

##### 14.6.1 Why the client is a different engineering problem

Nearly every assumption from Stages 1–5 inverts. Internalise the inversion before the tooling:

| Dimension | Datacentre | Client and edge |
|---|---|---|
| **Memory** | Dedicated high-bandwidth accelerator memory | Unified memory shared with the whole system; bandwidth contended |
| **Power** | A cost line | A **hard constraint**; often a fixed thermal envelope with no fan |
| **Batch** | Large batches, throughput-optimised | **Batch of one**, latency-optimised — so the arithmetic intensity is low and the workload is memory-bound by default |
| **Hardware** | Known, homogeneous, controlled | Unknown, heterogeneous, whatever the customer bought |
| **Precision** | FP16/BF16 typical, INT8 optional | **Integer-first**; unquantised models may not run on the accelerator at all |
| **Shapes** | Dynamic tolerated | Static strongly preferred, sometimes required |
| **Operator support** | Near-complete | **Partial** — and this is the central engineering problem |
| **Failure mode** | Too slow, too expensive | Falls back to CPU and drains the battery |
| **Who else is running** | You own the device | You share it with the OS and every other application |

**The consequence worth carrying into every exercise in this Stage:** on the client, the binding
constraint is usually *whether the accelerator can run your graph at all*, not how fast its kernels
are. Stage 3's question was "how fast is this kernel?" Stage 6's question is "how much of my model
actually landed on the NPU, and what happened to the rest of it?"

##### 14.6.2 ONNX Runtime and the Execution Provider architecture — [BUILD]

**This is the single most important abstraction in Stage 6**, and it is what makes ONNX Runtime the
common deployment substrate across vendors. Understand it thoroughly.

**The model.** ONNX Runtime accepts a hardware backend as a pluggable **Execution Provider (EP)**.
At session creation, the runtime asks each registered EP which nodes of the graph it can execute,
**partitions the graph accordingly**, assigns each subgraph to an EP, and runs unclaimed nodes on the
CPU EP. One runtime and one model format therefore target many vendors' silicon — which is precisely
why vendors invest in writing EPs rather than in bespoke runtimes.

**The provider landscape.** Verified against the ONNX Runtime API documentation:

| Execution Provider | Vendor | Target |
|---|---|---|
| `CPUExecutionProvider` | Microsoft | Default fallback, always present |
| `CUDAExecutionProvider` / `TensorRTExecutionProvider` | NVIDIA | NVIDIA GPUs |
| `ROCMExecutionProvider` | **AMD** | AMD GPUs (Linux) — Stage 3's hardware |
| `MIGraphXExecutionProvider` | **AMD** | AMD graph inference engine |
| `VitisAIExecutionProvider` | **AMD** | **AMD/Xilinx NPUs — the Ryzen AI path** |
| `QNNExecutionProvider` | **Qualcomm** | Qualcomm NPU, GPU and CPU |
| `OpenVINOExecutionProvider` | Intel | Intel CPU, iGPU, dGPU, NPU |
| `DmlExecutionProvider` (DirectML) | Microsoft | Any DirectX 12 GPU |
| `CoreMLExecutionProvider` | Apple | Apple CPU, GPU, Neural Engine |
| `XNNPACKExecutionProvider` | — | Optimised CPU inference |
| `ACLExecutionProvider` | Arm | Arm Compute Library |
| `WebGpuExecutionProvider` | Microsoft | Browser and cross-platform GPU |
| `NNAPIExecutionProvider` | Google | Android — **marked for deprecation** following Google's deprecation of NNAPI |
| `RknpuExecutionProvider` | Rockchip | Rockchip NPUs |

**Two structural points that are recent and worth knowing:**

- **Plugin EPs.** EPs are moving from being compiled into a custom ONNX Runtime build to being
  separately distributed shared libraries that plug into a standard installation at runtime. This
  materially changes deployment: no custom runtime build per vendor.
- **Windows ML as an EP broker.** On current Windows, the platform maintains a shared ONNX Runtime
  and **downloads vendor EPs on demand** rather than shipping them all. The catalogue of dynamically
  provisioned EPs includes AMD's MIGraphX and VitisAI, Qualcomm's QNN, Intel's OpenVINO and NVIDIA's
  TensorRT-RTX. DirectML, formerly the Windows abstraction of choice, is now positioned as legacy in
  this architecture. **This is the single most important recent shift in Windows client AI**, and a
  candidate targeting client roles at AMD or Qualcomm should be able to describe it.

**What to actually do:** run the same ONNX model under several EPs on whatever hardware you have,
inspect the partitioning, and compare. The partitioning report is the artefact, not the latency.

##### 14.6.3 Graph partitioning and operator coverage — [BUILD]

**The dominant performance factor on NPU targets, and the least-taught topic in this document's
subject area.**

- **How partitioning works** — the EP declares supported nodes; the runtime cuts the graph into
  subgraphs; each boundary is a **handoff between processors** with an associated data-movement and
  synchronisation cost
- **Why partition count dominates** — one unsupported operator in the middle of an otherwise
  supported model can split it into three partitions and force two round trips off the accelerator.
  A model with a slightly slower kernel and one partition routinely beats a model with faster kernels
  and eleven partitions.
- **Reading a partitioning report** — how to determine which nodes went to which EP, and how many
  subgraphs resulted. Learn this first; it is the primary diagnostic in this Stage.
- **Why an operator is rejected** — genuinely unimplemented · unsupported dtype · unsupported shape
  or rank · dynamic shape where static is required · an attribute combination outside the supported
  set · a quantisation format mismatch
- **Remedies, in the order to try them** — change the model to avoid the operator · adjust the export
  so it lowers differently · fuse or rewrite the subgraph · use a vendor-supported equivalent ·
  implement a custom operator · accept the fallback and place it at the graph boundary rather than
  the middle
- **Placing fallbacks well** — an unsupported operator at the input or output costs one transfer;
  the same operator in the middle of the network costs two and breaks the pipeline
- **The connection to Stage 5** — this is operator coverage analysis (Section 14.5.3) applied to a
  fixed-function accelerator, where the consequence of a gap is far more severe

##### 14.6.4 Quantisation for NPUs — [BUILD]

Week 10 introduced quantisation as an optimisation. **Here it is an admission requirement.**

- **QDQ (Quantize-DeQuantize) format** — the representation in which quantisation is expressed as
  explicit operator pairs in the ONNX graph, which the EP then recognises and fuses into integer
  execution. Several NPU EPs **require** a QDQ model; providing a float model results in CPU
  execution. This is a common and confusing first failure.
- **Post-training quantisation with calibration** — the practical default. Calibration dataset
  selection, size and representativeness; why an unrepresentative calibration set silently degrades
  accuracy on real inputs.
- **Quantisation-aware training** — when PTQ accuracy loss is unacceptable, and its cost
- **Granularity and symmetry** — per-tensor versus per-channel; symmetric versus asymmetric; which
  the target hardware supports, which is a hardware question and not a preference
- **Mixed precision in practice** — for example 16-bit activations with 8-bit weights, a common
  balance point on NPU targets. Also: some toolchains accept FP32 input and internally compile to
  **BF16**, which is a distinct path from integer quantisation with different accuracy behaviour.
- **Which layers to keep in higher precision** — first and last layers, normalisation, attention
  softmax; and how to find the sensitive ones empirically rather than by folklore
- **Accuracy validation** — the non-negotiable step. Quantised accuracy must be measured on a real
  evaluation set, not assumed. Report the delta.
- **The debugging loop** — quantise, measure accuracy, identify the layer responsible for the loss,
  exempt or adjust it, repeat. This loop *is* the job in a model optimisation role.

##### 14.6.5 The on-device runtime landscape — [KNOW] → [BUILD] for one

- **ONNX Runtime** — the cross-vendor default; the EP architecture in 14.6.2; broadest vendor support
- **LiteRT** — the renamed TensorFlow Lite. FlatBuffer model format, the converter and its
  quantisation modes, and the **delegate** mechanism, which is LiteRT's equivalent of an EP. Note
  that the delegate landscape has consolidated toward vendor-provided delegates as
  Google-maintained generic backends have been deprecated — verify current status before choosing.
- **ExecuTorch** — PyTorch's on-device runtime. The flow is `torch.export` → an edge dialect →
  a **backend partitioner** → a deployable artefact. Backends include an optimised CPU path and
  vendor delegates. *Note the structural symmetry: export, partition, delegate, fall back — the same
  four ideas as ONNX Runtime under different names. Learning one transfers.*
- **OpenVINO** (Intel), **Core ML** (Apple), **Windows ML** (Microsoft, per 14.6.2) — know what each
  is and which silicon it fronts
- **The unifying mental model:** every one of these is *capture a graph → convert to a portable
  format → quantise → partition across available processors → execute with CPU fallback*. Vendors
  differ in the names, not the pipeline. Learn the pipeline once.

##### 14.6.6 The AMD client stack — [BUILD]

*Verified against AMD documentation on 2026-08-30. Re-verify; this stack is under active development.*

- **Ryzen AI** — AMD's client AI platform: an NPU built on the **XDNA** architecture, alongside the
  integrated GPU, in Ryzen AI-branded processors. XDNA derives from AI Engine technology acquired
  with Xilinx, which is why the toolchain carries Xilinx-lineage naming.
- **The deployment path** — train in PyTorch or TensorFlow → **export to ONNX** → quantise →
  deploy with **ONNX Runtime using the `VitisAIExecutionProvider`**. The Vitis AI EP performs the
  partitioning decision described in 14.6.3, determining which portions of the model run on the NPU.
- **AMD Quark** — the current quantisation toolkit, covering both PyTorch and ONNX models.
  **Important and easy to get wrong: the older Vitis AI Quantizer is deprecated and Quark
  supersedes it.** A candidate citing the deprecated tool signals stale knowledge; this is exactly
  the kind of detail that distinguishes someone who has read current documentation from someone
  working from an old tutorial.
- **Two precision paths** — an **INT8** path requiring explicit quantisation through Quark, and a
  path where an FP32 model is supplied directly and the compiler converts internally to **BF16**.
  Know that both exist and that they have different accuracy and effort profiles.
- **EP configuration** — the Vitis AI EP takes provider options controlling the compilation target,
  configuration file, and **compiled-model caching**. Caching matters: first-run compilation cost
  versus warm-start latency is a real product decision, not a detail.
- **LLMs on client** — **ONNX Runtime GenAI (OGA)** as the underlying API for generative workloads
  on Ryzen AI, with **Lemonade** for serving and benchmarking LLMs across CPU, iGPU and NPU, and
  **TurnkeyML** for ONNX export and optimisation workflows.
- **The rest of AMD's ONNX Runtime surface** — `MIGraphXExecutionProvider` and
  `ROCMExecutionProvider` for AMD GPUs. Note that **AMD ships EPs across three quite different
  targets** (datacentre GPU, client GPU, client NPU), which is itself a useful thing to understand
  about how the company is organised.
- *Documentation:* https://ryzenai.docs.amd.com · https://quark.docs.amd.com ·
  https://vitisai.docs.amd.com

##### 14.6.7 The Qualcomm client stack — [BUILD]

*Verified against Qualcomm and ONNX Runtime documentation on 2026-08-30.*

- **The processors** — Qualcomm's AI capability spans the CPU, the **Adreno GPU**, and the
  **Hexagon Tensor Processor (HTP)**, which is the NPU in current Snapdragon SoCs. Deployment
  decisions are choices among these three.
- **QAIRT and QNN** — **Qualcomm AI Engine Direct**, commonly called **QNN**, distributed as part of
  the **Qualcomm AI Runtime (QAIRT) SDK**. It provides a unified API with backend-specific libraries
  per processor. **QNN is the modern successor to SNPE** (Snapdragon Neural Processing Engine) —
  another live deprecation worth knowing, directly parallel to the Vitis AI Quantizer/Quark change on
  the AMD side.
- **The QNN Execution Provider** — the ONNX Runtime route onto Qualcomm silicon, selectable by
  backend: a CPU reference backend useful for integration testing, a GPU backend, and the **HTP
  backend which targets the NPU and is the default**. Being able to name the CPU backend's purpose —
  a reference implementation for validation, not for production — is a good signal.
- **QDQ is required** — running through the QNN EP's NPU path requires a quantize-dequantize model.
  This is the concrete instance of the general rule in 14.6.4.
- **Context binaries** — the quantised graph is compiled ahead of time into a context binary
  **specialised to a specific SoC**, which can be cached and shipped. Understand the trade-off:
  large first-run compile cost avoided at runtime, in exchange for an artefact that is no longer
  portable across chips. This is a genuine product architecture decision.
- **Qualcomm AI Hub** — a hosted service for compiling, profiling and benchmarking models on real
  Snapdragon devices. **For a candidate without Snapdragon hardware this is the practical route to
  real measurements**, and using it is a legitimate and honest basis for an artefact.
- **Genie** — Qualcomm's generative AI framework within QAIRT, with a corresponding LLM inference
  pathway. The client-LLM counterpart to AMD's OGA.
- **LiteRT on Qualcomm** — a QNN delegate provides the LiteRT route to the same hardware, which is
  the common path for Android applications.
- **Breadth of target** — the same stack spans mobile, Windows-on-Arm laptops, automotive and XR.
  The breadth is the point: one runtime abstraction, many product categories.

##### 14.6.8 Power, thermal and on-device measurement — [BUILD]

The measurement discipline from Stage 5, adapted to a target where **energy is a first-class metric**:

- **Performance per watt** rather than raw latency; why an NPU can be slower per inference than the
  GPU and still be the correct choice by a wide margin
- **Sustained versus peak** — a device that hits a target latency for two seconds and then throttles
  has not met the requirement. Measure steady state after thermal saturation, not the first run.
- **First-inference versus warm latency** — model load, compilation and cache population; for an
  interactive application the cold path is frequently what the user actually experiences
- **Memory footprint** — on a shared unified-memory device this is a system-level constraint, not a
  private budget
- **Concurrency** — you share the device with the operating system and other applications; a
  benchmark run on an idle device overstates real performance
- **Benchmark suites** — **MLPerf Client**, **MLPerf Mobile** and **MLPerf Tiny** exist precisely
  because datacentre benchmarking methodology does not transfer to these targets
  (https://mlcommons.org)
- **Disclosure requirements, extended for client** — everything from Section 14.5.4, plus device
  model, thermal state, power mode, driver version, and whether the figure is cold or warm

##### 14.6.9 Stage 6 assessment questions

- What is an ONNX Runtime Execution Provider, and what does the runtime do when an EP supports only
  part of a graph?
- A model runs on the NPU at one-third of the expected speed. What do you inspect first?
- Why can one unsupported operator in the middle of a network cost more than a slow kernel?
- What is a QDQ model, and why does an NPU execution provider require one?
- Name AMD's ONNX Runtime execution provider for its client NPU, and the current quantisation
  toolkit. Which tool did that toolkit replace?
- Name Qualcomm's NPU, its runtime SDK, and the SDK it superseded.
- What is a context binary, and what do you trade away by shipping one?
- Your model loses four percent accuracy after INT8 quantisation. Walk me through the next steps.
- Why is performance per watt the right metric on a client device when it is rarely used in a
  datacentre?
- A benchmark shows 20 ms latency; the product team reports the feature feels slow. Give two
  explanations.
- How has the Windows client AI deployment architecture changed, and what does it mean for a vendor
  shipping an execution provider?

##### 14.6.10 Artefacts 18 and 19

**Artefact 18 — Cross-runtime edge deployment study.**
Take one model (a vision model is the easiest starting point) and deploy it through **at least three**
of: ONNX Runtime with two or more execution providers, LiteRT, and ExecuTorch. For each: record the
conversion path and what broke, the **graph partitioning outcome** (how many partitions, which nodes
fell back and why), latency both cold and warm, memory footprint, and accuracy against the FP32
reference. Conclude with a recommendation and the reasoning behind it.
*This artefact is achievable on ordinary hardware* — a laptop and a phone are sufficient — which
makes it the most accessible artefact in Section 10.17.

**Artefact 19 — NPU quantisation and partitioning study.**
Target a real NPU: an AMD Ryzen AI device via the Vitis AI EP, a Snapdragon device via the QNN EP or
Qualcomm AI Hub, or another vendor's NPU. Deliver:

1. **Baseline** — FP32 accuracy and latency on CPU
2. **Quantisation** — INT8 or a mixed-precision configuration produced with the vendor's current
   toolkit, with the calibration set described and justified
3. **Accuracy analysis** — per-layer sensitivity, which layers were exempted and why, final accuracy
   delta measured on a real evaluation set
4. **Partitioning analysis** — the partitioning report before and after any model changes, with each
   fallback attributed to a specific cause from the list in 14.6.3
5. **Optimisation** — at least one change that reduced partition count or improved NPU residency,
   with the before-and-after measurement
6. **Power and sustained performance** — warm and cold latency, and behaviour under sustained load
7. **Full disclosure** — device, driver, SDK version, toolkit version, thermal and power state

**Why these two artefacts are disproportionately valuable.** Client AI teams at silicon vendors spend
much of their time on exactly this: getting a model quantised without losing accuracy, and getting it
to stay resident on the accelerator. An applicant who has done it once, and who can discuss
partitioning and calibration from experience rather than from a blog post, is immediately
distinguishable. **Artefact 19 is to a client AI role what artefact 17 is to a datacentre enablement
role.**

*Documentation sources for this Stage, checked 2026-08-30:*
ONNX Runtime execution providers https://onnxruntime.ai/docs/execution-providers/ ·
AMD Ryzen AI https://ryzenai.docs.amd.com · AMD Quark https://quark.docs.amd.com ·
Qualcomm QNN EP https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html ·
Qualcomm AI Hub https://aihub.qualcomm.com · Windows ML execution providers (Microsoft Learn) ·
MLCommons https://mlcommons.org

---

#### 14.7 Section 10.17 completion criteria

| Criterion | Test |
|---|---|
| **Descent fluency** | Trace any operator from Python to hardware, naming every layer, without notes |
| **Layer attribution** | Given a symptom, name the candidate layers and the measurement that discriminates between them |
| **Framework extension** | A registered custom operator with a verified backward exists and works |
| **Compiler literacy** | Explain what the compiler did to a specific model, evidenced by generated code |
| **Cross-vendor portability** | Port a kernel between vendor languages and enumerate what did not translate |
| **AMD stack fluency** | Name every ROCm component's function and its NVIDIA counterpart; describe the profiling workflow |
| **Architecture awareness** | Explain how wavefront width, matrix-core operand shapes and the memory system change tuning decisions |
| **Scale** | Report scaling efficiency for DDP and FSDP with the configuration stated |
| **Correctness discipline** | Defend a tolerance choice and distinguish tolerance from a bug with evidence |
| **Measurement discipline** | No performance claim without configuration disclosure and a reproducible method |
| **External validation** | One merged contribution to a framework or vendor repository |

**Stage 6 additions** — required if client, mobile, automotive or embedded AI is in scope:

| Criterion | Test |
|---|---|
| **Execution Provider model** | Explain EP registration, graph partitioning and CPU fallback without notes |
| **Partitioning diagnosis** | Read a partitioning report and attribute every fallback to a cause |
| **Quantisation for NPUs** | Produce a QDQ model, defend the calibration set, and report a measured accuracy delta |
| **Vendor fluency** | Name AMD's and Qualcomm's NPUs, runtimes, execution providers and quantisation toolkits — **and the tools each superseded** |
| **Runtime breadth** | Deploy one model through three runtimes and explain what differed |
| **Client measurement** | Report cold and warm latency, sustained behaviour, and performance per watt with full device disclosure |

#### 14.8 Resources

*All unverified unless stated; verify against current documentation, and expect naming to have moved.*

**Official documentation — the primary sources for this Part**
- ROCm documentation: https://rocm.docs.amd.com — the authoritative source for HIP, the library stack,
  the profiling tools, hardware compatibility and current tool names
- PyTorch documentation and developer notes: https://pytorch.org/docs — the internals notes on
  autograd, the dispatcher and the compiler are the correct starting point, not third-party summaries
- Triton: https://triton-lang.org
- **ONNX Runtime, including the execution provider documentation**:
  https://onnxruntime.ai/docs/execution-providers/ — the central reference for Stage 6
- MLCommons and MLPerf: https://mlcommons.org
- TensorFlow: https://www.tensorflow.org · JAX: https://docs.jax.dev
- MLIR: https://mlir.llvm.org

**Client and edge — Stage 6** *(checked 2026-08-30; expect movement)*
- **AMD Ryzen AI**: https://ryzenai.docs.amd.com — NPU deployment, Vitis AI EP, provider options
- **AMD Quark** (quantisation): https://quark.docs.amd.com
- **AMD Vitis AI**: https://vitisai.docs.amd.com
- **Qualcomm QNN execution provider**:
  https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- **Qualcomm AI Hub** (hosted device compile, profile and benchmark): https://aihub.qualcomm.com
- **Qualcomm developer documentation**: https://docs.qualcomm.com
- **ExecuTorch** (PyTorch on-device): https://pytorch.org/executorch
- **LiteRT**: https://ai.google.dev/edge/litert
- **Windows ML execution providers**: Microsoft Learn, Windows AI documentation
- **OpenVINO** (Intel): https://docs.openvino.ai

**Source code as documentation.** For this Part specifically, **reading the repository outranks
reading tutorials.** Framework internals change faster than any written explanation of them, and the
ability to answer a question by reading the source is itself the skill being assessed. Practise
locating: an operator's schema, its registration, its backend kernels, and its tests.

**Publications worth reading for this lane**
FlashAttention · the PyTorch and `torch.compile` design papers · DLRM · ZeRO · Megatron-LM
(tensor and pipeline parallelism) · GPipe · a speculative decoding paper · MLPerf methodology papers.
Read these as *engineering* documents — what constraint did they hit, and what did they restructure to
avoid it — because that is the reasoning pattern the work requires.

#### 14.9 An honest assessment of this Part

**What Section 10.17 delivers:** a candidate who can hold a technical conversation with a model enablement,
framework, performance or client AI team as a peer rather than as an applicant, with up to eight
artefacts evidencing it. That is an unusual position for a recent graduate and it is the intended
outcome.

**What it does not deliver:** a kernel engineer or a compiler engineer. Those are C++ disciplines built
over years, and this Part deliberately stops at reading-level C++ (Section 10.3a). It positions you
for the Python-primary and Python-plus-reading-C++ roles that genuinely exist in volume at these
organisations — enablement, integration, inference, performance, benchmarking, validation — and it
positions you to *grow into* the deeper roles from inside, which is the normal path.

**The one thing that will limit you most:** hardware access. Everything in Stages 1 and 2 can be done
on a free-tier accelerator. Stages 3 and 4 cannot be done properly without real AMD hardware and more
than one device. Solve that before starting Stage 3, and where you cannot, **state the limitation in
the artefact rather than obscuring it.** This audience reads benchmarks for a living and will detect a
number that was not measured. A candidate who says "I could not measure this and here is what I did
instead" is credible; one who presents an unattributed figure is finished.

**Stage 6 is the way around the hardware problem, and it is worth saying so plainly.** Artefact 18
needs only a laptop and a phone. Artefact 19 needs an NPU, but the routes to one are far cheaper than
datacentre access: a Ryzen AI laptop is consumer hardware, and Qualcomm AI Hub provides hosted
Snapdragon devices for compilation, profiling and benchmarking. **A candidate blocked on datacentre
access should do Stage 6 before Stage 3**, not instead of it — the execution provider, partitioning,
quantisation and measurement skills all transfer upward, and client AI is a large, separately-staffed
organisation at both target companies rather than a consolation prize.

**A final note on this Part's shelf life.** Stages 1–2 describe mechanisms that change slowly. Stages
3 and 6 describe vendor stacks that change fast — during the writing of Stage 6, two tools named in
current-looking secondary sources turned out to have been superseded. Treat the *structure* of this
Part as durable and every *product name* in it as perishable. The habit this should instil is itself
part of the skill: **in this field, the engineer who checks the vendor's current documentation beats
the engineer who remembers last year's tutorial**, and interviewers at these companies can tell the
difference within one question.

---

### 10.18 Programme close

*Relocated in v2.1, and folded into Week 10 in v2.2 along with the rest of the post-curriculum
material.*

#### Outcome positioning

**Delivered by the Overview and Weekly Modules (ten weeks):** internship-ready and junior-engineer-ready capability,
evidenced by **eleven reproducible artefacts** and a working understanding spanning linear algebra
through GPU kernel optimisation, including retrieval and ranking, reinforcement learning foundations,
and written system design.

**Not delivered:** senior-level expertise. No 10-week programme produces it, and a curriculum claiming
otherwise sets participants up to fail technical assessment.

**Not delivered by the Overview and Weekly Modules alone: an offer.** the Overview and Weekly Modules produce a qualified candidate. **Section 10.16**
converts that into an interview outcome. This distinction is stated plainly because collapsing the two
is the characteristic error of self-directed preparation — a candidate arrives at the coding screen
with an excellent portfolio and fifty algorithm problems, and never reaches the round where the
portfolio would have mattered.

**Not delivered by the Overview, Weekly Modules and conversion phase either: the model-to-hardware lane.** the Overview, Weekly Modules and conversion phase prepare a candidate for
applied and product machine learning roles, and for performance roles at the level of measuring and
optimising a model from *outside* the stack. Working *inside* the stack — framework internals, the
compiler, HIP and the vendor libraries, distributed training, and model bring-up — is **Section 10.17**, a
further eight to twelve weeks. Section 0.8 sets out which lane to take and how to weight the shared
core accordingly.

##### The three horizons, stated plainly

| Horizon | Duration | Produces |
|---|---|---|
| **the Overview and Weekly Modules** | 10 weeks | A qualified candidate with eleven artefacts |
| **+ Section 10.16** | 4–6 weeks | A candidate who can convert interviews into offers |
| **+ Section 10.17, Stages 1–5** *(Lane B1)* | 8–12 weeks | A candidate credible to a framework, enablement or performance team at a silicon vendor |
| **+ Section 10.17, Stage 6** *(Lane B2)* | 2–3 weeks | A candidate credible to a client, edge or NPU software team |

The full Lane B path is therefore roughly six to eight months of sustained work. That figure is stated
rather than concealed, because the alternative — implying that ten weeks reaches the semiconductor
target — is precisely the class of claim this document's own audit (Section 0.7) was written to
eliminate.

**A shorter route worth naming.** the Overview and Weekly Modules plus Section 10.16 plus Stage 6 alone is roughly four months
and requires no specialist hardware, and it produces a candidate genuinely competitive for client AI,
NPU software and runtime integration roles — which exist in volume at both AMD and Qualcomm. For a
candidate constrained by hardware access or by time, that is a better plan than a partial attempt at
the datacentre path.

This positioning nonetheless places a participant ahead of the substantial majority of applicants, for
a specific reason: most present course completions, whereas a graduate of this programme presents
working systems with measured results attached.

#### Progression beyond the programme

Further capability derives from:
- Solving problems of greater scope and ambiguity
- Taking ownership of systems and teams
- Contributing to open research and open source
- Building and operating original products
- Teaching, mentoring and technical writing

For the model-to-hardware lane specifically, the natural progression beyond Section 10.17 is **write-level
C++**, which opens kernel-library, compiler and driver engineering. Section 10.17 deliberately stops at
reading level; that boundary is a scoping decision, not a claim that the deeper work is unimportant.

---

*Document consolidated 2026-08-27 (v1.0). All topics, subtopics, learning resources, practice tasks,
assessment questions and projects preserved in full from the 102-page 30-Week AI/ML Engineer Roadmap
(mahi community), restructured into 11 modules with depth-tier assignment, and extended with the GPU
performance, inference optimisation, MLOps and data structures and algorithms tracks absent from the
source. Every module carries a Real-World Applications and Industry Use Cases section.*

*Revised 2026-08-30 (v2.0) following a full line-by-line audit against the stated target. Six
internal defects corrected and eight structural gaps closed — recommender systems and ranking,
reinforcement learning foundations, ML system design with deliverables, computer science fundamentals,
online experimentation, LLM security, vendor GPU stacks and reading-level C++, and the algorithms
schedule — funded by demoting lower-value material rather than extending the timeline. Artefact count
corrected from eight to eleven. Two links verified by fetch; all others remain unverified and are
marked as such in Overview E. Audit summary in Section 0.7.*

*Extended 2026-08-30 (v2.1) after the target was specified as **both** large consumer technology
organisations **and** semiconductor organisations, spanning model through to hardware. Two changes:
Section 0.8 establishes the dual-lane routing and the shared core, and **Section 10.17** adds the
model-to-hardware specialisation track — framework internals and the dispatcher, the compiler and
graph layer, HIP and the ROCm stack with the CDNA execution model, distributed training and collective
communication, and the model bring-up and enablement workflow — with six further artefacts (12–17).
Week 10 gained the model-to-hardware descent map at [KNOW]. Section 10.17 is presented as a distinct
eight-to-twelve-week track rather than compressed into the programme, because compressing it would
repeat the defect identified in Section 0.7: a requirement stated with no schedule attached. Framework
and vendor API names in Section 10.17 are written as search terms against current documentation, not as
verified citations; ROCm tool naming in particular has changed across releases.*

*Also in v2.1: **Section 10.17, Stage 6 — Edge, NPU and client AI inference**, covering the ONNX Runtime
execution provider architecture, graph partitioning and operator coverage on fixed-function silicon,
quantisation for NPUs including the QDQ requirement, the on-device runtime landscape (ONNX Runtime,
LiteRT, ExecuTorch, Windows ML), the AMD client stack (Ryzen AI, XDNA, the Vitis AI execution
provider, AMD Quark, ONNX Runtime GenAI), the Qualcomm client stack (QAIRT/QNN, the Hexagon Tensor
Processor, the QNN execution provider, Qualcomm AI Hub), and power- and thermal-aware measurement —
with two further artefacts (18, 19). Section 0.8 now distinguishes datacentre (B1) from client and
edge (B2) sub-paths, since the latter requires no specialist hardware. **The vendor names, execution
provider identifiers and workflow steps in Stage 6 were verified against vendor and project
documentation on 2026-08-30**, which corrected two deprecations that older secondary sources still
present as current; this remains the fastest-moving material in the document and should be
re-checked before use.*
