"""Figure for docs/08-financial-math/03-time-value-of-money/02-annuities-and-geometric-series.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/08-financial-math/annuities-and-geometric-series.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "08-financial-math"
SLUG = "annuities-and-geometric-series"

PMT = 300.0
I = 0.05 / 12  # an example rate, not a market rate
N = 300


def balance(k):
    return PMT * ((1 + I) ** k - 1) / I


def build():
    fig, ax = fs.figure(6.2, 3.9)
    months = np.arange(0, N + 1)
    years = months / 12
    total = balance(months)
    paid = PMT * months

    ax.fill_between(years, 0, paid, color=fs.GRAY, alpha=0.45, lw=0)
    ax.fill_between(years, paid, total, color=fs.GREEN, alpha=0.55, lw=0)
    ax.plot(years, total, color=fs.DARK, lw=1.8)

    ax.set_xlim(0, 25)
    ax.set_ylim(0, 190000)
    ax.set_xlabel("years of monthly deposits")
    ax.set_ylabel("account value (dollars)")
    ax.set_xticks([0, 5, 10, 15, 20, 25])
    ax.set_yticks([0, 50000, 100000, 150000])
    ax.set_yticklabels(["0", "50,000", "100,000", "150,000"])
    ax.grid(True, axis="y")
    ax.set_axisbelow(True)

    ax.text(17.5, 30000, "deposits: \\$90,000 in total", color=fs.DARK, ha="center", va="center", fontsize=10.5)
    ax.text(9.0, 95000, "interest: \\$88,652.91 in total", color="#036b45", ha="center", va="center", fontsize=10.5)
    ax.text(24.7, balance(N) + 6000, "\\$178,652.91", color=fs.DARK, ha="right", va="bottom", fontsize=10.5)

    fs.save(fig, FOLDER, f"{SLUG}-savings-plan")


if __name__ == "__main__":
    build()
