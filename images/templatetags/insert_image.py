from django import template
from django.conf import settings
from images.models import Image

register = template.Library()

@register.simple_tag
def insert_image(id, class_names):
    image = Image.objects.get(id=id)
    return f"<img src='{settings.MEDIA_ROOT}/{image.file}' class='{class_names}' alt='{image.alt_tag}'>"

