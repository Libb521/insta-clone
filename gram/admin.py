from django.contrib import admin
from .models import image, Profile, Comment, Likes

# Register your models here.
admin.site.register(image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Likes)