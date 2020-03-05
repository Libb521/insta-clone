from django.db import models

# Create your models here.

class image(models.Model):
    image= models.ImageField(blank=True, null=True)
    image-name= models.TextField(max_length=70)
    image-caption= models.TextField(max_length=150)
    profile= models.ForeignKey('auth.user',on_delete=models.CASCADE)
    # likes=
    # comments=
