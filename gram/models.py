from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class image(models.Model):
    image= models.ImageField(blank=True, null=True)
    image_name= models.CharField(max_length=50)
    image_caption= models.CharField(max_length=100)
    profile= models.ForeignKey('auth.user',on_delete=models.CASCADE)
    
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
    class Meta:

        ordering = ['bio']

    def profile_save(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_username(cls, owner):
        profiles = cls.object.filter(owner_contains=owner)
        return profiles

class Comment(models.Model):
    image =  models.ForeignKey(image, blank=True, on_delete=models.CASCADE, related_name='comment')
    commenter = models.CharField(max_length=100)
    comment = models.TextField()

    def save_comment(self):
        self.save()

    def delete_comment(self):
        delete.comment()
    @classmethod
    def get_profile_comments(cls, profile):
        comments = comment.objects.filter(image_pk=id)
        return comments
    def __str__(self):
        return str(str.comment)

class Likes(models.Model):
    likes = models.PositiveIntegerField('Likes', blank=False, default=0)
    image =  models.ForeignKey(image, blank=True, on_delete=models.CASCADE, related_name='likes') 
