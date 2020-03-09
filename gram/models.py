from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='images')
    profile_avatar = models.ImageField(upload_to='Apic/')
    bio = models.TextField(max_length=200)

    @classmethod
    def search_by_title(cls,search_term):
        image = cls.objects.filter(title__icontains=search_term)
        return image

    def __str__(self):
        return self.bio
        
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


class image(models.Model):
    image= models.ImageField(blank=True, null=True)
    image_name= models.CharField(max_length=50)
    image_caption= models.CharField(max_length=100)
    tag_someone = models.CharField(max_length=50, blank=True)
    profile= models.ForeignKey('auth.user',on_delete=models.CASCADE)
    likes = models.PositiveIntegerField('Likes', blank=False, default=0)
    
    def __str__(self):
        return self.image_caption

    def save_image(self):
        self.save()

    def delete_image(self):
        delete.image()
    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile_pk=profile)
        return images

class Comment(models.Model):
    commented_image =  models.ForeignKey(image, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    comment_post = models.TextField()

    def save_comment(self):
        self.save()

    def delete_comment(self):
        delete.comment()
    @classmethod
    def get_profile_comments(cls, profile):
        comments = comment.objects.filter(image_pk=profile)
        return comments
    def __str__(self):
        return self.author
