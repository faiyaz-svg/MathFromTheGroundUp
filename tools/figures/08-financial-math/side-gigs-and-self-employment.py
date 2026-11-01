"""Figure for docs/08-financial-math/08-starting-your-career/03-side-gigs-and-self-employment.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/08-financial-math/side-gigs-and-self-employment.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "08-financial-math"
SLUG = "side-gigs-and-self-employment"

SALARY = 65_000
PAID_HOURS = 2_080
WORKED_HOURS = 46 * 40          # six weeks a year unpaid
BILLABLE_HOURS = WORKED_HOURS * 0.75
EXPENSES_AND_BENEFITS = 4_800 + 3_000
REQUIRED_REVENUE = 77_817.03    # from the lesson's calculator: net business income 73,017.03 plus 4,800


def main():
    bars = [
        ("job: paid hours", SALARY / PAID_HOURS),
        ("hours worked", SALARY / WORKED_HOURS),
        ("billable hours", SALARY / BILLABLE_HOURS),
        ("plus expenses\nand benefits", (SALARY + EXPENSES_AND_BENEFITS) / BILLABLE_HOURS),
        ("plus CPP\nand tax", REQUIRED_REVENUE / BILLABLE_HOURS),
    ]
    fig, ax = fs.figure(6.4, 4.0)
    ax.grid(True, axis="y")
    ax.set_axisbelow(True)
    colors = [fs.GRAY, fs.BLUE, fs.BLUE, fs.ORANGE, fs.GREEN]
    xs = range(len(bars))
    ax.bar(xs, [b[1] for b in bars], color=colors, width=0.62)
    for x, (_, v) in zip(xs, bars):
        ax.text(x, v + 1.0, "\\${:,.2f}".format(v), ha="center", va="bottom", fontsize=9.5, color=fs.DARK)
    ax.set_xticks(list(xs))
    ax.set_xticklabels([b[0] for b in bars], fontsize=9)
    ax.set_ylim(0, 66)
    ax.set_ylabel("hourly rate (dollars)", fontsize=10)
    ax.tick_params(labelsize=9, length=3)
    fs.save(fig, FOLDER, f"{SLUG}-bridge")


if __name__ == "__main__":
    main()
