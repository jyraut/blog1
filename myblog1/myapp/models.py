
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user_profile= models.OneToOneField(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    pic = models.FileField(upload_to='pic')

    def __str__(self):
        return self.location

class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

# Create your models here.
