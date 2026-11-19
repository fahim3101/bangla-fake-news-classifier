# Day 2 — ML concepts and the confusion matrix

**Date:** 2026-11-20
**Notebook:** none (handwritten practice)
**Project:** Bangla Fake News Classifier — core evaluation concepts

---

## 1. Train / test split

The model learns from **80%** of the data and is evaluated on the remaining **20%**, which it never
sees during training.

```python
train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
```

| Argument | Purpose |
|---|---|
| `test_size=0.2` | 20% of the data is held out for testing |
| `stratify=y` | keeps the real/fake ratio identical in both splits (essential for imbalanced data) |
| `random_state=42` | makes the split reproducible |

**Why hold out data:** memorising the exam paper gives 100% on that paper but fails on a new one.
A model scored on its own training data tells us nothing about real-world performance.

## 2. Overfitting and underfitting

| Situation | Training score | Test score | Meaning |
|---|---|---|---|
| Overfitting | very high (e.g. 0.99) | low (e.g. 0.70) | memorised the training set |
| Underfitting | low (e.g. 0.60) | low (e.g. 0.58) | failed to learn the pattern |
| Good fit | high (e.g. 0.92) | close to training (e.g. 0.90) | learned the pattern, not the noise |

In this project, more epochs on a small dataset can overfit BanglaBERT, which is why epochs 1, 3 and 5
are compared.

## 3. Confusion matrix

| | Model predicts **Fake (1)** | Model predicts **Real (0)** |
|---|---|---|
| **Actually Fake (1)** | **TP** — correctly caught | **FN** — missed |
| **Actually Real (0)** | **FP** — false alarm | **TN** — correctly cleared |

Reading rule:

- **Positive / Negative** = what the **model predicted** (Fake = positive).
- **True / False** = whether the model was **correct**.
- Therefore `FP` means "the model said fake, but the article was actually real".

## 4. Metrics

| Metric | Formula | Question it answers |
|---|---|---|
| Accuracy | `(TP + TN) / total` | out of all items, how many were correct |
| Precision | `TP / (TP + FP)` | of everything flagged fake, how much really was fake |
| Recall | `TP / (TP + FN)` | of all real fakes, how many were caught |
| F1 | `2 × (P × R) / (P + R)` | harmonic mean of precision and recall |

**Why accuracy alone is misleading:** with 95% real news, a model that always predicts "real" scores
95% accuracy while catching zero fakes (recall = 0). Macro F1 and recall must be reported instead.

**Precision vs recall trade-off in this project:**

- High FP → real articles are flagged as fake, which damages trust in the tool.
- High FN → fake news slips through, which is the harm the project is trying to prevent.

F1 summarises the balance in a single number.

## 5. Worked example (10 news items)

Setup: 10 items — 3 fake, 7 real. The model catches 2 fakes, misses 1, and wrongly flags 2 real items.

| | Predicted Fake | Predicted Real |
|---|---|---|
| Actually Fake (3) | 2 (TP) | 1 (FN) |
| Actually Real (7) | 2 (FP) | 5 (TN) |

```
Precision = 2 / (2 + 2) = 0.50
Recall    = 2 / (2 + 1) = 0.67
F1        = 2 × (0.50 × 0.67) / (0.50 + 0.67) = 0.57
Accuracy  = (2 + 5) / 10 = 0.70
```

## 6. Practice 2 (solved by hand)

**Problem:** 100 news items — 20 fake, 80 real. The model catches 15 fakes, misses 5, and wrongly
flags 10 real items as fake.

| | Predicted Fake | Predicted Real | Total |
|---|---|---|---|
| Actually Fake | 15 (TP) | 5 (FN) | 20 |
| Actually Real | 10 (FP) | 70 (TN) | 80 |

```
TN = 80 − 10 = 70

Precision = 15 / (15 + 10) = 15 / 25 = 0.60
Recall    = 15 / (15 + 5)  = 15 / 20 = 0.75
F1        = 2 × (0.60 × 0.75) / (0.60 + 0.75)
          = 0.90 / 1.35 = 0.67
Accuracy  = (15 + 70) / 100 = 0.85
```

| Metric | Value |
|---|---|
| Precision | 0.60 |
| Recall | 0.75 |
| F1 | 0.67 |
| Accuracy | 0.85 |

**Interpretation:** the model catches 75% of fake news but 10 real articles out of 100 are wrongly
flagged. Accuracy (0.85) looks healthy while precision (0.60) shows the cost of those false alarms,
which is exactly why F1 is reported alongside accuracy.

## 7. Takeaways

- Test data must stay unseen; `stratify=y` keeps the class ratio intact.
- A confusion matrix is the source of truth; every metric is derived from its four cells.
- Precision and recall measure different failure modes and usually trade off against each other.
- F1 is the single number used to compare models in this project (macro-averaged for multiple runs).

## 8. Next steps (Day 4–5)

- [ ] Bag of Words vs TF-IDF
- [ ] n-grams (`ngram_range=(1,1)`, `(1,2)`, `(1,3)`)
- [ ] **Practice 3:** extend the TF-IDF toy example with three more documents and inspect which
      words receive the highest scores and why
