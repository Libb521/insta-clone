from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class image(models.Model):
    image= models.ImageField(blank=True, null=True)
    image_name= models.TextField(max_length=50)
    image_caption= models.TextField(max_length=100)
    profile= models.ForeignKey('auth.user',on_delete=models.CASCADE)
    likes = models.PositiveIntegerField('Likes', blank=False, default=0)
    comments= models.TextField(max_length=150)
     # likes=

    def __str__(self):
        return self.caption