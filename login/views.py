from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = username  # Store username in session
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'login.html')

    return render(request, 'login.html')
