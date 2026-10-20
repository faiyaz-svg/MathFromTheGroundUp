"""Figures for docs/03-high-school/06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/polynomial-and-rational-inequalities.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "polynomial-and-rational-inequalities"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def num(v):
    return f"{v:g}".replace("-", M)


def sign_chart():
    """Sign chart of (x - 3)(x + 2) / ((x - 1)(x + 1)) with the solution of >= 0."""
    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    ax.set_xlim(-5.4, 5.2)
    ax.set_ylim(-3.2, 2.0)
    ax.axis("off")
    crit = [-2, -1, 1, 3]
    closed = {-2: True, -1: False, 1: False, 3: True}
    # the number line
    ax.plot([-4.0, 5.0], [0, 0], color=fs.DARK, lw=1.4, zorder=2)
    ax.plot(5.0, 0, ">", color=fs.DARK, ms=5, zorder=2)
    ax.plot(-4.0, 0, "<", color=fs.DARK, ms=5, zorder=2)
    # sign of each factor, one row each
    rows = [
        ("$x - 3$", lambda t: t - 3, 1.45),
        ("$x + 2$", lambda t: t + 2, 1.05),
        ("$x - 1$", lambda t: t - 1, 0.65),
        ("$x + 1$", lambda t: t + 1, 0.25),
    ]
    mids = [-3.1, -1.5, 0.0, 2.0, 4.1]
    for label, fn, y in rows:
        ax.text(-5.35, y, label, ha="left", va="center", fontsize=10)
        for m in mids:
            s = "+" if fn(m) > 0 else M
            ax.text(m, y, s, ha="center", va="center", fontsize=11, color=fs.DARK)
    # the quotient, below the line
    ax.text(-5.35, -0.75, "quotient", ha="left", va="center", fontsize=10)
    for m in mids:
        val = (m - 3) * (m + 2) / ((m - 1) * (m + 1))
        ax.text(m, -0.75, "+" if val > 0 else M, ha="center", va="center", fontsize=12, color=fs.GREEN if val > 0 else fs.RED, fontweight="bold")
    # shade the solution as thick green bars above the axis
    segs = [(-4.0, -2, True), (-1, 1, False), (3, 5.0, True)]
    for a, b, _ in segs:
        ax.plot([a, b], [-1.55, -1.55], color=fs.GREEN, lw=5, solid_capstyle="butt", zorder=3)
    ax.text(-5.35, -1.55, "solution", ha="left", va="center", fontsize=10, alpha=0)
    for c in crit:
        ax.plot([c, c], [-0.15, 0.15], color=fs.DARK, lw=1.2, zorder=3)
        ax.text(c, -0.28, num(c), ha="center", va="top", fontsize=10)
        # dots on the solution bar
        if closed[c]:
            ax.plot(c, -1.55, "o", color=fs.GREEN, ms=8, zorder=5)
        else:
            ax.plot(c, -1.55, "o", mfc="white", mec=fs.GREEN, mew=2, ms=8, zorder=5)
        ax.plot([c, c], [-1.45, 1.7], color=fs.GRAY, lw=0.8, ls=":", zorder=1)
    ax.text(0.5, -2.35, "$x \\leq -2$,   $-1 < x < 1$,   or   $x \\geq 3$", ha="center", va="center", fontsize=11, color=fs.GREEN)
    ax.text(0.5, -2.85, "closed dots: the numerator is 0, so the quotient is 0 and $\\geq$ allows it", ha="center", va="center", fontsize=8.5, color=fs.GRAY)
    fs.save(fig, FOLDER, f"{SLUG}-sign-chart")


def average_cost_target():
    fig, ax = fs.figure(5.8, 3.6)
    qs = np.linspace(250, 5300, 500)
    ax.set_xlim(0, 5300)
    ax.set_ylim(0, 46)
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.axhline(15, color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    ax.axhline(12, color=fs.GRAY, lw=1.0, ls=":", zorder=2)
    ax.plot(qs, 5000 / qs + 12, color=fs.GREEN, zorder=3)
    q0 = 5000 / 3
    ax.axvspan(q0, 5300, color=fs.GREEN, alpha=0.12, lw=0, zorder=1)
    ax.plot(q0, 15, "o", color=fs.DARK, zorder=5, ms=5)
    ax.text(q0 + 90, 17.2, "$q = \\frac{5000}{3} \\approx 1666.7$", ha="left", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(5250, 15.6, "target, \\$15", ha="right", va="bottom", fontsize=9.5, color=fs.GRAY)
    ax.text(5250, 10.4, "marginal cost, \\$12", ha="right", va="top", fontsize=9.5, color=fs.GRAY)
    ax.text(900, 40, "$\\overline{C}(q) = \\dfrac{5000}{q} + 12$", fontsize=11, color=fs.GREEN, ha="left", va="center", bbox=BOX, zorder=6)
    ax.text(4300, 30, "shaded: average cost\nat most \\$15", fontsize=9.5, color=fs.GREEN, ha="center", va="center")
    ax.set_xlabel("quantity $q$ (units)")
    ax.set_ylabel("dollars per unit")
    fs.save(fig, FOLDER, f"{SLUG}-average-cost-target")


if __name__ == "__main__":
    sign_chart()
    average_cost_target()
