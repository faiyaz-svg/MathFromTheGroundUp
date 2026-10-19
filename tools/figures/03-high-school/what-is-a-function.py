"""Figures for docs/03-high-school/03-functions/01-what-is-a-function.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/what-is-a-function.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Ellipse  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "what-is-a-function"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def codomain_range():
    """f(x) = x^2 from {-2,...,2} to {0,...,5}: the range sits inside the codomain."""
    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.3, 10.4)
    ax.axis("off")
    ax.add_patch(Ellipse((2.0, 5), 3.0, 8.6, fill=False, ec=fs.DARK, lw=1.2))
    ax.add_patch(Ellipse((8.0, 5), 3.0, 9.4, fill=False, ec=fs.DARK, lw=1.2))
    ax.text(2.0, 9.7, "domain A", ha="center", va="bottom", fontsize=11)
    ax.text(8.0, 9.9, "codomain B", ha="center", va="bottom", fontsize=11)

    a_vals = [-2, -1, 0, 1, 2]
    b_vals = [0, 1, 2, 3, 4, 5]
    a_y = {v: 8.0 - 1.5 * i for i, v in enumerate(a_vals)}
    b_y = {v: 8.5 - 1.5 * i for i, v in enumerate(b_vals)}
    in_range = {v * v for v in a_vals}

    for v, y in a_y.items():
        ax.text(2.0, y, f"{v}".replace("-", M), ha="center", va="center", fontsize=12)
    for v, y in b_y.items():
        col = fs.GREEN if v in in_range else fs.GRAY
        ax.text(8.0, y, str(v), ha="center", va="center", fontsize=12, color=col,
                fontweight="bold" if v in in_range else "normal")
    for a in a_vals:
        b = a * a
        ax.annotate("", xy=(7.4, b_y[b]), xytext=(2.6, a_y[a]),
                    arrowprops=dict(arrowstyle="-|>", color=fs.GREEN, lw=1.4, shrinkA=2, shrinkB=2))
    ax.text(5.0, -0.7, "green: in the range {0, 1, 4}    gray: in B but never an output",
            ha="center", va="center", fontsize=10, color=fs.DARK)
    fs.save(fig, FOLDER, f"{SLUG}-codomain-range")


def natural_domain():
    """y = sqrt(x + 1) / (x - 3): the formula works on [-1, 3) and (3, infinity)."""
    fig, ax = plt.subplots(figsize=(6.2, 4.0))
    ax.set_xlim(-2.2, 12.6)
    ax.set_ylim(-5.3, 4.2)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_xticks(range(-2, 13, 2))
    ax.set_yticks([-4, -2, 2, 4])
    ax.tick_params(labelsize=9)

    def h(t):
        return math.sqrt(t + 1) / (t - 3)

    left = [-1 + (2.9995 - (-1)) * i / 400 for i in range(401)]
    left = [t for t in left if h(t) > -4.4]
    right = [3.0006 + (12.4 - 3.0006) * i / 600 for i in range(601)]
    right = [t for t in right if h(t) < 4.1]
    ax.plot(left, [h(t) for t in left], color=fs.BLUE, zorder=3)
    ax.plot(right, [h(t) for t in right], color=fs.BLUE, zorder=3)
    ax.axvline(3, color=fs.RED, lw=1.2, ls="--", zorder=2)
    ax.plot(-1, 0, "o", color=fs.BLUE, zorder=5)
    ax.text(3.25, -3.7, "x = 3", color=fs.RED, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(5.5, 2.4, "h(x) = √(x + 1) / (x − 3)", color=fs.BLUE, fontsize=10.5,
            style="italic", ha="left", va="center", bbox=BOX)

    # The domain drawn on a strip near the bottom of the plot.
    y0 = -4.95
    ax.plot([-1, 2.97], [y0, y0], color=fs.GREEN, lw=5, solid_capstyle="butt", zorder=4)
    ax.plot([3.03, 12.5], [y0, y0], color=fs.GREEN, lw=5, solid_capstyle="butt", zorder=4)
    ax.plot(-1, y0, "o", color=fs.GREEN, ms=7, zorder=5)
    ax.plot(3, y0, "o", mfc="white", mec=fs.GREEN, ms=7, mew=1.6, zorder=6)
    ax.text(6.0, y0 + 0.55, "domain", color=fs.GREEN, fontsize=10, ha="left", va="bottom")
    ax.set_clip_on(False)
    fs.save(fig, FOLDER, f"{SLUG}-natural-domain")


def domain_changes_range():
    """The rule x^2 + 1 with two different domains is two different functions."""
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.8), sharey=True)
    for ax in axes:
        ax.set_xlim(-3.6, 4.2)
        ax.set_ylim(-0.6, 11.6)
        ax.set_xticks(range(-3, 5))
        ax.set_yticks([1, 5, 10])
        ax.grid(True)
        ax.set_axisbelow(True)
        ax.tick_params(labelsize=9)
        ax.spines["left"].set_position(("data", -3.6))
        ax.spines["bottom"].set_position(("data", -0.6))

    # Left: domain R, range [1, infinity).
    ax = axes[0]
    xs = [-3.2 + 6.9 * i / 300 for i in range(301)]
    ax.plot(xs, [t * t + 1 for t in xs], color=fs.BLUE, zorder=3)
    ax.plot([-3.2, 3.9], [-0.35, -0.35], color=fs.GREEN, lw=5, solid_capstyle="butt", zorder=4)
    ax.plot([-3.35, -3.35], [1, 11.4], color=fs.ORANGE, lw=5, solid_capstyle="butt", zorder=4)
    ax.text(0.2, -0.05, "domain: all real numbers", color=fs.GREEN, fontsize=9, ha="center",
            va="bottom", bbox=BOX, zorder=6)
    ax.text(-3.1, 2.8, "range\n[1, ∞)", color=fs.ORANGE, fontsize=9, ha="left", va="center",
            bbox=BOX, zorder=6)
    ax.text(1.5, 9.2, "x ∈ ℝ", color=fs.BLUE, fontsize=10, style="italic", bbox=BOX)

    # Right: domain [-2, 3], range [1, 10].
    ax = axes[1]
    xs = [-2 + 5 * i / 300 for i in range(301)]
    ax.plot(xs, [t * t + 1 for t in xs], color=fs.BLUE, zorder=3)
    ax.plot([-2, 3], [5, 10], "o", color=fs.BLUE, zorder=5)
    ax.plot([-2, 3], [-0.35, -0.35], color=fs.GREEN, lw=5, solid_capstyle="butt", zorder=4)
    ax.plot([-3.35, -3.35], [1, 10], color=fs.ORANGE, lw=5, solid_capstyle="butt", zorder=4)
    ax.text(0.5, -0.05, "domain [−2, 3]", color=fs.GREEN, fontsize=9, ha="center",
            va="bottom", bbox=BOX, zorder=6)
    ax.text(-3.1, 2.8, "range\n[1, 10]", color=fs.ORANGE, fontsize=9, ha="left", va="center",
            bbox=BOX, zorder=6)
    ax.text(-1.6, 9.2, f"x ∈ [{M}2, 3]", color=fs.BLUE, fontsize=10, style="italic", bbox=BOX)
    ax.text(3.15, 10, "(3, 10)", fontsize=9, ha="left", va="center")
    ax.text(-2.15, 5, f"({M}2, 5)", fontsize=9, ha="right", va="center", bbox=BOX)
    fig.tight_layout(w_pad=1.2)
    fs.save(fig, FOLDER, f"{SLUG}-domain-changes-range")


if __name__ == "__main__":
    codomain_range()
    natural_domain()
    domain_changes_range()
