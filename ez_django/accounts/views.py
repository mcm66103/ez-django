from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from datetime import datetime

from .models import Account
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "create_account"
        return context

class ConfirmAccount(TemplateView):

    template_name = "accounts/confirm_account.html"

    def dispatch(request, *args, **kwargs):
       account = Account.objects.get(confirmation_code = confirmation_code)
       account.confirmed_at = datetime.now() 
       account.save()

       self.account = account
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["account"] = self.account
        return context