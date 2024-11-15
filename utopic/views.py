# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from utopic.forms import SignupForm, LoginForm

def register(request):
    signup_error = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            signup_error = "There was an error with your registration details. Please try again."
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form, 'signup_error': signup_error})

def user_login(request):
    login_error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('personal_account')
        else:
            login_error = "Invalid username or password."
    return render(request, 'login.html')

@login_required
def personal_account(request):
    return render(request, 'personal_account.html')

def user_logout(request):
    logout(request)  # Завершение сессии пользователя
    return redirect('home')
