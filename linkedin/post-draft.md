# LinkedIn — accuracy vs precision post

**Files**

| File | Use |
|---|---|
| `accuracy-vs-precision.png` | Attach to the post (1200×1200) |
| `make_card.py` | Regenerates the image |
| `post-draft.md` | Drafts below |

---

## Main post (recommended)

```
Accuracy can make a bad model look good.

I ran a simple test: 100 news articles, 20 fake, 80 real.
The model caught 15 fakes, missed 5, and flagged 10 real ones as fake.

Accuracy: 0.85 — looks fine.
Precision: 0.60 — 40% of everything it called "fake" was actually real.

Same model, two very different stories. That's why I'm tracking precision, recall and F1 instead of chasing accuracy.

Building a Bangla fake news classifier in public — next up, TF-IDF and a classical baseline.

Repo: https://github.com/fahim3101/bangla-fake-news-classifier

#MachineLearning #NLP #BanglaNLP #BuildInPublic
```

---

## Even shorter

```
Accuracy 0.85. Precision 0.60.

Same model: 85% of its predictions were correct, but 40% of everything it flagged as "fake" was actually real.

That's why I'm tracking precision, recall and F1 — not just accuracy.

Building a Bangla fake news classifier in public.
Repo: https://github.com/fahim3101/bangla-fake-news-classifier

#MachineLearning #NLP #BanglaNLP
```

---

## Bangla version

```
Accuracy ০.৮৫ — দেখতে দারুণ।
Precision ০.৬০ — "ফেক" বলা সব খবরের ৪০% আসলে সত্যি ছিল।

একই মডেল, দুই রকম গল্প। তাই শুধু accuracy নয়, precision, recall আর F1 ট্র্যাক করছি।

বাংলা ফেক নিউজ ক্লাসিফায়ার বানাচ্ছি — পাবলিকলি।
Repo: https://github.com/fahim3101/bangla-fake-news-classifier

#MachineLearning #NLP #BanglaNLP
```

---

## Posting checklist

1. Attach `accuracy-vs-precision.png`.
2. First line is the hook — it survives LinkedIn's ~2-line preview cut.
3. Post weekday morning (9–11 AM) or evening (8–10 PM) Bangladesh time.
4. Reply to comments in the first hour.
5. 3–5 hashtags is enough.

## Next posts (same style, learning-first)

| After | Topic |
|---|---|
| TF-IDF | What TF-IDF actually does, in one example |
| EDA | What the dataset really looks like |
| Baselines | 3 models, one table |
| Error analysis | The 15 mistakes the model makes |
| Final | Classical vs BanglaBERT: was it worth it? |
