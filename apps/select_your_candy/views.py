from django.shortcuts import render,redirect,HttpResponse,reverse
from ..login.models import User
from .models import *
from django.contrib import messages

def select(request):
    return render(request,'select_your_candy/selectyourcandy.html')

def soft_candy(request):
    return render(request,'select_your_candy/soft_candy.html')

def hard_candy(request):
    return render(request,'select_your_candy/hard_candy.html')

def coconut(request):
    return render(request,'select_your_candy/coconut.html')

def cotton(request):
    return render(request,'select_your_candy/cotton.html')

def ice_cream(request):
    return render(request,'select_your_candy/icecream.html')

def liquor(request):
    return render(request,'select_your_candy/liquor.html')

def chocolate(request):
    return render(request,'select_your_candy/chocolate.html')

def red(request):
    return render(request,'select_your_candy/red.html')

def orange(request):
    return render(request,'select_your_candy/orange.html')


def yellow(request):
    return render(request,'select_your_candy/yellow.html')

def green(request):
    return render(request,'select_your_candy/green.html')

def indigo(request):
    return render(request,'select_your_candy/indigo.html')

def blue(request):
    return render(request,'select_your_candy/blue.html')

def violet(request):
    return render(request,'select_your_candy/violet.html')

def create_order(request,id):
    order_by = User.objects.get(id=request.session['user_id']) 
    Order.objects.create(candy_type=request.POST['candy_type'], candy_flavor=request.POST['candy_flavor'], candy_color=request.POST['candy_color'],themes=request.POST['themes'],brands=request.POST['brands'],order_by=order_by)
    return render(request,'select_your_candy/success_purchase.html')

# def collect_info(request,id):
#     return render(request,'select_your_candy/success_purchase.html',data)




