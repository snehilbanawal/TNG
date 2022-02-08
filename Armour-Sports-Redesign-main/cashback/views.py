from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages, auth
from accounts.models import Account
import requests

# Create your views here.


def home(request):

    return render(request, 'cashback/index.html')


def feedback(request):
    return render(request, 'cashback/index.html')


def cashback(request):
    # if request.method =='POST':
    users = Account.objects.all()
    return render(request, 'cashback/cashback.html', {'users': users})


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'cashback/login.html')


def signup(request):
    return render(request, 'cashback/signup.html')


def navbar(request):
    return render(request, 'cashback/navbar.html')
