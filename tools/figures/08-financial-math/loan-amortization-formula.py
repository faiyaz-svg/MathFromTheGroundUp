"""Figure for docs/08-financial-math/03-time-value-of-money/03-loan-amortization-formula.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/08-financial-math/loan-amortization-formula.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "08-financial-math"
SLUG = "loan-amortization-formula"

PV = 30000.0
I = 0.005  # an example rate of 6% a year, charged monthly


def split(n):
    pmt = PV * I / (1 - (1 + I) ** -n)
    b = PV
    interest, principal = [], []
    for _ in range(n):
        x = I * b
        interest.append(x)
        principal.append(pmt - x)
        b -= pmt - x
    return pmt, np.array(interest), np.array(principal)


def panel(ax, n, label_xy):
    pmt, interest, principal = split(n)
    k = np.arange(1, n + 1)
    ax.fill_between(k, 0, principal, color=fs.GREEN, alpha=0.6, lw=0)
    ax.fill_between(k, principal, pmt, color=fs.ORANGE, alpha=0.6, lw=0)
    ax.plot([0, n + 1], [pmt, pmt], color=fs.DARK, lw=1.4)
    ax.set_xlim(0, n + 1)
    ax.set_ylim(0, pmt * 1.18)
    ax.set_xlabel("payment number")
    ax.grid(True, axis="y")
    ax.set_axisbelow(True)
    return pmt, interest, principal


def build():
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(9.6, 3.9))

    pmt, interest, principal = panel(ax1, 120, None)
    ax1.set_ylabel("dollars of each payment")
    ax1.set_xticks([1, 30, 60, 90, 120])
    ax1.text(60, pmt * 1.04, "payment \\$333.06", ha="center", va="bottom", fontsize=10, color=fs.DARK)
    ax1.text(45, 270, "interest", ha="center", va="center", fontsize=10.5, color="#8a4a00")
    ax1.text(75, 120, "principal", ha="center", va="center", fontsize=10.5, color="#036b45")
    ax1.set_title("\\$30,000 over 10 years", fontsize=11, loc="left", color=fs.DARK)

    pmt2, interest2, principal2 = panel(ax2, 300, None)
    ax2.set_xticks([1, 75, 150, 225, 300])
    ax2.text(150, pmt2 * 1.04, "payment \\$193.29", ha="center", va="bottom", fontsize=10, color=fs.DARK)
    ax2.text(80, 130, "interest", ha="center", va="center", fontsize=10.5, color="#8a4a00")
    ax2.text(200, 55, "principal", ha="center", va="center", fontsize=10.5, color="#036b45")
    ax2.set_title("\\$30,000 over 25 years", fontsize=11, loc="left", color=fs.DARK)

    fig.tight_layout(w_pad=2.5)
    fs.save(fig, FOLDER, f"{SLUG}-interest-principal")


if __name__ == "__main__":
    build()
