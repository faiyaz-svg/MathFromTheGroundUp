"""Figure for docs/08-financial-math/07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/08-financial-math/income-tax-brackets-marginal-vs-effective.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "08-financial-math"
SLUG = "income-tax-brackets-marginal-vs-effective"

FED = [(58_523, 0.14), (117_045, 0.205), (181_440, 0.26), (258_482, 0.29), (float("inf"), 0.33)]
ONT = [(53_891, 0.0505), (107_785, 0.0915), (150_000, 0.1116), (220_000, 0.1216), (float("inf"), 0.1316)]


def bracket_tax(x, brackets):
    tax, lower = 0.0, 0.0
    for upper, rate in brackets:
        if x > lower:
            tax += (min(x, upper) - lower) * rate
        lower = upper
    return tax


def total_tax(x):
    """Federal plus Ontario tax on taxable income x, with only the basic personal amounts
    as credits (the full federal amount, no phase-down) and the Ontario surtax."""
    fed = max(0.0, bracket_tax(x, FED) - 16_452 * 0.14)
    on = max(0.0, bracket_tax(x, ONT) - 12_989 * 0.0505)
    surtax = 0.20 * max(0.0, on - 5_818) + 0.36 * max(0.0, on - 7_446)
    return fed + on + surtax


def main():
    xs = np.arange(1_000, 300_001, 250.0)
    tax = np.array([total_tax(x) for x in xs])
    tax_up = np.array([total_tax(x + 1) for x in xs])
    marginal = (tax_up - tax) * 100
    average = tax / xs * 100

    fig, ax = fs.figure(6.4, 4.0)
    ax.grid(True, axis="y")
    ax.set_axisbelow(True)
    ax.plot(xs / 1000, marginal, color=fs.ORANGE, lw=1.8, drawstyle="steps-post")
    ax.plot(xs / 1000, average, color=fs.BLUE, lw=2.2)
    ax.set_xlim(0, 300)
    ax.set_ylim(0, 58)
    ax.set_xlabel("taxable income (thousands of dollars)", fontsize=10)
    ax.set_ylabel("rate (%)", fontsize=10)
    ax.tick_params(labelsize=9, length=3)
    ax.text(4, 53, "marginal rate (tax on the next dollar)", color=fs.ORANGE, fontsize=9.5, ha="left", va="center")
    ax.text(298, 24, "average rate (tax / income)", color=fs.BLUE, fontsize=9.5, ha="right", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-rates")


if __name__ == "__main__":
    main()
