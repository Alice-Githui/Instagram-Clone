from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    profile_name=models.CharField(max_length=80, null=True)
    profile_photo=CloudinaryField('image')    
    bio=models.CharField(max_length=200)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Comment(models.Model):
    comment=models.CharField(max_length=500)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

class Image(models.Model):
    image=CloudinaryField('image')
    image_name=models.CharField(max_length=80)
    caption=models.TextField()
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    comments=models.ForeignKey(Comment, on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return self.caption

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


