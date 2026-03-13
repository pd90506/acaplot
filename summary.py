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

# ──────────────────────────────────────────────
# FIGURE SETUP
# ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5.5))
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

def draw_pillar(x, color, num, title, desc, badges):
    width = 0.26
    height = 0.75
    y = 0.5
    
    # Main Pillar Box
    card = patches.FancyBboxPatch((x - width/2, y - height/2), width, height, 
                                 boxstyle="round,pad=0.03,rounding_size=0.04", 
                                 linewidth=0, facecolor=WHITE, zorder=3)
    ax.add_patch(card)
    
    # Top Accent Header
    header_h = 0.18
    header = patches.FancyBboxPatch((x - width/2, y + height/2 - header_h), width, header_h, 
                                 boxstyle="round,pad=0.03,rounding_size=0.04", 
                                 linewidth=0, facecolor=color, zorder=4)
    # Square bottom of header
    rect = patches.Rectangle((x - width/2, y + height/2 - header_h), width, 0.05, facecolor=color, zorder=4)
    ax.add_patch(header)
    ax.add_patch(rect)
    
    # Number & Title
    ax.text(x, y + 0.38, f"0{num}", ha='center', va='center', color=WHITE, fontsize=24, fontweight='bold', alpha=0.3, zorder=5)
    ax.text(x, y + 0.28, title, ha='center', va='center', color=WHITE, fontsize=16, fontweight='bold', zorder=5)
    
    # Description Text
    # Wrap text manually for clean centering
    lines = desc.split('\n')
    for i, line in enumerate(lines):
        ax.text(x, y + 0.05 - (i * 0.06), line, ha='center', va='center', color=NAVY, fontsize=12, fontweight='bold', zorder=5)
        
    # Badges (Papers)
    badge_y = y - 0.25
    for badge in badges:
        bbox_props = dict(boxstyle="round,pad=0.3", fc=BG_COLOR, ec=color, lw=1.5)
        ax.text(x, badge_y, badge, ha='center', va='center', color=NAVY, fontsize=10, fontweight='bold', bbox=bbox_props, zorder=5)
        badge_y -= 0.10

# ──────────────────────────────────────────────
# DRAW 3 PILLARS
# ──────────────────────────────────────────────
# 1. Foundations
draw_pillar(0.2, NAVY, 1, "Foundations", 
            "Principled\ninterpretation via\nadversarial and\nlatent probing.", 
            ["AGI (IJCAI '21)", "AMCF (IJCAI '20)"])

# 2. Scalability
draw_pillar(0.5, TEAL, 2, "Scalability", 
            "Efficient LLM\nattribution via RL and\nbandit optimization.", 
            ["FEX (IJCAI '25)", "CAMAB (Under Review)"])

# 3. Alignment
draw_pillar(0.8, GOLD, 3, "Alignment", 
            "Active auditing\nand correction for\ntrustworthy deployment.", 
            ["NSF Initiative", "Industry Auditing"])

# Add subtle connecting arrows behind the pillars
ax.annotate("", xy=(0.37, 0.5), xytext=(0.33, 0.5), arrowprops=dict(arrowstyle="->", color=GRAY, lw=3, zorder=1))
ax.annotate("", xy=(0.67, 0.5), xytext=(0.63, 0.5), arrowprops=dict(arrowstyle="->", color=GRAY, lw=3, zorder=1))

plt.tight_layout()
plt.savefig('saved/summary_pillars.svg', format='svg', bbox_inches='tight', facecolor=BG_COLOR)
plt.savefig('saved/summary_pillars.png', dpi=300, bbox_inches='tight', facecolor=BG_COLOR)
print("Plot saved successfully.")