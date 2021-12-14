from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request, 'Registration.html')

def registration(request):
    name = request.GET['name']
    DOB = request.GET['dob']
    Gender = request.GET['gender'] 
    City = request.GET['city']
    Mobile = request.GET['mobile']
    Email = request.GET['email']
    Username = request.GET['username']

    User1 = {'name':name,'DOB':DOB,'Gender':Gender,'City':City,'Mobile':Mobile, 'Email':Email,'UserName':Username}

    return render(request, 'RegisterInfo.html',{'user':User1})

def login(request):

    return render(request, 'Login.html')

def home(request):

    return render(request, 'Home.html')

def logout(request):
    return render(request,'Logout.html')
