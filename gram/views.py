from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import authenticate, login, logout
# from .forms import PostForm
from .models import image, Profile, Comment
from . import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


# Create your views here.
def profile(request):
    current_user = request.current_user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = current_user
            profile.save()
    else:
        form=ProfileForm()
    return render(request, 'concept/new.html', locals())

def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('home')
    else:
        form = ImageForm()


    return render(request,'concept/image.html',locals())

def home(request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    profile = Profile.objects.all()
    print(likes)
    return render(request,'home.html',locals())

def search(request):
    profiles = User.objects.all()

    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        results = User.objects.filter(username__icontains=search_term)
        print(results)

        return render(request,'concept/search.html',locals())

    else:
        message = "Have not found what you are looking for"
        return render(request, 'concept/search.html', {"message":message})

def display_profile(request, id):
    seekuser=User.objects.filter(id=id).first()
    profile = seekuser.profile
    profile_details = Profile.get_by_id(id)
    images = Image.get_profile_images(id)

    usersss = User.objects.get(id=id)
    people=User.objects.all()
  

    return render(request,'concept/profile.html',locals())

def welcome(request):
    images= image.objects.all()
    return render(request, 'welcome.html',{"images":images})
