# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 21:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kerkdiensten', '0008_auto_20161202_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kerkdiensten',
            name='beschikbaar',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
