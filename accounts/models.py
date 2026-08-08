from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    LANGUAGE_CHOICES = [('en', 'English'), ('te', 'Telugu'), ('hi', 'Hindi')]
    phone = models.CharField(max_length=15, blank=True, null=True)
    language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='en')
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('M','Male'),('F','Female'),('O','Other')], blank=True)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username

class OTPVerification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"OTP for {self.phone}"
