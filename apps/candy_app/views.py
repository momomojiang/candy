from django.shortcuts import render,redirect, reverse
from django.contrib import messages
from ..login.models import User
from .models import *
import bcrypt


# Create your views here.
def index(request):
    context={
        'posts':Message.objects.all(),
        'poster':User.objects.all(),
        }
    return render(request,'candy_app/welcome.html',context)

def create(request):
    errors = Message.objects.message_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('main-page')
    else:
        poster=User.objects.get(id=request.session['user_id'])
        Message.objects.create(message=request.POST['message'], poster=poster)
        return redirect('main-page')
def delete(request,id):
    posts = Message.objects.get(id=id)
    posts.delete()
    return redirect('main-page')

