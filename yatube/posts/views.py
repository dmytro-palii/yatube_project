from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(
        'You <i>can not</i> get correct <b>answers</b>,<br> '
        'if you do not have correct <s>questions</s> requests.'
    ) 

def group_posts(request, slug):
    return HttpResponse(f"GROUPS: {slug}")