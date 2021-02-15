from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, "index.html")


def registration(request):
    return render(request, 'registration.html')

def home(request):
    return render(request, 'freebie.html')
