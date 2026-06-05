import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import warnings
warnings.filterwarnings('ignore')

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

C_DARK   = '#1D3557'
C_BLUE   = '#1D78C1'
C_GREEN  = '#2A9D8F'
C_ORANGE = '#F4A261'
C_RED    = '#E63946'
C_PURPLE = '#6D6875'

ax.text(7, 9.5, 'Research Pipeline Flowchart',
        ha='center', va='center', fontsize=15,
        fontweight='bold', color=C_DARK)

def draw_box(ax, x, y, w, h, color, title, subtitle=''):
    box = FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0.1,rounding_size=0.25",
                          facecolor=color, edgecolor='white',
                          linewidth=2, zorder=3)
    ax.add_patch(box)
    if subtitle:
        ax.text(x + w/2, y + h/2 + 0.15, title,
                ha='center', va='center', fontsize=10,
                fontweight='bold', color='white', zorder=4)
        ax.text(x + w/2, y + h/2 - 0.2, subtitle,
                ha='center', va='center', fontsize=8,
                color='white', alpha=0.9, zorder=4)
    else:
        ax.text(x + w/2, y + h/2, title,
                ha='center', va='center', fontsize=10,
                fontweight='bold', color='white', zorder=4)

def draw_arrow(ax, x1, y1, x2, y2, color=C_DARK):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=2.0, mutation_scale=20),
                zorder=2)

# Phase boxes — left column
phases = [
    (1.0, 8.2, 4.0, 0.8, C_BLUE,   'Phase 1',  'Data Collection & Loading',      '11,055 samples | PhishingData.csv'),
    (1.0, 6.8, 4.0, 0.8, C_BLUE,   'Phase 2',  'Data Preprocessing',             'Clean | Encode | Split 80/20'),
    (1.0, 5.4, 4.0, 0.8, C_ORANGE, 'Phase 3',  'Base Model Training',            '6 Individual ML Classifiers'),
    (1.0, 4.0, 4.0, 0.8, C_ORANGE, 'Phase 4',  'Hybrid Model Design',            'Voting & Stacking Combinations'),
    (1.0, 2.6, 4.0, 0.8, C_GREEN,  'Phase 5',  'Comprehensive Evaluation',       'Accuracy | Precision | Recall | F1'),
    (1.0, 1.2, 4.0, 0.8, C_GREEN,  'Phase 6',  'Comparative Analysis',           'Best Model Selection'),
]

for x, y, w, h, color, phase, title, subtitle in phases:
    # Phase label
    ax.text(x - 0.1, y + h/2, phase,
            ha='right', va='center', fontsize=8,
            fontweight='bold', color=color)
    draw_box(ax, x, y, w, h, color, title, subtitle)

# Arrows between phases
for y_from, y_to in [(8.2, 7.6), (6.8, 6.2), (5.4, 4.8),
                      (4.0, 3.4), (2.6, 2.0)]:
    draw_arrow(ax, 3.0, y_from, 3.0, y_to, C_DARK)

# Right column — details panel
details = [
    (8.0, 7.5, 5.5, 1.2, C_BLUE,   '📊 Dataset Details',
     '• 11,055 total samples\n• 30 binary features\n• 5,931 phishing | 5,124 legitimate'),
    (8.0, 5.8, 5.5, 1.2, C_ORANGE, '🤖 6 Base Models Evaluated',
     '• XGBoost  • Random Forest  • Decision Tree\n• SVM  • Logistic Regression  • Naive Bayes'),
    (8.0, 4.1, 5.5, 1.2, C_ORANGE, '🔗 Hybrid Model — Best Performer',
     '• XGBoost + Decision Tree (Stacking)\n• Accuracy: 96.83% | Recall: 98.01%'),
    (8.0, 2.4, 5.5, 1.2, C_GREEN,  '📈 Evaluation Metrics Used',
     '• Accuracy  • Precision  • Recall  • F1\n• Confusion Matrix  • ROC Curve & AUC'),
]

for x, y, w, h, color, title, body in details:
    box = FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor=color, edgecolor='white',
                          linewidth=1.5, alpha=0.15, zorder=2)
    ax.add_patch(box)
    ax.text(x + 0.2, y + h - 0.25, title,
            ha='left', va='center', fontsize=9,
            fontweight='bold', color=color)
    ax.text(x + 0.2, y + h/2 - 0.2, body,
            ha='left', va='center', fontsize=7.5, color=C_DARK)

# Connector lines from left to right
for y_left, y_right in [(8.6, 8.1), (6.0, 6.4), (4.4, 4.7), (2.0, 3.0)]:
    ax.plot([5.0, 8.0], [y_left, y_right],
            color=C_DARK, linewidth=1, linestyle='--', alpha=0.4, zorder=1)

plt.tight_layout()
plt.savefig('figure_3_1_research_pipeline.png', dpi=150, bbox_inches='tight')
print("Saved: figure_3_1_research_pipeline.png")
plt.show()
