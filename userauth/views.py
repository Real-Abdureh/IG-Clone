from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from userauth.models import Profile
from userauth.forms import EditProfileForm
from django.urls import resolve, reverse
from post.models import Post, Follow, Stream
from django.db import transaction 




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
    
    #Tracking Profile start
    post_count = Post.objects.filter(user=user).count
    following_count = Follow.objects.filter(follower=user).count
    followers_count = Follow.objects.filter(following=user).count

    #checking follow status

    follow_status = Follow.objects.filter(following=user, follower=request.user).exists()



   #pagination
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'profile':profile,
        'url_name':url_name,
        'post_count':post_count,
        'following_count':following_count,
        'follower_count':followers_count,
        'posts_paginator':posts_paginator,
        'follow_status':follow_status,
        # 'count_comment':count_comment,
    }
    return render(request, 'profile.html', context)

def follow(request, username, option):
    user = request.user
    following = get_object_or_404(User, username=username)
    try:
        f, created = Follow.objects.get_or_create(follower=user, following=following)
        if int(option) == 0:
            f.delete()
            Stream.objects.filter(following=following, user=user).all().delete()
        else:
            posts = Post.objects.filter(user=following)[:10]

            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post, user=user, date=post.posted, following=following)
                    stream.save()
        return HttpResponseRedirect(reverse('profile', args=[username ]))
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('profile', args=[username]))
    

def editProfile(request):
    user = request.user
    profile = Profile.objects.get(user_id=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST. request.FILES)
        if form.is_valid():
            profile.picture = form.cleaned_data.get('picture')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.bio = form.cleaned_data.get('bio')
            profile.url = form.cleaned_data.get('url')#
            profile.save()
            return redirect('profile')
    else:
        form = EditProfileForm()

        context = {
        'form': form,
        
    }
    return render(request, 'edit-profile.html', context)




# Create your views here.
