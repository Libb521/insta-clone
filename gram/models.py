from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='images')
    profile_avatar = models.ImageField(upload_to='images')
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
    def update_profile_picture(cls, owner):
        cls.objects.filter(id=id).update(image=image)
        updated_profile_picture =cls.objects.get(id=id)
        return updates_profile_pic

# Create Profile when creating a User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save Profile when saving a User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save

class image(models.Model):
    image= models.ImageField(blank=True, null=True)
    image_name= models.CharField(max_length=50)
    image_caption= models.CharField(max_length=100)
    tag_someone = models.CharField(max_length=50, blank=True)
    profile= models.ForeignKey('auth.user',on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    
    def __str__(self):
        return self.image_caption

    def save_image(self):
        self.save()

    def delete_image(self):
        delete.image()

    def addlikes(self):
        self.likes.count()

    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        for image in all_images:
            return images
    
    @classmethod
    def update_image(cls,current,new):
        to_update = Image.objects.filter(image_name=current).update(image_name=new)
        return to_update
    @classmethod
    def get_image_by_id(cls,id):
        image_result = cls.objects.get(id=id)
        return image_result

class Comment(models.Model):
    image =  models.ForeignKey(image, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    comment = models.CharField(max_length=150)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        delete.comment()

class Follow(models.Model):
    user = models.CharField(max_length=15)
    follower = models.CharField(max_length=15)
    following = models.CharField(max_length=15)