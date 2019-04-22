# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-08 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demos', '0004_auto_20180502_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='demonstration',
            name='form_link',
            field=models.URLField(blank=True),
        ),
        migrations.RemoveField(
            model_name='demonstration',
            name='courses',
        ),
        migrations.AddField(
            model_name='demonstration',
            name='courses',
            field=models.CharField(default='SAMPLE COURSE', max_length=150),
            preserve_default=False,
        ),
    ]
