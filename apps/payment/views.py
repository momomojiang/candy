from django.shortcuts import render,redirect,HttpResponse,reverse
from ..login.models import User
from .models import *
from django.contrib import messages

def payment(request,id):
    return render(request,'payment/payment.html')