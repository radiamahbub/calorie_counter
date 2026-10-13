from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from accounts.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def register_page(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    context = {
        'title':'Register',
        'form_title':'User Register Form',
        'form_btn':'Register',
        'form':form
    }    

    return render(request, 'form_base.html', context)

def login_page(request):

    form = AuthenticationForm()

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            user = form.get_user()

            if user:

                login(request, user)

                return redirect('dashboard')

    context = {
        'title':'Login',
        'form_title':'User Login Form',
        'form_btn':'Login',
        'form':form
    }

    return render(request, 'form_base.html', context)

def logout_page(request):

    return redirect('dashboard')

