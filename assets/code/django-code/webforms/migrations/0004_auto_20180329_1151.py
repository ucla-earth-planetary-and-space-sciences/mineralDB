# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-29 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webforms', '0003_auto_20180328_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webform',
            name='affiliation',
            field=models.CharField(help_text='<em>* required</em>', max_length=150),
        ),
        migrations.AlterField(
            model_name='webform',
            name='request_body',
            field=models.TextField(help_text='<em>* required</em>', max_length=2000),
        ),
    ]
