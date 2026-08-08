from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    phone = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number (+91XXXXXXXXXX)'}))
    
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','phone','password1','password2')
        widgets = {'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['password1','password2']:
            self.fields[field].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username or Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','phone','language','date_of_birth','gender','profile_picture')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'language': forms.Select(attrs={'class':'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'gender': forms.Select(attrs={'class':'form-select'}),
        }

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class':'form-control text-center fs-3 letter-spacing','maxlength':'6','placeholder':'000000'}))
