from django.shortcuts import render

from .models import Post


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
def detail(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'blog/detail.html', {'value': post})
