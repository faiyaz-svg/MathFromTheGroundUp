"""Figures for docs/02-middle-school/07-statistics-and-probability/01-describing-data.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/02-middle-school/describing-data.py
"""

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"

# Hypothetical incomes of 30 people, in thousands of dollars.
INCOMES = [22, 28, 31, 34, 36, 38, 40, 41, 43, 45, 46, 48, 50, 52, 54,
           55, 57, 60, 62, 65, 68, 72, 75, 80, 88, 95, 110, 130, 165, 240]

# Commute times of 11 students, in minutes (Example 1).
COMMUTES = [8, 12, 15, 18, 20, 22, 25, 28, 31, 35, 70]

# Quiz scores out of 12 in two sections (Example 3).
SECTION_A = [5, 6, 7, 7, 8, 9]
SECTION_B = [1, 3, 7, 8, 11, 12]


def income_histogram():
    fig, ax = fs.figure(5.6, 3.4)
    edges = list(range(20, 261, 20))
    ax.hist(INCOMES, bins=edges, color=fs.GREEN, edgecolor="white", linewidth=1.2)
    median = statistics.median(INCOMES)
    mean = statistics.mean(INCOMES)
    ax.plot([median, median], [0, 13.2], color=fs.BLUE, linewidth=2)
    ax.plot([mean, mean], [0, 12.0], color=fs.RED, linewidth=2, linestyle="--")
    ax.text(median, 13.4, f"median {median:g}", color=fs.BLUE, ha="center", va="bottom")
    ax.text(mean + 3, 12.0, f"mean {mean:.1f}", color=fs.RED, ha="left", va="center")
    ax.annotate("long tail to the right", xy=(225, 1.2), xytext=(185, 5),
                color=fs.DARK, ha="center",
                arrowprops=dict(arrowstyle="->", color=fs.GRAY))
    ax.set_xticks(edges)
    ax.tick_params(axis="x", labelsize=9)
    ax.set_yticks(range(0, 13, 2))
    ax.set_ylim(0, 14.5)
    ax.set_xlim(15, 265)
    ax.set_xlabel("Income (thousands of dollars)")
    ax.set_ylabel("Number of people")
    return fig, "describing-data-income-histogram"


def commute_boxplot():
    fig, ax = fs.figure(5.6, 2.3)
    lo, q1, med, q3 = 8, 15, 22, 31
    whisker_hi, outlier = 35, 70
    y, h = 0.0, 0.5
    ax.add_patch(fs.plt.Rectangle((q1, y - h / 2), q3 - q1, h, facecolor="#d7f2e6",
                                  edgecolor=fs.GREEN, linewidth=2))
    ax.plot([med, med], [y - h / 2, y + h / 2], color=fs.GREEN, linewidth=3)
    ax.plot([lo, q1], [y, y], color=fs.GREEN, linewidth=2)
    ax.plot([q3, whisker_hi], [y, y], color=fs.GREEN, linewidth=2)
    for x in (lo, whisker_hi):
        ax.plot([x, x], [y - h / 4, y + h / 4], color=fs.GREEN, linewidth=2)
    ax.plot([outlier], [y], marker="o", markersize=8, markerfacecolor="white",
            markeredgecolor=fs.RED, markeredgewidth=2)
    labels = [(lo, "min 8"), (q1, "Q1 = 15"), (med, "median 22"), (q3, "Q3 = 31"),
              (whisker_hi, "35")]
    for i, (x, text) in enumerate(labels):
        ypos = y + h / 2 + 0.18 if i % 2 == 0 else y - h / 2 - 0.18
        ax.text(x, ypos, text, ha="center", va="bottom" if i % 2 == 0 else "top")
    ax.text(outlier, y + 0.22, "outlier 70", ha="center", va="bottom", color=fs.RED)
    ax.annotate("", xy=(q1, -0.95), xytext=(q3, -0.95),
                arrowprops=dict(arrowstyle="<->", color=fs.GRAY))
    ax.text((q1 + q3) / 2, -1.02, "IQR = 16", ha="center", va="top", color=fs.DARK)
    ax.set_xlim(0, 80)
    ax.set_ylim(-1.35, 0.85)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xticks(range(0, 81, 10))
    ax.set_xlabel("Commute time (minutes)")
    return fig, "describing-data-commute-boxplot"


def dot_plots():
    fig, ax = fs.figure(5.6, 2.8)
    rows = [("Section A", SECTION_A, 2.2, fs.GREEN), ("Section B", SECTION_B, 0.0, fs.BLUE)]
    for name, data, base, colour in rows:
        counts = {}
        for x in data:
            counts[x] = counts.get(x, 0) + 1
            ax.plot([x], [base + 0.42 * counts[x]], marker="o", markersize=10, color=colour)
        ax.plot([0.5, 12.5], [base, base], color=fs.DARK, linewidth=1)
        ax.text(0.3, base + 0.42, name, ha="right", va="center", color=colour)
        ax.plot([7], [base - 0.05], marker="^", markersize=9, color=fs.RED, clip_on=False)
    ax.text(7.35, 0.05 - 0.4, "mean 7", color=fs.RED, ha="left", va="center")
    ax.text(7.35, 2.25 - 0.4, "mean 7", color=fs.RED, ha="left", va="center")
    ax.set_xlim(-2.3, 12.8)
    ax.set_ylim(-0.7, 3.4)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_xticks(range(1, 13))
    ax.tick_params(axis="x", length=0)
    ax.set_xlabel("Quiz score (out of 12)")
    return fig, "describing-data-dot-plots"


FIGURES = [income_histogram, commute_boxplot, dot_plots]

if __name__ == "__main__":
    for draw in FIGURES:
        fig, name = draw()
        fs.save(fig, FOLDER, name)
