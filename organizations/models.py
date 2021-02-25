from django.db import models

from ez_django.models import BaseModel
# Create your models here.
class Organization(BaseModel):
    name = models.CharField(max_length=256)
    
    @classmethod
    def new_default_organization(cls):
        organization = cls(name = "My New Organization")
        organization.save()
        return organization
