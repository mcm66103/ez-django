from django.shortcuts import render

def index(request):
    return render(request, 'ez_django/index.html')