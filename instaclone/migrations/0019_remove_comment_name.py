# Generated by Django 3.2.3 on 2021-05-24 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0018_remove_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
