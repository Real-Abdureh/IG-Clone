from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from PIL import Image
from django.db.models.base import Model
from django.db.models.fields import DateField
from django.urls import reverse
from django.db.models.signals import post_save
import uuid
from django.utils import timezone


#uploading user file to specific directory
def user_driectory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
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


   def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

   def __str__(self):
        return f'{self.user.username} - Profile'

   def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
















#    def save(self, args, **kwargs):
#         super().save(*args, **kwargs)
#         return self.first_name
   
#    def __str__(self):
#        return f'{self.user.username} -profile'
   
#    def save(self, args, **kwargs):
#         super().save(*args, **kwargs)
#         SIZE = 300, 300

#         if self.picture:
#            image = Image.open(self.picture.path)
#            image.thumbnail(SIZE, Image.LANCZOS)
#            image.save(self.picture.path)


# Create your models here.
