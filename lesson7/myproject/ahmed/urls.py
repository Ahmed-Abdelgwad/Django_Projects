from django.urls import path
from . import views

app_name = 'ahmed' 

urlpatterns = [
    path('ahmed_view/', views.ahmed_view, name='ahmed'),
]
