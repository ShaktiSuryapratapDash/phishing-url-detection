import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis('off')

C_RED   = '#E63946'
C_BLUE  = '#1D78C1'
C_DARK  = '#1D3557'
C_LIGHT = '#F1FAEE'

ax.text(7, 7.5, 'Traditional Detection Methods vs Machine Learning Based Detection',
        ha='center', va='center', fontsize=13, fontweight='bold', color=C_DARK)

# Column headers
for x, label, color in [(3.2, 'Traditional Methods', C_RED),
                          (10.2, 'Machine Learning Methods', C_BLUE)]:
    box = FancyBboxPatch((x - 2.8, 6.3), 5.6, 0.8,
                          boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor=color, edgecolor='white', linewidth=2)
    ax.add_patch(box)
    ax.text(x, 6.7, label, ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

# VS divider
ax.text(7, 3.8, 'VS', ha='center', va='center',
        fontsize=20, fontweight='bold', color=C_DARK, alpha=0.3)

# Comparison rows
rows = [
    ('Detection Approach', 'Rule-based & Blacklists',        'Data-driven Pattern Learning'),
    ('New Threats',        'Cannot detect unknown attacks',  'Adapts to new phishing patterns'),
    ('Maintenance',        'Requires constant manual updates','Self-improving through retraining'),
    ('Accuracy',           'Low to moderate accuracy',       'High accuracy (up to 96.83%)'),
    ('Scalability',        'Limited scalability',            'Highly scalable to large datasets'),
    ('False Negatives',    'High missed detection rate',     'Very low missed detection rate'),
    ('Speed',              'Fast but outdated responses',    'Real-time intelligent detection'),
]

y_start = 5.8
for i, (aspect, trad, ml) in enumerate(rows):
    y = y_start - i * 0.72
    bg = '#F8F9FA' if i % 2 == 0 else '#FFFFFF'

    # Row background
    box = FancyBboxPatch((0.2, y - 0.28), 13.6, 0.55,
                          boxstyle="round,pad=0.05,rounding_size=0.1",
                          facecolor=bg, edgecolor='#DEE2E6', linewidth=0.8)
    ax.add_patch(box)

    ax.text(7,    y, aspect, ha='center', va='center',
            fontsize=8.5, fontweight='bold', color=C_DARK)
    ax.text(3.2,  y, trad,   ha='center', va='center',
            fontsize=8,   color=C_RED)
    ax.text(10.2, y, ml,     ha='center', va='center',
            fontsize=8,   color=C_BLUE)

# Vertical dividers
for x in [0.2, 6.2, 7.8, 13.8]:
    ax.plot([x, x], [0.6, 6.1], color='#DEE2E6', linewidth=1)

ax.text(3.2,  0.35, '❌  Limited & Reactive', ha='center',
        fontsize=9, color=C_RED, fontweight='bold')
ax.text(10.2, 0.35, '✅  Adaptive & Proactive', ha='center',
        fontsize=9, color=C_BLUE, fontweight='bold')

plt.tight_layout()
plt.savefig('figure_2_2_traditional_vs_ml.png', dpi=150, bbox_inches='tight')
print("Saved: figure_2_2_traditional_vs_ml.png")
plt.show()
