from os import name
from re import template
from django.urls import path
from .views import *
urlpatterns=[
    path("",home,name="Home"),
    path("<slug:slug>/",Blog_Details,name="Blog_details"),
    path("registration",registration,name='register'),
    path("login",loginviews,name="Login"),
    path("logout",logoutview,name="logout"),
    path("blog-create",Blogcreate,name='blogcreate'),
    path("blog-update/<slug:slug>/",Blogupdate,name='update'),
    path("blog-delete/<int:pk>/",Blogdelete,name='delete'),
    path("user-details",userdetail,name="userdetail"),



] 
