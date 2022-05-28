from contextlib import redirect_stderr
import email
from urllib import request
from django.forms import PasswordInput
from django.shortcuts import render,redirect
from .models import Post,Userdetail
from django.contrib.auth.decorators import login_required
from.forms import NewCreationForm,BlogcreationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages




#  SHOWING ALL POSTS 
def home(request):
    post=Post.objects.all()
    paginator=Paginator(post,4)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    try:
        user=Userdetail.objects.get(user=request.user)
    except:
        user=None
    return render(request,"home.html",{"post":post,"user":user,"page_obj":page_obj})


# VIEW FOR SHOWING THE SELCTED POST
@login_required(login_url='/login')
def Post_details(request,pk):
    detail_post=Post.objects.get(id=pk)
    user=Userdetail.objects.get(user=request.user)
    return render(request,'details.html',{"details":detail_post,"user":user})



# registration 
def registration(request):
    if request.method=='POST':
        form=NewCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data["username"]
            messages.success(request, user+  "is created succesfully")
            return redirect(loginview)
        else:
            messages.error(request,"Email or Password is incorrect")
            messages.error(request,"Password must contain atleast 8 character and cant be similar to username")

    else:
        form=NewCreationForm()
    return render(request,'registration.html',{'form':form})
    
      

# LOGIN VIEW
def loginview(requests):
    if requests.method=='POST':
        username=requests.POST.get('username')
        password=requests.POST.get('password')
        email=requests.POST.get('email')
        user= authenticate(requests,username=username,password=password)
        if user is not None:
            login(requests,user)
            return redirect(home)
        else:
            messages.error(requests,"Enter correct Email and password")
            return render(requests,"login.html")
    else:
        return render(requests,'login.html')

#logout the user
def logoutview(request):
    logout(request)
    return redirect(loginview)

#create new Post
@login_required(login_url='/login')
def Create_post(request):
    if request.method=='POST':
        form=BlogcreationForm(request.POST,request.FILES)
        if form.is_valid():
            title=form.cleaned_data["Title"]
            image=form.cleaned_data["Image"] 
            Content=form.cleaned_data["content"]
            Post.objects.create(author=request.user,Title=title,Image=image,content=Content)
            return redirect(home)
    else:
        form=BlogcreationForm()
        return render(request,"blog-create.html",{"forms":form})

@login_required(login_url='/login')
def Update_post(request,slug):
    object=Post.objects.get(slug=slug)
    if object.author!=request.user:
        return redirect(home)
    else:
        form=BlogcreationForm(instance=object)
        if request.method=='POST':
            form=BlogcreationForm(request.POST,request.FILES,instance=object)
            if form.is_valid():
                form.save()
                return redirect(home)
        else:
            return render(request,"blog-update.html",{"form":form})

@login_required(login_url='/login') 
def Delete_post(request,pk):
    object=Post.objects.get(id=pk)
    if object.author!=request.user:
        return redirect(home)
    else:
        if request.method=='POST':
            object.delete()
            return redirect(home)
        else:
            return render(request,"blog-delete.html")    
    
@login_required(login_url='/login')
def user_detail(request):
    user=Userdetail.objects.get(user=request.user)
    userpost=Post.objects.filter(author=request.user)
    return render(request,"user-details.html",{"user":user,"userpost":userpost})


