"""Figures for docs/03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/exponential-functions-and-growth.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "exponential-functions-and-growth"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def frange(a, b, n=400):
    return [a + (b - a) * i / n for i in range(n + 1)]


def family():
    """Growth and decay curves y = b^x for several b, all through (0, 1)."""
    fig, ax = fs.figure(5.4, 4.0)
    xs = frange(-3, 3)
    ax.plot(xs, [3**t for t in xs], color=fs.RED, zorder=4)
    ax.plot(xs, [2**t for t in xs], color=fs.GREEN, zorder=4)
    ax.plot(xs, [1.5**t for t in xs], color=fs.BLUE, zorder=4)
    ax.plot(xs, [0.5**t for t in xs], color=fs.ORANGE, zorder=4)
    ax.axhline(0, color=fs.GRAY, lw=1.0, ls="--", zorder=2)
    ax.plot([0], [1], "o", color=fs.DARK, ms=6, zorder=6)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-0.8, 8)
    ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.text(1.18, 7.2, "$3^x$", color=fs.RED, fontsize=11, ha="left", va="center", bbox=BOX)
    ax.text(1.95, 5.2, "$2^x$", color=fs.GREEN, fontsize=11, ha="left", va="center", bbox=BOX)
    ax.text(2.55, 2.0, "$1.5^x$", color=fs.BLUE, fontsize=11, ha="left", va="center", bbox=BOX)
    ax.text(-2.8, 5.2, "$(1/2)^x$", color=fs.ORANGE, fontsize=11, ha="left", va="center", bbox=BOX)
    ax.annotate("(0, 1)", xy=(0, 1.1), xytext=(-0.3, 3.4), color=fs.DARK, fontsize=9, ha="center", va="center",
                arrowprops=dict(arrowstyle="-", color=fs.GRAY, lw=1.0))
    ax.text(-2.9, -0.42, "y = 0: the graphs get close to it but never touch it", color=fs.GRAY, fontsize=8.5,
            ha="left", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-family")


def linear_vs_exponential():
    """Savings: 1000 + 100t against 1000 * 1.07^t."""
    fig, ax = fs.figure(5.4, 3.8)
    ts = frange(0, 40)
    ax.plot(ts, [1000 + 100 * t for t in ts], color=fs.BLUE, zorder=4)
    ax.plot(ts, [1000 * 1.07**t for t in ts], color=fs.GREEN, zorder=4)
    ax.plot([11], [1000 * 1.07**11], "o", color=fs.DARK, ms=6, zorder=6)
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 16500)
    ax.set_xticks([0, 10, 20, 30, 40])
    ax.set_yticks([0, 5000, 10000, 15000])
    ax.set_yticklabels(["0", "5,000", "10,000", "15,000"])
    ax.set_xlabel("years t")
    ax.set_ylabel("balance (dollars)")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.text(31.5, 2450, "$1000 + 100t$ (linear)", color=fs.BLUE, fontsize=10, ha="center", va="center", bbox=BOX)
    ax.text(25, 12800, "$1000 \\cdot 1.07^t$ (exponential)", color=fs.GREEN, fontsize=10, ha="center", va="center",
            bbox=BOX)
    ax.annotate("they cross just before t = 11", xy=(11, 2105), xytext=(13, 6500), color=fs.DARK, fontsize=9,
                ha="left", va="bottom", arrowprops=dict(arrowstyle="-", color=fs.GRAY, lw=1.0, relpos=(0.05, 0.0)))
    fs.save(fig, FOLDER, f"{SLUG}-linear-vs-exponential")


def half_life():
    """A 200 mg dose with a half-life of 6 hours."""
    fig, ax = fs.figure(5.4, 3.8)
    ts = frange(0, 24)
    ax.plot(ts, [200 * 0.5 ** (t / 6) for t in ts], color=fs.GREEN, zorder=4)
    for k in range(5):
        t, a = 6 * k, 200 * 0.5**k
        ax.plot([t, t], [0, a], color=fs.GRAY, lw=0.9, ls=":", zorder=2)
        ax.plot([0, t], [a, a], color=fs.GRAY, lw=0.9, ls=":", zorder=2)
        ax.plot([t], [a], "o", color=fs.DARK, ms=6, zorder=6)
        label = f"{a:g} mg"
        ax.text(t + 0.4, a + 6, label, color=fs.DARK, fontsize=9, ha="left", va="bottom")
    ax.set_xlim(0, 25)
    ax.set_ylim(0, 225)
    ax.set_xticks([0, 6, 12, 18, 24])
    ax.set_yticks([0, 50, 100, 150, 200])
    ax.set_xlabel("hours t")
    ax.set_ylabel("drug in the body (mg)")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.text(15.5, 150, "$200 \\cdot (1/2)^{t/6}$", color=fs.GREEN, fontsize=11, ha="left", va="center", bbox=BOX)
    fs.save(fig, FOLDER, f"{SLUG}-half-life")


if __name__ == "__main__":
    family()
    linear_vs_exponential()
    half_life()
