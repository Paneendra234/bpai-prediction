from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DietPlan

@login_required
def diet_list(request):
    plans = DietPlan.objects.filter(user=request.user)
    return render(request, 'diet/list.html', {'plans': plans})

@login_required
def diet_detail(request, pk):
    plan = get_object_or_404(DietPlan, pk=pk, user=request.user)
    return render(request, 'diet/detail.html', {'plan': plan})
