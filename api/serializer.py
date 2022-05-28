from pyexpat import model
from rest_framework import serializers
from main.models import *

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"