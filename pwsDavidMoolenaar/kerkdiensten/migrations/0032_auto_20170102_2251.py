# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kerkdiensten', '0031_userroll_instrument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userroll',
            name='instrument',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kerkdiensten.Instrumenten'),
        ),
    ]
