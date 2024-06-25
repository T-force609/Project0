from django import forms
from .models import ApplicantForm, ParentForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = ApplicantForm
        fields = ('surname', 'firstname', 'lastname', 'gender', 'Date_of_birth','cls','phone_number','Email_Address', 'passport', 'birth_certificate', 'country', 'state', 'Address')
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']

        
class UserParentForm(forms.ModelForm):
    class Meta:
        model = ParentForm
        fields = ('Fathername', 'Mothername','F_number', 'M_number', 'F_occupation','M_occupation')