from django.db import models

# Create your models here.

class image(models.Model):
    image= models.ImageField(blank=True, null=True)
    image_name= models.TextField(max_length=70)
    image_caption= models.TextField(max_length=150)
    profile= models.ForeignKey('auth.user',on_delete=models.CASCADE)
    comments= models.TextField(max_length=150)
     # likes=

    def __str__(self):
        return self.caption