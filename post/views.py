from django.shortcuts import render
from post.models import Tag, Stream, Follow, Post
from django.contrib.auth.decorators import login_required

def index(request):
    user = request.user
    # # user = request.user
    # all_users = User.objects.all()
    # follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

    # profile = Profile.objects.all()

    posts = Stream.objects.filter(user=user)
    group_ids = []
    for post in posts:
        group_ids.append(post.post_id)
        
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    context = {
           'post_items': post_items
      }



    return render(request, 'index.html', context)


# Create your views here.
