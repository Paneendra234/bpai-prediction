from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .forms import PredictionForm
from .models import Prediction
from .ml_utils import predict_diabetes, get_model_accuracy
from diet.utils import generate_diet_plan
from diet.models import DietPlan

@login_required
def predict_view(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            prediction_label, risk_score, model_name = predict_diabetes(data)
            pred = Prediction.objects.create(
                user=request.user,
                pregnancies=data['pregnancies'],
                glucose=data['glucose'],
                blood_pressure=data['blood_pressure'],
                skin_thickness=data['skin_thickness'],
                insulin=data['insulin'],
                bmi=data['bmi'],
                diabetes_pedigree=data['diabetes_pedigree'],
                age=data['age'],
                prediction=prediction_label,
                risk_score=risk_score,
                model_used=model_name,
            )
            diet_plan = generate_diet_plan(data['glucose'], data['blood_pressure'], data['bmi'], request.user.language)
            DietPlan.objects.create(user=request.user, prediction=pred, recommendation=diet_plan)
            return redirect('prediction:result', pk=pred.pk)
    else:
        form = PredictionForm()
    accuracy = get_model_accuracy()
    return render(request, 'prediction/predict.html', {'form': form, 'accuracy': accuracy})

@login_required
def result_view(request, pk):
    pred = get_object_or_404(Prediction, pk=pk, user=request.user)
    diet_plan = DietPlan.objects.filter(prediction=pred).first()
    return render(request, 'prediction/result.html', {'pred': pred, 'diet_plan': diet_plan})

@login_required
def history_view(request):
    predictions = Prediction.objects.filter(user=request.user)
    return render(request, 'prediction/history.html', {'predictions': predictions})
