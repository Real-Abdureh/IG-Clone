from django.shortcuts import render, redirect, get_object_or_404
from post.models import Tag, Stream, Follow, Post
from .forms import NewPostForm
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

def NewPost(request):
    user = request.user.id
    tags_objs = []

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tag_form = form.cleaned_data.get('tag')
            tags_list = list(tag_form.split(',')) # tags will be separated by a comma

            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title = tag)
                tags_objs.append(t)
            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user_id=user)
            p.tag.set(tags_objs)
            p.save()
            return redirect('index')
        
    else:
        form = NewPostForm()
    context = {
    'form': form
    }
    return render(request, 'newpost.html', context)

def PostDetail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post
            }

    return render(request, 'post-detail.html')



# Create your views here.
