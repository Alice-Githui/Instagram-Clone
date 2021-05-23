# Generated by Django 3.2.3 on 2021-05-23 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instaclone', '0008_auto_20210523_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_photo',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=450),
        ),
    ]
