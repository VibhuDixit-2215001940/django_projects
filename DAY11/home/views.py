from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def dashboard(request):
    user = request.user 
    return render(request,"dashboard.html")

def Invalid(request):
    return render(request,"Invalid.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        userpass = request.POST.get("userpass")
        user = authenticate(username = username,password = userpass)
        if user is not None:
            login(request, user)
            return render(request, "dashboard")
        else:
            return redirect("Invalid")
    return render(request,"login.html")

def Signup(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        upass = request.POST.get("upass")

        myuser = User.objects.create_user(uname,fname,lname)
        myuser.fname = fname
        myuser.lname = lname

        myuser.save()
        messages.success(request,"Successfully Login!!")
        return redirect("dashboard")

    return render(request,"Signup.html")

def logout(request):
    auth.logout(request, user)
    return redirect("login")