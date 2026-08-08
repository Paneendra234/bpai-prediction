import os
import sys
import json
import unittest
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthmate_ai.settings')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from prediction.ml_utils import load_model, predict_diabetes, get_model_accuracy
from prediction.forms import PredictionForm

class ValidationTestSuite(unittest.TestCase):
    def test_ml_model_loading(self):
        model_data = load_model()
        self.assertIsNotNone(model_data)
        self.assertIn('model', model_data)

    def test_ml_prediction_logic(self):
        sample_data = {
            'pregnancies': 1,
            'glucose': 135,
            'blood_pressure': 75,
            'skin_thickness': 22,
            'insulin': 85,
            'bmi': 25.5,
            'diabetes_pedigree': 0.45,
            'age': 32
        }
        pred_label, score, model_name = predict_diabetes(sample_data)
        self.assertIn(pred_label, ['Diabetic', 'Non-Diabetic'])
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)

    def test_prediction_form_validation(self):
        form_data = {
            'pregnancies': 2,
            'glucose': 120,
            'blood_pressure': 70,
            'skin_thickness': 20,
            'insulin': 80,
            'bmi': 24.0,
            'diabetes_pedigree': 0.3,
            'age': 28
        }
        form = PredictionForm(data=form_data)
        self.assertTrue(form.is_valid())

if __name__ == '__main__':
    os.makedirs('reports_output', exist_ok=True)
    suite = unittest.TestLoader().loadTestsFromTestCase(ValidationTestSuite)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    report_data = {
        "suite": "Validation Tests",
        "total_tests": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "passed": result.testsRun - len(result.failures) - len(result.errors),
        "status": "PASSED" if result.wasSuccessful() else "FAILED"
    }
    
    with open('reports_output/validation-test-report.json', 'w') as f:
        json.dump(report_data, f, indent=2)
