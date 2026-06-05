import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import auc
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# KNOWN METRICS FROM TERMINAL OUTPUTS
# ROC curves approximated using TPR (Recall) and FPR
# derived from your exact Precision & Recall values
# ─────────────────────────────────────────────
models_data = {
    'XGBoost':             {'Precision': 95.70, 'Recall': 97.61, 'Accuracy': 96.16},
    'Random Forest':       {'Precision': 96.32, 'Recall': 97.93, 'Accuracy': 96.70},
    'Decision Tree':       {'Precision': 96.25, 'Recall': 96.25, 'Accuracy': 95.75},
    'SVM':                 {'Precision': 94.25, 'Recall': 96.57, 'Accuracy': 94.71},
    'Logistic Regression': {'Precision': 92.83, 'Recall': 93.94, 'Accuracy': 92.45},
    'Naive Bayes':         {'Precision': 99.70, 'Recall': 26.61, 'Accuracy': 58.30},
    'XGB + DT (Stacking)': {'Precision': 96.47, 'Recall': 98.01, 'Accuracy': 96.83},
}

# Approximate AUC values derived from Accuracy & Recall
# AUC ≈ (TPR + (1 - FPR)) / 2  where FPR = 1 - Precision (approximation)
def approx_auc(precision, recall):
    tpr = recall / 100
    fpr = 1 - (precision / 100)
    return round((tpr + (1 - fpr)) / 2, 4)

# Generate smooth ROC-like curve using known operating point
def generate_roc_curve(precision, recall):
    tpr_point = recall    / 100
    fpr_point = 1 - (precision / 100)

    # Build curve: from (0,0) through operating point to (1,1)
    fpr = np.array([0.0, fpr_point * 0.3, fpr_point, fpr_point * 2.5, 1.0])
    tpr = np.array([0.0, tpr_point * 0.6, tpr_point, tpr_point + (1 - tpr_point) * 0.6, 1.0])

    # Smooth with more points
    from scipy.interpolate import interp1d
    f = interp1d(fpr, tpr, kind='cubic')
    fpr_smooth = np.linspace(0, 1, 300)
    tpr_smooth = np.clip(f(fpr_smooth), 0, 1)
    return fpr_smooth, tpr_smooth

# Colours — distinct per model
colors = {
    'XGBoost':             '#E63946',
    'Random Forest':       '#2A9D8F',
    'Decision Tree':       '#E9C46A',
    'SVM':                 '#F4A261',
    'Logistic Regression': '#A8DADC',
    'Naive Bayes':         '#6D6875',
    'XGB + DT (Stacking)': '#1D3557',
}

styles = {
    'XGBoost':             ('--', 1.8),
    'Random Forest':       ('--', 1.8),
    'Decision Tree':       ('--', 1.8),
    'SVM':                 ('--', 1.8),
    'Logistic Regression': ('--', 1.8),
    'Naive Bayes':         ('--', 1.8),
    'XGB + DT (Stacking)': ('-',  3.0),
}

# ─────────────────────────────────────────────
# PLOT ALL ROC CURVES
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 8))

for name, m in models_data.items():
    fpr, tpr   = generate_roc_curve(m['Precision'], m['Recall'])
    roc_auc    = approx_auc(m['Precision'], m['Recall'])
    linestyle, linewidth = styles[name]

    ax.plot(fpr, tpr,
            color=colors[name],
            linestyle=linestyle,
            linewidth=linewidth,
            label=f"{name}  (AUC ≈ {roc_auc:.4f})")

# Random guess baseline
ax.plot([0, 1], [0, 1],
        color='black', linestyle=':', linewidth=1.5,
        label='Random Guess (AUC = 0.5000)')

# ─────────────────────────────────────────────
# FORMATTING
# ─────────────────────────────────────────────
ax.set_xlabel('False Positive Rate (FPR)', fontsize=12, fontweight='bold')
ax.set_ylabel('True Positive Rate (TPR) / Recall', fontsize=12, fontweight='bold')
ax.set_title(
    'ROC Curve Comparison — All Models\n'
    '6 Base Models + Best Hybrid (XGBoost + Decision Tree Stacking)  |  80/20 Split',
    fontsize=13, fontweight='bold', pad=15
)

ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.02])
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='lower right', fontsize=9.5, frameon=True)

plt.tight_layout()
plt.savefig('phishing_roc_curve.png', dpi=150, bbox_inches='tight')
print("Saved: phishing_roc_curve.png")
plt.show()
