import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from xgboost import XGBClassifier

# Load dataset
data = pd.read_csv('PhishingData.csv')
X = data.drop('Result', axis=1)
y = data['Result']

# 80/20 Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define base models
xgb = XGBClassifier(eval_metric='logloss', random_state=42)
dt = DecisionTreeClassifier(random_state=42)
# ─────────────────────────────────────────────
# Stacking Classifier (XGBoost + Decision Tree)
# ─────────────────────────────────────────────
stacking_clf = StackingClassifier(
    estimators=[('xgb', xgb), ('dt', dt)],
    final_estimator=LogisticRegression(max_iter=5000),
    cv=5
)
stacking_clf.fit(X_train, y_train)
stacking_pred = stacking_clf.predict(X_test)

print("=" * 55)
print("  Hybrid Model 1: XGBoost + Decision Tree")
print("=" * 55)

print("\n--- Stacking Classifier Results ---")
print(f"Accuracy  : {accuracy_score(y_test, stacking_pred)*100:.2f}%")
print(f"Precision : {precision_score(y_test, stacking_pred, zero_division=0)*100:.2f}%")
print(f"Recall    : {recall_score(y_test, stacking_pred, zero_division=0)*100:.2f}%")
print(f"F1 Score  : {f1_score(y_test, stacking_pred, zero_division=0)*100:.2f}%")