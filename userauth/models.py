from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite = models.ManyToManyField(Post)
    
    # def __str__(self):
    #     return user.username


# Create your models here.
