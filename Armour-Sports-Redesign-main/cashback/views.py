from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def feedback(request):
    return render(request,'cashback/index.html')

def cashback(request):
    return render(request,'cashback/cashback.html')

def login(request):
    return render(request,'cashback/login.html')

def signup(request):
    return render(request,'cashback/signup.html')

def navbar(request):
    return render(request,'cashback/navbar.html')
