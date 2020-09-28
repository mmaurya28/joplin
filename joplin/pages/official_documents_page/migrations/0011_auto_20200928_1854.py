# Generated by Django 2.2.16 on 2020-09-28 18:54

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('official_documents_page', '0010_merge_20200914_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officialdocumentpage',
            name='summary',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=600, verbose_name='Document summary'),
        ),
        migrations.AlterField(
            model_name='officialdocumentpage',
            name='summary_ar',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=600, null=True, verbose_name='Document summary'),
        ),
        migrations.AlterField(
            model_name='officialdocumentpage',
            name='summary_en',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=600, null=True, verbose_name='Document summary'),
        ),
        migrations.AlterField(
            model_name='officialdocumentpage',
            name='summary_es',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=600, null=True, verbose_name='Document summary'),
        ),
        migrations.AlterField(
            model_name='officialdocumentpage',
            name='summary_vi',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=600, null=True, verbose_name='Document summary'),
        ),
    ]
