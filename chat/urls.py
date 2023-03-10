from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create',views.create, name='create'),
    path('auth', views.authentication, name='auth'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('check_username', views.check_username, name='check_username'),
    path('check_email', views.check_email, name='check_email'),
    path('send', views.send, name='send'),
    path("getMessages/<str:room1>/",views.getMessages, name='room'),
    path("<str:room1>/",views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    
]
