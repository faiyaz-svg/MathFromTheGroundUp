"""Figures for docs/03-high-school/09-trigonometry/03-graphs-of-trig-functions.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/graphs-of-trig-functions.py
"""

import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "graphs-of-trig-functions"
PI = math.pi
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def pi_label(k, d):
    """Label for k*pi/d as mathtext."""
    from fractions import Fraction

    fr = Fraction(k, d)
    if fr == 0:
        return "0"
    sign = "-" if fr < 0 else ""
    n, m = abs(fr.numerator), fr.denominator
    num = "\\pi" if n == 1 else f"{n}\\pi"
    if m == 1:
        return f"${sign}{num}$"
    return f"${sign}\\frac{{{num}}}{{{m}}}$"


def axes_through_zero(ax, xlim, ylim, xticks, xlabels, yticks, size=9):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    keep = [i for i, t in enumerate(xticks) if abs(t) > 1e-9]
    ax.set_xticks([xticks[i] for i in keep])
    ax.set_xticklabels([xlabels[i] for i in keep])
    ax.set_yticks([t for t in yticks if t != 0])
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=size, length=3)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)


def sine_cosine():
    fig, ax = fs.figure(7.2, 3.3)
    ks = list(range(-8, 9))
    ticks = [k * PI / 2 for k in ks if k % 1 == 0 and k % 2 == 0] + []
    ticks = [k * PI / 2 for k in range(-4, 5)]
    labels = [pi_label(k, 2) for k in range(-4, 5)]
    axes_through_zero(ax, (-2 * PI - 0.5, 2 * PI + 0.7), (-1.6, 1.6), ticks, labels, [-1, 1])
    xs = np.linspace(-2 * PI, 2 * PI, 600)
    ax.plot(xs, np.sin(xs), color=fs.GREEN, zorder=4)
    ax.plot(xs, np.cos(xs), color=fs.BLUE, zorder=4)
    ax.text(0.85, 0.99, r"$y = \sin x$", color=fs.GREEN, fontsize=11, ha="left", va="bottom", bbox=BOX)
    ax.text(-0.15, 1.12, r"$y = \cos x$", color=fs.BLUE, fontsize=11, ha="right", va="bottom", bbox=BOX)
    for k in range(-4, 5):
        ax.plot([k * PI / 2], [math.sin(k * PI / 2)], "o", color=fs.GREEN, ms=4.5, zorder=5)
        ax.plot([k * PI / 2], [math.cos(k * PI / 2)], "o", color=fs.BLUE, ms=4.5, zorder=5, mfc="white", mew=1.4)
    fs.save(fig, FOLDER, f"{SLUG}-sine-cosine")


def anatomy():
    """y = 3 sin(2(x - pi/4)) + 1: midline, amplitude, period, shift."""
    fig, ax = fs.figure(7.2, 3.8)
    ticks = [k * PI / 4 for k in range(-1, 8)]
    labels = [pi_label(k, 4) for k in range(-1, 8)]
    axes_through_zero(ax, (-PI / 4 - 0.3, 7 * PI / 4 + 0.6), (-2.8, 5.0), ticks, labels, [-2, 2, 4])
    xs = np.linspace(-PI / 4, 7 * PI / 4, 600)
    ys = 3 * np.sin(2 * (xs - PI / 4)) + 1
    ax.plot(xs, ys, color=fs.GREEN, zorder=4)
    ax.axhline(1, color=fs.GRAY, lw=1.2, ls=(0, (5, 3)), zorder=2)
    ax.text(7 * PI / 4 + 0.05, 1.12, "midline $y = 1$", color=fs.GRAY, fontsize=10, ha="right", va="bottom")
    pts = [(PI / 4, 1), (PI / 2, 4), (3 * PI / 4, 1), (PI, -2), (5 * PI / 4, 1)]
    for px, py in pts:
        ax.plot([px], [py], "o", color=fs.DARK, ms=5, zorder=6)
    # amplitude arrow at the first maximum
    ax.annotate("", xy=(PI / 2, 4), xytext=(PI / 2, 1),
                arrowprops=dict(arrowstyle="<->", color=fs.ORANGE, lw=1.3))
    ax.text(PI / 2 + 0.15, 4.35, "amplitude 3", color=fs.ORANGE, fontsize=10, ha="left", va="center")
    # period bracket below
    yb = -2.35
    ax.annotate("", xy=(5 * PI / 4, yb), xytext=(PI / 4, yb), arrowprops=dict(arrowstyle="<->", color=fs.BLUE, lw=1.3))
    ax.text(3 * PI / 4, yb - 0.12, r"period $\pi$", color=fs.BLUE, fontsize=10, ha="center", va="top")
    # shift arrow near the start
    ax.annotate("", xy=(PI / 4, 2.9), xytext=(0, 2.9), arrowprops=dict(arrowstyle="->", color=fs.RED, lw=1.3))
    ax.text(PI / 4, 3.05, r"shift $\frac{\pi}{4}$ right", color=fs.RED, fontsize=10, ha="right", va="bottom")
    ax.text(PI / 4 + 0.08, 0.72, r"$(\frac{\pi}{4}, 1)$", fontsize=9, ha="left", va="top")
    fs.save(fig, FOLDER, f"{SLUG}-anatomy")


