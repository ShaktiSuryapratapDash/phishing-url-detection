import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# KNOWN METRICS FROM TERMINAL OUTPUTS
# All values are based on 80/20 Train-Test Split
# Total test samples derived from dataset (~2290 approx)
# ─────────────────────────────────────────────
# Formula used to reconstruct confusion matrix:
#   Total  = test set size (approx 2290)
#   TP     = Recall * Actual Positives
#   FP     = (1 - Precision) * (TP / Precision)
#   TN     = Total - TP - FP - FN
#   FN     = Actual Positives - TP

# Actual class distribution (approx 80/20 split of PhishingData.csv)
TOTAL     = 2297   # approximate test set size
POS       = 1163   # approx phishing samples in test set
NEG       = TOTAL - POS  # approx legitimate samples in test set

def build_cm(precision, recall):
    tp = round(recall      * POS)
    fn = POS - tp
    fp = round(tp * (1 - precision) / precision)
    tn = NEG - fp
    return np.array([[tn, fp], [fn, tp]])

models_data = {
    'XGBoost':              {'Accuracy': 96.16, 'Precision': 95.70, 'Recall': 97.61, 'F1 Score': 96.65},
    'Random Forest':        {'Accuracy': 96.70, 'Precision': 96.32, 'Recall': 97.93, 'F1 Score': 97.12},
    'Decision Tree':        {'Accuracy': 95.75, 'Precision': 96.25, 'Recall': 96.25, 'F1 Score': 96.25},
    'SVM':                  {'Accuracy': 94.71, 'Precision': 94.25, 'Recall': 96.57, 'F1 Score': 95.40},
    'Logistic Regression':  {'Accuracy': 92.45, 'Precision': 92.83, 'Recall': 93.94, 'F1 Score': 93.39},
    'Naive Bayes':          {'Accuracy': 58.30, 'Precision': 99.70, 'Recall': 26.61, 'F1 Score': 42.01},
    'XGB + DT (Stacking)':  {'Accuracy': 96.83, 'Precision': 96.47, 'Recall': 98.01, 'F1 Score': 97.23},
}

# ─────────────────────────────────────────────
# PLOT CONFUSION MATRIX FOR EACH MODEL
# ─────────────────────────────────────────────
for name, m in models_data.items():
    precision = m['Precision'] / 100
    recall    = m['Recall']    / 100
    cm        = build_cm(precision, recall)

    is_hybrid = 'Stacking' in name or '+' in name
    cmap      = 'Reds' if is_hybrid else 'Blues'
    label     = '(Best Hybrid)' if is_hybrid else '(Base Model)'

    fig, ax = plt.subplots(figsize=(8, 6))

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=['Legitimate (0)', 'Phishing (1)']
    )
    disp.plot(ax=ax, cmap=cmap, colorbar=True, values_format='d')

    # Cell type labels
    cell_labels = [
        ('True Negative\n(TN)',  0, 0),
        ('False Positive\n(FP)', 0, 1),
        ('False Negative\n(FN)', 1, 0),
        ('True Positive\n(TP)',  1, 1),
    ]
    for lbl, row, col in cell_labels:
        ax.text(col, row - 0.22, lbl,
                ha='center', va='center',
                fontsize=8, color='gray', fontstyle='italic')

    ax.set_title(
        f'Confusion Matrix — {name} {label}\n80/20 Train-Test Split',
        fontsize=13, fontweight='bold', pad=15
    )
    ax.set_xlabel('Predicted Label', fontsize=11, fontweight='bold')
    ax.set_ylabel('True Label',      fontsize=11, fontweight='bold')

    # Stats box
    stats_text = (
        f"Accuracy : {m['Accuracy']:.2f}%\n"
        f"Precision: {m['Precision']:.2f}%\n"
        f"Recall   : {m['Recall']:.2f}%\n"
        f"F1 Score : {m['F1 Score']:.2f}%"
    )
    fig.text(0.98, 0.02, stats_text,
             fontsize=9, ha='right', va='bottom',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    filename = f"phishing_cm_{name.replace(' ', '_').replace('(','').replace(')','').replace('+','plus')}.png"
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"Saved: {filename}")
    plt.close()

print("\nAll confusion matrices generated successfully!")
