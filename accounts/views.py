import random
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import CustomUser, OTPVerification
from .forms import SignupForm, LoginForm, ProfileUpdateForm, OTPForm

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, f'Welcome to HealthMate AI, {user.first_name}!')
            return redirect('dashboard:home')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect(request.GET.get('next', 'dashboard:home'))
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('core:home')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})

def send_otp_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        otp = str(random.randint(100000, 999999))
        # In production, integrate with SMS service (Twilio, MSG91 etc.)
        # For demo, we store and show it
        if request.user.is_authenticated:
            OTPVerification.objects.create(user=request.user, otp=otp, phone=phone)
            request.session['otp_phone'] = phone
            messages.info(request, f'Demo OTP: {otp} (In production this would be sent via SMS)')
            return redirect('accounts:verify_otp')
    return render(request, 'accounts/send_otp.html')

def verify_otp_view(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            phone = request.session.get('otp_phone')
            if request.user.is_authenticated:
                otp_obj = OTPVerification.objects.filter(
                    user=request.user, phone=phone, otp=entered_otp, is_verified=False
                ).order_by('-created_at').first()
                if otp_obj:
                    otp_obj.is_verified = True
                    otp_obj.save()
                    request.user.phone = phone
                    request.user.save()
                    messages.success(request, 'Phone number verified successfully!')
                    return redirect('accounts:profile')
                else:
                    messages.error(request, 'Invalid OTP. Please try again.')
    else:
        form = OTPForm()
    return render(request, 'accounts/verify_otp.html', {'form': form})

from django.http import JsonResponse
import json

def set_language_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            lang = data.get('language', 'en')
            if lang in ['en', 'te', 'hi']:
                if request.user.is_authenticated:
                    request.user.language = lang
                    request.user.save()
                request.session['user_language'] = lang
        except:
            pass
    return JsonResponse({'status': 'ok'})
