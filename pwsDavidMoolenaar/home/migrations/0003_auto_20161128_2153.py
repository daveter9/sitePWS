# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 20:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_images_image_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'images'},
        ),
    ]