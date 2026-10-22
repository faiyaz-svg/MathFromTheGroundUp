"""Figures for docs/05-university-core/08-statistics/04-correlation-and-linear-regression.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/correlation-and-linear-regression.py
"""

import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "correlation-and-linear-regression"

HOURS = np.array([1, 1.5, 2, 3, 3.5, 4, 5, 5.5, 6, 7, 8, 9])
SCORE = np.array([50, 58, 55, 65, 60, 70, 68, 77, 80, 79, 90, 91])


def style(ax, grid="y"):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True, axis=grid)
    ax.set_axisbelow(True)


def line_fit(x, y):
    b, a = np.polyfit(x, y, 1)
    return a, b


def fit():
    """The least-squares line, the point of means and the residuals."""
    a, b = line_fit(HOURS, SCORE)
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    style(ax)
    xs = np.array([0.5, 9.5])
    ax.plot(xs, a + b * xs, color=fs.GREEN, lw=2.2, zorder=3)
    for x, y in zip(HOURS, SCORE):
        ax.plot([x, x], [y, a + b * x], color=fs.RED, lw=1.4, zorder=2)
    ax.plot(HOURS, SCORE, "o", color=fs.DARK, ms=6, zorder=4)
    xb, yb = HOURS.mean(), SCORE.mean()
    ax.plot([xb], [yb], "D", color=fs.ORANGE, ms=8, zorder=5)
    ax.annotate("(mean hours, mean score)\n= (4.625, 70.25)", (xb, yb), (5.6, 54), color="#a35a00", fontsize=9.5,
                arrowprops=dict(arrowstyle="-", color=fs.ORANGE, lw=1))
    ax.text(0.6, 88, f"score = {a:.2f} + {b:.2f} × hours", color="#027a50", fontsize=10.5, ha="left")
    ax.text(0.6, 83, "red: residuals", color=fs.RED, fontsize=10, ha="left")
    ax.set_xlabel("hours studied", fontsize=10)
    ax.set_ylabel("exam score", fontsize=10)
    ax.set_xlim(0, 10)
    ax.set_ylim(45, 97)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-fit")


def angle():
    """Correlation as the cosine of the angle between centred data vectors."""
    fig, axes = plt.subplots(1, 3, figsize=(8.6, 2.9))
    cases = [(0.972, "r = 0.97"), (0.0, "r = 0"), (-0.8, "r = −0.8")]
    for ax, (r, label) in zip(axes, cases):
        theta = math.acos(r)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.annotate("", (1, 0), (0, 0), arrowprops=dict(arrowstyle="-|>", color=fs.BLUE, lw=2.2))
        ax.annotate("", (math.cos(theta), math.sin(theta)), (0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=fs.GREEN, lw=2.2))
        t = np.linspace(0, theta, 40)
        ax.plot(0.32 * np.cos(t), 0.32 * np.sin(t), color=fs.DARK, lw=1.2)
        mid = theta / 2
        ax.text(0.47 * math.cos(mid) + (0.06 if theta < 0.5 else 0), 0.47 * math.sin(mid) + (0.04 if theta < 0.5 else 0),
                f"{math.degrees(theta):.0f}°", fontsize=9.5, ha="center", va="center")
        ax.text(1.04, -0.02, "x", color=fs.BLUE, fontsize=11, ha="left", va="top")
        ax.text(1.05 * math.cos(theta), 1.05 * math.sin(theta) + 0.05, "y", color="#027a50", fontsize=11, ha="center")
        ax.text(0.2, -0.35, label, fontsize=11, ha="center")
        ax.set_xlim(-1.1, 1.3)
        ax.set_ylim(-0.5, 1.2)
    fig.tight_layout(w_pad=0.5)
    fs.save(fig, FOLDER, f"{SLUG}-angle")


