"""Generate the LinkedIn summary card for Day 1-2 of the project.

Usage:  python linkedin/make_card.py
Output: linkedin/day01-02-summary.png  (1200 x 1200)
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent / "day01-02-summary.png"

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

# Top accent bar
ax.add_patch(plt.Rectangle((0, H - 10), W, 10, color=ACCENT, lw=0))


def card(x, y, w, h, color=CARD):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0,rounding_size=16",
            facecolor=color,
            edgecolor="none",
        )
    )


# ---------- Header ----------
ax.text(80, 1110, "14-DAY ML PROJECT  ·  BUILD IN PUBLIC", color=ACCENT,
        fontsize=19, fontweight="bold", va="center")
ax.text(80, 1020, "Day 1–2", color=TEXT, fontsize=88, fontweight="bold", va="center")
ax.text(80, 950, "Setup, pandas fundamentals & the confusion matrix",
        color=MUTED, fontsize=29, va="center")

ax.plot([80, 1120], [905, 905], color=LINE, lw=2)

# ---------- Section: what I built ----------
ax.text(80, 855, "WHAT I BUILT", color=ACCENT, fontsize=19, fontweight="bold", va="center")

chips = ["Python 3.14 + venv", "pandas 3.1", "scikit-learn 1.9", "JupyterLab"]
chip_w, chip_h, gap = 245, 56, 15
for i, label in enumerate(chips):
    x = 80 + i * (chip_w + gap)
    card(x, 775, chip_w, chip_h)
    ax.text(x + chip_w / 2, 775 + chip_h / 2, label, color=TEXT,
            fontsize=16, ha="center", va="center")

# ---------- Section: practice ----------
ax.text(80, 705, "PRACTICE: 100 NEWS  →  20 FAKE / 80 REAL",
        color=ACCENT, fontsize=19, fontweight="bold", va="center")
for x, label in zip((80, 340, 600, 860), ("TP 15", "FN 5", "FP 10", "TN 70")):
    ax.text(x, 650, label, color=TEXT, fontsize=28, fontweight="bold", va="center")

metrics = [("0.60", "Precision"), ("0.75", "Recall"), ("0.67", "F1 score"), ("0.85", "Accuracy")]
mw, mh, mgap = 245, 105, 15
for i, (value, label) in enumerate(metrics):
    x = 80 + i * (mw + mgap)
    card(x, 520, mw, mh)
    ax.text(x + mw / 2, 585, value, color=ACCENT, fontsize=38,
            fontweight="bold", ha="center", va="center")
    ax.text(x + mw / 2, 545, label, color=MUTED, fontsize=17, ha="center", va="center")

# ---------- Section: takeaway ----------
ax.text(80, 460, "THE TAKEAWAY", color=ACCENT, fontsize=19, fontweight="bold", va="center")
ax.text(80, 410, "Accuracy 85% looked fine — precision showed that 40%",
        color=TEXT, fontsize=26, va="center")
ax.text(80, 365, "of everything flagged “fake” was actually real.",
        color=TEXT, fontsize=26, va="center")

# ---------- Section: next ----------
ax.text(80, 290, "NEXT", color=ACCENT, fontsize=19, fontweight="bold", va="center")
ax.text(80, 240, "TF-IDF + n-grams  →  classical baseline  →  BanglaBERT",
        color=MUTED, fontsize=23, va="center")

# ---------- Footer ----------
ax.plot([80, 1120], [140, 140], color=LINE, lw=2)
ax.text(80, 90, "github.com/fahim3101/bangla-fake-news-classifier",
        color=ACCENT, fontsize=20, va="center")
ax.text(1120, 90, "Day 1–2 of 14", color=DIM, fontsize=18, ha="right", va="center")

fig.savefig(OUT, facecolor=BG)
print(f"saved: {OUT}")
