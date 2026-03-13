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
fig, ax = plt.subplots(figsize=(10, 6.5))
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

def draw_collab_card(x, y, name, title, research, synergy, accent_color):
    width, height = 0.42, 0.38
    margin = 0.03
    top = y + height / 2
    bot = y - height / 2

    # Main Card Background
    card = patches.FancyBboxPatch((x - width/2, bot), width, height,
                                 boxstyle="round,pad=0.02,rounding_size=0.03",
                                 linewidth=1.5, edgecolor=GRAY, facecolor=WHITE, zorder=3)
    ax.add_patch(card)

    # Accent Header Bar (compact)
    header_h = 0.08
    header = patches.FancyBboxPatch((x - width/2, top - header_h), width, header_h,
                                 boxstyle="round,pad=0.02,rounding_size=0.03",
                                 linewidth=0, facecolor=accent_color, zorder=4)
    rect = patches.Rectangle((x - width/2 - 0.02, top - header_h), width + 0.04, 0.04,
                              facecolor=accent_color, zorder=4)
    ax.add_patch(header)
    ax.add_patch(rect)

    # Name & Title
    ax.text(x, top - 0.025, name, ha='center', va='center', color=WHITE,
            fontsize=15, fontweight='bold', zorder=5)
    ax.text(x, top - 0.055, title, ha='center', va='center', color=WHITE,
            fontsize=11, style='italic', zorder=5)

    # Research Focus
    ax.text(x - width/2 + margin, y + 0.04, "Research Focus:", ha='left', va='center',
            color=NAVY, fontsize=11, fontweight='bold', zorder=5)
    ax.text(x - width/2 + margin, y, research, ha='left', va='center',
            color=NAVY, fontsize=11, zorder=5)

    # Divider Line
    ax.plot([x - width/2 + margin, x + width/2 - margin], [y - 0.05, y - 0.05],
            color=GRAY, lw=1, ls='--', zorder=5)

    # Synergy
    ax.text(x - width/2 + margin, y - 0.09, "Synergy:", ha='left', va='center',
            color=accent_color, fontsize=11, fontweight='bold', zorder=5)

    synergy_lines = synergy.split('\n')
    for i, line in enumerate(synergy_lines):
        ax.text(x - width/2 + margin, y - 0.13 - (i * 0.04), line, ha='left', va='center',
                color=NAVY, fontsize=10.5, zorder=5)

# ──────────────────────────────────────────────
# DRAW CARDS
# ──────────────────────────────────────────────
# Top Left: Dr. Yao Qiang (Highlighting prior collaboration)
draw_collab_card(0.26, 0.72, "Dr. Yao Qiang", "SAFE AI Lab Director", 
                 "Trustworthy AI, LLM Safety, NLP", 
                 "Direct collaboration on Auditing & Alignment\n(Co-authored prior work: AttCAT & CIA)", TEAL)

# Top Right: Dr. Guangzhi Qu
draw_collab_card(0.74, 0.72, "Dr. Guangzhi Qu", "Professor & Dept. Chair", 
                 "Machine Learning, Systems, Data Sci.", 
                 "Computational infrastructure for scaling;\nHealthcare AI applications", NAVY)

# Bottom Left: Dr. Huirong Fu
draw_collab_card(0.26, 0.28, "Dr. Huirong Fu", "Cybersecurity Center", 
                 "Cybersecurity, AI Security", 
                 "Intersection of AI trustworthiness and\nadversarial robustness (NSF CyberCorps)", GOLD)

# Bottom Right: Dr. Weicheng Ma
draw_collab_card(0.74, 0.28, "Dr. Weicheng Ma", "Asst. Prof., NLP", 
                 "Natural Language Processing", 
                 "Linguistic foundations for LLM interpretation;\nText understanding methods", GRAY)

# Optional Center linking graphic
circle = patches.Circle((0.5, 0.5), 0.07, facecolor=BG_COLOR, edgecolor=GOLD, lw=3, zorder=6)
ax.add_patch(circle)
ax.text(0.5, 0.5, "Trustworthy\nAI", ha='center', va='center', color=NAVY, fontsize=13, fontweight='bold', zorder=7)

plt.tight_layout()
plt.savefig('saved/ou_faculty_collab.svg', format='svg', bbox_inches='tight', facecolor=BG_COLOR)
plt.savefig('saved/ou_faculty_collab.png', dpi=300, bbox_inches='tight', facecolor=BG_COLOR)
print("Plot saved successfully.")