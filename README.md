# Bangla Fake News Classification: Classical ML vs BanglaBERT

> **Status:** 🚧 Day 1 / 14 — setup + pandas basics done

Ekta Bangla text fake news (ba spam) naki real — eta detect korar binary classification project.
Ei repo te classical ML baseline (TF-IDF + Logistic Regression / Naive Bayes / Linear SVM) er sathe
fine-tuned **BanglaBERT** er comparison thakbe.

---

## 1. Problem

Bangladesh e social media te fake news chhorate thake, ar manush verify na kore share kore.
Ei project er uddesho: ekta Bangla news text input hisebe niye **0 = real, 1 = fake** label predict kora,
ar dekha classical ML koto ta pare vs deep learning (BanglaBERT) koto ta pare.

## 2. Dataset

- **Asol dataset:** _TODO — Bangla fake news dataset (Kaggle / Hugging Face), source link + license ekhane likha hobe_
- **Practice dataset (Day 1):** Kaggle — [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic) (public competition dataset)
- Local path (git e push kora hoy na): `data/titanic/train.csv`
- Size: 891 row × 12 column

> Dataset repo te rakha hoy na (`.gitignore` e `data/`). Source ar license niche update hobe.

## 3. Method

- **Baseline:** TF-IDF (1,2-gram) + Logistic Regression / MultinomialNB / LinearSVC
- **Deep model:** BanglaBERT (`csebuetnlp/banglabert`) fine-tuned — 3 epochs, lr 2e-5, max_len 128
- **Split:** 80/20 stratified, `random_state=42`
- **Metric:** Accuracy, Macro F1, Confusion matrix

## 4. Results

| Model | Accuracy | Macro F1 | Training time | Note |
|---|---|---|---|---|
| TF-IDF + LogReg | _TODO_ | _TODO_ | _TODO_ | Baseline |
| TF-IDF + NaiveBayes | _TODO_ | _TODO_ | _TODO_ | |
| TF-IDF + LinearSVM | _TODO_ | _TODO_ | _TODO_ | |
| BanglaBERT | _TODO_ | _TODO_ | _TODO_ | Fine-tuned, 3 epochs |

## 5. Error Analysis

_TODO — confusion matrix + 10-15 ta vul example er pattern_

## 6. Limitations

_TODO — dataset bias, source dependency, satire, notun topic e generalization_

## 7. How to run

```powershell
# 1. venv banao (first time only)
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. dependencies
pip install -r requirements.txt

# 3. notebook
jupyter lab
```

Notebook order:

1. `notebooks/day1_pandas.ipynb` — pandas basics
2. _TODO: EDA, baseline, BanglaBERT, analysis_

Demo app:

```powershell
# streamlit run app/app.py   (Step 10 e add hobe)
```

## 8. References

- BanglaBERT: _Language Model Pretraining and Benchmarks for Low-Resource Language Understanding Evaluation in Bangla_
- Hugging Face model: [`csebuetnlp/banglabert`](https://huggingface.co/csebuetnlp/banglabert)
- scikit-learn — Working With Text Data
- Hugging Face NLP Course — Text classification

---

## Progress

- [x] Day 1 — setup + pandas basics (Practice 1)
- [ ] Day 2–3 — ML concepts + confusion matrix (Practice 2)
- [ ] Day 4–5 — TF-IDF, n-gram (Practice 3)
- [ ] Day 6–7 — dataset, EDA, preprocessing
- [ ] Day 8–9 — baseline models + comparison (Practice 5)
- [ ] Day 10–11 — error analysis
- [ ] Day 12–13 — BanglaBERT fine-tune (Colab)
- [ ] Day 14 — final table, Streamlit demo, README, push
