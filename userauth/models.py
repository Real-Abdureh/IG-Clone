from django.db import models
from django.contrib.auth.models import User
from post.models import Post


#uploading user file to specific directory
def user_driectory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
   first_name = models.CharField(max_length=50, null=True, blank=True)
   last_name = models.CharField(max_length=50, null=True, blank=True)
   location =  models.CharField(max_length=50, null=True, blank=True)
   url = models.URLField(max_length=1000, null=True, blank=True)
   bio = models.CharField(max_length=200, null=True, blank=True)
   created = models.DateField(auto_now_add=True)
   favourite = models.ManyToManyField(Post)
   picture = models.ImageField(upload_to=user_driectory_path, blank=True, null=True, verbose_name='Picture')
   favourite = models.ManyToManyField(Post)
#    def __str__(self):
#         return self.first_name


# Create your models here.
