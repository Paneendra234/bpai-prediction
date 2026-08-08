import joblib
import numpy as np
import pandas as pd
from django.conf import settings

_model_cache = None
FEATURE_COLS = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']

def load_model():
    global _model_cache
    if _model_cache is None:
        _model_cache = joblib.load(settings.ML_MODEL_PATH)
    return _model_cache

def predict_diabetes(data):
    model_data = load_model()
    model = model_data['model']
    scaler = model_data.get('scaler')
    model_name = model_data.get('model_name', 'Random Forest')

    features_df = pd.DataFrame([[
        data['pregnancies'], data['glucose'], data['blood_pressure'],
        data['skin_thickness'], data['insulin'], data['bmi'],
        data['diabetes_pedigree'], data['age']
    ]], columns=FEATURE_COLS)

    if 'Logistic' in model_name and scaler:
        proba = model.predict_proba(scaler.transform(features_df))[0]
    else:
        proba = model.predict_proba(features_df)[0]

    risk_score = round(proba[1] * 100, 1)
    prediction = 'Diabetic' if proba[1] >= 0.5 else 'Non-Diabetic'
    return prediction, risk_score, model_name

def get_model_accuracy():
    return load_model().get('accuracy', {})
