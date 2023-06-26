from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from users.forms import *


def register_view(request):
    if request.method == 'GET':
        context_data = {
            'form': RegisterForm
        }
        return render(request, 'users/register.html', context=context_data)
    if request.method == 'POST':
        data = request.POST
        form = RegisterForm(data=data)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/users/login/')
            else:
                form.add_error('password1', 'error message :(')

        return render(request, 'users/register.html', context={
            'form': form
        })


def login_view(request):
    if request.method == 'GET':
        context_data = {
            'form': LoginForm
        }
        return render(request, 'users/login.html', context=context_data)
    if request.method == 'POST':
        data = request.POST
        form = LoginForm(data=data)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password1'))
            if user:
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error('username', 'try again :(')

        return render(request, 'users/login.html', context={
            'form': form
        })


def logout_view(request):
    logout(request)
    return redirect('/products/')
