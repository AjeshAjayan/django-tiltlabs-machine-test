from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'password')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')