# Generated by Django 2.2.9 on 2020-01-23 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20200123_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='event_is_free',
            field=models.BooleanField(default=False, verbose_name='This event is free'),
        ),
    ]
