"""Figures for docs/08-financial-math/05-housing/03-mortgage-amortization-schedules.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/08-financial-math/mortgage-amortization-schedules.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "08-financial-math"

LOAN = 560_000
QUOTED = 0.05  # made-up example rate, compounded semi-annually
YEARS = 25


def monthly_rate(quoted):
    return (1 + quoted / 2) ** (1 / 6) - 1


def payment(loan, quoted, years):
    i = monthly_rate(quoted)
    n = 12 * years
    return loan * i / (1 - (1 + i) ** -n)


def schedule(loan, quoted, years):
    i = monthly_rate(quoted)
    pay = payment(loan, quoted, years)
    balance = loan
    rows = []
    for _ in range(12 * years):
        interest = balance * i
        principal = pay - interest
        balance -= principal
        rows.append((interest, principal, balance))
    return rows


def balance_curve():
    rows = schedule(LOAN, QUOTED, YEARS)
    months = [0] + list(range(1, len(rows) + 1))
    bal = [LOAN] + [r[2] / 1000 * 1000 for r in rows]
    fig, ax = fs.figure(5.6, 3.8)
    ax.grid(True, axis="y", zorder=0)
    ax.axvspan(0, 5, color=fs.LIGHT, zorder=1)
    ax.plot([m / 12 for m in months], [b / 1000 for b in bal], color=fs.GREEN, zorder=3)
    b60 = rows[59][2] / 1000
    ax.plot([5], [b60], marker="o", color=fs.DARK, zorder=4)
    ax.annotate("after 5 years: about \\$495,600 still owed", xy=(5, b60), xytext=(7.5, 520),
                color=fs.DARK, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=fs.GRAY))
    ax.text(2.5, 30, "first term", color=fs.DARK, ha="center", va="bottom")
    ax.text(25, 20, "paid off at 25 years", color=fs.DARK, ha="right", va="bottom")
    ax.set_xlim(0, 25)
    ax.set_ylim(0, 600)
    ax.set_xticks(range(0, 26, 5))
    ax.set_xlabel("Years since the mortgage started")
    ax.set_ylabel("Balance owed (thousands of dollars)")
    return fig, "mortgage-amortization-schedules-balance"


def interest_vs_principal():
    rows = schedule(LOAN, QUOTED, YEARS)
    years = range(1, YEARS + 1)
    interest = [sum(r[0] for r in rows[12 * (y - 1):12 * y]) / 1000 for y in years]
    principal = [sum(r[1] for r in rows[12 * (y - 1):12 * y]) / 1000 for y in years]
    fig, ax = fs.figure(5.6, 3.8)
    ax.grid(True, axis="y", zorder=0)
    ax.bar(list(years), principal, color=fs.GREEN, zorder=3, width=0.75)
    ax.bar(list(years), interest, bottom=principal, color=fs.ORANGE, zorder=3, width=0.75)
    ax.text(14, 46, "principal (green)", color="#027a4e", ha="left", va="center")
    ax.text(1, 46, "interest (orange)", color="#a85c00", ha="left", va="center")
    ax.set_xlim(0.3, 25.7)
    ax.set_ylim(0, 50)
    ax.set_xticks([1, 5, 10, 15, 20, 25])
    ax.set_xlabel("Year of the mortgage")
    ax.set_ylabel("Paid in the year (thousands of dollars)")
    return fig, "mortgage-amortization-schedules-split"


if __name__ == "__main__":
    for make in (balance_curve, interest_vs_principal):
        fig, name = make()
        fs.save(fig, FOLDER, name)
