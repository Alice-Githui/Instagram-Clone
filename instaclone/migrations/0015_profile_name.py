# Generated by Django 3.2.3 on 2021-05-23 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0014_auto_20210523_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
