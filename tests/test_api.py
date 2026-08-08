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

class APITestSuite(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user, _ = CustomUser.objects.get_or_create(username='testuser')
        self.user.set_password('Password123')
        self.user.save()
        self.client.force_login(self.user)

    def test_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_prediction_page(self):
        response = self.client.get('/prediction/')
        self.assertEqual(response.status_code, 200)

    def test_diet_list_page(self):
        response = self.client.get('/diet/')
        self.assertEqual(response.status_code, 200)

    def test_analytics_page(self):
        response = self.client.get('/dashboard/analytics/')
        self.assertEqual(response.status_code, 200)

    def test_profile_page(self):
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    os.makedirs('reports_output', exist_ok=True)
    suite = unittest.TestLoader().loadTestsFromTestCase(APITestSuite)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    report_data = {
        "suite": "Unit Tests - API",
        "total_tests": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "passed": result.testsRun - len(result.failures) - len(result.errors),
        "status": "PASSED" if result.wasSuccessful() else "FAILED"
    }
    
    with open('reports_output/unit-test-report.json', 'w') as f:
        json.dump(report_data, f, indent=2)
