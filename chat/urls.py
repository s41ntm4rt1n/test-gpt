from django.urls import path, include
from .views import ChatDetailView, ChatListView

from . import views
app_name='chat'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('chat/', ChatListView.as_view(), name='index'),
    path('chat/<slug:chat_slug>', ChatDetailView.as_view(), name='chat'),
    path('chat/<slug:chat_slug>/delete/', views.delete_chat, name='delete_chat'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('send_message/<slug:chat_slug>/', views.send_message, name='send_message'),
    path('new_chat/', views.new_chat, name='new_chat'),#
    path('save_api_key/<slug:chat_slug>', views.save_api_key, name='save_api_key'),
]
    