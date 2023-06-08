from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from userauth.models import Profile
from django.urls import resolve
from post.models import Post




# def UserProfile(request, username):
#     Profile.objects.get_or_create(user=request.user)
#     user = get_object_or_404(User, username=username)
#     profile = Profile.objects.get(user=user)
#     url_name = resolve(request.path).url_name
#     posts = Post.objects.filter(user=user).order_by('-posted')

#     if url_name == 'profile':
#         posts = Post.objects.filter(user=user).order_by('-posted')
#     else:
#         posts = profile.favourite.all()
    

#     #pagination
#     paginator = Paginator(posts, 3)
#     page_number = request.GET.get('page')
#     posts_paginator = paginator.get_page(page_number)

#     context = {
#         'posts_paginator':posts_paginator
#     }

#     return render(request, 'profile.html', context)


def UserProfile(request, username):
    Profile.objects.get_or_create(user=request.user)
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url_name = resolve(request.path).url_name
    posts = Post.objects.filter(user=user).order_by('-posted')

    if url_name == 'profile':
        posts = Post.objects.filter(user=user).order_by('-posted')
    else:
        posts = profile.favourite.all()
    
    # Profile Stats
    # posts_count = Post.objects.filter(user=user).count()
    # following_count = Follow.objects.filter(follower=user).count()
    # followers_count = Follow.objects.filter(following=user).count()
    # # count_comment = Comment.objects.filter(post=posts).count()
    # follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

    # pagination
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'profile':profile,
        # 'posts_count':posts_count,
        # 'following_count':following_count,
        # 'followers_count':followers_count,
        'posts_paginator':posts_paginator,
        # 'follow_status':follow_status,
        # 'count_comment':count_comment,
    }
    return render(request, 'profile.html', context)



# Create your views here.
