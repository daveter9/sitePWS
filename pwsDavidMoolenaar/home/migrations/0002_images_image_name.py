# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image_name',
            field=models.CharField(default='ik.png', max_length=256),
            preserve_default=False,
        ),
    ]
