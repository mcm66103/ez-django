from django.db import models
from tinymce import HTMLField


# Create your models here.
class Snippet(models.Model):

    class Meta:
        ordering = ('-published',)

    status_choices = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )

    title = models.CharField(max_length=128)
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=status_choices)

    snippet = HTMLField()

    def __str__(self):
        return self.title
