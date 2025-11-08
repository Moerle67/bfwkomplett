from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def start(request):
    return render(request, 'verwaltung/start.html')

def user_login(request):
    name = request.POST['name']
    password = request.POST['password']
    user = authenticate(request, username=name, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Success")
    # Redirect to a success page.
    else:
        # Return an 'invalid login' error message.
        message = "Eingabe inkorrekt"
        return HttpResponse("Error")

def user_logout(request):
    logout(request)
    return HttpResponse("Succes")
