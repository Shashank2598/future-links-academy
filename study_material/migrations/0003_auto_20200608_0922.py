# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-06-08 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_material', '0002_auto_20200520_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterdetail',
            name='standard',
            field=models.PositiveSmallIntegerField(choices=[(9, b'Class 9'), (10, b'Class 10'), (11, b'Class 11'), (12, b'Class 12')]),
        ),
    ]
