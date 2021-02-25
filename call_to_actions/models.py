from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class CTA(models.Model):
    status_choices = (
        ('P', 'Published'),
        ('D', 'Draft'),
    )

    message = models.TextField(max_length=512)
    status = models.CharField(max_length=1, choices=status_choices)
    cta = models.TextField(max_length=64)
    cta_link = models.URLField()

class HeaderCTA(CTA):
    def save(self, *args, **kwargs):
        if not self.pk and HeaderCTA.objects.exists():
            raise ValidationError('There is can be only one HeaderCTA instance')
        return super(HeaderCTA, self).save(*args, **kwargs)

class BlogEmbeddedCTA(CTA):
    def save(self, *args, **kwargs):
        if not self.pk and BlogEmbeddedCTA.objects.exists():
            raise ValidationError('There is can be only one BlogEmbeddedCTA instance')
        return super(BlogEmbeddedCTA, self).save(*args, **kwargs)

