from email import message
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import cashbackus, feedbackus

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

def cashbackform(request):
    if request.method == 'POST':
        name1 = request.POST['name1']
        num1 = request.POST['num1']
        amount1 = request.POST['amount1']
       
        # services1 = request.POST['services1']

        cont_obj = cashbackus(name=name1, num=num1, amount=amount1)
        cont_obj.save()

        return redirect('cashback')
    else:
        return redirect('/')

def feedbackform(request):
    if request.method == 'POST':
        ratingg = request.POST['ratingg']
        recommendation1 = request.POST['recommendation1']
        service1 = request.POST['service1']
        message1 = request.POST['message1']
       
        # services1 = request.POST['services1']

        cont_obj = feedbackus(rating=ratingg, recommendation=recommendation1, service=service1,msg=message1)
        cont_obj.save()

        return redirect('feedback')
    else:
        return redirect('/')