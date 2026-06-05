import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

fig, ax = plt.subplots(figsize=(13, 6))
ax.axis('off')

C_DARK   = '#1D3557'
C_BLUE   = '#1D78C1'
C_RED    = '#E63946'
C_GREEN  = '#2A9D8F'

ax.set_title('Final Summary — All Models All Metrics\nPhishing Website Detection | 80/20 Train-Test Split',
             fontsize=13, fontweight='bold', color=C_DARK, pad=20)

# Table data
columns = ['Model', 'Type', 'Accuracy', 'Precision', 'Recall', 'F1 Score', 'Rank']
data = [
    ['XGB + DT (Stacking)', 'Hybrid',  '96.83%', '96.47%', '98.01%', '97.23%', '🥇 1st'],
    ['Random Forest',        'Base',   '96.70%', '96.32%', '97.93%', '97.12%', '🥈 2nd'],
    ['XGBoost',              'Base',   '96.16%', '95.70%', '97.61%', '96.65%', '🥉 3rd'],
    ['Decision Tree',        'Base',   '95.75%', '96.25%', '96.25%', '96.25%', '4th'],
    ['SVM',                  'Base',   '94.71%', '94.25%', '96.57%', '95.40%', '5th'],
    ['Logistic Regression',  'Base',   '92.45%', '92.83%', '93.94%', '93.39%', '6th'],
    ['Naive Bayes',          'Base',   '58.30%', '99.70%', '26.61%', '42.01%', '⚠️ 7th'],
]

table = ax.table(
    cellText=data,
    colLabels=columns,
    loc='center',
    cellLoc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2.2)

# Style header
for j in range(len(columns)):
    table[0, j].set_facecolor(C_DARK)
    table[0, j].set_text_props(color='white', fontweight='bold', fontsize=10)

# Style rows
for i in range(1, len(data) + 1):
    for j in range(len(columns)):
        cell = table[i, j]
        if i == 1:  # Best hybrid — highlight
            cell.set_facecolor('#D4EDDA')
            cell.set_text_props(fontweight='bold', color=C_DARK)
        elif i == 7:  # Naive Bayes — warning
            cell.set_facecolor('#FFF3CD')
            cell.set_text_props(color=C_DARK)
        elif i % 2 == 0:
            cell.set_facecolor('#F8F9FA')
        else:
            cell.set_facecolor('#FFFFFF')

        # Highlight recall column for Naive Bayes
        if i == 7 and j == 4:
            cell.set_facecolor('#F8D7DA')
            cell.set_text_props(color=C_RED, fontweight='bold')

        # Highlight best values
        if i == 1 and j in [2, 4, 5]:
            cell.set_text_props(color=C_GREEN, fontweight='bold')

# Legend
ax.text(0.01, 0.02,
        '🟢 Green highlight = Best Hybrid Model (Winner)    '
        '🟡 Yellow highlight = Naive Bayes Anomaly    '
        '🔴 Red cell = Critical low recall',
        transform=ax.transAxes, fontsize=8,
        color=C_DARK, va='bottom')

plt.tight_layout()
plt.savefig('figure_7_1_summary_table.png', dpi=150, bbox_inches='tight')
print("Saved: figure_7_1_summary_table.png")
plt.show()
