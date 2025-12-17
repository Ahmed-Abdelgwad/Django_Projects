from django.shortcuts import render

# Create your views here.
def ahmed_view(request):
    return render(request, 'ahmed/ahmed.html')
