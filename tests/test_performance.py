import os
import sys
import time
import json
import unittest
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthmate_ai.settings')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from django.test import Client
from accounts.models import CustomUser

class PerformanceTestSuite(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user, _ = CustomUser.objects.get_or_create(username='perf_tester')
        self.client.force_login(self.user)

    def test_page_load_latencies(self):
        endpoints = ['/', '/dashboard/', '/prediction/', '/diet/', '/dashboard/analytics/']
        latencies = {}
        for ep in endpoints:
            start = time.time()
            res = self.client.get(ep)
            duration_ms = round((time.time() - start) * 1000, 2)
            latencies[ep] = duration_ms
            self.assertEqual(res.status_code, 200)
            self.assertLess(duration_ms, 2000) # Response under 2 sec

        print("Page Load Latencies (ms):", latencies)

if __name__ == '__main__':
    os.makedirs('reports_output', exist_ok=True)
    suite = unittest.TestLoader().loadTestsFromTestCase(PerformanceTestSuite)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    report_data = {
        "suite": "Load Testing — Performance",
        "total_tests": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "passed": result.testsRun - len(result.failures) - len(result.errors),
        "status": "PASSED" if result.wasSuccessful() else "FAILED"
    }
    
    with open('reports_output/load-test-report.json', 'w') as f:
        json.dump(report_data, f, indent=2)
