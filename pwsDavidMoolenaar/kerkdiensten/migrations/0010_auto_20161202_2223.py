# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 21:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kerkdiensten', '0009_auto_20161202_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kerkdiensten',
            name='beschikbaar',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
