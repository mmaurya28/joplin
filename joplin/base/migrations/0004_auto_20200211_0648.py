# Generated by Django 2.2.9 on 2020-02-11 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20200107_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departmentcontact',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='departmentcontact',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='DepartmentContact',
        ),
    ]
