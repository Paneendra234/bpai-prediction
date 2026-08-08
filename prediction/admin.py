from django.contrib import admin
from .models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['user', 'glucose', 'bmi', 'prediction', 'risk_score', 'created_at']
    list_filter = ['prediction', 'created_at']
    search_fields = ['user__username']
