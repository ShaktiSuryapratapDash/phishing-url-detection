🛡️ Phishing Website Detection using Machine Learning
A comprehensive machine learning project for automated detection of phishing websites, evaluating six individual classifiers and a hybrid ensemble model across multiple performance metrics.
---
📌 Project Overview
Phishing attacks remain one of the most dangerous cybersecurity threats globally. This project develops and compares machine learning models to automatically detect phishing websites using a dataset of 11,055 website samples with 30 distinct features.
Six base models were evaluated alongside a hybrid Stacking Classifier (XGBoost + Decision Tree with Logistic Regression as meta-learner), which achieved the best overall performance.
---
🏆 Results Summary
Model	Accuracy	Precision	Recall	F1 Score
XGB + DT (Stacking)	96.83%	96.47%	98.01%	97.23%
Random Forest	96.70%	96.32%	97.93%	97.12%
XGBoost	96.16%	95.70%	97.61%	96.65%
Decision Tree	95.75%	96.25%	96.25%	96.25%
SVM	94.71%	94.25%	96.57%	95.40%
Logistic Regression	92.45%	92.83%	93.94%	93.39%
Naive Bayes	58.30%	99.70%	26.61%	42.01%
> ✅ The hybrid XGBoost + Decision Tree Stacking model achieved the highest Accuracy, Recall and F1 Score among all evaluated models.
---
📂 Project Structure
```
phishing-url-detection/
│
├── PhishingData.csv                  # Dataset (11,055 samples, 30 features)
│
├── phishing_WebD_XB.py               # XGBoost model
├── phishing_WebD_RFM.py              # Random Forest model
├── phishing_WebD_DT.py               # Decision Tree model
├── phishing_WebD_SVM.py              # Support Vector Machine model
├── phishing_webD_LRM.py              # Logistic Regression model
├── phishing_WebD_NB.py               # Naive Bayes model
├── G_DT_Hyb_Sta.py                   # Hybrid Stacking Classifier (XGB + DT)
│
├── confusion_matrix_plot.py          # Confusion matrix visualizations
├── figure_1_1_phishing_attack.py     # Phishing attack architecture diagram
├── figure_2_1_phishing_timeline.py   # Phishing evolution timeline
│
└── phishing-url-detection.docx       # Full dissertation report
```
---
🗃️ Dataset
Source: Publicly available Phishing Website Dataset
Samples: 11,055 websites
Features: 30 (URL properties, domain info, security attributes, page structure)
Classes: Phishing (53.64%) | Legitimate (46.36%)
Missing Values: None
---
⚙️ Models Implemented
✅ XGBoost (Extreme Gradient Boosting)
✅ Random Forest
✅ Decision Tree
✅ Support Vector Machine (RBF Kernel)
✅ Logistic Regression
✅ Naive Bayes (Gaussian)
✅ Hybrid Stacking Classifier (XGBoost + Decision Tree → Logistic Regression meta-learner)
---
🧪 Evaluation Framework
Each model was evaluated using:
Accuracy, Precision, Recall, F1 Score
Confusion Matrix Analysis
ROC Curve & AUC Score
Train-Test Split: 80/20
---
🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.x-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Boosting-green)
![pandas](https://img.shields.io/badge/pandas-Data-lightgrey)
![matplotlib](https://img.shields.io/badge/matplotlib-Visualization-yellow)
Language: Python 3.x
Libraries: scikit-learn, XGBoost, pandas, NumPy, matplotlib, seaborn
---
🚀 How to Run
Clone the repository:
```bash
git clone https://github.com/ShaktiSuryapratapDash/phishing-url-detection.git
cd phishing-url-detection
```
Install dependencies:
```bash
pip install scikit-learn xgboost pandas numpy matplotlib seaborn
```
Run any model script:
```bash
python phishing_WebD_XB.py       # XGBoost
python phishing_WebD_RFM.py      # Random Forest
python G_DT_Hyb_Sta.py           # Hybrid Stacking Model
```
---
📈 Key Findings
The Hybrid XGBoost + Decision Tree Stacking model outperformed all individual classifiers
Naive Bayes showed an anomalous precision-recall imbalance (99.70% precision vs 26.61% recall) due to violated feature independence assumptions
Recall is the most critical metric in phishing detection — missing a phishing site is far more dangerous than a false alarm
Tree-based and ensemble models consistently outperformed linear and probabilistic models
---
👤 Author
Shakti Suryapratap Dash
Aspiring Software Engineer | Python | Machine Learning | DevOps
![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)
![GitHub](https://img.shields.io/badge/GitHub-Follow-black)
---
📄 License
This project is for academic and educational purposes.
