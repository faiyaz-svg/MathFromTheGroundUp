"""Figure for docs/08-financial-math/03-time-value-of-money/01-present-and-future-value.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/08-financial-math/present-and-future-value.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from matplotlib.patches import FancyArrowPatch  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "08-financial-math"
SLUG = "present-and-future-value"

I = 0.05
FLOWS = [(1, 1500), (2, 2500), (4, 4000)]


def money(x):
    # A backslash before $ stops matplotlib from reading it as math.
    return "\\${:,.2f}".format(x)


def timeline(ax, y, label):
    ax.plot([-0.35, 4.45], [y, y], color=fs.DARK, lw=1.6, zorder=2)
    for t in range(5):
        ax.plot([t, t], [y - 0.07, y + 0.07], color=fs.DARK, lw=1.6, zorder=2)
        ax.text(t, y - 0.2, str(t), ha="center", va="top", fontsize=10, color=fs.DARK)
    ax.text(-0.35, y + 1.55, label, ha="left", va="bottom", fontsize=11, color=fs.DARK, weight="bold")


def up_arrow(ax, x, y, color, text, height=0.75, ha="center", dx=0.0):
    ax.add_patch(
        FancyArrowPatch((x, y + height), (x, y + 0.05), arrowstyle="-|>", mutation_scale=14, color=color, lw=2.0, zorder=3)
    )
    ax.text(x + dx, y + height + 0.08, text, ha=ha, va="bottom", fontsize=10, color=color)


def curve(ax, start, end, y, rad):
    ax.add_patch(
        FancyArrowPatch(
            (start, y + 0.08), (end, y + 0.08), connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>",
            mutation_scale=11, color=fs.GRAY, lw=1.3, ls="--", zorder=1,
        )
    )


def build():
    fig, ax = fs.figure(7.2, 6.6)
    ax.set_xlim(-0.5, 4.7)
    ax.set_ylim(-1.1, 9.4)
    ax.axis("off")

    ya, yb, yc = 7.0, 3.6, 0.2
    timeline(ax, ya, "Cash flows (end of each year)")
    timeline(ax, yb, "Each moved to date 0: divide by $1.05^{t}$")
    timeline(ax, yc, "Each moved to date 4: multiply by $1.05^{4-t}$")

    for t, c in FLOWS:
        up_arrow(ax, t, ya, fs.DARK, money(c))

    # Row B: dashed arcs from each date back to date 0, and the total at date 0.
    pv_total = sum(c / (1 + I) ** t for t, c in FLOWS)
    for (t, c), rad in zip(FLOWS, (0.5, 0.42, 0.3)):
        curve(ax, t, 0.12, yb, rad)
        ax.text(t, yb - 0.62, money(c / (1 + I) ** t), ha="center", va="top", fontsize=9, color=fs.DARK)
    up_arrow(ax, 0, yb, fs.GREEN, money(pv_total), ha="left", dx=-0.1)

    # Row C: dashed arcs forward to date 4, and the total at date 4.
    fv_total = sum(c * (1 + I) ** (4 - t) for t, c in FLOWS)
    for (t, c), rad in zip(FLOWS[:2], (-0.4, -0.3)):
        curve(ax, t, 3.88, yc, rad)
    for t, c in FLOWS:
        ax.text(t, yc - 0.62, money(c * (1 + I) ** (4 - t)), ha="center", va="top", fontsize=9, color=fs.DARK)
    up_arrow(ax, 4, yc, fs.BLUE, money(fv_total), ha="right", dx=0.1)

    fs.save(fig, FOLDER, f"{SLUG}-timelines")


if __name__ == "__main__":
    build()
