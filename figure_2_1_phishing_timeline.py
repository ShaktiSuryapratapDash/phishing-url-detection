import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

fig, ax = plt.subplots(figsize=(15, 7))
ax.set_xlim(0, 15)
ax.set_ylim(0, 7)
ax.axis('off')

C_DARK   = '#1D3557'
C_BLUE   = '#1D78C1'
C_RED    = '#E63946'
C_GREEN  = '#2A9D8F'
C_ORANGE = '#F4A261'
C_PURPLE = '#6D6875'

ax.text(7.5, 6.5, 'Evolution of Phishing Attacks — Timeline',
        ha='center', va='center', fontsize=15,
        fontweight='bold', color=C_DARK)

# Main timeline line
ax.plot([0.5, 14.5], [3.5, 3.5], color=C_DARK, linewidth=3, zorder=1)

# Timeline events
events = [
    (1.2,  '1990s', 'Early Email\nPhishing',       'Mass email\ncampaigns',          C_BLUE,   'above'),
    (3.2,  '2000s', 'Website\nSpoofing',            'Fake bank\nwebsites',            C_RED,    'below'),
    (5.2,  '2005', 'Spear\nPhishing',               'Targeted\nattacks',              C_ORANGE, 'above'),
    (7.2,  '2010', 'Smishing &\nVishing',           'SMS & voice\nphishing',          C_PURPLE, 'below'),
    (9.2,  '2015', 'Pharming\nAttacks',             'DNS record\nmanipulation',       C_GREEN,  'above'),
    (11.2, '2018', 'AI Powered\nPhishing',          'Machine learning\nbased attacks', C_RED,   'below'),
    (13.2, '2020s', 'Advanced\nDeepfake Phishing', 'Voice & video\nimpersonation',   C_DARK,   'above'),
]

for x, year, title, desc, color, pos in events:
    # Dot on timeline
    ax.plot(x, 3.5, 'o', color=color, markersize=14, zorder=3)
    ax.plot(x, 3.5, 'o', color='white', markersize=7, zorder=4)

    if pos == 'above':
        y_box   = 4.1
        y_title = 5.3
        y_desc  = 4.8
        y_year  = 4.2
        ax.plot([x, x], [3.5, 4.0], color=color, linewidth=2, zorder=2)
    else:
        y_box   = 1.5
        y_title = 1.8
        y_desc  = 2.4
        y_year  = 3.0
        ax.plot([x, x], [2.0, 3.5], color=color, linewidth=2, zorder=2)

    box = FancyBboxPatch((x - 0.75, y_box - 0.1), 1.5, 1.2,
                          boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor=color, edgecolor='white',
                          linewidth=1.5, alpha=0.9, zorder=3)
    ax.add_patch(box)

    ax.text(x, y_title, title, ha='center', va='center',
            fontsize=8, fontweight='bold', color='white', zorder=4)
    ax.text(x, y_desc - 0.55, desc, ha='center', va='center',
            fontsize=6.5, color='white', alpha=0.9, zorder=4)
    ax.text(x, y_year + (0.3 if pos == 'above' else -0.25),
            year, ha='center', va='center',
            fontsize=8, fontweight='bold', color=color, zorder=4)

plt.tight_layout()
plt.savefig('figure_2_1_phishing_timeline.png', dpi=150, bbox_inches='tight')
print("Saved: figure_2_1_phishing_timeline.png")
plt.show()
