from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home:home")
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home:home")
    return render(request,"account/login.html")

def logout_view(request):
    logout(request)
    return redirect("home:home")

def Regester(request):
    return render(request,"account/regester.html",context={})