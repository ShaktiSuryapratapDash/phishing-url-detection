import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 6)
ax.axis('off')

C_DARK   = '#1D3557'
C_BLUE   = '#1D78C1'
C_GREEN  = '#2A9D8F'
C_ORANGE = '#F4A261'

ax.text(6, 5.6, '80 / 20 Train-Test Split — PhishingData.csv',
        ha='center', va='center', fontsize=14,
        fontweight='bold', color=C_DARK)

# Full dataset bar
full = FancyBboxPatch((0.5, 4.0), 11, 0.9,
                       boxstyle="round,pad=0.05,rounding_size=0.2",
                       facecolor=C_DARK, edgecolor='white', linewidth=2)
ax.add_patch(full)
ax.text(6, 4.45, '📁  Full Dataset — 11,055 Samples  |  30 Features',
        ha='center', va='center', fontsize=10,
        fontweight='bold', color='white')

# Arrow down
ax.annotate('', xy=(6, 3.55), xytext=(6, 3.95),
            arrowprops=dict(arrowstyle='->', color=C_DARK, lw=2.5,
                            mutation_scale=20))
ax.text(6.2, 3.75, 'train_test_split(test_size=0.2, random_state=42)',
        ha='center', va='center', fontsize=8,
        color=C_DARK, fontstyle='italic')

# Training set bar (80%)
train = FancyBboxPatch((0.5, 2.2), 8.8, 1.0,
                        boxstyle="round,pad=0.05,rounding_size=0.2",
                        facecolor=C_BLUE, edgecolor='white', linewidth=2)
ax.add_patch(train)
ax.text(4.9, 2.85, '🎓  Training Set',
        ha='center', va='center', fontsize=10,
        fontweight='bold', color='white')
ax.text(4.9, 2.5, '8,844 Samples  |  80%',
        ha='center', va='center', fontsize=9, color='white', alpha=0.9)

# Test set bar (20%)
test = FancyBboxPatch((9.5, 2.2), 2.0, 1.0,
                       boxstyle="round,pad=0.05,rounding_size=0.2",
                       facecolor=C_GREEN, edgecolor='white', linewidth=2)
ax.add_patch(test)
ax.text(10.5, 2.85, '🧪  Test Set',
        ha='center', va='center', fontsize=10,
        fontweight='bold', color='white')
ax.text(10.5, 2.5, '2,211  |  20%',
        ha='center', va='center', fontsize=9, color='white', alpha=0.9)

# Arrows down to outcomes
ax.annotate('', xy=(4.9, 1.55), xytext=(4.9, 2.2),
            arrowprops=dict(arrowstyle='->', color=C_BLUE, lw=2, mutation_scale=18))
ax.annotate('', xy=(10.5, 1.55), xytext=(10.5, 2.2),
            arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=2, mutation_scale=18))

# Outcome boxes
for x, w, color, text in [
    (1.5, 6.8, C_BLUE,  '⚙️  Model Training\nLearn patterns from labelled data'),
    (9.0, 2.5, C_GREEN, '📊  Model Evaluation\nUnbiased performance assessment'),
]:
    box = FancyBboxPatch((x, 0.4), w, 1.0,
                          boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor=color, edgecolor='white',
                          linewidth=1.5, alpha=0.85)
    ax.add_patch(box)
    ax.text(x + w/2, 0.9, text, ha='center', va='center',
            fontsize=9, fontweight='bold', color='white')

plt.tight_layout()
plt.savefig('figure_3_2_train_test_split.png', dpi=150, bbox_inches='tight')
print("Saved: figure_3_2_train_test_split.png")
plt.show()
