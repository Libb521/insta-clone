from django import forms
from .models import Profile, image, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['User']

class ImageForms(forms.ModelForm):
    class Meta:
        model = image
        exclude = ['profile',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image']

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
