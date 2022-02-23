from tokenize import group
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<str:slug>', views.group_posts)
]