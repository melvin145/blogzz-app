from pickle import GET
from turtle import title
from .serializer import *
from rest_framework.response import Response
from main.models import Post
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(["GET"])
def Posts_api(request):
    posts=Post.objects.all()
    serializer=Postserializer(posts,many=True)
    return Response(serializer.data)
    

    


