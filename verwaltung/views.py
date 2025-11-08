from django.shortcuts import render, HttpResponse

# Create your views here.

def start(request):
    return render(request, 'verwaltung/start.html')

def login(request):
    print("login")
    return HttpResponse("Liked!")
