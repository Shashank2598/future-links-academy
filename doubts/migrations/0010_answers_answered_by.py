# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 21:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doubts', '0009_question_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='answered_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
