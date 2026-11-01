"""Figure for docs/08-financial-math/08-starting-your-career/01-comparing-job-offers.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/08-financial-math/comparing-job-offers.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "08-financial-math"
SLUG = "comparing-job-offers"

UNITS = 1920          # RSUs in the grant
PRICE = 25.0          # price per unit at grant, dollars
CLIFF = 12            # months before the first vest


def vested_with_cliff(m):
    """Units vested after m whole months: nothing before the cliff, then 1/48 of the grant per month."""
    return 0.0 if m < CLIFF else UNITS * m / 48


def vested_straight(m):
    return UNITS * m / 48


def main():
    months = np.arange(0, 49)
    cliff = np.array([vested_with_cliff(m) for m in months]) * PRICE / 1000
    straight = np.array([vested_straight(m) for m in months]) * PRICE / 1000

    fig, ax = fs.figure(6.4, 4.0)
    ax.grid(True, axis="y")
    ax.set_axisbelow(True)
    ax.plot(months, straight, color=fs.GRAY, lw=1.6, ls="--")
    ax.plot(months, cliff, color=fs.GREEN, lw=2.4, drawstyle="steps-post")
    ax.set_xlim(0, 48)
    ax.set_ylim(0, 52)
    ax.set_xticks([0, 6, 12, 18, 24, 30, 36, 42, 48])
    ax.set_xlabel("months since the start date", fontsize=10)
    ax.set_ylabel("value of vested units at \\$25 (thousands of dollars)", fontsize=10)
    ax.tick_params(labelsize=9, length=3)

    # the jump at the cliff
    ax.plot([12, 12], [0, 12], color=fs.GREEN, lw=1.0, ls=":")
    ax.text(13.0, 7.5, "cliff: 25% vests at month 12 (\\$12,000)", color=fs.GREEN, fontsize=9.5, ha="left", va="center")

    # a person who leaves at month 11 or month 18
    ax.plot([11], [0], "o", color=fs.RED, ms=6, zorder=5)
    ax.annotate("leave at month 11: \\$0", xy=(11, 0.6), xytext=(13.0, 3.0), fontsize=9.5, color=fs.RED,
                ha="left", va="center", arrowprops=dict(arrowstyle="-", color=fs.RED, lw=1.0))
    ax.plot([18], [vested_with_cliff(18) * PRICE / 1000], "o", color=fs.RED, ms=6, zorder=5)
    ax.text(18.8, 14.6, "leave at month 18: \\$18,000", color=fs.RED, fontsize=9.5, ha="left", va="center")

    ax.text(28, 38.0, "no cliff", color=fs.GRAY, fontsize=9.5, ha="center", va="center")
    ax.text(38, 28.0, "1-year cliff", color=fs.GREEN, fontsize=9.5, ha="center", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-vesting")


if __name__ == "__main__":
    main()
