"""Figure for docs/07-economics-math/04-more-tools/04-game-theory-and-nash-equilibrium.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/game-theory-and-nash-equilibrium.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"
SLUG = "game-theory-and-nash-equilibrium"


def best_responses():
    """Cournot best-response lines for P = 100 - Q and cost 10 per unit."""
    fig, ax = fs.figure(5.4, 5.0)
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9, length=3)
    q = np.linspace(0, 90, 100)
    br = (90 - q) / 2
    ax.plot(q, br, color=fs.GREEN, lw=2.2)          # firm 2's best response, plotted against q1
    ax.plot(br, q, color=fs.BLUE, lw=2.2)           # firm 1's best response, plotted against q2
    ax.plot([30], [30], "o", color=fs.DARK, zorder=5)
    ax.plot([22.5], [22.5], "o", color=fs.ORANGE, zorder=5)
    ax.plot([33.75], [22.5], "s", color=fs.RED, zorder=5)
    ax.annotate("Nash equilibrium (30, 30)", xy=(30, 30), xytext=(44, 40), color=fs.DARK, fontsize=9.5,
                arrowprops=dict(arrowstyle="-", color=fs.DARK, lw=0.8))
    ax.annotate("shared monopoly (22.5, 22.5)", xy=(22.5, 22.5), xytext=(1, 6), color=fs.ORANGE,
                fontsize=9.5, arrowprops=dict(arrowstyle="-", color=fs.ORANGE, lw=0.8))
    ax.annotate("firm 1 cheats on it", xy=(33.75, 22.5), xytext=(58, 29), color=fs.RED, fontsize=9.5,
                arrowprops=dict(arrowstyle="-", color=fs.RED, lw=0.8))
    ax.text(56, 4, "firm 2's best response", color=fs.GREEN, fontsize=9.5, ha="left", va="bottom")
    ax.text(14, 82, "firm 1's best response", color=fs.BLUE, fontsize=9.5, ha="left", va="bottom")
    ax.set_xlim(0, 90)
    ax.set_ylim(0, 90)
    ax.set_xlabel("firm 1's output $q_1$")
    ax.set_ylabel("firm 2's output $q_2$")
    ax.set_aspect("equal", adjustable="box")
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-cournot")


if __name__ == "__main__":
    best_responses()
