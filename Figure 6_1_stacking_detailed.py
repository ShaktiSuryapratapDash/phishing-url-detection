import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

C_DARK   = '#1D3557'
C_BLUE   = '#1D78C1'
C_RED    = '#E63946'
C_GREEN  = '#2A9D8F'
C_ORANGE = '#F4A261'
C_PURPLE = '#6D6875'

ax.text(7, 9.6, 'Detailed Stacking Ensemble Architecture',
        ha='center', va='center', fontsize=15,
        fontweight='bold', color=C_DARK)
ax.text(7, 9.2, 'How XGBoost and Decision Tree Combine Through Meta-Learning',
        ha='center', va='center', fontsize=10,
        color=C_DARK, fontstyle='italic')

def draw_box(ax, x, y, w, h, color, title, subtitle='', alpha=1.0):
    box = FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0.1,rounding_size=0.25",
                          facecolor=color, edgecolor='white',
                          linewidth=2, zorder=3, alpha=alpha)
    ax.add_patch(box)
    if subtitle:
        ax.text(x+w/2, y+h/2+0.2,  title,    ha='center', va='center',
                fontsize=9,  fontweight='bold', color='white', zorder=4)
        ax.text(x+w/2, y+h/2-0.18, subtitle, ha='center', va='center',
                fontsize=7.5, color='white', alpha=0.9, zorder=4)
    else:
        ax.text(x+w/2, y+h/2, title, ha='center', va='center',
                fontsize=9, fontweight='bold', color='white', zorder=4)

def arrow(ax, x1, y1, x2, y2, color=C_DARK, label='', lw=2.0):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, mutation_scale=18), zorder=2)
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx+0.1, my, label, fontsize=7.5,
                color=color, fontstyle='italic', zorder=5)

# ── LAYER 0: Full Dataset ────────────────────────────────────
draw_box(ax, 3.5, 8.2, 7.0, 0.75, C_DARK,
         '📁  Full Dataset — 11,055 Samples | 30 Features',
         '5-Fold Cross Validation applied during training')

# ── LAYER 1: Base Classifiers ────────────────────────────────
# Section label
ax.text(0.2, 7.4, 'LEVEL 1\nBase Classifiers', fontsize=8,
        fontweight='bold', color=C_BLUE, ha='left', va='center')

draw_box(ax, 1.0, 6.6, 5.0, 0.95, C_BLUE,
         '🤖  XGBoost Classifier',
         'Gradient Boosting | Learns complex non-linear patterns\neval_metric=logloss | random_state=42')

draw_box(ax, 8.0, 6.6, 5.0, 0.95, C_RED,
         '🌳  Decision Tree Classifier',
         'Hierarchical Rule-Based | Captures dominant patterns\nmax_depth=default | random_state=42')

# Arrows input → base classifiers
arrow(ax, 6.0, 8.2, 3.5, 7.55, C_BLUE,  'Train (80%)')
arrow(ax, 8.0, 8.2, 10.5, 7.55, C_RED,  'Train (80%)')

# ── LAYER 2: Predictions ─────────────────────────────────────
ax.text(0.2, 5.9, 'LEVEL 1\nPredictions', fontsize=8,
        fontweight='bold', color=C_PURPLE, ha='left', va='center')

draw_box(ax, 1.0, 5.3, 5.0, 0.75, C_BLUE,
         'XGBoost Out-of-Fold Predictions',
         'P(Phishing) probability for each training sample',
         alpha=0.75)

draw_box(ax, 8.0, 5.3, 5.0, 0.75, C_RED,
         'Decision Tree Out-of-Fold Predictions',
         'P(Phishing) probability for each training sample',
         alpha=0.75)

arrow(ax, 3.5, 6.6, 3.5, 6.05, C_BLUE)
arrow(ax, 10.5, 6.6, 10.5, 6.05, C_RED)

# ── LAYER 3: Meta Feature Stack ──────────────────────────────
ax.text(0.2, 4.6, 'LEVEL 2\nMeta Features', fontsize=8,
        fontweight='bold', color=C_ORANGE, ha='left', va='center')

