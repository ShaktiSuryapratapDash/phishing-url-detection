import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.patheffects as pe
import warnings
warnings.filterwarnings('ignore')

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis('off')

# ── Colour palette ──────────────────────────────────────────
C_RED    = '#E63946'
C_BLUE   = '#1D78C1'
C_GREEN  = '#2A9D8F'
C_ORANGE = '#F4A261'
C_DARK   = '#1D3557'
C_LIGHT  = '#F1FAEE'
C_GREY   = '#6C757D'

def draw_box(ax, x, y, w, h, color, text, subtext='', text_color='white', radius=0.3):
    box = FancyBboxPatch((x, y), w, h,
                          boxstyle=f"round,pad=0.1,rounding_size={radius}",
                          facecolor=color, edgecolor='white', linewidth=2,
                          zorder=3)
    ax.add_patch(box)
    if subtext:
        ax.text(x + w/2, y + h/2 + 0.18, text,
                ha='center', va='center', fontsize=10,
                fontweight='bold', color=text_color, zorder=4)
        ax.text(x + w/2, y + h/2 - 0.22, subtext,
                ha='center', va='center', fontsize=7.5,
                color=text_color, alpha=0.9, zorder=4)
    else:
        ax.text(x + w/2, y + h/2, text,
                ha='center', va='center', fontsize=10,
                fontweight='bold', color=text_color, zorder=4)

def draw_arrow(ax, x1, y1, x2, y2, color, label='', style='->', lw=2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color,
                                lw=lw, connectionstyle='arc3,rad=0.0'),
                zorder=2)
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx, my + 0.18, label, ha='center', va='bottom',
                fontsize=7.5, color=color, fontweight='bold', zorder=5)

# ── Title ────────────────────────────────────────────────────
ax.text(7, 7.5, 'Phishing Attack Architecture',
        ha='center', va='center', fontsize=15,
        fontweight='bold', color=C_DARK)

# ── ACTORS ───────────────────────────────────────────────────
# Cybercriminal
draw_box(ax, 0.3, 4.8, 2.2, 1.2, C_RED,
         '🕵️  Cybercriminal', 'Attacker')

# Phishing Website
draw_box(ax, 0.3, 2.8, 2.2, 1.2, C_RED,
         '🌐  Fake Website', 'Mimics legitimate site')

# Phishing Email
draw_box(ax, 0.3, 0.8, 2.2, 1.2, C_ORANGE,
         '📧  Phishing Email', 'Malicious link inside')

# Victim User
draw_box(ax, 5.9, 3.3, 2.2, 1.2, C_BLUE,
         '👤  Victim User', 'Unsuspecting target')

# Legitimate Website
draw_box(ax, 11, 4.8, 2.4, 1.2, C_GREEN,
         '✅  Legitimate Site', 'e.g. Real Bank Website')

# Stolen Data
draw_box(ax, 11, 2.8, 2.4, 1.2, C_RED,
         '💀  Stolen Data', 'Credentials / Finance')

# Detection System
draw_box(ax, 5.9, 0.8, 2.2, 1.2, C_GREEN,
         '🛡️  ML Detection', 'Phishing Filter')

# ── STEP LABELS ──────────────────────────────────────────────
steps = [
    (2.5,  5.4, 5.9,  5.4, C_RED,    'Step 1: Creates fake website'),
    (1.4,  4.8, 1.4,  2.8, C_RED,    ''),
    (2.5,  1.4, 5.9,  1.4, C_ORANGE, 'Step 2: Sends phishing email'),
    (7.0,  3.9, 11.0, 5.4, C_GREY,   'Step 3: User visits fake site'),
    (7.0,  3.3, 11.0, 3.3, C_RED,    'Step 4: Credentials stolen'),
    (7.0,  1.4, 11.0, 1.4, C_GREEN,  'Step 5: ML system detects & blocks'),
]

draw_arrow(ax, 2.5, 5.4,  5.9, 5.4,  C_RED,    'Step 1: Creates fake website')
draw_arrow(ax, 2.5, 3.4,  5.9, 3.9,  C_ORANGE, 'Step 2: Sends phishing email')
draw_arrow(ax, 8.1, 3.9,  11.0, 5.4, C_GREY,   'Step 3: Visits fake site')
draw_arrow(ax, 8.1, 3.3,  11.0, 3.3, C_RED,    'Step 4: Data stolen')
draw_arrow(ax, 7.0, 1.4,  11.0, 1.4, C_GREEN,  'Step 5: ML blocks phishing')
draw_arrow(ax, 7.0, 0.8,  2.5,  0.8, C_GREEN,  'Step 6: Alert sent back', lw=1.5)

# ── LEGEND ───────────────────────────────────────────────────
legend_elements = [
    mpatches.Patch(facecolor=C_RED,    label='Malicious / Attack Components'),
    mpatches.Patch(facecolor=C_BLUE,   label='Victim'),
    mpatches.Patch(facecolor=C_GREEN,  label='Protection / Legitimate'),
    mpatches.Patch(facecolor=C_ORANGE, label='Attack Vector'),
]
ax.legend(handles=legend_elements, loc='upper right',
          fontsize=8.5, frameon=True, framealpha=0.9,
          bbox_to_anchor=(0.98, 0.92))

plt.tight_layout()
plt.savefig('figure_1_1_phishing_attack.png', dpi=150, bbox_inches='tight')
print("Saved: figure_1_1_phishing_attack.png")
plt.show()
