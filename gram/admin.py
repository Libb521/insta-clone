from django.contrib import admin
from .models import image, Profile, Comment

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('likes',)

# Register your models here.
admin.site.register(image)
admin.site.register(Profile)
admin.site.register(Comment)