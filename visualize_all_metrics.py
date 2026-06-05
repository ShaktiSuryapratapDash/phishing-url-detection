import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# RESULTS — exact values from terminal outputs
# 80/20 Train-Test Split
# ─────────────────────────────────────────────
results = {
    'XGBoost': {
        'Accuracy':  96.16,
        'Precision': 95.70,
        'Recall':    97.61,
        'F1 Score':  96.65,
    },
    'Random Forest': {
        'Accuracy':  96.70,
        'Precision': 96.32,
        'Recall':    97.93,
        'F1 Score':  97.12,
    },
    'Decision Tree': {
        'Accuracy':  95.75,
        'Precision': 96.25,
        'Recall':    96.25,
        'F1 Score':  96.25,
    },
    'SVM': {
        'Accuracy':  94.71,
        'Precision': 94.25,
        'Recall':    96.57,
        'F1 Score':  95.40,
    },
    'Logistic\nRegression': {
        'Accuracy':  92.45,
        'Precision': 92.83,
        'Recall':    93.94,
        'F1 Score':  93.39,
    },
    'Naive Bayes': {
        'Accuracy':  58.30,
        'Precision': 99.70,
        'Recall':    26.61,
        'F1 Score':  42.01,
    },
    'XGB + DT\n(Stacking)': {
        'Accuracy':  96.83,
        'Precision': 96.47,
        'Recall':    98.01,
        'F1 Score':  97.23,
    },
}

# ─────────────────────────────────────────────
# COLOURS
# ─────────────────────────────────────────────
BASE_COLOR   = '#1D78C1'   # Blue  — singular models
HYBRID_COLOR = '#E63946'   # Red   — best hybrid

def get_colors(labels):
    return [HYBRID_COLOR if ('+' in l or 'Stacking' in l) else BASE_COLOR
            for l in labels]

# ─────────────────────────────────────────────
# PLOT HELPER
# ─────────────────────────────────────────────
def plot_metric(metric_name, y_label, filename):
    # Extract and sort best -> worst
    data = {name: scores[metric_name] for name, scores in results.items()}
    sorted_pairs  = sorted(data.items(), key=lambda x: x[1], reverse=True)
    labels_sorted = [l for l, _ in sorted_pairs]
    values_sorted = [v for _, v in sorted_pairs]
    colors        = get_colors(labels_sorted)

    fig, ax = plt.subplots(figsize=(13, 7))

    bars = ax.bar(
        range(len(labels_sorted)),
        values_sorted,
        color=colors,
        edgecolor='black',
        linewidth=0.8,
        width=0.55
    )

    # Detailed value labels on each bar
    for bar, val in zip(bars, values_sorted):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.3,
            f'{val:.2f}%',
            ha='center', va='bottom',
            fontsize=10, fontweight='bold'
        )

    ax.set_xticks(range(len(labels_sorted)))
    ax.set_xticklabels(labels_sorted, fontsize=10.5)
    ax.set_ylabel(y_label, fontsize=12, fontweight='bold')
    ax.set_title(
        f'Phishing Website Detection — {metric_name} Comparison\n'
        '6 Base Models + Best Hybrid (XGBoost + Decision Tree Stacking)  |  80/20 Split',
        fontsize=13, fontweight='bold', pad=15
    )

    min_val = min(values_sorted)
    ax.set_ylim(max(0, min_val - 5), 104)
    ax.yaxis.grid(True, linestyle='--', alpha=0.5)
    ax.set_axisbelow(True)

    # Green reference line at best value
    best_val = max(values_sorted)
    ax.axhline(y=best_val, color='green', linewidth=1.2, linestyle='--', alpha=0.7)
    ax.text(
        len(labels_sorted) - 0.45, best_val + 0.35,
        f'Best: {best_val:.2f}%',
        color='green', fontsize=9, fontstyle='italic'
    )

    legend_elements = [
        mpatches.Patch(facecolor=BASE_COLOR,   edgecolor='black', label='Singular / Base Models'),
        mpatches.Patch(facecolor=HYBRID_COLOR, edgecolor='black', label='Best Hybrid Model (XGB + DT Stacking)'),
    ]
    ax.legend(handles=legend_elements, fontsize=10, loc='lower right', frameon=True)

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"Saved: {filename}")
    plt.show()

# ─────────────────────────────────────────────
# GENERATE ALL 4 GRAPHS
# ─────────────────────────────────────────────
plot_metric('Accuracy',  'Accuracy (%)',  'phishing_accuracy_comparison.png')
plot_metric('Precision', 'Precision (%)', 'phishing_precision_comparison.png')
plot_metric('Recall',    'Recall (%)',    'phishing_recall_comparison.png')
plot_metric('F1 Score',  'F1 Score (%)',  'phishing_f1_comparison.png')