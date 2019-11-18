from ez_django.settings import BASE_URL, MEDIA_URL

def ez_django_context(request):
  return{
        "BASE_URL": BASE_URL,
        "MEDIA_URL": MEDIA_URL,
    }