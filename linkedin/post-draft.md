# LinkedIn — Day 1–2 post

**Files in this folder**

| File | Use |
|---|---|
| `day01-02-summary.png` | Attach this image to the post (1200×1200) |
| `make_card.py` | Regenerates the image if the numbers change |
| `post-draft.md` | This file — copy-paste drafts |

**Image text check:** Day 1–2 · Python 3.14 + venv · pandas 3.1 · scikit-learn 1.9 · JupyterLab ·
TP 15 / FN 5 / FP 10 / TN 70 · P 0.60 · R 0.75 · F1 0.67 · Acc 0.85

---

## Option A — Main post (English, recommended)

> Copy everything between the lines. LinkedIn does not render Markdown, so it is plain text.

---

Day 1–2 of a 14-day ML project: building a Bangla Fake News Classifier — and documenting every step in public.

Most tutorials jump straight to "fine-tune a transformer". I'm doing the opposite: fundamentals first, then earn the big model.

What I actually did:

→ Set up a clean environment (Python 3.14 + venv, pandas, scikit-learn, matplotlib, JupyterLab)
→ Loaded a real dataset and inspected it properly: shape, missing values, class balance, groupby
→ Learned the metric most beginners skip

The practice problem that made it click:

100 news articles. 20 fake, 80 real.
The model caught 15 fakes, missed 5, and flagged 10 real articles as fake.

Precision 0.60 | Recall 0.75 | F1 0.67 | Accuracy 0.85

Accuracy looks healthy. But precision says 40% of everything flagged "fake" was actually real. No accuracy score will show you that trade-off.

Next: TF-IDF + n-grams, a classical baseline, then BanglaBERT.

Repo (work in progress): github.com/fahim3101/bangla-fake-news-classifier

#MachineLearning #NLP #BanglaNLP #BuildInPublic #DataScience

---

## Option B — Short version

---

Day 1–2 of my 14-day ML project: a Bangla Fake News Classifier, built in public.

Setup done, pandas fundamentals done — and one metric lesson that changed how I read results.

100 news articles. 20 fake, 80 real.
Model caught 15 fakes, missed 5, flagged 10 real ones as fake.

Accuracy 0.85 — looks great.
Precision 0.60 — 40% of everything flagged "fake" was actually real.

That gap is why I'm tracking Precision, Recall and F1 from day one instead of chasing accuracy.

Next: TF-IDF → classical baseline → BanglaBERT.

Repo: github.com/fahim3101/bangla-fake-news-classifier

#MachineLearning #NLP #BanglaNLP #BuildInPublic

---

## Option C — Bangla version

---

১৪ দিনের একটা ML প্রজেক্ট শুরু করেছি: বাংলা ফেক নিউজ ক্লাসিফায়ার। প্রতিদিন যা শিখছি, পাবলিকলি ডকুমেন্ট করছি।

বেশিরভাগ টিউটোরিয়াল সোজা "transformer fine-tune" দিয়ে শুরু করে। আমি উল্টো পথে যাচ্ছি — আগে ফাউন্ডেশন, তারপর বড় মডেল।

Day 1–2 এ যা করেছি:

→ Python 3.14 + venv, pandas, scikit-learn, JupyterLab দিয়ে environment
→ আসল ডেটাসেট নিয়ে shape, missing value, class balance, groupby
→ যে মেট্রিকটা বেশিরভাগ বিগিনার এড়িয়ে যায়

প্র্যাকটিস প্রবলেম যেটা ব্যাপারটা পরিষ্কার করে দিল:

১০০টা নিউজ। ২০টা ফেক, ৮০টা রিয়াল।
মডেল ১৫টা ফেক ধরল, ৫টা মিস করল, আর ১০টা রিয়ালকে ভুল করে ফেক বলল।

Precision 0.60 | Recall 0.75 | F1 0.67 | Accuracy 0.85

Accuracy ০.৮৫ — দেখতে ভালোই। কিন্তু Precision বলছে, "ফেক" বলা সব নিউজের ৪০% আসলে রিয়াল ছিল। এই trade-off accuracy কখনো দেখায় না।

পরের ধাপ: TF-IDF + n-gram, classical baseline, তারপর BanglaBERT।

Repo: github.com/fahim3101/bangla-fake-news-classifier

#MachineLearning #NLP #BanglaNLP #BuildInPublic

---

## Posting checklist

1. **Attach** `day01-02-summary.png` — posts with a clean visual get noticeably more reach.
2. **Link placement:** put the repo link in the **first comment** instead of the post body if you want
   slightly better reach. (The drafts above keep it in the body — both are fine.)
3. **Timing:** weekday morning (9–11 AM) or evening (8–10 PM) Bangladesh time.
4. **First line matters:** LinkedIn truncates after ~2 lines. "Day 1–2 of a 14-day ML project…" is
   designed to survive that cut.
5. **Reply to every comment** in the first hour — it signals engagement.
6. **Don't over-hashtag:** 3–5 is the sweet spot. The drafts use 5.
7. **Consistency beats reach:** post at each milestone (Day 7, Day 9, Day 11, Day 14), not every day.

## Series plan (future posts)

| Post | When | Hook |
|---|---|---|
| Day 1–2 | now | Setup + why accuracy lies |
| Day 4–5 | after TF-IDF | What TF-IDF actually does, in one example |
| Day 7 | after EDA | What the dataset looks like (class chart) |
| Day 9 | after baselines | 3 classical models, one table |
| Day 11 | after error analysis | The 15 mistakes the model makes |
| Day 14 | final | Classical vs BanglaBERT: was it worth it? |
