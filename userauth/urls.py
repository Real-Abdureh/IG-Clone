from django.urls import path
from . import views

urlpatterns = [
    path('profile/update', views.editProfile, name='editprofile'),
   
]