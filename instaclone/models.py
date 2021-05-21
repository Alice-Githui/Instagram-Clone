from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    profile_name=models.CharField(max_length=80, null=True)
    profile_photo=CloudinaryField('image')    
    bio=models.CharField(max_length=200)

    def __str__(self):
        return self.bio

class Comment(models.Model):
    comment=models.CharField(max_length=500)

    def __str__(self):
        return self.comment

class Image(models.Model):
    image=CloudinaryField('image')
    image_name=models.CharField(max_length=80)
    caption=models.TextField()
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    comments=models.ForeignKey(Comment, on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return self.caption


