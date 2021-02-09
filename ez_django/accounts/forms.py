from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Account

class LoginForm(AuthenticationForm):
    pass