from turtle import title
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = "posts/index.html"
    title = "POSTS"
    context = {
        "title" : title,
        "text"  : "Это главная страница проекта Yatube"
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = "posts/index.html"
    title = "POSTS"
    context = {
        "title" : title,
        "text"  : "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, template, context)
    # return HttpResponse(f"GROUPS: {slug}")