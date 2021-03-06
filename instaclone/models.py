from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.CharField(max_length=450)
    profile_pic=CloudinaryField('image')
    following=models.ManyToManyField(User, related_name="following")
    followers=models.ManyToManyField(User, related_name="followers")

    def __str__(self):
        return str(self.user)

    def total_followers(self):
        return self.followers.count()

    def total_following(self):
        return self.following.count()


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
    profile=models.ForeignKey(User, on_delete=models.CASCADE)
    comments=models.TextField()
    likes=models.ManyToManyField(User, related_name="image_posts")
   

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.caption

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self,caption, new_caption):
        self.save(caption)

    def search_by_user(profile):
        images=Image.objects.filter(profile__username=profile)
        # print(images)
        return images


class ImageLikes(models.Model):
    image=models.ForeignKey(Image, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user



