# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-27 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_topic_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='topics', to='base.Theme'),
        ),
    ]