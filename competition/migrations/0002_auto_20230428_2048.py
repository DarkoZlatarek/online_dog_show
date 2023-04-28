# Generated by Django 3.2.18 on 2023-04-28 20:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enter',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='enter',
            name='excerpt',
        ),
        migrations.AlterField(
            model_name='enter',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]