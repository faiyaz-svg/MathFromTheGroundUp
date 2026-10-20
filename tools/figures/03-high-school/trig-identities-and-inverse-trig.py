"""Figures for docs/03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/trig-identities-and-inverse-trig.py
"""

import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
from matplotlib.patches import Arc, Circle

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "trig-identities-and-inverse-trig"
PI = math.pi
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def pi_label(k, d):
    fr = Fraction(k, d)
    if fr == 0:
        return "0"
    sign = "-" if fr < 0 else ""
    n, m = abs(fr.numerator), fr.denominator
    num = "\\pi" if n == 1 else f"{n}\\pi"
    if m == 1:
        return f"${sign}{num}$"
    return f"${sign}\\frac{{{num}}}{{{m}}}$"


def through_zero(ax, xlim, ylim, size=9):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=size, length=3)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)


def circle_panel(ax, a_deg, b_deg, rotated):
    a, b = math.radians(a_deg), math.radians(b_deg)
    ax.add_patch(Circle((0, 0), 1, fill=False, edgecolor=fs.GRAY, lw=1.3))
    ax.annotate("", xy=(1.35, 0), xytext=(-1.35, 0), arrowprops=dict(arrowstyle="-|>", color=fs.DARK, lw=0.9))
    ax.annotate("", xy=(0, 1.35), xytext=(0, -1.35), arrowprops=dict(arrowstyle="-|>", color=fs.DARK, lw=0.9))
    if not rotated:
        P, Q = np.array([math.cos(a), math.sin(a)]), np.array([math.cos(b), math.sin(b)])
        ang_from, ang_to = b_deg, a_deg
        pl, ql = r"$P = (\cos a, \sin a)$", r"$Q = (\cos b, \sin b)$"
        ax.plot([0, P[0]], [0, P[1]], color=fs.DARK, lw=1.4)
        ax.plot([0, Q[0]], [0, Q[1]], color=fs.DARK, lw=1.4)
        ax.add_patch(Arc((0, 0), 0.7, 0.7, theta1=0, theta2=a_deg, color=fs.BLUE, lw=1.2))
        ax.add_patch(Arc((0, 0), 0.45, 0.45, theta1=0, theta2=b_deg, color=fs.ORANGE, lw=1.2))
        ax.text(-0.05, 0.42, "$a$", color=fs.BLUE, fontsize=11, ha="right", va="center")
        ax.text(0.33, 0.07, "$b$", color=fs.ORANGE, fontsize=11, ha="left", va="center")
        ax.text(P[0] - 0.06, P[1] + 0.08, pl, fontsize=10, ha="right", va="bottom")
        ax.text(Q[0] + 0.06, Q[1] + 0.02, ql, fontsize=10, ha="left", va="bottom")
    else:
        d = a - b
        P, Q = np.array([math.cos(d), math.sin(d)]), np.array([1.0, 0.0])
        ax.plot([0, P[0]], [0, P[1]], color=fs.DARK, lw=1.4)
        ax.plot([0, Q[0]], [0, Q[1]], color=fs.DARK, lw=1.4)
        ax.add_patch(Arc((0, 0), 0.7, 0.7, theta1=0, theta2=a_deg - b_deg, color=fs.GREEN, lw=1.4))
        ax.text(0.15, -0.1, "angle $a - b$", color=fs.GREEN, fontsize=10, ha="left", va="top")
        ax.text(0.2, 1.42, r"$P' = (\cos(a-b), \sin(a-b))$", fontsize=10, ha="center", va="bottom")
        ax.text(1.06, -0.02, "$Q' = (1, 0)$", fontsize=10, ha="left", va="top")
    ax.plot([P[0], Q[0]], [P[1], Q[1]], color=fs.RED, lw=2.4, zorder=4)
    ax.plot(*P, "o", color=fs.DARK, ms=5, zorder=5)
    ax.plot(*Q, "o", color=fs.DARK, ms=5, zorder=5)
    mid = (P + Q) / 2
    ax.text(mid[0] + 0.12, mid[1] + 0.02, "$d$", color=fs.RED, fontsize=12, ha="left", va="center", bbox=BOX)
    ax.set_xlim(-2.0 if not rotated else -2.2, 1.9)
    ax.set_ylim(-1.15, 1.6)
    ax.set_aspect("equal")
    ax.axis("off")


def distance_proof():
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(7.4, 3.6))
    circle_panel(ax1, 110, 30, False)
    circle_panel(ax2, 110, 30, True)
    fig.tight_layout(w_pad=0.2)
    fs.save(fig, FOLDER, f"{SLUG}-distance-proof")


