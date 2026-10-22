"""Figure for docs/07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/present-value-npv-and-bond-prices.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"
SLUG = "present-value-npv-and-bond-prices"


def price(y, face=1000.0, coupon=0.04, n=10):
    c = face * coupon
    k = np.arange(1, n + 1)
    return np.sum(c / (1 + y) ** k) + face / (1 + y) ** n


def price_yield():
    fig, ax = fs.figure(5.4, 3.7)
    ys = np.linspace(0.005, 0.085, 200)
    ps = [price(y) for y in ys]
    ax.plot(ys * 100, ps, color=fs.GREEN, lw=2.2)
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_xlabel("yield (% per year)")
    ax.set_ylabel("bond price")
    ax.set_xlim(0, 9)
    ax.set_ylim(700, 1250)
    ax.axhline(1000, color=fs.GRAY, lw=1.0, ls="--")
    ax.text(8.9, 990, "face value 1000", color=fs.GRAY, ha="right", va="top", fontsize=9.5)
    for y, dx, dy, ha in ((0.03, 0.2, 14, "left"), (0.04, 0.2, 14, "left"), (0.05, 0.2, 14, "left")):
        p = price(y)
        col = fs.ORANGE if y != 0.04 else fs.DARK
        ax.plot([y * 100], [p], "o", color=col, zorder=5)
        ax.text(y * 100 + dx, p + dy, f"{y * 100:.0f}%: {p:.2f}", color=col, fontsize=9.5, ha=ha, va="bottom")
    ax.text(5.6, 1150, "10-year bond, 4% annual coupon", color=fs.GREEN, fontsize=10, ha="left")
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-price-yield")


if __name__ == "__main__":
    price_yield()
