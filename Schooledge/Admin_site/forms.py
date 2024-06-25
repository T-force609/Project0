from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username' , max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput)
