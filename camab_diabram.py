import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path as MPath

# ──────────────────────────────────────────────
# COLOR PALETTE (Matched to your slides)
# ──────────────────────────────────────────────
BG_COLOR = '#E8ECF1'
NAVY     = '#1B3A5C'
TEAL     = '#2EAB8B'
GOLD     = '#D4A843'
WHITE    = '#FFFFFF'
GRAY     = '#8899AA'

# ──────────────────────────────────────────────
# FIGURE SETUP
# ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

def draw_box(x, y, text, color, text_color=WHITE, width=0.18, height=0.1,
             fontsize=12, fontweight='bold', alpha=1.0, edgecolor=None, pad=0.05):
    if edgecolor is None:
        edgecolor = color
    box = patches.FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle=f"round,pad={pad},rounding_size=0.03",
        linewidth=1.5, edgecolor=edgecolor, facecolor=color, alpha=alpha, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', color=text_color,
            fontsize=fontsize, fontweight=fontweight, zorder=4)
    return x, y - height/2, x, y + height/2

# ──────────────────────────────────────────────
# DRAW NODES
# ──────────────────────────────────────────────
# 1. Question Node
q_x, q_y_bot, _, q_y_top = draw_box(0.18, 0.85, "Question (Q)", NAVY, width=0.22)

# 2. Context Segments (The "Arms") — spaced to avoid overlap
ctx_box = patches.FancyBboxPatch(
    (0.42, 0.76), 0.53, 0.18,
    boxstyle="round,pad=0.02,rounding_size=0.05",
    linewidth=1.5, edgecolor=GRAY, facecolor='none', linestyle='--', zorder=1)
ax.add_patch(ctx_box)
ax.text(0.685, 0.98, "Context Segments (Bandit Arms)",
        ha='center', va='center', color=NAVY, fontsize=11, fontweight='bold')

seg_y = 0.85
seg_w, seg_h, seg_pad = 0.08, 0.08, 0.012
draw_box(0.50, seg_y, "$s_1$", GRAY, width=seg_w, height=seg_h, alpha=0.5, pad=seg_pad)
c_x, c_y_bot, _, _ = draw_box(0.61, seg_y, "$s_2$", GOLD, width=seg_w, height=seg_h,
                                text_color=NAVY, pad=seg_pad)
draw_box(0.72, seg_y, "$s_3$", GRAY, width=seg_w, height=seg_h, alpha=0.5, pad=seg_pad)
ax.text(0.81, seg_y, "···", ha='center', va='center', color=NAVY, fontsize=16, fontweight='bold')
draw_box(0.89, seg_y, "$s_n$", GRAY, width=seg_w, height=seg_h, alpha=0.5, pad=seg_pad)

# 3. Black-Box LLM API
llm_x, llm_y_bot, _, llm_y_top = draw_box(0.5, 0.52, "Black-Box LLM API", NAVY,
                                            width=0.55, height=0.12, fontsize=14)

# 4. Response Node
r_x, r_y_bot, _, r_y_top = draw_box(0.5, 0.22, "Response (R)", TEAL, width=0.3)

# ──────────────────────────────────────────────
# DRAW ARROWS
# ──────────────────────────────────────────────
arrow_kwargs = dict(arrowstyle="-|>", mutation_scale=20, color=NAVY, lw=2, zorder=2)

# Q -> LLM
ax.annotate("", xy=(0.32, llm_y_top + 0.05), xytext=(q_x, q_y_bot - 0.02),
            arrowprops=dict(**arrow_kwargs, connectionstyle="arc3,rad=0.1"))

# Context -> LLM
ax.annotate("", xy=(0.65, llm_y_top + 0.05), xytext=(0.685, 0.74),
            arrowprops=dict(**arrow_kwargs, connectionstyle="arc3,rad=-0.1"))

# LLM -> Response
ax.annotate("", xy=(r_x, r_y_top + 0.02), xytext=(llm_x, llm_y_bot - 0.02),
            arrowprops=arrow_kwargs)

# ──────────────────────────────────────────────
# ATTRIBUTION ARROW (routes LEFT of the LLM box)
# ──────────────────────────────────────────────
arrow_verts = [
    (r_x - 0.16, 0.22),   # start: left edge of Response
    (0.07, 0.22),          # swing far left
    (0.07, 0.85),          # rise above LLM box on the left
    (c_x, c_y_bot - 0.03), # arrive at s2
]
arrow_codes = [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4]
arrow_path = MPath(arrow_verts, arrow_codes)

gold_arrow = patches.FancyArrowPatch(
    path=arrow_path, arrowstyle="-|>", mutation_scale=20,
    color=GOLD, lw=2.5, linestyle='--', zorder=5)
ax.add_patch(gold_arrow)

# Label for the Gold Arrow
ax.text(0.08, 0.52, "Attribution:\nWhich arms\nmaximized reward?",
        ha='center', va='center', color=GOLD, fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_COLOR, edgecolor=GOLD, lw=1.5))

plt.tight_layout()
plt.savefig('saved/camab_problem_diagram.svg', format='svg', bbox_inches='tight', facecolor=BG_COLOR)
plt.savefig('saved/camab_problem_diagram.png', dpi=300, bbox_inches='tight', facecolor=BG_COLOR)
print("Plot saved successfully.")