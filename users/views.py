from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *


# def log_in(request):
#     form = LoginForm(data=request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         user = form.get_user()
#         login(request, user)
#         return redirect('store:main')
#     return render(request, 'log_in.html', {'form': form})

class Register(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:log_in')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('store:main')


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('store:main')


# def register(request):
#     form = RegisterForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         user = form.save()
#         login(request, user)
#         return redirect('users:log_in')
#
#     return render(request, 'register.html', {'form': form})
#

def log_out(request):
    logout(request)
    return redirect('store:main')

