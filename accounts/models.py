from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.urls import reverse_lazy

from .helpers import generate_confirmation_number
from .mailers import AccountMailer

from accounts.managers import AccountManager
from organizations.models import Organization


class Account(AbstractUser):
    ROLE_CHOICES = (
        ("sa", "Super Admin"),
        ("wd", "Web Developer"),
        ("oa", "Organization Admin"),
        ("ou", "Organization User"),
    )
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    username = None
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AccountManager()

    confirmation_number = models.CharField(max_length=32, default=generate_confirmation_number)
    confirmed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.pk == None:
            self.send_account_confirmation_email()

        if self.organization == None: 
            self.organization = Organization.new_default_organization()

        return super().save()
        

    def get_absolute_url(self):
        return reverse_lazy("profile")
    
    def is_confirmed(self):
        return self.confirmed_at == None

    def send_account_confirmation_email(self):
        AccountMailer().account_confirmation_email(self)