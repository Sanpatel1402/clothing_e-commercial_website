from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=40)
    pass1 = forms.CharField(max_length=20)
    pass2 = forms.CharField(max_length=20)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)


class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'pass1', 'pass2')