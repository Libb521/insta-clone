from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class image(models.Model):
    image= models.ImageField(blank=True, null=True)
    image_name= models.CharField(max_length=50)
    image_caption= models.CharField(max_length=100)
    profile= models.ForeignKey('auth.user',on_delete=models.CASCADE)
    likes = models.PositiveIntegerField('Likes', blank=False, default=0)
    comments= models.TextField(max_length=150)

    def __str__(self):
        return str(self.name)

    def save_image(self):
        self.save()

    def delete_image(self):
        delete.image()
    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile_pk=profile)
        return images
    

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='prof_images')
    bio = models.TextField(max_length=200)

    def __str__(self):
        return str(self.bio)

    def profile_save(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_username(cls, owner):
        profiles = cls.object.filter(owner_contains=owner)
        return profiles
    