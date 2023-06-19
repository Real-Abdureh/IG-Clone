from directs.views import inbox, Directs, SendDirect, UserSearch, NewMessage
from django.urls import path


urlpatterns = [
    path('', inbox, name="message"),
    path('direct/<username>', Directs, name="directs"),
    path('send/', SendDirect, name="send-message"),
    path('new/', UserSearch, name="user-search"),
    path('new<username>/', NewMessage, name="new-message"),
    
]



# from directs.views import inbox, Directs, SendMessage
# from django.urls import path

# urlpatterns = [
#     path('inbox/', inbox, name="inbox"),
#     path('direct/<username>', Directs, name="directs"),
#     path('send/', SendMessage, name="send-message"),

# ]