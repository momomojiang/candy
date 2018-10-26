from django.shortcuts import render,redirect,HttpResponse,reverse
from ..login.models import User
from .models import *
from django.contrib import messages

def payment(request,id):
    return render(request,'payment/payment.html')

def make_payment(request,id):
    return redirect('/success_purchase')
def successs_purchase(request,id):
    return render(request,'payment/success.html')