def residuals():
    """Residual plots: a good linear fit, and a line fitted to curved data."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.3))
    a, b = line_fit(HOURS, SCORE)
    style(ax1)
    ax1.axhline(0, color=fs.DARK, lw=1.2)
    ax1.plot(HOURS, SCORE - (a + b * HOURS), "o", color=fs.GREEN, ms=6, zorder=3)
    ax1.set_xlabel("hours studied (study data)", fontsize=10)
    ax1.set_ylabel("residual (points)", fontsize=10)
    ax1.set_ylim(-9, 9)
    speed = np.array([30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130])
    fuel = np.array([9.0, 7.6, 6.7, 6.1, 5.8, 5.9, 6.4, 7.1, 8.0, 9.1, 10.3])
    a2, b2 = line_fit(speed, fuel)
    style(ax2)
    ax2.axhline(0, color=fs.DARK, lw=1.2)
    ax2.plot(speed, fuel - (a2 + b2 * speed), "o", color=fs.RED, ms=6, zorder=3)
    ax2.set_xlabel("speed, km/h (fuel data)", fontsize=10)
    ax2.set_ylabel("residual (L/100 km)", fontsize=10)
    ax2.set_ylim(-3, 3)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-residuals")


def anscombe():
    """Anscombe's quartet: four data sets with the same line and the same r."""
    x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
    y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
    y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
    x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
    y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]
    sets = [(x1, y1), (x1, y2), (x1, y3), (x4, y4)]
    fig, axes = plt.subplots(1, 4, figsize=(9.6, 2.7), sharex=True, sharey=True)
    for ax, (x, y), name in zip(axes, sets, "ABCD"):
        style(ax)
        ax.plot([3, 20], [3 + 0.5 * 3, 3 + 0.5 * 20], color=fs.GREEN, lw=1.8, zorder=2)
        ax.plot(x, y, "o", color=fs.DARK, ms=5, zorder=3)
        ax.text(3.4, 12.8, name, fontsize=11, color=fs.DARK, va="top")
        ax.set_xlim(2.5, 20.5)
        ax.set_ylim(2, 14)
        ax.set_xticks([5, 10, 15, 20])
    axes[0].set_ylabel("y", fontsize=10)
    for ax in axes:
        ax.set_xlabel("x", fontsize=10)
    fig.tight_layout(w_pad=0.6)
    fs.save(fig, FOLDER, f"{SLUG}-anscombe")


def influence():
    """One distant point flips the line."""
    x2 = np.append(HOURS, 14)
    y2 = np.append(SCORE, 50)
    a, b = line_fit(HOURS, SCORE)
    a2, b2 = line_fit(x2, y2)
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    style(ax)
    xs = np.array([0, 15])
    ax.plot([0, 12.5], [a, a + b * 12.5], color=fs.GREEN, lw=2, zorder=3)
    ax.plot(xs, a2 + b2 * xs, color=fs.RED, lw=2, ls="--", zorder=3)
    ax.plot(HOURS, SCORE, "o", color=fs.DARK, ms=6, zorder=4)
    ax.plot([14], [50], "o", color=fs.RED, ms=9, zorder=5)
    ax.text(14, 44, "one more student: (14, 50)", color=fs.RED, ha="right", fontsize=9.5)
    ax.text(0.3, 103, f"without: slope {b:.2f}, r = 0.97", color="#027a50", ha="left", fontsize=10)
    ax.text(15.1, a2 + b2 * 15 - 1, f"with: slope {b2:.2f},\nr = 0.32", color=fs.RED, ha="left", va="top", fontsize=10)
    ax.set_xlabel("hours studied", fontsize=10)
    ax.set_ylabel("exam score", fontsize=10)
    ax.set_xlim(0, 19.5)
    ax.set_ylim(38, 108)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-influence")


def regression_to_mean():
    """Two exams with correlation 0.5: the top scorers on the first do worse on the second."""
    rng = random.Random(4)
    rho, n = 0.5, 2000
    first, second = [], []
    for _ in range(n):
        z1 = rng.gauss(0, 1)
        z2 = rho * z1 + math.sqrt(1 - rho * rho) * rng.gauss(0, 1)
        first.append(70 + 10 * z1)
        second.append(70 + 10 * z2)
    first, second = np.array(first), np.array(second)
    cut = np.quantile(first, 0.9)
    top = first >= cut
    print("top 10%:", top.sum(), "first mean", first[top].mean(), "second mean", second[top].mean())
    print("r =", np.corrcoef(first, second)[0, 1])
    fig, ax = plt.subplots(figsize=(5.6, 5.0))
    style(ax, "both")
    ax.plot(first[~top], second[~top], "o", color=fs.GRAY, ms=3, alpha=0.5, zorder=2)
    ax.plot(first[top], second[top], "o", color=fs.ORANGE, ms=3.5, zorder=3)
    xs = np.array([35, 105])
    ax.plot(xs, xs, color=fs.DARK, lw=1.4, ls="--", zorder=4)
    b, a = np.polyfit(first, second, 1)
    ax.plot(xs, a + b * xs, color=fs.GREEN, lw=2.2, zorder=4)
    ax.axvline(cut, color=fs.ORANGE, lw=1, zorder=1)
    ax.text(104, 106, "second = first", color=fs.DARK, ha="right", fontsize=10)
    ax.annotate("regression line", (99, a + b * 99), (97, 45), color="#027a50", ha="center", fontsize=10,
                arrowprops=dict(arrowstyle="-", color=fs.GREEN, lw=1))
    ax.text(cut + 1, 40, "top 10% on\nthe first exam", color="#a35a00", ha="left", fontsize=9.5)
    ax.set_xlabel("first exam", fontsize=10)
    ax.set_ylabel("second exam", fontsize=10)
    ax.set_aspect("equal")
    ax.set_xlim(35, 108)
    ax.set_ylim(35, 108)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-mean")


if __name__ == "__main__":
    fit()
    angle()
    residuals()
    anscombe()
    influence()
    regression_to_mean()
