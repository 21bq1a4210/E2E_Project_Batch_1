from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    #return HttpResponse('hello user')
    return render(request, 'login.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse('succrssfully registered')  # Replace 'home' with the name of your homepage URL
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'login.html')

    return render(request, 'login.html')