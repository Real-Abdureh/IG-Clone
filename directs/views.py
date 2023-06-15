from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message



@login_required
def inbox(request):
    user = request.user
    messages = Message.get_message(user=user)
    active_directs = None
    directs = None

    if messages:
        message = messages[0]
        active_directs = message['user'].username
        directs = Message.objects.filter(user=user, recipient=message['user'])
        directs.update(is_read=True)

        for message in message:
            if messages['user'].username == active_directs:
                messages['unread'] = 0
        
        context = {
            'directs':directs,
            'active_directs':active_directs,
            'messages':messages
        }

        return render(request, 'inbox.html', context)

# Create your views here.
