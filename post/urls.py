from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newpost', views.NewPost, name='newpost'),
    path('<uuid:post_id>/', views.PostDetail, name='post-detail'),
    path('<uuid:post_id>/like', views.like, name='like'),
    path('<uuid:post_id>/favourite', views.favourite, name='post-favourite'),
]