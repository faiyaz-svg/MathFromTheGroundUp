"""Figures for docs/02-middle-school/07-statistics-and-probability/02-basic-probability.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/02-middle-school/basic-probability.py
"""

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"


def running_proportion():
    """The share of heads after each of 2,000 simulated coin flips."""
    random.seed(19)
    flips = 2000
    heads = 0
    xs, ys = [], []
    for n in range(1, flips + 1):
        heads += random.random() < 0.5
        xs.append(n)
        ys.append(heads / n)
    fig, ax = fs.figure(5.6, 3.3)
    ax.axhline(0.5, color=fs.GRAY, linewidth=1.2, linestyle="--")
    ax.plot(xs, ys, color=fs.GREEN, linewidth=1.6)
    ax.text(1990, 0.46, "theoretical probability 0.5", color=fs.GRAY, ha="right", va="top")
    ax.annotate(f"{ys[-1]:.3f} after 2,000 flips", xy=(xs[-1], ys[-1]), xytext=(700, 0.82),
                color=fs.GREEN, ha="center", va="bottom",
                arrowprops=dict(arrowstyle="->", color=fs.GRAY))
    ax.set_xscale("log")
    ax.set_xlim(1, 2200)
    ax.set_ylim(0, 1)
    ax.set_xticks([1, 10, 100, 1000])
    ax.set_xticklabels(["1", "10", "100", "1,000"])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xlabel("Number of flips (log scale)")
    ax.set_ylabel("Share of flips that were heads")
    return fig, "basic-probability-running-proportion"


FIGURES = [running_proportion]

if __name__ == "__main__":
    for draw in FIGURES:
        fig, name = draw()
        fs.save(fig, FOLDER, name)
