# Generated by Django 4.2.17 on 2025-01-08 00:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_collaboraterequest_alter_about_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
