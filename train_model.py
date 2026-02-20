import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import shap

# load data
df = pd.read_csv("data/featured_transactions.csv")

features = [
    'amount',
    'hour',
    'user_txn_count',
    'amt_deviation',
    'device_usage',
    'txn_per_hour',
    'location_change'
]

X = df[features]
y = df['is_fraud']

# split data
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,stratify=y,random_state=42
)

# improved model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train,y_train)

# probability predictions
y_scores = model.predict_proba(X_test)[:,1]

# threshold tuning (increase fraud detection)
threshold = 0.30
y_pred = (y_scores > threshold).astype(int)

print("\n📊 MODEL PERFORMANCE\n")
print(classification_report(y_test,y_pred))
print("ROC AUC:", roc_auc_score(y_test,y_scores))
print("Confusion Matrix:\n", confusion_matrix(y_test,y_pred))

# feature importance
importance = model.feature_importances_
plt.bar(features, importance)
plt.title("Feature Importance")
plt.xticks(rotation=45)
plt.show()

# SHAP explainability
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

print("\nGenerating SHAP summary plot...")
shap.summary_plot(shap_values[1], X_test)