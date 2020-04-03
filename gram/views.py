from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.urls import include, path
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import image, Profile, Comment
from . import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,ProfileForm,ImageForms,CommentForm

# Create your views here.
# @login_required(login_url='login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = User
            profile.save()
    else:
        form=ProfileForm()
        
    return render(request, 'concept/new_profile.html', locals())

# @login_required(login_url='login/')
def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForms(request.POST, request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            return redirect('welcome')
    else:
        form = ImageForms()


    return render(request,'concept/image.html',locals())

# @login_required(login_url='login/')
def home(request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    profile = Profile.objects.all()
    images = image.objects.filter(profile__id=current_user.id)
    print(likes)
    return render(request,'welcome.html', {'user':current_user, 'images':all-images, 'comments':comments, 'likes':likes})

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

# @login_required(login_url='login')
def upload_form(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(request, 'upload_image.html', {'form': form})

# @login_required(login_url='login/')
def display_profile(request, id):
    seekuser=User.objects.filter(id=id).first()
    profile = seekuser.profile
    profile_details = Profile.get_by_id(id)
    images = Image.get_profile_images(id)

    usersss = User.objects.get(id=id)
    people=User.objects.all()
  

    return render(request,'concept/profile.html',locals())

# @login_required(login_url='login/')
def welcome(request):
    images= image.objects.all()
    return render(request, 'welcome.html',{"images":images})

# @login_required(login_url='login/')
def comment(request,image_id):
    current_user=request.user
    image = Image.objects.get(pk=image_id)
    profile_owner = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.comment_owner = current_user
            comment.save()

            print(comments)


        return redirect('welcome')

    else:
        form = CommentForm()

    return render(request, 'comment.html', context())

def follow(request,user_id):
    users=User.objects.get(id=user_id)

    return redirect('profile/', locals())


def likes(request, image_id):
    def likes(request, post_id):
        image = Image.objects.get(pk=post_id)
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        is_liked = False
    else:
        image.likes.add(request.user)
        is_liked = True

    return redirect('welcome')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('welcome')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})