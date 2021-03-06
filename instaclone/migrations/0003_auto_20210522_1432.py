# Generated by Django 3.2.3 on 2021-05-22 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instaclone', '0002_profile_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
