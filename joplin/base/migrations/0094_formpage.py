# Generated by Django 2.2.5 on 2019-10-18 20:19

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('base', '0093_janisbranchsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author_notes', wagtail.core.fields.RichTextField(blank=True, verbose_name='Notes for authors (Not visible on the resident facing site)')),
                ('coa_global', models.BooleanField(default=False, verbose_name='Make this a top level page')),
                ('description', models.TextField(blank=True, verbose_name='Write a description of this page')),
                ('description_ar', models.TextField(blank=True, null=True, verbose_name='Write a description of this page')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Write a description of this page')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Write a description of this page')),
                ('description_vi', models.TextField(blank=True, null=True, verbose_name='Write a description of this page')),
                ('script_tag', models.TextField(blank=True, verbose_name='Enter the script tag from Formstack')),
                ('script_tag_ar', models.TextField(blank=True, null=True, verbose_name='Enter the script tag from Formstack')),
                ('script_tag_en', models.TextField(blank=True, null=True, verbose_name='Enter the script tag from Formstack')),
                ('script_tag_es', models.TextField(blank=True, null=True, verbose_name='Enter the script tag from Formstack')),
                ('script_tag_vi', models.TextField(blank=True, null=True, verbose_name='Enter the script tag from Formstack')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
