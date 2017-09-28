# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='environment',
            name='data_base',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='environment',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='environment',
            name='project_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
