from django.shortcuts import render
from .models import posts
# Create your views here.
def post_detale(request,pk):

    post = posts.objects.get(id=pk)
    return render(request,"blog/post-details.html",{"post":post})