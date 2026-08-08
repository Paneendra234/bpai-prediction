from django.db import models
from django.conf import settings

class Prediction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='predictions')
    pregnancies = models.IntegerField(default=0)
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField(default=20)
    insulin = models.FloatField(default=79)
    bmi = models.FloatField()
    diabetes_pedigree = models.FloatField(default=0.5)
    age = models.IntegerField()
    prediction = models.CharField(max_length=20)  # 'Diabetic' or 'Non-Diabetic'
    risk_score = models.FloatField()  # 0-100
    model_used = models.CharField(max_length=50, default='Random Forest')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def get_risk_color(self):
        if self.risk_score < 30: return 'success'
        elif self.risk_score < 60: return 'warning'
        else: return 'danger'
    
    def get_sugar_status(self):
        if self.glucose < 100: return ('Normal', 'success')
        elif self.glucose < 126: return ('Pre-Diabetic', 'warning')
        else: return ('High Risk', 'danger')
    
    def get_bp_status(self):
        if self.blood_pressure < 80: return ('Normal', 'success')
        elif self.blood_pressure < 90: return ('Warning', 'warning')
        else: return ('High', 'danger')
    
    def get_bmi_status(self):
        if self.bmi < 18.5: return ('Underweight', 'warning')
        elif self.bmi < 25: return ('Normal', 'success')
        elif self.bmi < 30: return ('Overweight', 'warning')
        else: return ('Obese', 'danger')

    def __str__(self):
        return f"{self.user.username} - {self.prediction} ({self.created_at.strftime('%Y-%m-%d')})"
