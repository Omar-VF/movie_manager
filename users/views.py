from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def signup(request):
    user = None
    error_messasge = None
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.create_user(username=username, password=password)
            return redirect('home')
        except Exception as e:
            error_messasge = str(e)
            if error_messasge.split()[-2:]:
                error_messasge = 'Username Already Exists!'

    return render(
        request,
        "users/signup.html",
        {"user": user, "error_message": error_messasge} 
    )

def user_login(request):
    user= None
    error_message = None
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_message = 'Username or Password do not match!'
            

    return render(request,'users/login.html',{'user':user,'error_message': error_message})

def user_logout(request):
    logout(request)
    return redirect('home')