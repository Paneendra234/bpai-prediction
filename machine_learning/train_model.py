import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import xgboost as xgb
import joblib
import os

# Generate synthetic PIMA-like diabetes dataset
np.random.seed(42)
n = 768

data = {
    'Pregnancies': np.random.randint(0, 17, n),
    'Glucose': np.random.normal(120, 32, n).clip(0, 200).astype(int),
    'BloodPressure': np.random.normal(69, 19, n).clip(0, 122).astype(int),
    'SkinThickness': np.random.normal(20, 16, n).clip(0, 99).astype(int),
    'Insulin': np.random.normal(79, 115, n).clip(0, 846).astype(int),
    'BMI': np.random.normal(32, 7, n).clip(0, 67).round(1),
    'DiabetesPedigreeFunction': np.random.exponential(0.47, n).clip(0.078, 2.42).round(3),
    'Age': np.random.randint(21, 81, n),
}
df = pd.DataFrame(data)

# Create outcome based on realistic rules
risk = (
    (df['Glucose'] > 140).astype(int) * 3 +
    (df['BMI'] > 30).astype(int) * 2 +
    (df['Age'] > 45).astype(int) * 1 +
    (df['BloodPressure'] > 80).astype(int) * 1 +
    (df['DiabetesPedigreeFunction'] > 0.5).astype(int) * 1 +
    (df['Pregnancies'] > 3).astype(int) * 1
)
df['Outcome'] = (risk >= 4).astype(int)

# Add some noise
flip_idx = np.random.choice(n, int(n * 0.08), replace=False)
df.loc[flip_idx, 'Outcome'] = 1 - df.loc[flip_idx, 'Outcome']

df.to_csv(os.path.join(os.path.dirname(__file__), 'dataset.csv'), index=False)

X = df.drop('Outcome', axis=1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'XGBoost': xgb.XGBClassifier(n_estimators=100, random_state=42, eval_metric='logloss')
}

best_model = None
best_acc = 0
best_name = ''
results = {}

for name, model in models.items():
    if name == 'Logistic Regression':
        model.fit(X_train_scaled, y_train)
        acc = accuracy_score(y_test, model.predict(X_test_scaled))
    else:
        model.fit(X_train, y_train)
        acc = accuracy_score(y_test, model.predict(X_test))
    results[name] = round(acc * 100, 2)
    if acc > best_acc:
        best_acc = acc
        best_model = model
        best_name = name

print("Model Accuracies:")
for name, acc in results.items():
    print(f"  {name}: {acc}%")
print(f"\nBest Model: {best_name} ({results[best_name]}%)")

save_dir = os.path.dirname(os.path.abspath(__file__))
joblib.dump({'model': best_model, 'scaler': scaler, 'model_name': best_name, 'accuracy': results}, 
            os.path.join(save_dir, 'model.pkl'))
print(f"Model saved to {save_dir}/model.pkl")
