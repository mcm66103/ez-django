from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def blog_list(request):
    context = {
        "posts": Post.objects.all().filter(status='P')}
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, slug):
    context = {
        "post": get_object_or_404(Post, slug=slug)}
    return render(request, 'blog/blog_detail.html', context)
