from django.db import models
from django.conf import settings

class DietPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='diet_plans')
    prediction = models.OneToOneField('prediction.Prediction', on_delete=models.CASCADE, null=True, blank=True)
    recommendation = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Diet Plan for {self.user.username} - {self.created_at.strftime('%Y-%m-%d')}"
