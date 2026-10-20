"""Figures for docs/03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/logarithm-properties.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "logarithm-properties"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def ruler(ax, y, shift, color, label_above):
    """A log scale from 1 to 10: the mark for k sits at log10(k), moved right by shift."""
    ax.add_patch(Rectangle((shift, y), 1.0, 0.5, facecolor="#f6f7f8", edgecolor=fs.DARK, lw=1.0, zorder=2))
    for k in range(1, 11):
        x = shift + math.log10(k)
        ax.plot([x, x], [y, y + 0.22], color=fs.DARK, lw=1.0, zorder=3)
        ty = y + 0.62 if label_above else y - 0.12
        va = "bottom" if label_above else "top"
        ax.text(x, ty, str(k), color=color, fontsize=9.5, ha="center", va=va, zorder=4)


def slide_rule():
    """2 times 3 on two sliding log scales: lengths add."""
    fig, ax = plt.subplots(figsize=(6.2, 2.9))
    s = math.log10(2)
    ruler(ax, 1.5, 0.0, fs.GREEN, True)
    ruler(ax, 1.0, s, fs.BLUE, False)
    # lengths along the top scale
    ax.annotate("", xy=(s, 2.75), xytext=(0, 2.75), arrowprops=dict(arrowstyle="<->", color=fs.GREEN, lw=1.3))
    ax.text(s / 2, 2.85, "$\\log 2$", color=fs.GREEN, fontsize=9.5, ha="center", va="bottom")
    ax.annotate("", xy=(math.log10(6), 2.75), xytext=(s, 2.75),
                arrowprops=dict(arrowstyle="<->", color=fs.BLUE, lw=1.3))
    ax.text((s + math.log10(6)) / 2, 2.85, "$\\log 3$", color=fs.BLUE, fontsize=9.5, ha="center", va="bottom")
    # guide lines for the answer
    x6 = math.log10(6)
    ax.plot([x6, x6], [1.12, 1.5], color=fs.RED, lw=1.3, ls="--", zorder=5)
    ax.plot([s, s], [1.0, 2.75], color=fs.GRAY, lw=0.9, ls=":", zorder=1)
    ax.text(-0.04, 1.75, "fixed\nscale", color=fs.GREEN, fontsize=9, ha="right", va="center")
    ax.text(s - 0.04, 1.25, "sliding\nscale", color=fs.BLUE, fontsize=9, ha="right", va="center")
    ax.text(x6, 0.45, "the 3 on the sliding scale sits under the 6: $2 \\times 3 = 6$", color=fs.RED, fontsize=9.5,
            ha="center", va="center")
    ax.set_xlim(-0.2, 1.32)
    ax.set_ylim(0.2, 3.2)
    ax.axis("off")
    fs.save(fig, FOLDER, f"{SLUG}-slide-rule")


def semilog():
    """The same growth, y = 2^t, on a linear axis and on a log axis."""
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.5))
    ts = [i / 20 for i in range(0, 201)]
    ax = axes[0]
    ax.plot(ts, [2**t for t in ts], color=fs.GREEN, zorder=4)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1100)
    ax.set_xticks([0, 2, 4, 6, 8, 10])
    ax.set_yticks([0, 250, 500, 750, 1000])
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_xlabel("t")
    ax.set_ylabel("$2^t$")
    ax.text(0.3, 1010, "linear axis: a curve", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax = axes[1]
    ax.plot(ts, [2**t for t in ts], color=fs.GREEN, zorder=4)
    ax.set_yscale("log")
    ax.set_xlim(0, 10)
    ax.set_ylim(0.7, 1800)
    ax.set_xticks([0, 2, 4, 6, 8, 10])
    ax.set_yticks([1, 10, 100, 1000])
    ax.set_yticklabels(["1", "10", "100", "1000"])
    ax.minorticks_off()
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_xlabel("t")
    ax.set_ylabel("$2^t$")
    ax.text(0.3, 1250, "log axis: a straight line", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    for t in (0, 1, 2):
        ax.plot([t], [2**t], "o", color=fs.DARK, ms=5, zorder=6)
    ax.text(1.4, 1.3, "each step of 1 in $t$\nmoves up by $\\log_{10} 2$", color=fs.DARK, fontsize=8.5, ha="left",
            va="center")
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-semilog")


if __name__ == "__main__":
    slide_rule()
    semilog()
