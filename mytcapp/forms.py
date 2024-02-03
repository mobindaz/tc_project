# mytcapp/forms.py
from django import forms
from .models import TCRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your full name.')
    admission_number = forms.CharField(max_length=15, required=True, help_text='Required. Enter your admission number.')
    
    class Meta:
        model = User
        fields = ['name', 'username', 'admission_number', 'email', 'password1', 'password2']

class TCRequestForm(forms.ModelForm):
    class Meta:
        model = TCRequest
        fields = '__all__'
