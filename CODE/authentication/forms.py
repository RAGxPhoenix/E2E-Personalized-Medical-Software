from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Doctor

class PatientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number']


class DoctorSignUpForm(UserCreationForm):
    med_license = forms.CharField(max_length=100, label='Medical License Number')
    specialization = forms.CharField(max_length=100, label='Specialization')

    class Meta(UserCreationForm.Meta):
        model = Doctor
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'med_license', 'specialization']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
