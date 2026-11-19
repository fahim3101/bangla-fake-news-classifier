"""Generate the LinkedIn card for the accuracy vs precision lesson.

Usage:  python linkedin/make_card.py
Output: linkedin/accuracy-vs-precision.png  (1200 x 1200)
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent / "accuracy-vs-precision.png"

W, H = 1200, 1200
BG = "#0B1220"
CARD = "#131C2E"
ACCENT = "#38BDF8"
TEXT = "#F8FAFC"
MUTED = "#94A3B8"
DIM = "#64748B"
LINE = "#1E293B"

fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

ax.add_patch(plt.Rectangle((0, H - 10), W, 10, color=ACCENT, lw=0))


def card(x, y, w, h):
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0,rounding_size=16",
            facecolor=CARD, edgecolor="none",
        )
    )


# ---------- Header ----------
ax.text(80, 1105, "BANGLA FAKE NEWS CLASSIFIER  ·  BUILD IN PUBLIC",
        color=ACCENT, fontsize=18, fontweight="bold", va="center")
ax.text(80, 1005, "Why accuracy", color=TEXT, fontsize=74, fontweight="bold", va="center")
ax.text(80, 920, "lies.", color=ACCENT, fontsize=74, fontweight="bold", va="center")

# ---------- Practice numbers ----------
ax.text(80, 850, "100 news  →  20 fake, 80 real", color=MUTED, fontsize=24, va="center")
for x, label in zip((80, 340, 600, 860), ("TP 15", "FN 5", "FP 10", "TN 70")):
    ax.text(x, 790, label, color=TEXT, fontsize=30, fontweight="bold", va="center")

# ---------- Metric cards ----------
metrics = [("0.85", "Accuracy"), ("0.60", "Precision"), ("0.75", "Recall"), ("0.67", "F1 score")]
mw, mh, mgap = 245, 110, 15
for i, (value, label) in enumerate(metrics):
    x = 80 + i * (mw + mgap)
    card(x, 650, mw, mh)
    ax.text(x + mw / 2, 720, value, color=ACCENT, fontsize=40,
            fontweight="bold", ha="center", va="center")
    ax.text(x + mw / 2, 680, label, color=MUTED, fontsize=17, ha="center", va="center")

# ---------- The gap ----------
ax.plot([80, 1120], [600, 600], color=LINE, lw=2)
ax.text(80, 550, "THE GAP", color=ACCENT, fontsize=18, fontweight="bold", va="center")
ax.text(80, 490, "Accuracy said the model was fine.", color=TEXT, fontsize=27, va="center")
ax.text(80, 440, "Precision said 40% of its “fake” calls were wrong.",
        color=TEXT, fontsize=27, va="center")

# ---------- Next ----------
ax.text(80, 340, "NEXT", color=ACCENT, fontsize=18, fontweight="bold", va="center")
ax.text(80, 290, "TF-IDF + n-grams  →  classical baseline  →  BanglaBERT",
        color=MUTED, fontsize=22, va="center")

# ---------- Footer ----------
ax.plot([80, 1120], [160, 160], color=LINE, lw=2)
ax.text(80, 105, "github.com/fahim3101/bangla-fake-news-classifier",
        color=ACCENT, fontsize=20, va="center")
ax.text(1120, 105, "Bangla NLP", color=DIM, fontsize=18, ha="right", va="center")

fig.savefig(OUT, facecolor=BG)
print(f"saved: {OUT}")
