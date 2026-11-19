# Day 1 — Setup + pandas basics

**Date:** 2026-11-20
**Notebook:** `notebooks/day1_pandas.ipynb`
**Topic:** Project 1 (Bangla Fake News Classifier) — environment setup + pandas er prothom din

---

## 1. Setup (ja ja kora hoyeche)

| Jinish | Version / Value |
|---|---|
| Python | 3.14.6 |
| venv | `F:\AI-ML\venv` |
| pandas | 3.1.1 |
| numpy | 2.5.5 |
| scikit-learn | 1.9.1 |
| matplotlib | 3.11.2 |
| seaborn | 0.13.2 |
| joblib | 1.6.0 |
| JupyterLab | 4.6.6 |
| Kernel | `bangla-fake` (venv er sathe linked) |
| Editor | VS Code + Python / Pylance / Jupyter extension |

venv activate:

```powershell
.\venv\Scripts\Activate.ps1
```

Kichu install korte hole age venv activate korte hobe, tarpor `pip install ...`.

---

## 2. Dataset

- Source: Kaggle — *Titanic: Machine Learning from Disaster* (practice er jonno, asol project e Bangla fake news dataset hobe)
- Local path: `data/titanic/train.csv`
- Size: 891 row × 12 column

---

## 3. Notebook e ja ja chalalam

### File load

```python
import pandas as pd

df = pd.read_csv(r"F:\AI-ML\data\titanic\train.csv")
print(df.shape)
```

Output: `(891, 12)` → 891 row, 12 column

### Prothom 5 row

```python
df.head()
```

### Structure + missing value

```python
df.info()
```

Dekha gelo:

- `Age` → 714 non-null → **177 missing**
- `Cabin` → 204 non-null → **687 missing**
- `Embarked` → 889 non-null → **2 missing**

### Missing value count

```python
df.isnull().sum()
```

### Label distribution (class balance)

```python
df["Survived"].value_counts()
```

Output:

```
0    549
1    342
```

`normalize=True` dile percentage: `0 → 0.616`, `1 → 0.384`
→ **imbalanced dataset** (61.6% vs 38.4%)

### Bar chart

```python
import matplotlib.pyplot as plt

df["Sex"].value_counts().plot(kind="bar")
plt.title("Sex distribution")
plt.show()
```

Pclass er jonno:

```python
df["Pclass"].value_counts().sort_index().plot(kind="bar")
plt.title("Passenger class")
plt.show()
```

> `sort_index()` na dile count onujayi order hoy (`3, 1, 2`), `sort_index()` dile `1, 2, 3`.

---

## 4. Command cheat-sheet

| Kaj | Command |
|---|---|
| File load | `pd.read_csv("path")` |
| Size (row, col) | `df.shape` |
| Prothom / shesh row | `df.head()` / `df.tail()` |
| Random sample | `df.sample(5)` |
| Column name list | `df.columns.tolist()` |
| Structure + dtype + non-null | `df.info()` |
| Missing value count | `df.isnull().sum()` |
| Value count | `df["col"].value_counts()` |
| Percentage | `df["col"].value_counts(normalize=True)` |
| Number summary | `df.describe()` |
| Group er average | `df.groupby("col")["target"].mean()` |
| Bar chart | `df["col"].value_counts().plot(kind="bar")` |

---

## 5. Bhul theke shikha

**Error:**

```
FileNotFoundError: [Errno 2] No such file or directory: 'F:\\AI-ML\\data\\train.csv'
```

**Karon:** file ta `data\titanic\` folder er bhitore chilo, `data\` e na.

**Shikha:**

- `FileNotFoundError` = path e file nai; Python path ta literally pore.
- Error ashle age path ta alada kore check koro:

```python
import os
os.path.exists(r"F:\AI-ML\data\titanic\train.csv")
```

- GitHub e push korar por absolute path (`F:\...`) onno machine e kaj korbe na — tokhon relative path use korbo: `../data/titanic/train.csv`

---

## 6. Aajker insight

- `Survived` column ta 0/1 — ঠিক fake news project er `label` (0 = real, 1 = fake) er moto. Same `value_counts()` pattern porer project e direct kaje lagbe.
- `df.info()` / `isnull()` diye model banar age data er quality bujhte hoy.
- Imbalanced data te shudhu accuracy na dekhe **macro F1 / recall** dekha lage (PDF section 2.3).

---

## 7. Porer kaj (Day 2–3)

- [ ] `df.describe()` — number column er summary
- [ ] `df.groupby("Sex")["Survived"].mean()` — kon group beshi bneche
- [ ] Train/test split, overfitting, accuracy vs precision vs recall vs F1
- [ ] **Practice 2 (khatay hate likha):** 100 news, 20 fake; 15 fake dhora porse, 5 miss, 10 real ke vul fake bola hoyeche → Precision, Recall, F1 ber kora
