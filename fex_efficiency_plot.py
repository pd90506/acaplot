"""
FEX Inference Cost Bar Chart
FEX highlighted in gold, baselines in navy/gray
With 40x faster callout
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as pe

# ──────────────────────────────────────────────
# COLOR PALETTE
# ──────────────────────────────────────────────
BG_COLOR = '#E8ECF1'
NAVY     = '#1B3A5C'
TEAL     = '#2EAB8B'
GOLD     = '#D4A843'
RED      = '#C74B4B'
WHITE    = '#FFFFFF'
GRAY     = '#8899AA'
LIGHT_GOLD = '#F0DCA0'

# ──────────────────────────────────────────────
# DATA (dropped GradCAM)
# ──────────────────────────────────────────────
methods = ['FEX (Ours)', 'FastSHAP', 'RISE', 'IG']
time_seconds = [7.0, 11.6, 260.2, 311.9]
memory_gb = [2.0, 1.2, 15.9, 24.5]

# Colors: gold for FEX, navy for baselines
time_colors = [GOLD, NAVY, NAVY, NAVY]
mem_colors = [LIGHT_GOLD, GRAY, GRAY, GRAY]

# ──────────────────────────────────────────────
# FIGURE
# ──────────────────────────────────────────────
fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))
fig.patch.set_facecolor(BG_COLOR)
ax1.set_facecolor(BG_COLOR)

x = np.arange(len(methods))
bar_width = 0.35

# Time bars (left y-axis)
bars_time = ax1.bar(x - bar_width/2, time_seconds, bar_width,
                     color=time_colors, edgecolor=WHITE, linewidth=1.5,
                     zorder=3, label='Inference Time (s)')

# Value labels on time bars
for bar, val in zip(bars_time, time_seconds):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 8,
             f'{val}', ha='center', va='bottom', fontsize=11,
             fontweight='bold', color=TEAL)

ax1.set_ylabel('Inference Time (Seconds)', fontsize=12, color=TEAL,
               fontweight='bold')
ax1.set_yscale('log')
ax1.set_ylim(0.8, 600)
ax1.tick_params(axis='y', labelcolor=TEAL, labelsize=10)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(True)
ax1.spines['left'].set_color(TEAL)
ax1.spines['left'].set_linewidth(1.5)
ax1.spines['bottom'].set_color(NAVY)
ax1.spines['bottom'].set_linewidth(1.5)

# Memory bars (right y-axis)
ax2 = ax1.twinx()
bars_mem = ax2.bar(x + bar_width/2, memory_gb, bar_width,
                    color=mem_colors, edgecolor=WHITE, linewidth=1.5,
                    zorder=3, label='Memory (GB)')

# Value labels on memory bars
for bar, val in zip(bars_mem, memory_gb):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{val}', ha='center', va='bottom', fontsize=11,
             fontweight='bold', color=NAVY)

ax2.set_ylabel('Memory Usage (GB)', fontsize=12, color=NAVY,
               fontweight='bold')
ax2.set_ylim(0, 32)
ax2.tick_params(axis='y', labelcolor=NAVY, labelsize=10)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_color(NAVY)
ax2.spines['right'].set_linewidth(1.5)

# X axis
ax1.set_xticks(x)
ax1.set_xticklabels(methods, fontsize=12, fontweight='bold', color=NAVY)

# Title
ax1.set_title('Inference Cost: 1,000 Image Predictions',
              fontsize=14, fontweight='bold', color=NAVY, pad=15)

# ──────────────────────────────────────────────
# CALLOUT: 40× faster annotation
# ──────────────────────────────────────────────
# Arrow from RISE bar down to FEX bar
ax1.annotate('',
             xy=(0 - bar_width/2, 12),       # point near FEX bar top
             xytext=(2 - bar_width/2, 200),   # point near RISE bar
             arrowprops=dict(arrowstyle='->', color=RED, lw=2.5,
                            connectionstyle='arc3,rad=0.2'))

# "40× faster" label
ax1.text(0.85, 80, '40× faster',
         fontsize=16, fontweight='bold', color=RED,
         ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=WHITE,
                   edgecolor=RED, linewidth=2, alpha=0.95),
         zorder=10)

# ──────────────────────────────────────────────
# LEGEND
# ──────────────────────────────────────────────
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=TEAL, edgecolor=WHITE, label='Inference Time (s)'),
                   Patch(facecolor=GRAY, edgecolor=WHITE, label='Memory (GB)')]
ax1.legend(handles=legend_elements, loc='upper left', fontsize=10,
           framealpha=0.9, edgecolor=NAVY)

plt.tight_layout()
plt.savefig('saved/fex_efficiency_chart.svg', format='svg',
            bbox_inches='tight', facecolor=BG_COLOR)
plt.savefig('saved/fex_efficiency_chart.png', dpi=300,
            bbox_inches='tight', facecolor=BG_COLOR)
print("Done")