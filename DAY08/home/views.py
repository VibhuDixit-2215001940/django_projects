from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        upass = request.POST.get("upass")
        if uname == "angaar" and upass == "angaar":
            return redirect("success")#only url name that is given
        else:
            return redirect("invalid")

    return render(request,"home.html")

def success(request):
    return render(request,"success.html")

def invalid(request):
    return render(request,"invalid.html")