from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class SiteInfo(models.Model):
    name = models.TextField(max_length=255)
    description = models.CharField()
    phone_number = models.TextField(max_lenght=16)
    email = models.EmailField()
    keywords = models.TexField(max_length=512)
    logo = models.ImageField(upload_to='site_info/')
    favicon = models.ImageField(upload_to='site_info/')
    facebook_url = models.CharField(max_length=512)
    instagram_url = models.CharField(max_length=512)
    twitter_url = models.CharField(max_length=512)
    linkedin_url = models.CharField(max_length=512)
    address = models.CharField(max_length=512)

    def save(self, *args, **kwargs):
        if not self.pk and SiteInfo.objects.exists():
            raise ValidationError('There is can be only one SiteInfo instance')
        return super(SiteInfo, self).save(*args, **kwargs)