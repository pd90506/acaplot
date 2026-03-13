import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ──────────────────────────────────────────────
# COLOR PALETTE
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
fig, ax = plt.subplots(figsize=(11, 4))
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

def draw_chevron(x, y, width, height, color, title, subtitle, list_items, is_first=False):
    arrow_depth = 0.04
    if is_first:
        verts = [
            (x, y - height/2),
            (x + width - arrow_depth, y - height/2),
            (x + width, y),
            (x + width - arrow_depth, y + height/2),
            (x, y + height/2),
            (x, y),
        ]
    else:
        verts = [
            (x, y - height/2),
            (x + width - arrow_depth, y - height/2),
            (x + width, y),
            (x + width - arrow_depth, y + height/2),
            (x, y + height/2),
            (x + arrow_depth, y),
        ]

    poly = patches.Polygon(verts, closed=True, facecolor=color, edgecolor=WHITE, lw=2, zorder=3)
    ax.add_patch(poly)

    # Center text in the flat region of the chevron
    if is_first:
        text_x = x + (width - arrow_depth) / 2
    else:
        text_x = x + arrow_depth + (width - 2 * arrow_depth) / 2

    ax.text(text_x, y + 0.15, title, ha='center', va='center',
            color=WHITE, fontsize=16, fontweight='bold', zorder=4)
    ax.text(text_x, y + 0.05, subtitle, ha='center', va='center',
            color=WHITE, fontsize=11, style='italic', zorder=4)

    bullet_y = y - 0.05
    for item in list_items:
        ax.text(text_x, bullet_y, f"• {item}", ha='center', va='center',
                color=WHITE, fontsize=11, fontweight='bold', zorder=4)
        bullet_y -= 0.09

# ──────────────────────────────────────────────
# DRAW PIPELINE
# ──────────────────────────────────────────────
y_pos = 0.55
box_w = 0.30
box_h = 0.60

draw_chevron(0.03, y_pos, box_w, box_h, NAVY,
             "1. Interpret", "What is the AI doing?",
             ["FEX: Amortized probing", "CAMAB: Bandit attribution"],
             is_first=True)

draw_chevron(0.35, y_pos, box_w, box_h, TEAL,
             "2. Audit", "When does it fail?",
             ["Detect LLM hallucination", "Identify data imbalances"])

draw_chevron(0.67, y_pos, box_w, box_h, GOLD,
             "3. Align", "How do we fix it?",
             ["Design corrective loops", "Steer human values", "NSF Initiative focus"])

# ──────────────────────────────────────────────
# THE FEEDBACK LOOP
# ──────────────────────────────────────────────
ax.annotate("",
            xy=(0.13, y_pos - box_h/2 - 0.03),
            xytext=(0.82, y_pos - box_h/2 - 0.03),
            arrowprops=dict(arrowstyle="-|>", mutation_scale=20, color=NAVY, lw=2.5, ls='--',
                            connectionstyle="arc3,rad=-0.2", zorder=2))

ax.text(0.475, 0.12, "Continuous Alignment & Refinement", ha='center', va='center',
        color=NAVY, fontsize=12, fontweight='bold', style='italic')

plt.tight_layout()
plt.savefig('saved/auditing_alignment_pipeline.svg', format='svg', bbox_inches='tight', facecolor=BG_COLOR)
plt.savefig('saved/auditing_alignment_pipeline.png', dpi=300, bbox_inches='tight', facecolor=BG_COLOR)
print("Plot saved successfully.")