def inverses():
    fig, axes = fs.plt.subplots(1, 3, figsize=(7.4, 3.1))
    # arcsin
    ax = axes[0]
    through_zero(ax, (-1.6, 1.6), (-2.0, 3.6), size=8)
    ax.set_xticks([-1, 1])
    ax.set_yticks([-PI / 2, PI / 2])
    ax.set_yticklabels([pi_label(-1, 2), pi_label(1, 2)])
    xs = np.linspace(-1, 1, 400)
    ax.plot(xs, np.arcsin(xs), color=fs.GREEN, zorder=4)
    for px, py in ((-1, -PI / 2), (1, PI / 2)):
        ax.plot([px], [py], "o", color=fs.DARK, ms=4.5, zorder=5)
    ax.text(-1.5, 3.2, r"$y = \sin^{-1} x$", color=fs.GREEN, fontsize=10, ha="left", va="center")
    ax.text(-1.5, 2.55, "domain $[-1, 1]$", fontsize=8.5, ha="left", va="center")
    # arccos
    ax = axes[1]
    through_zero(ax, (-1.6, 1.6), (-0.6, 3.6), size=8)
    ax.set_xticks([-1, 1])
    ax.set_yticks([PI / 2, PI])
    ax.set_yticklabels([pi_label(1, 2), pi_label(1, 1)])
    ax.plot(xs, np.arccos(xs), color=fs.BLUE, zorder=4)
    for px, py in ((-1, PI), (1, 0)):
        ax.plot([px], [py], "o", color=fs.DARK, ms=4.5, zorder=5)
    ax.text(-1.5, 3.2, r"$y = \cos^{-1} x$", color=fs.BLUE, fontsize=10, ha="left", va="center")
    ax.text(0.15, 3.0, "range $[0, \\pi]$", fontsize=8.5, ha="left", va="center")
    # arctan
    ax = axes[2]
    through_zero(ax, (-5.5, 5.5), (-2.0, 2.0), size=8)
    ax.set_xticks([-4, -2, 2, 4])
    ax.set_yticks([-PI / 2, PI / 2])
    ax.set_yticklabels([pi_label(-1, 2), pi_label(1, 2)])
    xt = np.linspace(-5.3, 5.3, 400)
    ax.plot(xt, np.arctan(xt), color=fs.ORANGE, zorder=4)
    for yy in (-PI / 2, PI / 2):
        ax.axhline(yy, color=fs.RED, lw=1.0, ls=(0, (5, 3)), zorder=2)
    ax.text(-5.3, 1.75, r"$y = \tan^{-1} x$", color=fs.ORANGE, fontsize=10, ha="left", va="center")
    ax.text(5.3, -1.35, "asymptotes", color=fs.RED, fontsize=8.5, ha="right", va="top")
    fig.tight_layout(w_pad=0.8)
    fs.save(fig, FOLDER, f"{SLUG}-inverses")


def equation():
    fig, ax = fs.figure(7.2, 3.0)
    ticks = [k * PI / 6 for k in (0, 1, 5, 12, 13, 17, 24)]
    through_zero(ax, (-0.5, 4 * PI + 0.7), (-1.5, 1.5))
    xs = np.linspace(0, 4 * PI, 800)
    ax.plot(xs, np.sin(xs), color=fs.GREEN, zorder=4)
    ax.axhline(0.5, color=fs.RED, lw=1.2, ls=(0, (5, 3)), zorder=2)
    ax.text(4 * PI + 0.05, 0.62, "$y = \\frac{1}{2}$", color=fs.RED, fontsize=10, ha="right", va="bottom")
    labels = {PI / 6: r"$\frac{\pi}{6}$", 5 * PI / 6: r"$\frac{5\pi}{6}$",
              13 * PI / 6: r"$\frac{13\pi}{6}$", 17 * PI / 6: r"$\frac{17\pi}{6}$"}
    for x, lab in labels.items():
        ax.plot([x], [0.5], "o", color=fs.DARK, ms=5.5, zorder=6)
        ax.plot([x, x], [0, 0.5], color=fs.GRAY, lw=0.9, ls=(0, (2, 2)), zorder=3)
        ax.text(x, -0.1, lab, fontsize=9.5, ha="center", va="top")
    ax.set_xticks([k * PI for k in (1, 2, 3, 4)])
    ax.set_xticklabels([pi_label(k, 1) for k in (1, 2, 3, 4)])
    ax.tick_params(axis="x", pad=18)
    fs.save(fig, FOLDER, f"{SLUG}-equation")


if __name__ == "__main__":
    distance_proof()
    inverses()
    equation()