def tangent():
    fig, ax = fs.figure(7.2, 3.4)
    ticks = [k * PI / 2 for k in range(-3, 4)]
    labels = [pi_label(k, 2) for k in range(-3, 4)]
    axes_through_zero(ax, (-3 * PI / 2 - 0.3, 3 * PI / 2 + 0.6), (-4.2, 4.2), ticks, labels, [-3, -1, 1, 3])
    for k in (-3, -1, 1, 3):
        ax.axvline(k * PI / 2, color=fs.RED, lw=1.1, ls=(0, (5, 3)), zorder=2)
    for lo in (-3 * PI / 2, -PI / 2, PI / 2):
        xs = np.linspace(lo + 0.03, lo + PI - 0.03, 400)
        ax.plot(xs, np.tan(xs), color=fs.GREEN, zorder=4)
    for k in (-1, 0, 1):
        ax.plot([k * PI], [0], "o", color=fs.DARK, ms=5, zorder=6)
    ax.plot([PI / 4], [1], "o", color=fs.DARK, ms=5, zorder=6)
    ax.plot([-PI / 4], [-1], "o", color=fs.DARK, ms=5, zorder=6)
    ax.text(PI / 4 + 0.1, 0.85, r"$(\frac{\pi}{4}, 1)$", fontsize=9, ha="left", va="top")
    ax.text(0.72, 3.5, r"$y = \tan x$", color=fs.GREEN, fontsize=11, ha="left", va="center", bbox=BOX)
    ax.text(PI / 2 + 0.08, -3.7, "asymptote", color=fs.RED, fontsize=9.5, ha="left", va="center", bbox=BOX)
    fs.save(fig, FOLDER, f"{SLUG}-tangent")


def tangent_example():
    """y = 2 tan(3x) - 1."""
    fig, ax = fs.figure(6.4, 3.6)
    ticks = [k * PI / 6 for k in range(-3, 4)]
    labels = [pi_label(k, 6) for k in range(-3, 4)]
    axes_through_zero(ax, (-PI / 2 - 0.1, PI / 2 + 0.4), (-6.5, 6.5), ticks, labels, [-4, -2, 2, 4])
    for k in (-3, -1, 1, 3):
        ax.axvline(k * PI / 6, color=fs.RED, lw=1.1, ls=(0, (5, 3)), zorder=2)
    for lo in (-PI / 2, -PI / 6, PI / 6):
        xs = np.linspace(lo + 0.015, lo + PI / 3 - 0.015, 400)
        ax.plot(xs, 2 * np.tan(3 * xs) - 1, color=fs.GREEN, zorder=4)
    for px, py in ((0, -1), (PI / 12, 1), (-PI / 12, -3)):
        ax.plot([px], [py], "o", color=fs.DARK, ms=5, zorder=6)
    ax.text(0.07, -1.35, "$(0, -1)$", fontsize=9, ha="left", va="top")
    ax.text(PI / 12 + 0.07, 1.0, r"$(\frac{\pi}{12}, 1)$", fontsize=9, ha="left", va="center", bbox=BOX)
    ax.text(-PI / 12 - 0.07, -3.0, r"$(-\frac{\pi}{12}, -3)$", fontsize=9, ha="right", va="center", bbox=BOX)
    ax.text(PI / 6 + 0.06, 5.6, r"$x = \frac{\pi}{6}$", color=fs.RED, fontsize=9.5, ha="left", va="center", bbox=BOX)
    fs.save(fig, FOLDER, f"{SLUG}-tangent-example")


