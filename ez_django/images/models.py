from django.db import models

# Create your models here.
class Image(models.Model):
    class Meta:
        ordering = ('-created',)

    title = models.CharField(max_length=128)
    alt_tag = models.CharField(max_length=128)
    file = models.ImageField(upload_to='images/')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
