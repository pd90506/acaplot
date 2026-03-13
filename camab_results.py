import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# ──────────────────────────────────────────────
# COLOR PALETTE
# ──────────────────────────────────────────────
BG_COLOR = '#E8ECF1'
NAVY     = '#1B3A5C'
TEAL     = '#2EAB8B'
GOLD     = '#D4A843'
WHITE    = '#FFFFFF'
GRAY     = '#8899AA'
RED      = '#C74B4B'

# ──────────────────────────────────────────────
# FIGURE SETUP
# ──────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
fig.patch.set_facecolor(BG_COLOR)

# ──────────────────────────────────────────────
# PANEL 1: ATTRIBUTION QUALITY (Bar Chart)
# ──────────────────────────────────────────────
ax1.set_facecolor(BG_COLOR)
datasets = ['HotpotQA', 'TyDi QA']
camab_qual = [0.717, 0.893]
shap_qual  = [0.648, 0.872]
cc_qual    = [0.632, 0.631]

x = np.arange(len(datasets))
width = 0.25

bars1 = ax1.bar(x - width, camab_qual, width, label='CAMAB (Ours)', color=GOLD, edgecolor=WHITE, lw=1.5, zorder=3)
bars2 = ax1.bar(x, shap_qual, width, label='SHAP', color=TEAL, edgecolor=WHITE, lw=1.5, zorder=3)
bars3 = ax1.bar(x + width, cc_qual, width, label='ContextCite', color=NAVY, edgecolor=WHITE, lw=1.5, zorder=3)

# Labels and Styling
ax1.set_ylabel('Log-Prob Drop (↑ Better)', fontsize=12, fontweight='bold', color=NAVY)
ax1.set_title('Attribution Quality (Budget = 40)', fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax1.set_xticks(x)
ax1.set_xticklabels(datasets, fontsize=12, fontweight='bold', color=NAVY)
ax1.set_ylim(0.5, 1.0)

for spine in ['top', 'right']: ax1.spines[spine].set_visible(False)
for spine in ['left', 'bottom']: 
    ax1.spines[spine].set_color(NAVY)
    ax1.spines[spine].set_linewidth(1.5)
ax1.tick_params(colors=NAVY, labelsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.3, zorder=0, color=NAVY)

# Add values on top of bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        ax1.annotate(f'{bar.get_height():.3f}',
                     xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                     xytext=(0, 3), textcoords="offset points",
                     ha='center', va='bottom', fontsize=10, fontweight='bold', color=NAVY)

ax1.legend(loc='upper left', fontsize=10, framealpha=0.9, edgecolor=NAVY)

# ──────────────────────────────────────────────
# PANEL 2: QUERY EFFICIENCY (Line Chart)
# ──────────────────────────────────────────────
ax2.set_facecolor(BG_COLOR)
budgets = [20, 40, 60]
camab_eff = [0.525, 0.509, 0.511]
shap_eff  = [0.668, 0.562, 0.527]
cc_eff    = [0.605, 0.601, 0.598]

ax2.plot(budgets, camab_eff, marker='o', markersize=8, lw=3, label='CAMAB (Ours)', color=GOLD, zorder=4)
ax2.plot(budgets, shap_eff, marker='s', markersize=8, lw=3, label='SHAP', color=TEAL, zorder=3)
ax2.plot(budgets, cc_eff, marker='^', markersize=8, lw=3, label='ContextCite', color=NAVY, zorder=3)

# Labels and Styling
ax2.set_ylabel('BERTScore (↓ Better)', fontsize=12, fontweight='bold', color=NAVY)
ax2.set_xlabel('Query Budget (s)', fontsize=12, fontweight='bold', color=NAVY)
ax2.set_title('Efficiency on HotpotQA', fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax2.set_xticks(budgets)
ax2.set_ylim(0.48, 0.70)

for spine in ['top', 'right']: ax2.spines[spine].set_visible(False)
for spine in ['left', 'bottom']: 
    ax2.spines[spine].set_color(NAVY)
    ax2.spines[spine].set_linewidth(1.5)
ax2.tick_params(colors=NAVY, labelsize=10)
ax2.grid(axis='both', linestyle='--', alpha=0.3, zorder=0, color=NAVY)

# Callout: CAMAB @ 20 vs SHAP @ 40
ax2.annotate('', xy=(20.5, 0.525), xytext=(39.5, 0.562),
             arrowprops=dict(arrowstyle='<->', color=RED, lw=2.5, ls='--'))
ax2.text(30, 0.515, '50% fewer\nqueries', fontsize=12, fontweight='bold', color=RED,
         ha='center', va='top', bbox=dict(boxstyle='round,pad=0.3', facecolor=WHITE, edgecolor=RED, lw=1.5, alpha=0.9))

ax2.legend(loc='upper right', fontsize=10, framealpha=0.9, edgecolor=NAVY)

plt.tight_layout()
plt.savefig('saved/camab_results_dual.svg', format='svg', bbox_inches='tight', facecolor=BG_COLOR)
plt.savefig('saved/camab_results_dual.png', dpi=300, bbox_inches='tight', facecolor=BG_COLOR)
print("Plot saved successfully.")