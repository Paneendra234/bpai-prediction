from django.contrib import admin
from .models import DietPlan

@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
