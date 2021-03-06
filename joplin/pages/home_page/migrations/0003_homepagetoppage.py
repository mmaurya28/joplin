# Generated by Django 2.2.16 on 2020-10-02 20:21

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('home_page', '0002_remove_default_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageTopPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('department', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_pages', to='home_page.HomePage')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page', verbose_name='Select a page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
