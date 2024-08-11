from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=20)
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    created_time = models.DateField(auto_now_add=True)
    edit_time = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="image/posts")


    def __str__(self) :
        return f"{self.title}:{self.writer}"