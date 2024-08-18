from django.shortcuts import render
from blog.models import posts

def home(request):
    Posts = posts.objects.all()  
    return render(request,"home/index.html",{"posts":Posts})