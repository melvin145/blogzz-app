from os import name
from re import template
from django.urls import path
from .views import *
urlpatterns=[
    path("",home,name="Home"),
    path("<slug:slug>/",Post_details,name="Blog_details"),
    path("registration",registration,name='register'),
    path("login",loginview,name="Login"),
    path("logout",logoutview,name="logout"),
    path("blog-create",Create_post,name='blogcreate'),
    path("blog-update/<slug:slug>/",Update_post,name='update'),
    path("blog-delete/<int:pk>/",Delete_post,name='delete'),
    path("user-details",user_detail,name="userdetail"),
] 
