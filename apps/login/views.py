from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib import messages


# Create your views here.
def index(request):
	return render(request, 'login/index.html')

def register(request):
    print("you are in register")
    if request.method =='POST':
        first_name=request.POST['first_name']
        lastt_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        errors = User.objects.basic_validator(request.POST)
        if 'userreg' in errors:
            request.session['user_id'] = errors['userreg'].id
            request.session['first_name'] = errors['userreg'].first_name
            request.session['record'] = "registered!"
            return redirect('/select_your_candy')
        else:
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
            return redirect('/login')
def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if 'userlog' in errors:
            request.session['user_id'] = errors['userlog'].id
            request.session['first_name'] = errors['userlog'].first_name
            request.session['record'] = "logged in!"
            return redirect('/select_your_candy')
            
        else:
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
    return redirect('/login')

def logout(request):
	request.session.clear()
	return redirect('/')


# def edit(request,id):
#     print("@@@@@@@@@ EDIT FUNCTION @@@@@@@@@")
#     context={
#         'user': User.objects.get(id=id)
#     }
#     return render(request,'login/edit.html',context)

# def update(request,id):
#     errors = User.objects.update_validator(request.POST)
#     if len(errors)>0:
#         for key,value in errors.items():
#             messages.error(request,value)
#         return redirect(reverse('edit_user', kwargs={'id':id}))
#     else:
#         user=User.objects.get(id=id)
#         user.first_name=request.POST['first_name']
#         user.last_name=request.POST['last_name']
#         user.email=request.POST['email']
#         user.save()
#         return redirect('dashboard')





