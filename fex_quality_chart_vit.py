import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# ──────────────────────────────────────────────
# COLOR PALETTE (Matched to Left Panel)
# ──────────────────────────────────────────────
BG_COLOR = '#E8ECF1'
NAVY     = '#1B3A5C'
TEAL     = '#2EAB8B'
GOLD     = '#D4A843'
WHITE    = '#FFFFFF'
GRAY     = '#8899AA'
LIGHT_GOLD = '#F0DCA0'

# ──────────────────────────────────────────────
# DATA (Extracted from Table 2 - ImageNet)
# Insertion = Negative AUC (Higher is better)
# Deletion = Positive AUC * -1 (Higher/closer to 0 is better)
# ──────────────────────────────────────────────
methods = ['FEX (Ours)', 'FastSHAP', 'RISE', 'IG']

# ImageNet values from table
insertion_scores = np.array([0.7296, 0.7084, 0.7229, 0.7216])
deletion_scores  = np.array([-0.3221, -0.4591, -0.5040, -0.4276])

# Colors: FEX highlighted in Gold/Light Gold, Baselines in Navy/Gray
ins_colors = [GOLD, NAVY, NAVY, NAVY]
del_colors = [LIGHT_GOLD, GRAY, GRAY, GRAY]

# ──────────────────────────────────────────────
# FIGURE SETUP
# ──────────────────────────────────────────────
fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))
fig.patch.set_facecolor(BG_COLOR)
ax1.set_facecolor(BG_COLOR)

x = np.arange(len(methods))
bar_width = 0.35

# Set baseline bottoms so bars grow upwards visually
bottom_ins = 0.68
bottom_del = -0.55

# ──────────────────────────────────────────────
# LEFT AXIS: INSERTION SCORE
# ──────────────────────────────────────────────
# Calculate heights relative to the customized bottom
ins_heights = insertion_scores - bottom_ins

bars_ins = ax1.bar(x - bar_width/2, ins_heights, bar_width, bottom=bottom_ins,
                   color=ins_colors, edgecolor=WHITE, linewidth=1.5,
                   zorder=3, label='Insertion Score')

# Value labels on insertion bars
for bar, val in zip(bars_ins, insertion_scores):
    ax1.text(bar.get_x() + bar.get_width()/2, val + 0.002,
             f'{val:.4f}', ha='center', va='bottom', fontsize=11,
             fontweight='bold', color=TEAL)

ax1.set_ylabel('Insertion Score', fontsize=12, color=TEAL, fontweight='bold')
ax1.set_ylim(bottom_ins, 0.745)
ax1.tick_params(axis='y', labelcolor=TEAL, labelsize=10)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color(TEAL)
ax1.spines['left'].set_linewidth(1.5)
ax1.spines['bottom'].set_color(NAVY)
ax1.spines['bottom'].set_linewidth(1.5)

# ──────────────────────────────────────────────
# RIGHT AXIS: DELETION SCORE (NEGATIVE)
# ──────────────────────────────────────────────
ax2 = ax1.twinx()

# Calculate heights relative to the customized bottom
del_heights = deletion_scores - bottom_del

bars_del = ax2.bar(x + bar_width/2, del_heights, bar_width, bottom=bottom_del,
                   color=del_colors, edgecolor=WHITE, linewidth=1.5,
                   zorder=3, label='Negative Deletion Score')

# Value labels on deletion bars
for bar, val in zip(bars_del, deletion_scores):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 0.005,
             f'{val:.4f}', ha='center', va='bottom', fontsize=11,
             fontweight='bold', color=NAVY)

ax2.set_ylabel('Negative Deletion Score', fontsize=12, color=NAVY, fontweight='bold')
ax2.set_ylim(bottom_del, -0.25)
ax2.tick_params(axis='y', labelcolor=NAVY, labelsize=10)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_color(NAVY)
ax2.spines['right'].set_linewidth(1.5)

# ──────────────────────────────────────────────
# FORMATTING & LEGEND
# ──────────────────────────────────────────────
ax1.set_xticks(x)
ax1.set_xticklabels(methods, fontsize=12, fontweight='bold', color=NAVY)

ax1.set_title('Explanation Quality: ImageNet',
              fontsize=14, fontweight='bold', color=NAVY, pad=15)

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=NAVY, edgecolor=WHITE, label='Insertion Score (Left Y)'),
    Patch(facecolor=GRAY, edgecolor=WHITE, label='Neg. Deletion Score (Right Y)')
]

ax1.legend(handles=legend_elements, loc='upper right', fontsize=10,
           framealpha=0.9, edgecolor=NAVY)

plt.tight_layout()
plt.savefig('saved/fex_quality_ins_del.svg', format='svg', bbox_inches='tight', facecolor=BG_COLOR)
plt.savefig('saved/fex_quality_ins_del.png', dpi=300, bbox_inches='tight', facecolor=BG_COLOR)
print("Plot saved successfully.")