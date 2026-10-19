"""Figures for docs/02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/02-middle-school/scatter-plots-and-two-way-tables.py
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"

# Hours studied and exam scores of 12 students (Example 1).
HOURS = [1, 1.5, 2, 3, 3.5, 4, 5, 5.5, 6, 7, 8, 9]
SCORES = [50, 58, 55, 65, 60, 70, 68, 77, 80, 79, 90, 91]

# Speed and fuel use of one car (Example 3).
SPEEDS = list(range(30, 131, 10))
FUEL = [9.0, 7.6, 6.7, 6.1, 5.8, 5.9, 6.4, 7.1, 8.0, 9.1, 10.3]


def study_scatter():
    fig, ax = fs.figure(5.4, 3.8)
    ax.grid(True, zorder=0)
    xs = np.linspace(0, 10, 2)
    ax.plot(xs, 5 * xs + 47, color=fs.BLUE, linewidth=2, zorder=2)
    ax.scatter(HOURS, SCORES, color=fs.GREEN, s=40, zorder=3)
    for x, y, tx, ty in [(1, 52, 0.15, 56.5), (9, 92, 8.75, 94.5)]:
        ax.plot([x], [y], marker="o", markersize=9, markerfacecolor="white",
                markeredgecolor=fs.BLUE, markeredgewidth=2, zorder=4)
        ax.text(tx, ty, f"({x}, {y})", color=fs.BLUE, ha="left" if x < 5 else "right",
                va="bottom")
    ax.plot([6, 6, 0], [40, 77, 77], color=fs.GRAY, linestyle=":", linewidth=1.5, zorder=1)
    ax.text(6.15, 72, "6 h predicts 77", color=fs.DARK, ha="left", va="top")
    ax.text(8.6, 82.5, "y = 5x + 47", color=fs.BLUE, ha="left", va="top")
    ax.set_xlim(0, 10)
    ax.set_ylim(40, 100)
    ax.set_xticks(range(0, 11))
    ax.set_xlabel("Hours studied")
    ax.set_ylabel("Exam score")
    return fig, "scatter-plots-and-two-way-tables-study-line"


def association_panels():
    rng = np.random.default_rng(4)
    fig, axes = fs.plt.subplots(3, 2, figsize=(5.6, 6.6))
    n = 30
    x = rng.uniform(0, 10, n)

    def tidy(ax, title):
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-0.5, 10.5)
        ax.set_ylim(-1, 11)
        ax.set_title(title, fontsize=11, color=fs.DARK, pad=6)

    panels = [
        ("positive, linear", x, 0.8 * x + 1 + rng.normal(0, 0.9, n), None),
        ("negative, linear", x, 9.5 - 0.8 * x + rng.normal(0, 0.9, n), None),
        ("no association", x, rng.uniform(0.5, 9.5, n), None),
        ("nonlinear", x, 0.4 * (x - 5) ** 2 + 0.5 + rng.normal(0, 0.5, n), None),
    ]
    for ax, (title, px, py, _) in zip(axes.flat[:4], panels):
        ax.scatter(px, py, color=fs.GREEN, s=16)
        tidy(ax, title)

    ax = axes.flat[4]
    c1x = rng.normal(2.5, 0.8, 15)
    c2x = rng.normal(7.5, 0.8, 15)
    ax.scatter(c1x, rng.normal(3, 0.9, 15), color=fs.GREEN, s=16)
    ax.scatter(c2x, rng.normal(7.5, 0.9, 15), color=fs.GREEN, s=16)
    tidy(ax, "two clusters")

    ax = axes.flat[5]
    ox = rng.uniform(0, 10, 25)
    ax.scatter(ox, 0.7 * ox + 1.5 + rng.normal(0, 0.6, 25), color=fs.GREEN, s=16)
    ax.scatter([8], [1.5], color=fs.RED, s=30)
    ax.text(7.6, 1.5, "outlier", color=fs.RED, ha="right", va="center")
    tidy(ax, "positive, with an outlier")

    fig.tight_layout(h_pad=1.2, w_pad=1.5)
    return fig, "scatter-plots-and-two-way-tables-associations"


def fuel_curve():
    fig, ax = fs.figure(5.4, 3.5)
    ax.grid(True, zorder=0)
    ax.scatter(SPEEDS, FUEL, color=fs.GREEN, s=40, zorder=3)
    m, b = np.polyfit(SPEEDS, FUEL, 1)
    xs = np.array([25, 135])
    ax.plot(xs, m * xs + b, color=fs.RED, linestyle="--", linewidth=1.6, zorder=2)
    ax.annotate("a straight line\nmisses the pattern", xy=(125, m * 125 + b),
                xytext=(118, 4.6), ha="center", va="top", color=fs.RED,
                arrowprops=dict(arrowstyle="->", color=fs.RED))
    ax.annotate("lowest fuel use near 70 km/h", xy=(70, 5.6), xytext=(57, 4.4),
                ha="center", va="top", color=fs.DARK,
                arrowprops=dict(arrowstyle="->", color=fs.GRAY))
    ax.set_xlim(20, 140)
    ax.set_ylim(3.5, 11)
    ax.set_xticks(range(20, 141, 20))
    ax.set_xlabel("Speed (km/h)")
    ax.set_ylabel("Fuel use (L/100 km)")
    return fig, "scatter-plots-and-two-way-tables-fuel"


def os_bars():
    fig, ax = fs.figure(5.6, 2.4)
    rows = [("Economics (80)", [45, 33, 2], 80), ("CS (120)", [48, 36, 36], 120)]
    colours = [fs.GREEN, fs.BLUE, fs.ORANGE]
    names = ["Windows", "macOS", "Linux"]
    for i, (label, counts, total) in enumerate(rows):
        left = 0.0
        for j, c in enumerate(counts):
            share = 100 * c / total
            ax.barh(i, share, left=left, color=colours[j], edgecolor="white", height=0.6)
            text = f"{share:g}%"
            if share >= 8:
                ax.text(left + share / 2, i, text, color="white", ha="center", va="center")
            else:
                ax.text(left + share + 1, i, text, color=fs.DARK, ha="left", va="center")
            if i == 1:
                ax.text(left + share / 2, i + 0.42, names[j], color=colours[j], ha="center",
                        va="bottom")
            left += share
    ax.set_yticks([0, 1])
    ax.set_yticklabels([r[0] for r in rows])
    ax.set_xlim(0, 106)
    ax.set_ylim(-0.5, 1.75)
    ax.set_xticks(range(0, 101, 25))
    ax.set_xticklabels([f"{t}%" for t in range(0, 101, 25)])
    ax.set_xlabel("Share of students in the program")
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    return fig, "scatter-plots-and-two-way-tables-os-bars"


FIGURES = [study_scatter, association_panels, fuel_curve, os_bars]

if __name__ == "__main__":
    for draw in FIGURES:
        fig, name = draw()
        fs.save(fig, FOLDER, name)
