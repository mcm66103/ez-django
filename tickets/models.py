from django.db import models

from ez_django.models import BaseModel
from accounts.models import Account 
from websites.models import Website

class Ticket(BaseModel): 
    STATUS_CHOICES = (
        ("new", "New"),
        ("in progress", "In Progress"),
        ("ready for deployment", "Ready For Deployment"),
        ("complete", "Complete"),
        ("rejected", "Rejected"),
    )

    owner = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True, related_name="owner")
    worker = models.ForeignKey(Account, on_delete=models.SET_NULL,  blank=True, null=True, related_name="worker")

    status = models.CharField(choices=STATUS_CHOICES, default="new", max_length=48)

    name = models.CharField(max_length=128)
    description = models.TextField()

    website = models.ForeignKey(Website, on_delete=models.SET_NULL, blank=True, null=True)
