from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView as BaseLoginView
from django import forms
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .forms import LoginForm
from .models import Account

# Create your views here.

class LoginView(BaseLoginView):
    """The user can log in to the application."""

    template_name = "accounts/login.html"
    authentication_form = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "login"
        return context
    

@login_required
def ProfileView(request):
    """
        The user can see information about their profile when
        the user logs in.
    """

    context = { "account": request.user }
    return render(request, "accounts/profile.html", context)


class CreateAccountView(CreateView):
    """
        A new user can create a new account.
    """

    model = Account
    template_name = "accounts/create_account.html"
    fields = ["email", "password"]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "create_account"
        return context


class ConfirmAccount(TemplateView):

    template_name = "accounts/profile.html"

    def dispatch(self, request, *args, **kwargs):
        confirmation_number = kwargs["confirmation_number"]
        account = Account.objects.get(confirmation_number=confirmation_number)

        if account.is_confirmed():
            account.confirmed_at = datetime.now() 
            account.save()
            messages.success(request, "Your account is confirmed. Please log in to continue.")

        else: 
            messages.info(request, "It looks like this account has already been confirmed. Log in to continue")


        return redirect(reverse_lazy("profile"))