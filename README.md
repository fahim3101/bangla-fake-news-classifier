# Bangla Fake News Classification: Classical ML vs BanglaBERT

**Status:** Day 1 of 14 — environment setup and pandas fundamentals complete.

A binary text classification project: given a Bangla news article, predict whether it is
**real (0)** or **fake (1)**. The project compares a classical machine learning baseline
(TF-IDF + Logistic Regression / Naive Bayes / Linear SVM) against a fine-tuned **BanglaBERT** model,
and reports accuracy, macro F1, training cost, and error patterns.

---

## 1. Problem

Fake news spreads quickly on social media in Bangladesh, and most readers share content without
verifying it. This project trains a model that reads a Bangla news text and predicts whether it is
real or fake, then measures how much a large pre-trained language model (BanglaBERT) actually
improves over a simple classical baseline — and whether that improvement justifies the extra cost.

## 2. Dataset

| | |
|---|---|
| **Target dataset** | _To be added — Bangla fake news dataset (Kaggle / Hugging Face), with source link and license_ |
| **Practice dataset (Day 1)** | [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic) (public competition dataset) |
| **Local path** | `data/titanic/train.csv` (not committed — see `.gitignore`) |
| **Size used for practice** | 891 rows × 12 columns |

Dataset files are intentionally excluded from this repository. The source and license of the final
dataset will be documented here before training begins.

## 3. Method

- **Baseline:** TF-IDF (`ngram_range=(1,2)`, `max_features=50000`) + Logistic Regression / MultinomialNB / LinearSVC
- **Deep model:** BanglaBERT (`csebuetnlp/banglabert`) fine-tuned for 3 epochs, learning rate `2e-5`, `max_length=128`
- **Split:** 80/20 stratified, `random_state=42`
- **Vectorizer rule:** fit on training data only (no data leakage)
- **Metrics:** Accuracy, Macro F1, confusion matrix, training time

## 4. Results

| Model | Accuracy | Macro F1 | Training time | Note |
|---|---|---|---|---|
| TF-IDF + Logistic Regression | — | — | — | Baseline |
| TF-IDF + Naive Bayes | — | — | — | |
| TF-IDF + Linear SVM | — | — | — | |
| BanglaBERT (fine-tuned) | — | — | — | 3 epochs, T4 GPU |

Results will be filled in during Days 8–13.

## 5. Error Analysis

_To be added: confusion matrix and a review of 10–15 misclassified examples with observed patterns._

## 6. Limitations

_To be added: dataset bias, source dependency, satire, and generalization to new topics._

## 7. How to run

```powershell
# 1. Create and activate a virtual environment (first time only)
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Jupyter
jupyter lab
```

Notebooks should be run in order:

1. `notebooks/day1_pandas.ipynb` — pandas fundamentals
2. _Upcoming: EDA, baseline models, BanglaBERT fine-tuning, error analysis_

## 8. Project structure

```
.
├── app/            # Streamlit demo (Step 10)
├── data/           # datasets (git-ignored)
├── docs/           # project guide
├── models/         # saved vectorizer / model files
├── notebooks/      # Jupyter notebooks, in order
├── notes/          # daily learning notes
├── requirements.txt
└── README.md
```

## 9. References

- BanglaBERT: *Language Model Pretraining and Benchmarks for Low-Resource Language Understanding Evaluation in Bangla*
- Hugging Face model: [`csebuetnlp/banglabert`](https://huggingface.co/csebuetnlp/banglabert)
- scikit-learn: *Working With Text Data* tutorial
- Hugging Face NLP Course: *Text classification*

---

## Progress

- [x] Day 1 — environment setup and pandas fundamentals (Practice 1)
- [ ] Day 2–3 — ML concepts and confusion matrix (Practice 2)
- [ ] Day 4–5 — TF-IDF and n-grams (Practice 3)
- [ ] Day 6–7 — dataset, EDA, preprocessing
- [ ] Day 8–9 — baseline models and comparison (Practice 5)
- [ ] Day 10–11 — error analysis
- [ ] Day 12–13 — BanglaBERT fine-tuning (Colab)
- [ ] Day 14 — final comparison, Streamlit demo, documentation
