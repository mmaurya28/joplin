# Generated by Django 2.2.14 on 2020-08-07 18:37

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('official_documents_collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officialdocumentcollection',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='officialdocumentcollection',
            name='description_ar',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='officialdocumentcollection',
            name='description_en',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='officialdocumentcollection',
            name='description_es',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='officialdocumentcollection',
            name='description_vi',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
