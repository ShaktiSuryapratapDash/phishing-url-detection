import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

fig, ax = plt.subplots(figsize=(13, 9))
ax.set_xlim(0, 13)
ax.set_ylim(0, 9)
ax.axis('off')

C_DARK   = '#1D3557'
C_BLUE   = '#1D78C1'
C_RED    = '#E63946'
C_GREEN  = '#2A9D8F'
C_ORANGE = '#F4A261'

ax.text(6.5, 8.6, 'Stacking Classifier Architecture\nXGBoost + Decision Tree → Logistic Regression Meta-Learner',
        ha='center', va='center', fontsize=13,
        fontweight='bold', color=C_DARK)

def draw_box(ax, x, y, w, h, color, title, subtitle='', alpha=1.0):
    box = FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0.1,rounding_size=0.25",
                          facecolor=color, edgecolor='white',
                          linewidth=2, zorder=3, alpha=alpha)
    ax.add_patch(box)
    if subtitle:
        ax.text(x+w/2, y+h/2+0.18, title, ha='center', va='center',
                fontsize=9, fontweight='bold', color='white', zorder=4)
        ax.text(x+w/2, y+h/2-0.2, subtitle, ha='center', va='center',
                fontsize=7.5, color='white', alpha=0.9, zorder=4)
    else:
        ax.text(x+w/2, y+h/2, title, ha='center', va='center',
                fontsize=9, fontweight='bold', color='white', zorder=4)

def arrow(ax, x1, y1, x2, y2, color=C_DARK, label=''):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=2.0, mutation_scale=18), zorder=2)
    if label:
        ax.text((x1+x2)/2 + 0.15, (y1+y2)/2,
                label, fontsize=7.5, color=color, fontstyle='italic')

# ── Layer labels ─────────────────────────────────────────────
for y, label, color in [(7.2, 'INPUT LAYER', C_DARK),
                         (5.2, 'BASE CLASSIFIERS  (Level 1)', C_BLUE),
                         (3.0, 'META-LEARNER  (Level 2)', C_ORANGE),
                         (1.1, 'OUTPUT LAYER', C_GREEN)]:
    ax.text(0.2, y, label, fontsize=8, fontweight='bold',
            color=color, alpha=0.7, rotation=0)

# Input
draw_box(ax, 4.0, 6.8, 5.0, 0.9, C_DARK,
         '📁  Training Dataset',
         '8,844 samples | 30 features | 80/20 split')

# 5-fold CV label
ax.text(6.5, 6.3, '5-Fold Cross Validation', ha='center',
        fontsize=8, color=C_DARK, fontstyle='italic',
        bbox=dict(boxstyle='round', facecolor='#F1FAEE', alpha=0.8))

# Base classifiers
draw_box(ax, 1.5, 4.8, 4.0, 0.9, C_BLUE,
         '🤖  XGBoost',
         'Gradient Boosting Ensemble')
draw_box(ax, 7.5, 4.8, 4.0, 0.9, C_RED,
         '🌳  Decision Tree',
         'Hierarchical Rule Based')

# Arrows from input to base classifiers
arrow(ax, 5.5, 6.8, 3.5, 5.7, C_BLUE,  'Train')
arrow(ax, 7.5, 6.8, 9.5, 5.7, C_RED,   'Train')

# Out of fold predictions
draw_box(ax, 1.5, 3.4, 4.0, 0.7, C_BLUE,
         'Out-of-Fold Predictions (XGB)', alpha=0.7)
draw_box(ax, 7.5, 3.4, 4.0, 0.7, C_RED,
         'Out-of-Fold Predictions (DT)',  alpha=0.7)

arrow(ax, 3.5, 4.8, 3.5, 4.1, C_BLUE)
arrow(ax, 9.5, 4.8, 9.5, 4.1, C_RED)

# Meta learner
draw_box(ax, 4.0, 2.2, 5.0, 0.9, C_ORANGE,
         '⚙️  Meta-Learner — Logistic Regression',
         'Learns optimal combination of base predictions')

arrow(ax, 3.5, 3.4, 5.5, 3.1, C_ORANGE, 'Feed')
arrow(ax, 9.5, 3.4, 7.5, 3.1, C_ORANGE, 'Feed')

# Final output
draw_box(ax, 4.0, 0.8, 5.0, 0.9, C_GREEN,
         '✅  Final Prediction',
         'Phishing (1)  or  Legitimate (0)')

arrow(ax, 6.5, 2.2, 6.5, 1.7, C_GREEN)

# Performance box
perf = FancyBboxPatch((9.8, 0.5), 2.9, 1.8,
                       boxstyle="round,pad=0.1,rounding_size=0.2",
                       facecolor=C_GREEN, edgecolor='white',
                       linewidth=1.5, alpha=0.15)
ax.add_patch(perf)
ax.text(11.25, 2.0, '🏆 Best Performance',
        ha='center', fontsize=8, fontweight='bold', color=C_GREEN)
ax.text(11.25, 1.7, 'Accuracy : 96.83%', ha='center', fontsize=7.5, color=C_DARK)
ax.text(11.25, 1.45, 'Precision : 96.47%', ha='center', fontsize=7.5, color=C_DARK)
ax.text(11.25, 1.2,  'Recall    : 98.01%', ha='center', fontsize=7.5, color=C_DARK)
ax.text(11.25, 0.95, 'F1 Score  : 97.23%', ha='center', fontsize=7.5, color=C_DARK)

plt.tight_layout()
plt.savefig('figure_3_3_stacking_architecture.png', dpi=150, bbox_inches='tight')
print("Saved: figure_3_3_stacking_architecture.png")
plt.show()
