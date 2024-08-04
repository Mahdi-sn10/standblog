from django.db import models

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=20)
    writer = models.CharField(max_length=30)
    body = models.TextField()
    created_time = models.DateField(auto_now_add=True)
    edit_time = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="image/posts")


    def __str__(self) :
        return f"{self.title}:{self.writer}"