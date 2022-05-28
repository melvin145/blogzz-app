from venv import create
from django.urls import path

from api.views import Post_api, Posts_api, getroutes


urlpatterns=[
    path("",getroutes,name="getroutes"),
    path("posts",Posts_api,name="posts"),
    path("posts/<int:pk>/",Post_api,name="postapi"),
    ]