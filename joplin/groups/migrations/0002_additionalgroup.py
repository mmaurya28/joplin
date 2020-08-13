# Generated by Django 2.2.14 on 2020-08-13 20:36

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
            ],
            options={
                'verbose_name_plural': 'NonEditorGroups',
                'ordering': ['name'],
            },
            bases=('auth.group', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
