import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from xgboost import XGBClassifier

print("Program Started")

# Load dataset
df = pd.read_csv("PhishingData.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove index column if it exists
if 'index' in df.columns:
    df = df.drop('index', axis=1)

# Separate features and target
X = df.drop('Result', axis=1)
y = df['Result']

# Convert labels (-1 → 0)
y = y.replace(-1, 0)

splits = [(0.8,0.2)]

for train_size, test_size in splits:

    print("\nRunning Split:", train_size, "/", test_size)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=train_size, random_state=42
    )

    model = XGBClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=6,
        random_state=42,
        eval_metric='logloss'
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("================================")
    print(f"Train/Test Split: {int(train_size*100)}/{int(test_size*100)}")
    print("Accuracy :", round(accuracy,4))
    print("Precision:", round(precision,4))
    print("Recall   :", round(recall,4))
    print("F1 Score :", round(f1,4))