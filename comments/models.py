from django.db import models

from accounts.models import Account
from ez_django.models import BaseModel
from tickets.models import Ticket


class Comment(BaseModel):
    account = models.ForeignKey(Account, blank=True, null=True, on_delete=models.SET_NULL)
    comments = models.TextField()

    class Meta:
        abstract = True

class TicketComment(Comment):
    ticket = models.ForeignKey(Ticket, blank=True, null=True, on_delete=models.SET_NULL)