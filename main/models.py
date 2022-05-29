
from contextlib import nullcontext
from email.mime import image
from email.policy import default
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.forms import SlugField
from .helper import *
from froala_editor.fields import FroalaField
#MODEL FOR THE BLOG POST

class Post(models.Model):
    Image=models.ImageField(upload_to='uploads',blank=True,default="images/5353134.png")
    Title= models.CharField(max_length=100)
    content=FroalaField( theme='dark',blank=True,null=True)
    slug=models.SlugField(null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-updated_at",]

    def __str__(self):
        return self.Title

    def save(self,*args,**kwargs) :
        self.slug=generate_slug(self.Title)
        super(Post,self).save(*args,**kwargs)

class Userdetail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
