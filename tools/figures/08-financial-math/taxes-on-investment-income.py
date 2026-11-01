"""Figure for docs/08-financial-math/08-starting-your-career/02-taxes-on-investment-income.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/08-financial-math/taxes-on-investment-income.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "08-financial-math"
SLUG = "taxes-on-investment-income"

FED = [(58_523, 0.14), (117_045, 0.205), (181_440, 0.26), (258_482, 0.29), (float("inf"), 0.33)]
ONT = [(53_891, 0.0505), (107_785, 0.0915), (150_000, 0.1116), (220_000, 0.1216), (float("inf"), 0.1316)]


def slices(x, brackets):
    tax, lower = 0.0, 0.0
    for upper, rate in brackets:
        tax += rate * max(0.0, min(x, upper) - lower)
        lower = upper
    return tax


def income_tax(salary, interest=0.0, div=0.0, gain=0.0):
    """Federal plus Ontario income tax for an employee with extra investment income, 2026 rules.

    Leaves out the Ontario Health Premium and smaller credits, as the lesson says.
    """
    pens = max(0.0, min(salary, 74_600) - 3_500)
    cpp_base, cpp_enh = 0.0495 * pens, 0.01 * pens
    cpp2 = 0.04 * max(0.0, min(salary, 85_000) - 74_600)
    ei = 0.0163 * min(salary, 68_900)
    grossed = 1.38 * div
    taxable = salary + interest + grossed + 0.5 * gain - cpp_enh - cpp2
    shrink = (min(max(taxable, 181_440), 258_482) - 181_440) / (258_482 - 181_440)
    bpa = 16_452 - (16_452 - 14_829) * shrink
    fed_basic = max(0.0, slices(taxable, FED) - 0.14 * (bpa + min(1_501, salary) + cpp_base + ei))
    fed = max(0.0, fed_basic - 0.150198 * grossed)
    ont_basic = max(0.0, slices(taxable, ONT) - 0.0505 * (12_989 + cpp_base + ei))
    surtax = 0.20 * max(0.0, ont_basic - 5_818) + 0.36 * max(0.0, ont_basic - 7_446)
    ont = max(0.0, ont_basic + surtax - 0.10 * grossed)
    return fed + ont


def extra(salary, **kw):
    return income_tax(salary, **kw) - income_tax(salary)


def main():
    salaries = np.arange(12_000, 250_001, 500.0)
    interest = np.array([extra(s, interest=1_000) for s in salaries])
    dividend = np.array([extra(s, div=1_000) for s in salaries])
    gain = np.array([extra(s, gain=1_000) for s in salaries])

    fig, ax = fs.figure(6.4, 4.0)
    ax.grid(True, axis="y")
    ax.set_axisbelow(True)
    ax.axhline(0, color=fs.DARK, lw=0.8)
    ax.plot(salaries / 1000, interest, color=fs.ORANGE, lw=2.0)
    ax.plot(salaries / 1000, gain, color=fs.BLUE, lw=2.0)
    ax.plot(salaries / 1000, dividend, color=fs.GREEN, lw=2.0)
    ax.set_xlim(0, 250)
    ax.set_ylim(-160, 600)
    ax.set_xlabel("salary (thousands of dollars)", fontsize=10)
    ax.set_ylabel("tax on an extra \\$1,000 received (dollars)", fontsize=10)
    ax.tick_params(labelsize=9, length=3)
    ax.text(150, 535, "interest", color=fs.ORANGE, fontsize=9.5, ha="center", va="center")
    ax.text(190, 378, "eligible dividends", color=fs.GREEN, fontsize=9.5, ha="center", va="center")
    ax.text(205, 203, "capital gains", color=fs.BLUE, fontsize=9.5, ha="center", va="center")
    ax.text(37, -122, "credits cancel\nother tax", color=fs.GREEN, fontsize=9.0, ha="center", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-by-type")


if __name__ == "__main__":
    main()
