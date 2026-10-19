"""Figures for docs/02-middle-school/05-linear-relationships-and-functions/01-coordinate-plane.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/02-middle-school/coordinate-plane.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"
SLUG = "coordinate-plane"
M = "−"  # the minus sign, so labels match the tick labels


def num(v):
    """A number for a label, with a real minus sign."""
    text = f"{v:g}"
    return text.replace("-", M)


def pt(x, y):
    return f"({num(x)}, {num(y)})"


def plane(ax, xmin, xmax, ymin, ymax, every=1):
    """Axes through the origin with arrows, a light grid and equal units."""
    ax.set_xlim(xmin - 0.5, xmax + 0.6)
    ax.set_ylim(ymin - 0.5, ymax + 0.6)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks(range(xmin, xmax + 1))
    ax.set_yticks(range(ymin, ymax + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=3)
    ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    # Tick labels as text on a white patch, drawn above the data lines.
    box = dict(facecolor="white", edgecolor="none", pad=0.2)
    for t in range(xmin, xmax + 1):
        if t != 0 and t % every == 0:
            ax.text(t, -0.18, num(t), ha="center", va="top", fontsize=9, zorder=4, bbox=box)
    for t in range(ymin, ymax + 1):
        if t != 0 and t % every == 0:
            ax.text(-0.18, t, num(t), ha="right", va="center", fontsize=9, zorder=4, bbox=box)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)
    ax.text(xmax + 0.6, 0.3, "x", ha="right", va="bottom", style="italic", fontsize=12)
    ax.text(0.3, ymax + 0.6, "y", ha="left", va="top", style="italic", fontsize=12)


def label(ax, x, y, text, dx=0.25, dy=0.25, ha="left", va="bottom", color=fs.DARK, size=10):
    ax.text(
        x + dx, y + dy, text, ha=ha, va=va, color=color, fontsize=size,
        bbox=dict(facecolor="white", edgecolor="none", pad=0.6, alpha=0.9),
    )


def quadrants():
    fig, ax = fs.figure(5.6, 4.8)
    plane(ax, -6, 6, -5, 5)
    style = dict(fontsize=10, color=fs.GRAY)
    ax.text(5.9, 4.9, f"Quadrant I\n(+, +)", ha="right", va="top", **style)
    ax.text(-5.9, 4.9, f"Quadrant II\n({M}, +)", ha="left", va="top", **style)
    ax.text(-5.9, -4.9, f"Quadrant III\n({M}, {M})", ha="left", va="bottom", **style)
    ax.text(5.9, -4.9, f"Quadrant IV\n(+, {M})", ha="right", va="bottom", **style)

    # The route to the cafe: 3 right, then 2 up.
    ax.annotate("", xy=(3, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=fs.GREEN, lw=1.6, shrinkA=0, shrinkB=0))
    ax.annotate("", xy=(3, 2), xytext=(3, 0),
                arrowprops=dict(arrowstyle="->", color=fs.GREEN, lw=1.6, shrinkA=0, shrinkB=3))
    ax.text(1.5, 0.2, "3 right", ha="center", va="bottom", fontsize=9, color=fs.GREEN,
            bbox=dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9))
    ax.text(3.2, 1.0, "2 up", ha="left", va="center", fontsize=9, color=fs.GREEN,
            bbox=dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9))

    points = [
        (3, 2, "café (3, 2)", fs.GREEN, 0.25, 0.2, "left", "bottom"),
        (-3, 3, f"library ({M}3, 3)", fs.BLUE, 0.0, 0.3, "center", "bottom"),
        (-4, -1, f"gym ({M}4, {M}1)", fs.RED, 0.0, -0.35, "center", "top"),
        (2, -3, f"station (2, {M}3)", fs.ORANGE, 0.25, -0.2, "left", "top"),
    ]
    for x, y, text, colour, dx, dy, ha, va in points:
        ax.plot(x, y, "o", color=colour, zorder=5)
        label(ax, x, y, text, dx, dy, ha, va, colour)
    ax.plot(0, 0, "o", color=fs.DARK, ms=4, zorder=5)
    label(ax, 0, 0, "origin (0, 0)", -0.2, 0.25, "right", "bottom", fs.DARK, 9)
    fs.save(fig, FOLDER, f"{SLUG}-quadrants")


def rectangle():
    fig, ax = fs.figure(5.0, 3.9)
    plane(ax, -5, 6, -3, 4)
    xs = [-3, 4, 4, -3, -3]
    ys = [2, 2, -1, -1, 2]
    ax.fill(xs[:4], ys[:4], color=fs.GREEN, alpha=0.12, zorder=1)
    ax.plot(xs, ys, color=fs.GREEN, zorder=3)
    corners = [
        (-3, 2, -0.2, 0.2, "right", "bottom"),
        (4, 2, 0.2, 0.2, "left", "bottom"),
        (4, -1, 0.2, -0.2, "left", "top"),
        (-3, -1, -0.2, -0.2, "right", "top"),
    ]
    for x, y, dx, dy, ha, va in corners:
        ax.plot(x, y, "o", color=fs.GREEN, zorder=5)
        label(ax, x, y, pt(x, y), dx, dy, ha, va)
    ax.text(2.0, 2.25, "7 units", ha="center", va="bottom", fontsize=10, color=fs.BLUE,
            bbox=dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9))
    ax.text(4.25, 1.1, "3 units", ha="left", va="center", fontsize=10, color=fs.BLUE,
            bbox=dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9))
    fs.save(fig, FOLDER, f"{SLUG}-rectangle")


def reflections():
    fig, ax = fs.figure(5.0, 4.2)
    plane(ax, -5, 5, -4, 4)
    dash = dict(color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    ax.plot([3, 3], [2, -2], **dash)
    ax.plot([3, -3], [2, 2], **dash)
    ax.plot([3, -3], [2, -2], color=fs.GRAY, lw=1.2, ls=":", zorder=2)
    pts = [
        (3, 2, "P (3, 2)", fs.GREEN, 0.25, 0.2, "left", "bottom"),
        (3, -2, f"(3, {M}2)\nin the x-axis", fs.BLUE, 0.25, -0.2, "left", "top"),
        (-3, 2, f"({M}3, 2)\nin the y-axis", fs.RED, -0.25, 0.2, "right", "bottom"),
        (-3, -2, f"({M}3, {M}2)\nin both axes", fs.ORANGE, -0.25, -0.2, "right", "top"),
    ]
    for x, y, text, colour, dx, dy, ha, va in pts:
        ax.plot(x, y, "o", color=colour, zorder=5)
        label(ax, x, y, text, dx, dy, ha, va, colour, 9.5)
    fs.save(fig, FOLDER, f"{SLUG}-reflections")


def temperature():
    hours = [0, 3, 6, 9, 12, 15, 18, 21, 24]
    temps = [-6, -7, -8, -4, 2, 5, 3, -3, -5]
    fig, ax = fs.figure(5.6, 3.6)
    ax.set_xlim(0, 24)
    ax.set_ylim(-10, 7)
    ax.set_xticks(range(0, 25, 3))
    ax.set_xticks(range(0, 25, 1), minor=True)
    ax.set_yticks(range(-10, 7, 2))
    ax.set_yticks(range(-10, 8, 1), minor=True)
    ax.set_yticklabels([num(t) for t in range(-10, 7, 2)])
    ax.grid(True, which="major")
    ax.grid(True, which="minor", lw=0.35, color="#e6e8ea")
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.axhline(0, color=fs.DARK, lw=1.0, zorder=2)
    ax.plot(hours, temps, "-o", color=fs.BLUE, zorder=4, ms=5)
    ax.set_xlabel("hours after midnight")
    ax.set_ylabel("temperature (°C)")
    fs.save(fig, FOLDER, f"{SLUG}-temperature")


def phone_plan():
    fig, ax = fs.figure(5.0, 3.6)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 80)
    ax.set_xticks(range(0, 11, 1))
    ax.set_yticks(range(0, 81, 10))
    ax.set_yticks(range(0, 81, 5), minor=True)
    ax.grid(True, which="major")
    ax.grid(True, which="minor", lw=0.35, color="#e6e8ea")
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.plot([0, 4, 10], [30, 30, 75], color=fs.GREEN, zorder=4, clip_on=False)
    ax.set_xlabel("data used in a month (GB)")
    ax.set_ylabel("monthly cost (dollars)")
    fs.save(fig, FOLDER, f"{SLUG}-phone-plan")


if __name__ == "__main__":
    quadrants()
    rectangle()
    reflections()
    temperature()
    phone_plan()
