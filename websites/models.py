from django.db import models

from ez_django.models import BaseModel
from organizations.models import Organization

# Create your models here.
class Website (BaseModel):
    base_url = models.URLField(max_length=256)
    name = models.CharField(max_length=256)
    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.SET_NULL)