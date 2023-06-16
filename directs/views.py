from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message



@login_required
def inbox(request):
    user = request.user
    messages = Message.get_message(user=request.user)
    active_direct = None
    directs = None
    

    if messages:
        message = messages[0]
        active_directs = message['user'].username
        directs = Message.objects.filter(user=request.user, recipient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                messages['unread'] = 0
               
        
    context = {
         'directs':directs,
         'active_directs':active_directs,
        'messages':messages
        }
        
   
    return render(request, 'directs/inbox.html', context)

def Directs(request, username):
    user = request.user
    messages = Message.get_message(user=user)
    active_directs = username
    directs = Message.objects.filter(user=user, recipient__username=username)
    directs.update(is_read=True)

    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0
    
    context = {
         'directs':directs,
         'active_directs':active_directs,
        'messages':messages
        }
    
    return render(request, 'directs/directs.html', context)
        
# Create your views here.
