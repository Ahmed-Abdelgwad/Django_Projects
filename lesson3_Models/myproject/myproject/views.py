from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("I am Ahmed Abdul jawad!, HI!!")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("I'm Here!!!!!")
    return render(request, 'about.html')
