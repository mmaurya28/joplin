# Generated by Django 2.2.10 on 2020-03-13 19:17

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_merge_20200212_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidepage',
            name='sections',
            field=wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StructBlock([('section_heading_en', wagtail.core.blocks.TextBlock(label='Heading [en]')), ('section_heading_es', wagtail.core.blocks.TextBlock(label='Heading [es]', required=False)), ('section_heading_ar', wagtail.core.blocks.TextBlock(label='Heading [ar]', required=False)), ('section_heading_vi', wagtail.core.blocks.TextBlock(label='Heading [vi]', required=False)), ('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(label='Page', page_type=['base.InformationPage', 'base.ServicePage']), help_text='Select existing pages in the order you want them                         to display within each heading.                        Pages should be added only once to any single guide.'))], label='Section'))], blank=True, verbose_name='Add a section header and pages to each section'),
        ),
    ]