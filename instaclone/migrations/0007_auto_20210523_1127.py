# Generated by Django 3.2.3 on 2021-05-23 08:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instaclone', '0006_imagelikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(related_name='image_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
