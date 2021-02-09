from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.urls import reverse_lazy

from .helpers import generate_confirmation_number
from .mailers import AccountMailer

from accounts.managers import AccountManager


class Account(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    confirmation_number = models.CharField(max_length=32, default=generate_confirmation_number)
    confirmed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.pk == None:
            self.send_account_confirmation_email()
        super(Account, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('profile')
    
    def is_confirmed(self):
        return self.confirmed_at == None

    def send_account_confirmation_email(self):
        AccountMailer().account_confirmation_email(self)