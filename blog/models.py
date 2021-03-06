from django.db import models
from tinymce.models import HTMLField

from images.models import Image
# Create your models here.
class Post(models.Model):
    class Meta:
        ordering = ('-published',)

    status_choices = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )

    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=256)
    content = HTMLField('Content')
    published = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=status_choices)
    description = models.TextField()
    keywords = models.TextField()
    featured_image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

def Slugify(title):
    slugged_title = title.replace(' ', '-').lower()
    return slugged_title