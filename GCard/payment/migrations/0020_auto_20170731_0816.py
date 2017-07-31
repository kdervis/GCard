# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0019_auto_20170731_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='digits',
            field=models.CharField(default='bd15f13c', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='slug',
            field=models.SlugField(default='bd15f13c'),
        ),
    ]
