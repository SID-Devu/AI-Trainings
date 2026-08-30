# AI-Trainings

Self-directed AI / Machine Learning / Deep Learning engineering programme.

## Contents

| File | What it is |
|---|---|
| [`AI-ML-DL-COMPLETE-ROADMAP.md`](AI-ML-DL-COMPLETE-ROADMAP.md) | The full programme specification — 10 weekly modules, plus the conversion phase and the model-to-hardware specialisation track. 19 portfolio artefacts. |
| [`textbook/WEEK-01-MATHEMATICS-FOUNDATIONS.md`](textbook/WEEK-01-MATHEMATICS-FOUNDATIONS.md) | Week 1 textbook, written from zero. 117 concepts: Python, NumPy, linear algebra, calculus, optimisation, information theory. |

## Structure

```
AI-Trainings/
├── AI-ML-DL-COMPLETE-ROADMAP.md    # the plan
├── textbook/
│   └── WEEK-01-MATHEMATICS-FOUNDATIONS.md
└── week01/                          # my code and deliverables (to come)
```

## The roadmap in one table

| Wk | Module |
|---|---|
| 1 | Mathematics: linear algebra, calculus, optimisation, information theory *(double weight)* |
| 2 | Probability, statistics, experimentation, data handling, SQL |
| 3 | ML foundations and supervised learning |
| 4 | Unsupervised learning, model selection, tuning |
| 5 | Neural networks and PyTorch |
| 6 | Training techniques, optimisers, CNNs |
| 7 | Sequence models and transformers |
| 8 | Specialisations: NLP, vision, generative AI, ranking, RL |
| 9 | MLOps, deployment, data engineering, system design, ethics |
| 10 | Systems, GPU performance, inference optimisation, career conversion |

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

## Status

Week 1 in progress.
