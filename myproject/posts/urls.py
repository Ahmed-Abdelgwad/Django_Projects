from django.urls import path
from . import views

urlpatterns = [
    path('about', views.posts_list),
]
