from directs.views import inbox, Directs, SendMessage
from django.urls import path


urlpatterns = [
    path('', inbox, name="message"),
    path('direct/<username>', Directs, name="directs"),
    path('send/', SendMessage, name="send-message"),
#     path('search/', UserSearch, name="search-users"),
#     path('new/<username>', NewConversation, name="conversation"),
]





# from directs.views import inbox, Directs, SendMessage
# from django.urls import path

# urlpatterns = [
#     path('inbox/', inbox, name="inbox"),
#     path('direct/<username>', Directs, name="directs"),
#     path('send/', SendMessage, name="send-message"),

# ]