def daylight():
    fig, ax = fs.figure(7.0, 3.8)
    t = np.linspace(0, 365, 500)
    ax.plot(t, 3.27 * np.cos(2 * np.pi / 365 * (t - 172)) + 12.18, color=fs.GREEN, zorder=3)
    ax.axhline(12.18, color=fs.GRAY, lw=1.1, ls=(0, (5, 3)), zorder=2)
    ax.text(6, 12.35, "midline 12.18 h", color=fs.GRAY, fontsize=9.5, ha="left", va="bottom")
    data = [(172, 15 + 27 / 60, "June 21"), (355, 8 + 55 / 60, "Dec 21"),
            (274, 11 + 48 / 60, "Oct 1"), (304, 10 + 22 / 60, "Oct 31")]
    for d, h, name in data:
        ax.plot([d], [h], "o", color=fs.ORANGE, ms=6, zorder=5)
    ax.text(172, 15.75, "June 21: 15 h 27 min", ha="center", va="bottom", fontsize=9.5, color=fs.ORANGE)
    ax.text(352, 8.6, "Dec 21: 8 h 55 min", ha="right", va="top", fontsize=9.5, color=fs.ORANGE)
    ax.text(280, 12.1, "Oct 1", ha="left", va="bottom", fontsize=9.5, color=fs.ORANGE)
    ax.text(302, 10.55, "Oct 31", ha="left", va="bottom", fontsize=9.5, color=fs.ORANGE)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    starts = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    ax.set_xticks([s + 14 for s in starts])
    ax.set_xticklabels(months, fontsize=9)
    ax.tick_params(length=0)
    ax.set_xlim(0, 366)
    ax.set_ylim(7.5, 16.8)
    ax.set_ylabel("hours of daylight", fontsize=10)
    ax.grid(True, axis="y")
    ax.set_axisbelow(True)
    ax.set_yticks([8, 10, 12, 14, 16])
    fs.save(fig, FOLDER, f"{SLUG}-daylight")


def tide():
    fig, ax = fs.figure(6.6, 3.4)
    t = np.linspace(0, 25, 500)
    ax.plot(t, 2 * np.cos(2 * np.pi / 12.4 * (t - 3)) + 3, color=fs.BLUE, zorder=3)
    ax.axhline(3, color=fs.GRAY, lw=1.1, ls=(0, (5, 3)), zorder=2)
    ax.text(0.4, 2.85, "midline 3 m", color=fs.GRAY, fontsize=9.5, ha="left", va="top")
    for tp, dp in ((3, 5), (15.4, 5), (9.2, 1), (21.6, 1)):
        ax.plot([tp], [dp], "o", color=fs.DARK, ms=5.5, zorder=5)
    ax.text(3.2, 5.12, "high tide, t = 3", fontsize=9.5, ha="left", va="bottom")
    ax.text(9.4, 0.85, "low tide, t = 9.2", fontsize=9.5, ha="left", va="top")
    ax.annotate("", xy=(15.4, 5.65), xytext=(3, 5.65), arrowprops=dict(arrowstyle="<->", color=fs.ORANGE, lw=1.3))
    ax.text(9.2, 5.75, "period 12.4 h", color=fs.ORANGE, fontsize=9.5, ha="center", va="bottom")
    ax.set_xlim(0, 25)
    ax.set_ylim(0, 6.6)
    ax.set_xlabel("hours after midnight, $t$", fontsize=10)
    ax.set_ylabel("water depth (m)", fontsize=10)
    ax.set_xticks(range(0, 25, 4))
    ax.grid(True)
    ax.set_axisbelow(True)
    fs.save(fig, FOLDER, f"{SLUG}-tide")


if __name__ == "__main__":
    sine_cosine()
    anatomy()
    tangent()
    tangent_example()
    daylight()
    tide()
