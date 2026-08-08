from django.db import models
from django.conf import settings

class HealthReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prediction = models.ForeignKey('prediction.Prediction', on_delete=models.CASCADE, null=True)
    report_file = models.FileField(upload_to='reports/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
