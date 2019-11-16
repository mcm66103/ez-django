from django import template
from django.conf import settings
from images.models import Image

register = template.Library()

@register.filter(name='insert_image', is_safe=True)
def insert_image(id, class):
    image = Image.objects.get(id=id)
    return f"<img src='{settings.MEDIA_ROOT}/{image.file}' class='{class}' alt='{image.alt_tag}'

