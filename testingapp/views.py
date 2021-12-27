from typing import ParamSpecKwargs
from django.db.models.expressions import Value
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth, messages
from .models import Users
# Create your views here.

def home(request):

    return render(request, 'Home.html')

def registration(request):
    if request.method == "POST":
        Name = request.POST['name']
        Dob = request.POST['dob']
        Gender = request.POST['gender']
        City = request.POST['city']
        Mobile = request.POST['mobile']
        Email = request.POST['email']
        Username = request.POST['username']
        Create_Password = request.POST['newpass']
        Confirm_Password = request.POST['Confirmpass']

        if (Create_Password == Confirm_Password):
            if User.objects.filter(username=Username).exists():
                messages.info(request,'Username exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name = Name, email = Email, username = Username, password = Confirm_Password)
                user.save()
                messages.info(request,'User created')
                return redirect('login')
        else:
            messages.info(request,'Password not Matched')
            return redirect('register')
    else:
        return render(request, 'Registration.html')

def login(request):

    if request.method == "POST":
        Username = request.POST['Username']
        Password = request.POST['password']

        user = auth.authenticate(username = Username, password = Password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'Login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')