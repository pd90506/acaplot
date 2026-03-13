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
LIGHT_BLUE = '#D6E1EE'

# ──────────────────────────────────────────────
# FIGURE SETUP
# ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8.5, 6))
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

def draw_box(x, y, text, color, text_color=WHITE, width=0.18, height=0.1, pad=0.03, fontsize=12, fontweight='bold', edgecolor=None, lw=1.5, ls='solid'):
    if edgecolor is None:
        edgecolor = color
    box = patches.FancyBboxPatch((x - width/2, y - height/2), width, height, 
                                 boxstyle=f"round,pad={pad},rounding_size=0.04", 
                                 linewidth=lw, edgecolor=edgecolor, facecolor=color, linestyle=ls, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', color=text_color, 
            fontsize=fontsize, fontweight=fontweight, zorder=4)
    return x - width/2 - pad, x + width/2 + pad, y - height/2 - pad, y + height/2 + pad

# ──────────────────────────────────────────────
# 1. CONTEXT & BELIEF POOL (Top Left)
# ──────────────────────────────────────────────
# Outer Container
ctx_x, ctx_y = 0.28, 0.72
ctx_w, ctx_h = 0.36, 0.44
ctx_left, ctx_right, ctx_bot, ctx_top = draw_box(ctx_x, ctx_y, "", 'none', width=ctx_w, height=ctx_h, 
                                                 edgecolor=GRAY, lw=2, pad=0.0)
# Container Label
ax.text(ctx_x, ctx_top - 0.04, "Context & Relevance Scores", ha='center', va='center', 
        color=NAVY, fontsize=12, fontweight='bold')

# Helper to draw s_i and r_i pairs
def draw_pair(y_pos, s_label, r_label):
    s_x, r_x = ctx_x - 0.06, ctx_x + 0.10
    # Dotted line connecting them
    ax.plot([s_x, r_x], [y_pos, y_pos], color=NAVY, ls=':', lw=2, zorder=2)
    # Sentence Box
    draw_box(s_x, y_pos, s_label, LIGHT_BLUE, text_color=NAVY, width=0.14, height=0.05, pad=0.01, lw=1.2, edgecolor=NAVY)
    # Reward/Belief Box
    draw_box(r_x, y_pos, r_label, WHITE, text_color=NAVY, width=0.06, height=0.05, pad=0.01, lw=1.2, edgecolor=NAVY)

draw_pair(0.82, "$s_1$", "$r_1$")
draw_pair(0.72, "$s_2$", "$r_2$")
ax.text(ctx_x, 0.63, "...", ha='center', va='center', color=NAVY, fontsize=16, fontweight='bold')
draw_pair(0.55, "$s_n$", "$r_n$")

# ──────────────────────────────────────────────
# 2. SELECTED SUBSET (Top Right)
# ──────────────────────────────────────────────
sub_x, sub_y = 0.80, 0.72
sub_left, sub_right, sub_bot, sub_top = draw_box(sub_x, sub_y, "Selected Subset\n$\{s_i, s_j, s_k, \dots\}$", 
                                                 WHITE, text_color=NAVY, width=0.28, height=0.12, pad=0.02, edgecolor=GOLD, lw=2.5)

# ──────────────────────────────────────────────
# 3. LLM API (Bottom Right)
# ──────────────────────────────────────────────
llm_x, llm_y = 0.80, 0.28
llm_left, llm_right, llm_bot, llm_top = draw_box(llm_x, llm_y, "Black-Box LLM API", NAVY, width=0.28, height=0.12, pad=0.02, fontsize=14)

# ──────────────────────────────────────────────
# 4. REWARD CALCULATION (Bottom Left)
# ──────────────────────────────────────────────
rew_x, rew_y = 0.28, 0.28
rew_left, rew_right, rew_bot, rew_top = draw_box(rew_x, rew_y, "Reward $V(S_t)$", TEAL, width=0.32, height=0.12, pad=0.02, fontsize=14)

# ──────────────────────────────────────────────
# ARROWS & FLOW
# ──────────────────────────────────────────────
arrow_style = dict(arrowstyle="-|>", mutation_scale=22, color=NAVY, lw=2.5, zorder=2)

# Context -> Subset (Right)
ax.annotate("", xy=(sub_left, ctx_y), xytext=(ctx_right, ctx_y), arrowprops={**arrow_style, 'color': GOLD})
ax.text((ctx_right + sub_left)/2, ctx_y + 0.03, "MAB Pull", ha='center', va='bottom', color=GOLD, fontsize=13, fontweight='bold')

# Subset -> LLM (Down)
ax.annotate("", xy=(sub_x, llm_top), xytext=(sub_x, sub_bot), arrowprops=arrow_style)
ax.text(sub_x + 0.02, (sub_bot + llm_top)/2, "Query", ha='left', va='center', color=NAVY, fontsize=12, fontweight='bold')

# LLM -> Reward (Left)
ax.annotate("", xy=(rew_right, llm_y), xytext=(llm_left, llm_y), arrowprops=arrow_style)
ax.text((llm_left + rew_right)/2, llm_y + 0.03, "Response", ha='center', va='bottom', color=NAVY, fontsize=12, fontweight='bold')

# Reward -> Context (Up)
ax.annotate("", xy=(ctx_x, ctx_bot), xytext=(ctx_x, rew_top), arrowprops=arrow_style)
ax.text(ctx_x + 0.02, (rew_top + ctx_bot)/2, "Update $r_i$", ha='left', va='center', color=NAVY, fontsize=13, fontweight='bold')

# ──────────────────────────────────────────────
# LEGEND
# ──────────────────────────────────────────────
ax.text(0.5, 0.05, "$s_i$: Context segment $i$    |    $r_i$: Relevance belief for segment $i$", 
        ha='center', va='center', color=GRAY, fontsize=12, fontweight='bold', style='italic')

plt.tight_layout()
plt.savefig('saved/camab_mab_optimization.svg', format='svg', bbox_inches='tight', facecolor=BG_COLOR)
plt.savefig('saved/camab_mab_optimization.png', dpi=300, bbox_inches='tight', facecolor=BG_COLOR)
print("Plot saved successfully.")