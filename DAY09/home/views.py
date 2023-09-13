from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        password = request.POST.get("password")
        data = {
            "usname" : uname,
            "password" : password
        }
        return render(request,"home.html", data)

    return render(request,"home.html")

