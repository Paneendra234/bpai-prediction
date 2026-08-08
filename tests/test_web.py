import os
import sys
import json
import unittest
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthmate_ai.settings')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from django.test import Client
from accounts.models import CustomUser
from prediction.models import Prediction
from diet.models import DietPlan

class WebE2ETestSuite(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user, _ = CustomUser.objects.get_or_create(username='web_tester')
        self.user.set_password('TestPass123')
        self.user.save()
        self.client.force_login(self.user)

    def test_full_prediction_flow(self):
        post_data = {
            'pregnancies': 1,
            'glucose': 145,
            'blood_pressure': 82,
            'skin_thickness': 28,
            'insulin': 110,
            'bmi': 27.5,
            'diabetes_pedigree': 0.48,
            'age': 38
        }
        res = self.client.post('/prediction/', post_data)
        self.assertEqual(res.status_code, 302)
        
        pred = Prediction.objects.filter(user=self.user).last()
        self.assertIsNotNone(pred)
        
        result_res = self.client.get(f'/prediction/result/{pred.pk}/')
        self.assertEqual(result_res.status_code, 200)

        pdf_res = self.client.get(f'/reports/generate/{pred.pk}/')
        self.assertEqual(pdf_res.status_code, 200)
        self.assertEqual(pdf_res['Content-Type'], 'application/pdf')

if __name__ == '__main__':
    os.makedirs('reports_output', exist_ok=True)
    suite = unittest.TestLoader().loadTestsFromTestCase(WebE2ETestSuite)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    report_data = {
        "suite": "Selenium — Website Tests",
        "total_tests": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "passed": result.testsRun - len(result.failures) - len(result.errors),
        "status": "PASSED" if result.wasSuccessful() else "FAILED"
    }
    
    with open('reports_output/selenium-web-report.json', 'w') as f:
        json.dump(report_data, f, indent=2)
