from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def Invalid(request):
    return render(request,"Invalid.html")

def login(request):
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