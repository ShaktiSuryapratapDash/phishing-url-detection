import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

fig, axes = plt.subplots(1, 2, figsize=(13, 6))
fig.suptitle('Naive Bayes vs XGB + DT Stacking — Precision & Recall Anomaly Analysis',
             fontsize=13, fontweight='bold', color='#1D3557', y=1.01)

C_RED   = '#E63946'
C_BLUE  = '#1D78C1'
C_DARK  = '#1D3557'
C_GREEN = '#2A9D8F'

metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
nb_vals     = [58.30, 99.70, 26.61, 42.01]
hybrid_vals = [96.83, 96.47, 98.01, 97.23]

x = np.arange(len(metrics))
width = 0.32

# Left chart — side by side bars
ax = axes[0]
bars1 = ax.bar(x - width/2, nb_vals,     width, label='Naive Bayes',
               color=C_RED,  edgecolor='white', linewidth=1.5)
bars2 = ax.bar(x + width/2, hybrid_vals, width, label='XGB + DT (Stacking)',
               color=C_BLUE, edgecolor='white', linewidth=1.5)

for bar, val in zip(bars1, nb_vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
            f'{val:.2f}%', ha='center', va='bottom',
            fontsize=8, fontweight='bold', color=C_RED)
for bar, val in zip(bars2, hybrid_vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
            f'{val:.2f}%', ha='center', va='bottom',
            fontsize=8, fontweight='bold', color=C_BLUE)

ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=9)
ax.set_ylabel('Score (%)', fontsize=10, fontweight='bold')
ax.set_ylim(0, 115)
ax.set_title('Side-by-Side Metric Comparison', fontsize=10, fontweight='bold')
ax.legend(fontsize=8.5)
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

# Right chart — radar / gap analysis
ax2 = axes[1]
categories = ['Precision', 'Recall']
nb_sub     = [99.70, 26.61]
hybrid_sub = [96.47, 98.01]

x2 = np.arange(len(categories))
bars3 = ax2.bar(x2 - width/2, nb_sub,     width, label='Naive Bayes',
                color=C_RED,  edgecolor='white', linewidth=1.5)
bars4 = ax2.bar(x2 + width/2, hybrid_sub, width, label='XGB + DT (Stacking)',
                color=C_BLUE, edgecolor='white', linewidth=1.5)

for bar, val in zip(bars3, nb_sub):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{val:.2f}%', ha='center', va='bottom',
             fontsize=9, fontweight='bold', color=C_RED)
for bar, val in zip(bars4, hybrid_sub):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{val:.2f}%', ha='center', va='bottom',
             fontsize=9, fontweight='bold', color=C_BLUE)

# Gap annotations
ax2.annotate('', xy=(0 - width/2, 99.70), xytext=(0 - width/2, 26.61),
             arrowprops=dict(arrowstyle='<->', color=C_DARK, lw=1.5))
ax2.text(-0.42, 63, '73.09%\ngap!', ha='center', fontsize=8,
         color=C_DARK, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

ax2.set_xticks(x2)
ax2.set_xticklabels(categories, fontsize=10)
ax2.set_ylabel('Score (%)', fontsize=10, fontweight='bold')
ax2.set_ylim(0, 115)
ax2.set_title('Precision vs Recall — The Anomaly', fontsize=10, fontweight='bold')
ax2.legend(fontsize=8.5)
ax2.yaxis.grid(True, linestyle='--', alpha=0.5)
ax2.set_axisbelow(True)

ax2.text(0.5, 8,
         '⚠️  Naive Bayes: High Precision but critically LOW Recall\n'
         '✅  Hybrid Model: Balanced and consistently HIGH across all metrics',
         ha='center', fontsize=8, color=C_DARK,
         bbox=dict(boxstyle='round', facecolor='#F1FAEE', alpha=0.9),
         transform=ax2.transAxes, va='bottom')

plt.tight_layout()
plt.savefig('figure_6_2_nb_vs_hybrid.png', dpi=150, bbox_inches='tight')
print("Saved: figure_6_2_nb_vs_hybrid.png")
plt.show()
