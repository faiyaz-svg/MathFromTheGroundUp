"""Figure for docs/05-university-core/04-integrals/04-integration-by-parts-and-trig-integrals.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/integration-by-parts-and-trig-integrals.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "integration-by-parts-and-trig-integrals"


def quarter():
    """The area under y = sqrt(1 - x^2) on [0, 1] is a quarter of the unit disc; x = sin(theta)."""
    fig, ax = fs.figure(5.0, 4.6)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_xlim(-0.12, 1.3)
    ax.set_ylim(-0.12, 1.2)
    ax.set_xticks([0.5, 1])
    ax.set_yticks([0.5, 1])
    xs = np.linspace(0, 1, 400)
    ax.fill_between(xs, 0, np.sqrt(1 - xs**2), color=fs.GREEN, alpha=0.2, zorder=1)
    ax.plot(xs, np.sqrt(1 - xs**2), color=fs.DARK, lw=2.2, zorder=4)
    theta = math.radians(40)
    px, py = math.sin(theta), math.cos(theta)
    ax.plot([0, px], [0, py], color=fs.BLUE, lw=1.8, zorder=5)
    ax.plot([px, px], [0, py], color=fs.ORANGE, lw=1.8, zorder=5)
    ax.plot([px], [py], "o", color=fs.DARK, ms=6, zorder=6)
    arc = np.linspace(math.pi / 2, math.pi / 2 - theta, 30)
    ax.plot(0.22 * np.cos(arc), 0.22 * np.sin(arc), color=fs.RED, lw=1.5, zorder=5)
    ax.text(0.05, 0.31, "θ", color=fs.RED, fontsize=12, ha="left", va="center")
    ax.text(0.19, 0.34, "radius 1", color=fs.BLUE, fontsize=10, ha="center", va="center", rotation=-0 + 50)
    ax.text(px + 0.03, py / 2 - 0.12, "height\ncos θ", color=fs.ORANGE,
            fontsize=10, ha="left", va="center")
    ax.text(px / 2, -0.07, "x = sin θ", color=fs.DARK, fontsize=10, ha="center", va="top")
    ax.text(0.28, 0.12, "area = π/4", color=fs.GREEN, fontsize=11, ha="center", va="center")
    ax.text(1.0, 1.13, "y = √(1 − x²)", color=fs.DARK, fontsize=10.5, ha="left", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-quarter")


if __name__ == "__main__":
    quarter()
