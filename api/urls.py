from django.urls import path

from api.views import Posts_api


urlpatterns=[path("",Posts_api,name="getroutes")]