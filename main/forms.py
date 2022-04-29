from dataclasses import fields
from distutils.command.upload import upload
import email
from pyexpat import model
#from tkinter import Image, Widget
#from turtle import title
from django.contrib.auth.forms import UserCreationForm
from django import forms
from.models import Post
from froala_editor.widgets import FroalaEditor
from django.contrib.auth.models import User



class NewCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-input', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-input', 'type':' password ', 'align':'center', 'placeholder':' enter password again'}),
    )
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        widgets={
            'username':forms.TextInput(attrs={
                'class':'form-input',
                'placeholder':'Username'
            }),
             'email':forms.EmailInput(attrs={
                'class':'form-input',
                'placeholder':'Email'
            }), 
            
        }

class BlogcreationForm(forms.ModelForm):
    #content = forms.CharField(widget=CKEditorWidget())
    content = forms.CharField(widget=FroalaEditor)
    Image=forms.ImageField()
    class Meta:
        model=Post
        fields=["Title",'Image',"content"]
        widgets={
            'Title':forms.TextInput(attrs={
                'class':'author-input',
                'placeholder':'Enter the title here'
            }),}
           
      