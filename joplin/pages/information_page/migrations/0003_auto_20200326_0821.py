# Generated by Django 2.2.11 on 2020-03-26 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information_page', '0002_auto_20200326_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationpage',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='contact.Contact'),
        ),
    ]
