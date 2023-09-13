from django.shortcuts import render

def index(request):
    if request.method == "POST":
        utext = request.POST["utext"]
        print(utext)
        if utext == "angaar":
            return render(request,"success.html")
        else:
            return render(request,"invalid.html")

    return render(request,"index.html")

def invalid(request):
    return render(request,"invalid.html")

def success(request):
    return render(request,"success.html")