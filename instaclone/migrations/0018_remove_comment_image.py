# Generated by Django 3.2.3 on 2021-05-24 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0017_auto_20210524_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
    ]
