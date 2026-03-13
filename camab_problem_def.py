import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ──────────────────────────────────────────────
# COLOR PALETTE
# ──────────────────────────────────────────────
BG_COLOR   = '#E8ECF1'
NAVY       = '#1B3A5C'
TEAL       = '#2EAB8B'
GOLD       = '#D4A843'
WHITE      = '#FFFFFF'
GRAY       = '#8899AA'
LIGHT_BLUE = '#D6E1EE' # Subtle gradient fill color from your spec

# ──────────────────────────────────────────────
# FIGURE SETUP
# ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

def draw_box(x, y, text, color, text_color=WHITE, width=0.85, height=0.1,
             pad=0.02, fontsize=12, fontweight='normal', edgecolor=None, lw=1.5):
    if edgecolor is None:
        edgecolor = color
    box = patches.FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle=f"round,pad={pad},rounding_size=0.03",
        linewidth=lw, edgecolor=edgecolor, facecolor=color, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', color=text_color,
            fontsize=fontsize, fontweight=fontweight, zorder=4)
    return x, y - height/2 - pad, y + height/2 + pad

# ──────────────────────────────────────────────
# 1. QUESTION NODE
# ──────────────────────────────────────────────
q_text = "Question (Q):\nWhich magazine was started first\nArthur's Magazine or First for Women?"
_, q_bot, _ = draw_box(0.5, 0.91, q_text, NAVY, width=0.82, height=0.10,
                        pad=0.012, fontsize=12, fontweight='bold')

# ──────────────────────────────────────────────
# 2. CONTEXT BLOCK
# ──────────────────────────────────────────────
ctx_box = patches.FancyBboxPatch(
    (0.06, 0.27), 0.88, 0.50,
    boxstyle="round,pad=0.02,rounding_size=0.04",
    linewidth=2, edgecolor=GRAY, facecolor='none', linestyle='--', zorder=1)
ax.add_patch(ctx_box)
ax.text(0.11, 0.79, "Context (C)", ha='left', va='center',
        color=NAVY, fontsize=11, fontweight='bold')

seg_pad = 0.006
seg_h = 0.050
seg_w = 0.76

s1_text = "$s_1$: Arthur's Magazine (1844–1846) was an\nAmerican literary periodical..."
draw_box(0.5, 0.70, s1_text, LIGHT_BLUE, text_color=NAVY,
         width=seg_w, height=seg_h, pad=seg_pad, edgecolor=GOLD, lw=2, fontsize=10)

s2_text = "$s_2$: Edited by T.S. Arthur, it featured work\nby Edgar A. Poe, J.H. Ingraham..."
draw_box(0.5, 0.60, s2_text, LIGHT_BLUE, text_color=NAVY,
         width=seg_w, height=seg_h, pad=seg_pad, edgecolor=GRAY, lw=1, fontsize=10)

s3_text = "$s_3$: First for Women is a woman's magazine\npublished by Bauer Media Group..."
draw_box(0.5, 0.50, s3_text, LIGHT_BLUE, text_color=NAVY,
         width=seg_w, height=seg_h, pad=seg_pad, edgecolor=GRAY, lw=1, fontsize=10)

s4_text = "$s_4$: The magazine was started in 1989."
draw_box(0.5, 0.40, s4_text, LIGHT_BLUE, text_color=NAVY,
         width=seg_w, height=seg_h, pad=seg_pad, edgecolor=GOLD, lw=2, fontsize=10)

# ──────────────────────────────────────────────
# 3. RESPONSE NODE
# ──────────────────────────────────────────────
r_text = "LLM Response (R):\nArthur's Magazine was started first."
_, _, r_top = draw_box(0.5, 0.10, r_text, TEAL, width=0.82, height=0.08,
                        pad=0.012, fontsize=12, fontweight='bold')

# ──────────────────────────────────────────────
# ARROWS & ANNOTATIONS
# ──────────────────────────────────────────────
ax.annotate("", xy=(0.5, 0.79), xytext=(0.5, q_bot),
            arrowprops=dict(arrowstyle="-|>", mutation_scale=18, color=NAVY, lw=2))
ax.annotate("", xy=(0.5, r_top), xytext=(0.5, 0.27),
            arrowprops=dict(arrowstyle="-|>", mutation_scale=18, color=NAVY, lw=2))

ax.annotate("", xy=(0.88, 0.53), xytext=(0.92, 0.10),
            arrowprops=dict(arrowstyle="-|>", mutation_scale=18, color=GOLD, lw=3, ls='--',
                            connectionstyle="arc3,rad=0.3", zorder=5))

ax.text(0.93, 0.20, "Attribution:\nWhich $s_i$ caused\nthis answer?",
        ha='right', va='center', color=GOLD, fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=WHITE, edgecolor=GOLD, lw=2, alpha=0.9))

plt.tight_layout()
plt.savefig('saved/camab_hotpotqa_problem.svg', format='svg', bbox_inches='tight', facecolor=BG_COLOR)
plt.savefig('saved/camab_hotpotqa_problem.png', dpi=300, bbox_inches='tight', facecolor=BG_COLOR)
print("Plot saved successfully.")