from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from App_login.forms import *
from App_login.models import *


def signup_system(request):
    form = SignUpForm()
    employees_id = EmployeeID.objects.all()
    listing_employees_id = []
    for i in employees_id:
        listing_employees_id.append(i.ids)
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        id = request.POST['employee_id']
        print(id)
        if form.is_valid():
            if id in listing_employees_id:
                form.save()
                return HttpResponseRedirect(reverse('App_login:login'))
            else:
                messages.info(request, 'Your Teacher ID is not valid.')
                return HttpResponseRedirect(reverse('App_login:signup'))
    return render(request, 'App_login/signup.html', context={'form': form})


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            passwd = form.cleaned_data.get('password')
            this_user = authenticate(username=username, password=passwd)
            if this_user is not None:
                login(request, this_user)
                return HttpResponseRedirect(reverse('App_library:home'))
    return render(request, 'App_login/login.html', context={'form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:login'))
