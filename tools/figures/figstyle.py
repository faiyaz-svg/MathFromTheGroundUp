"""Shared look for the SVG figures in docs/assets/figures/.

Each lesson that needs figures has its own script, tools/figures/<folder>/<lesson-slug>.py.
The script imports this module, draws with matplotlib and calls save() once per figure.
Run a script from the repo root:

    .venv/Scripts/python tools/figures/02-middle-school/slope-and-linear-equations.py

Lessons embed a figure with a relative image link and real alt text:

    ![The line y = 2x + 1 rising through (0, 1)](../../assets/figures/02-middle-school/slope-and-linear-equations-rise-run.svg)
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("svg")

import matplotlib.pyplot as plt  # noqa: E402
from cycler import cycler  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "docs" / "assets" / "figures"

# The site palette (DESIGN.md). No purple, no gradients.
GREEN = "#04aa6d"
DARK = "#282a35"
RED = "#d9212c"
ORANGE = "#d97a00"
BLUE = "#1f6fb2"
GRAY = "#8a8f98"
LIGHT = "#ebedee"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "mathtext.fontset": "dejavusans",
        "font.size": 11,
        "text.color": DARK,
        "axes.edgecolor": DARK,
        "axes.labelcolor": DARK,
        "axes.linewidth": 1.0,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.prop_cycle": cycler(color=[GREEN, BLUE, RED, ORANGE, DARK]),
        "xtick.color": DARK,
        "ytick.color": DARK,
        "grid.color": "#d5d8db",
        "grid.linewidth": 0.6,
        "lines.linewidth": 2.0,
        "lines.markersize": 6,
        "legend.frameon": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.08,
        # Text is drawn as paths, so the figure looks the same in every browser.
        "svg.fonttype": "path",
        # Fixed ids, so a re-run doesn't change the file unless the drawing changed.
        "svg.hashsalt": "math-from-the-ground-up",
    }
)


def figure(width: float = 5.0, height: float = 3.6):
    """A new figure and axes. Sizes are in inches; 5 by 3.6 suits most plots."""
    return plt.subplots(figsize=(width, height))


def save(fig, folder: str, name: str) -> Path:
    """Write docs/assets/figures/<folder>/<name>.svg and close the figure."""
    path = OUT / folder / f"{name}.svg"
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, format="svg", metadata={"Date": None, "Creator": None})
    plt.close(fig)
    print("wrote", path.relative_to(ROOT).as_posix())
    return path
