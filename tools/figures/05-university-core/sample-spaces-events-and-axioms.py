"""Figures for docs/05-university-core/07-probability/01-sample-spaces-events-and-axioms.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/sample-spaces-events-and-axioms.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, Rectangle  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "sample-spaces-events-and-axioms"


def venn():
    """Two overlapping events with the probability of each of the four regions."""
    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Rectangle((0.2, 0.2), 9.6, 5.5, fill=False, ec=fs.DARK, lw=1.4))
    ca = Circle((3.9, 3.0), 2.0, fc=fs.BLUE, ec=fs.BLUE, alpha=0.22, lw=0)
    cb = Circle((6.1, 3.0), 2.0, fc=fs.ORANGE, ec=fs.ORANGE, alpha=0.22, lw=0)
    ax.add_patch(ca)
    ax.add_patch(cb)
    ax.add_patch(Circle((3.9, 3.0), 2.0, fill=False, ec=fs.BLUE, lw=2))
    ax.add_patch(Circle((6.1, 3.0), 2.0, fill=False, ec=fs.ORANGE, lw=2))
    ax.text(2.55, 3.0, "0.3", ha="center", va="center", fontsize=12)
    ax.text(5.0, 3.0, "0.2", ha="center", va="center", fontsize=12)
    ax.text(7.45, 3.0, "0.2", ha="center", va="center", fontsize=12)
    ax.text(0.7, 0.75, "0.3", ha="left", va="center", fontsize=12)
    ax.text(0.5, 5.25, "Ω", ha="left", va="center", fontsize=12, color=fs.DARK)
    ax.text(3.0, 5.3, "A", ha="center", va="center", fontsize=13, color=fs.BLUE)
    ax.text(7.0, 5.3, "B", ha="center", va="center", fontsize=13, color=fs.ORANGE)
    ax.text(5.0, 0.7, "A ∩ B", ha="center", va="center", fontsize=10, color=fs.DARK)
    ax.plot([5.0, 5.0], [0.95, 2.65], color=fs.DARK, lw=0.8)
    fs.save(fig, FOLDER, f"{SLUG}-venn")


def square():
    """Three events for a random point in the unit square."""
    fig, axes = plt.subplots(1, 3, figsize=(8.6, 3.2))
    x = np.linspace(0, 1, 400)
    panels = [
        ("x + y ≤ 1", "area 1/2", fs.GREEN),
        ("|x − y| < 0.1", "area 0.19", fs.BLUE),
        ("x² + y² ≤ 1", "area π/4 ≈ 0.785", fs.ORANGE),
    ]
    for ax, (title, area, col) in zip(axes, panels):
        ax.set_xlim(-0.08, 1.08)
        ax.set_ylim(-0.08, 1.08)
        ax.set_aspect("equal")
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.tick_params(labelsize=9, length=3)
        ax.add_patch(Rectangle((0, 0), 1, 1, fill=False, ec=fs.DARK, lw=1.4))
        ax.set_xlabel(title, fontsize=10.5, color=col)
        ax.text(0.5, -0.30, area, ha="center", va="top", fontsize=9.5, color=fs.DARK,
                transform=ax.transAxes)
    a, b, c = axes
    a.fill_between(x, 0, 1 - x, color=fs.GREEN, alpha=0.3)
    a.plot(x, 1 - x, color=fs.GREEN, lw=2)
    b.fill_between(x, np.clip(x - 0.1, 0, 1), np.clip(x + 0.1, 0, 1), color=fs.BLUE, alpha=0.3)
    b.plot(x, np.clip(x - 0.1, 0, 1), color=fs.BLUE, lw=1.6)
    b.plot(x, np.clip(x + 0.1, 0, 1), color=fs.BLUE, lw=1.6)
    c.fill_between(x, 0, np.sqrt(1 - x**2), color=fs.ORANGE, alpha=0.3)
    c.plot(x, np.sqrt(1 - x**2), color=fs.ORANGE, lw=2)
    fig.tight_layout(w_pad=1.2)
    fs.save(fig, FOLDER, f"{SLUG}-square")


if __name__ == "__main__":
    venn()
    square()
