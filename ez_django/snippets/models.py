from django.db import models
from tinymce import models as tinymce_models


# Create your models here.
class Snippet(models.Model):

    class Meta:
        ordering = ('-published',)

    status_choices = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )

    location_choices = (
        ('BOH', 'After <head>'),
        ('EOH', 'Before </head>'),
        ('BOB', 'After <body>'),
        ('EOB', 'Before </body>'),
    )

    title = models.CharField(max_length=128)
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=status_choices)
    location = models.CharField(max_length=3, choices=location_choices)

    snippet = tinymce_models.HTMLField()

    def __str__(self):
        return self.title
