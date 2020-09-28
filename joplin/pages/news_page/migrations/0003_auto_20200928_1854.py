# Generated by Django 2.2.16 on 2020-09-28 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_page', '0002_auto_20200508_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='written_for_department',
            field=models.ForeignKey(blank=True, help_text="If this news article is written for another department, select that department below. This ensures that this news article is associated with that department's news content", null=True, on_delete=django.db.models.deletion.SET_NULL, to='department_page.DepartmentPage', verbose_name='Assign a different department'),
        ),
    ]
