# Day 1 — Environment setup and pandas fundamentals

**Date:** 2026-11-20
**Notebook:** `notebooks/day1_pandas.ipynb`
**Project:** Bangla Fake News Classifier — setup and first pandas session

---

## 1. Environment

| Component | Version |
|---|---|
| Python | 3.14.6 |
| Virtual environment | `venv/` |
| pandas | 3.1.1 |
| numpy | 2.5.5 |
| scikit-learn | 1.9.1 |
| matplotlib | 3.11.2 |
| seaborn | 0.13.2 |
| joblib | 1.6.0 |
| JupyterLab | 4.6.6 |
| Jupyter kernel | `bangla-fake` (linked to `venv`) |
| Editor | VS Code with Python, Pylance, and Jupyter extensions |

Activate the environment before installing anything:

```powershell
.\venv\Scripts\Activate.ps1
```

## 2. Dataset

- Source: Kaggle — *Titanic: Machine Learning from Disaster* (practice dataset only)
- Local path: `data/titanic/train.csv`
- Shape: 891 rows × 12 columns

## 3. Work log

### Loading the file

```python
import pandas as pd

df = pd.read_csv(r"F:\AI-ML\data\titanic\train.csv")
print(df.shape)
```

Output: `(891, 12)` — 891 rows, 12 columns.

### Inspecting rows and columns

```python
df.head()               # first 5 rows
df.columns.tolist()     # column names
```

### Structure and missing values

```python
df.info()
```

Findings:

- `Age` — 714 non-null → **177 missing**
- `Cabin` — 204 non-null → **687 missing**
- `Embarked` — 889 non-null → **2 missing**

```python
df.isnull().sum()
```

### Class distribution

```python
df["Survived"].value_counts()
```

```
0    549
1    342
```

With `normalize=True`: `0 → 0.616`, `1 → 0.384`, i.e. an **imbalanced** target
(61.6% vs 38.4%). This is why accuracy alone is misleading and macro F1 / recall must be reported.

### Bar charts

```python
import matplotlib.pyplot as plt

df["Sex"].value_counts().plot(kind="bar")
plt.title("Sex distribution")
plt.show()
```

```python
df["Pclass"].value_counts().sort_index().plot(kind="bar")
plt.title("Passenger class")
plt.show()
```

`sort_index()` is required for ordered categories; otherwise `value_counts()` sorts by count.

## 4. Command reference

| Task | Command |
|---|---|
| Load a CSV | `pd.read_csv("path")` |
| Shape (rows, columns) | `df.shape` |
| First / last rows | `df.head()` / `df.tail()` |
| Random sample | `df.sample(5)` |
| Column names | `df.columns.tolist()` |
| Structure, dtypes, non-null counts | `df.info()` |
| Missing values per column | `df.isnull().sum()` |
| Value counts | `df["col"].value_counts()` |
| Percentages | `df["col"].value_counts(normalize=True)` |
| Numeric summary | `df.describe()` |
| Group averages | `df.groupby("col")["target"].mean()` |
| Bar chart | `df["col"].value_counts().plot(kind="bar")` |

## 5. Debugging lesson

**Error:**

```
FileNotFoundError: [Errno 2] No such file or directory: 'F:\\AI-ML\\data\\train.csv'
```

**Cause:** the file was inside `data/titanic/`, not directly in `data/`.

**Lesson:**

- `FileNotFoundError` means the path does not exist; Python reads the path literally.
- Verify the path separately before blaming the code:

```python
import os
os.path.exists(r"F:\AI-ML\data\titanic\train.csv")
```

- Absolute paths (`F:\...`) will not work on another machine after cloning. Relative paths
  (e.g. `../data/titanic/train.csv` from inside `notebooks/`) will be used for the final version.

## 6. Key takeaways

- The `Survived` column is binary (0/1), exactly like the `label` column (0 = real, 1 = fake) in the
  fake news project. The same `value_counts()` pattern will be reused.
- `df.info()` and `df.isnull().sum()` are the first checks before any modeling, because unhandled
  missing values break the pipeline.
- With imbalanced classes, accuracy is not enough — macro F1 and recall must be reported.

## 7. Next steps (Day 2–3)

- [ ] `df.describe()` — numeric summary
- [ ] `df.groupby("Sex")["Survived"].mean()` — survival rate by group
- [ ] Train/test split, overfitting, accuracy vs precision vs recall vs F1
- [ ] **Practice 2 (handwritten):** 100 news items, 20 fake; 15 fakes caught, 5 missed, 10 real items
      wrongly flagged → compute precision, recall, and F1
