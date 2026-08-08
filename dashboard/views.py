import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from prediction.models import Prediction
from diet.models import DietPlan

@login_required
def home(request):
    predictions = Prediction.objects.filter(user=request.user)
    total = predictions.count()
    latest = predictions.first()
    diabetic_count = predictions.filter(prediction='Diabetic').count()
    safe_count = predictions.filter(prediction='Non-Diabetic').count()
    
    # Chart data - last 10 predictions
    recent = list(predictions[:10][::-1])
    labels = [p.created_at.strftime('%b %d') for p in recent]
    glucose_data = [p.glucose for p in recent]
    bp_data = [p.blood_pressure for p in recent]
    bmi_data = [p.bmi for p in recent]
    risk_data = [p.risk_score for p in recent]
    
    context = {
        'total_predictions': total,
        'latest': latest,
        'diabetic_count': diabetic_count,
        'safe_count': safe_count,
        'labels': json.dumps(labels),
        'glucose_data': json.dumps(glucose_data),
        'bp_data': json.dumps(bp_data),
        'bmi_data': json.dumps(bmi_data),
        'risk_data': json.dumps(risk_data),
    }
    return render(request, 'dashboard/home.html', context)

@login_required
def analytics(request):
    predictions = Prediction.objects.filter(user=request.user)
    return render(request, 'dashboard/analytics.html', {'predictions': predictions})
