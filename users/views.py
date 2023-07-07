from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from users.forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView


class LoginCBV(LoginView):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            context_data = {
                'form': LoginForm
            }
            return render(request, self.template_name, context=context_data)
        if request.method == 'POST':
            data = request.POST
            form = LoginForm(data=data)

            if form.is_valid():
                user = authenticate(username=form.cleaned_data.get('username'),
                                    password=form.cleaned_data.get('password'))
                if user:
                    login(request, user)
                    return redirect('/products/')
                else:
                    form.add_error('username', 'try again :(')

            return render(request, self.template_name, context={
                'form': form
            })

    def get_success_url(self):
        return '/products/'


class RegisterCBV(CreateView):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            context_data = {
                'form': RegisterForm
            }
            return render(request, self.template_name, context=context_data)
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

            return render(request, self.template_name, context={
                'form': form
            })


class LogoutCBV(LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/products/')

# def logout_view(request):
#     logout(request)
#     return redirect('/products/')
