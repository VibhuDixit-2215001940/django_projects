from django.shortcuts import render
def index(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        uemail = request.POST["uemail"]
        print(uname)
        print(uemail)
    return render(request,"index.html")