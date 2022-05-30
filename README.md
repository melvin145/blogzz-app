
<img width="1240" alt="Screenshot 2022-05-30 143639" src="https://user-images.githubusercontent.com/83630577/170958461-486f5d23-a25e-4715-abdf-119b9c899ba1.png">


# Blogzz-app

  blogzz-app is an blog-application developed using python web framework Django 4.0.2
  
  where users can create,update and delete their blog also read blogs writen by others users
  
## Maintainer

   1. Melvin mathai https://github.com/melvin145

## How it Works ?

  User can create their own blog when they are logined.By clicking the create button an form for creating the post will appears.
  user need  to enter the title,content and image for creating their blog post.User can delete and update their post whenever needed
  Userprofile contains the list posts created by the user
  
## WEBSITE LINK

   https://blogzzz-app.herokuapp.com/
  

## Technologies and Libraries used

  cloudinary==1.29.0(for storing useruploaded images )
  
  dj3-cloudinary-storage==0.0.6
  
  Django==4.0.2
  
  django-cors-headers==3.12.0
  
  django-froala-editor==4.0.10(froala editor to editing content of the blog)
  
  django-heroku==0.3.1
  
  djangorestframework==3.13.1
  
  Pillow==9.1.0
  
  whitenoise==6.0.0

## How to configure

1.)Clone the repository

    git clone https://github.com/melvin145/blogzz-app

2.)Create your own virtual environment

     pip install virtualenvwrapper-win
  
     mkvirtualenv Name
  
     workon Name
  
3.)Install your requirements
  
    pip install -r requirements.txt
  
4.)Generate a new SECRET_KEY

    Djecrety to generate secure secret_key https://djecrety.ir/
  
     in settings.py add
      SECRET_KEY=your secret key
  
5.)configure cloudinary for storing images
  
   In settings.py add
  
    CLOUDINARY_STORAGE = {
     'CLOUD_NAME':your cloud name,
     'API_KEY':api key,
     'API_SECRET': api secret,
    }
  
## How to Run

  1.) Make your migrations
  
    python manage.py makemigrations
  
    python manage.py migrate
  
  2.)Create an superuser
  
     python manage.py createsuperuser
    
  3.)Run django server
  
      python manage.py runserver
  

## Improvements Required

  1)Add  rest api for creating,deleting and updating the post
  2)Add restapi for user registration
  3)connect postgresql or mysql 
