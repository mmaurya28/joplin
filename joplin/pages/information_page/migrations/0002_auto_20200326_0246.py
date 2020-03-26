# Generated by Django 2.2.11 on 2020-03-26 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200312_0925'),
        ('information_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informationpage',
            name='options',
        ),
        migrations.RemoveField(
            model_name='informationpage',
            name='options_ar',
        ),
        migrations.RemoveField(
            model_name='informationpage',
            name='options_en',
        ),
        migrations.RemoveField(
            model_name='informationpage',
            name='options_es',
        ),
        migrations.RemoveField(
            model_name='informationpage',
            name='options_vi',
        ),
        migrations.AddField(
            model_name='informationpage',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.Contact'),
        ),
        migrations.DeleteModel(
            name='InformationPageContact',
        ),
    ]
