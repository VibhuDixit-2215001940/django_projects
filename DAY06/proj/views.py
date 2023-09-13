from django.shortcuts import render
def index(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        # uemail = request.POST["uemail"]
        upass = request.POST["upass"]

        if uname == "vibhu" and upass == "angaar":
            print("ACCESS GRANTED!!")
        else:
            print("ACCESS NOT GRANTED!!")
            
        print(uname)
        # print(uemail)
        print(upass)
    return render(request,"index.html")