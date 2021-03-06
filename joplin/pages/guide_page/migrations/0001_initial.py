# Generated by Django 2.2.12 on 2020-04-10 10:54

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0002_contact_location_page'),
        ('base', '0001_initial'),
        ('topic_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuidePage',
            fields=[
                ('janisbasepagewithtopics_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='topic_page.JanisBasePageWithTopics')),
                ('description', models.TextField(blank=True, verbose_name='Write a description of the guide')),
                ('description_ar', models.TextField(blank=True, null=True, verbose_name='Write a description of the guide')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Write a description of the guide')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Write a description of the guide')),
                ('description_vi', models.TextField(blank=True, null=True, verbose_name='Write a description of the guide')),
                ('sections', wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StructBlock([('section_heading_en', wagtail.core.blocks.TextBlock(label='Heading [en]')), ('section_heading_es', wagtail.core.blocks.TextBlock(label='Heading [es]', required=False)), ('section_heading_ar', wagtail.core.blocks.TextBlock(label='Heading [ar]', required=False)), ('section_heading_vi', wagtail.core.blocks.TextBlock(label='Heading [vi]', required=False)), ('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(label='Page', page_type=['information_page.InformationPage', 'service_page.ServicePage']), help_text='Select existing pages in the order you want them                         to display within each heading.                        Pages should be added only once to any single guide.'))], label='Section'))], blank=True, verbose_name='Add a section header and pages to each section')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='contact.Contact')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.TranslatedImage')),
            ],
            options={
                'abstract': False,
            },
            bases=('topic_page.janisbasepagewithtopics',),
        ),
    ]