draw_box(ax, 3.5, 4.0, 7.0, 0.75, C_ORANGE,
         '⚙️  Stacked Meta-Feature Matrix',
         '[XGB Predictions | DT Predictions] → Combined input for Meta-Learner')

arrow(ax, 3.5, 5.3,  5.0, 4.75, C_ORANGE, 'Stack')
arrow(ax, 10.5, 5.3, 9.0, 4.75, C_ORANGE, 'Stack')

# ── LAYER 4: Meta Learner ────────────────────────────────────
ax.text(0.2, 3.3, 'LEVEL 2\nMeta-Learner', fontsize=8,
        fontweight='bold', color=C_ORANGE, ha='left', va='center')

draw_box(ax, 3.5, 2.6, 7.0, 0.95, C_ORANGE,
         '🧠  Meta-Learner — Logistic Regression',
         'Learns optimal weighting of XGBoost vs Decision Tree predictions\nmax_iter=1000 | Trained on out-of-fold predictions | 5-Fold CV')

arrow(ax, 7.0, 4.0, 7.0, 3.55, C_ORANGE)

# ── LAYER 5: Final Output ────────────────────────────────────
ax.text(0.2, 2.0, 'OUTPUT\nLayer', fontsize=8,
        fontweight='bold', color=C_GREEN, ha='left', va='center')

draw_box(ax, 3.5, 1.2, 7.0, 0.95, C_GREEN,
         '✅  Final Classification Output',
         'Phishing (1)  or  Legitimate (0)\nThreshold = 0.5 applied to meta-learner probability')

arrow(ax, 7.0, 2.6, 7.0, 2.15, C_GREEN)

# ── Performance metrics box ──────────────────────────────────
perf = FancyBboxPatch((0.2, 0.2), 2.8, 2.5,
                       boxstyle="round,pad=0.1,rounding_size=0.2",
                       facecolor=C_GREEN, edgecolor='white',
                       linewidth=1.5, alpha=0.15, zorder=2)
ax.add_patch(perf)
ax.text(1.6, 2.45, '🏆 Best Performance',
        ha='center', fontsize=8.5, fontweight='bold', color=C_GREEN)
ax.text(1.6, 2.15, f'Accuracy  :  96.83%',
        ha='center', fontsize=8, color=C_DARK)
ax.text(1.6, 1.85, f'Precision :  96.47%',
        ha='center', fontsize=8, color=C_DARK)
ax.text(1.6, 1.55, f'Recall    :  98.01%',
        ha='center', fontsize=8, color=C_DARK)
ax.text(1.6, 1.25, f'F1 Score  :  97.23%',
        ha='center', fontsize=8, color=C_DARK)
ax.text(1.6, 0.7,  '★ Best among all\n   7 evaluated models',
        ha='center', fontsize=7.5, color=C_GREEN, fontweight='bold')

# ── Why it works box ─────────────────────────────────────────
why = FancyBboxPatch((11.0, 0.2), 2.8, 2.5,
                      boxstyle="round,pad=0.1,rounding_size=0.2",
                      facecolor=C_BLUE, edgecolor='white',
                      linewidth=1.5, alpha=0.15, zorder=2)
ax.add_patch(why)
ax.text(12.4, 2.45, '💡 Why It Works',
        ha='center', fontsize=8.5, fontweight='bold', color=C_BLUE)
ax.text(12.4, 2.1,  'XGBoost captures\ncomplex patterns',
        ha='center', fontsize=7.5, color=C_DARK)
ax.text(12.4, 1.65, 'DT captures\ndominant rules',
        ha='center', fontsize=7.5, color=C_DARK)
ax.text(12.4, 1.2,  'LR meta-learner\ncombines optimally',
        ha='center', fontsize=7.5, color=C_DARK)
ax.text(12.4, 0.7,  'Result: Lower\nvariance + higher\ngeneralisation',
        ha='center', fontsize=7.5, color=C_BLUE, fontweight='bold')

plt.tight_layout()
plt.savefig('figure_6_1_stacking_detailed.png', dpi=150, bbox_inches='tight')
print("Saved: figure_6_1_stacking_detailed.png")
plt.show()