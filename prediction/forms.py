from django import forms

class PredictionForm(forms.Form):
    pregnancies = forms.IntegerField(min_value=0, max_value=20, initial=0,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'0-20'}))
    glucose = forms.FloatField(min_value=0, max_value=300,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'mg/dL (70-200)','step':'0.1'}))
    blood_pressure = forms.FloatField(min_value=0, max_value=200,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'mmHg (60-120)','step':'0.1'}))
    skin_thickness = forms.FloatField(min_value=0, max_value=100, initial=20,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'mm (10-50)','step':'0.1'}))
    insulin = forms.FloatField(min_value=0, max_value=900, initial=79,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'mu U/ml (0-300)','step':'0.1'}))
    bmi = forms.FloatField(min_value=0, max_value=70,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'kg/m² (15-50)','step':'0.1'}))
    diabetes_pedigree = forms.FloatField(min_value=0, max_value=3, initial=0.5,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'0.0-2.5','step':'0.001'}))
    age = forms.IntegerField(min_value=1, max_value=120,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Years'}))
