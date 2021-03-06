# Generated by Django 2.2.12 on 2020-04-10 10:54

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0002_contact_location_page'),
        ('topic_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformationPage',
            fields=[
                ('janisbasepagewithtopics_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='topic_page.JanisBasePageWithTopics')),
                ('description', models.TextField(blank=True, verbose_name='Write a description of this page')),
                ('description_ar', models.TextField(blank=True, null=True, verbose_name='Write a description of this page')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Write a description of this page')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Write a description of this page')),
                ('description_vi', models.TextField(blank=True, null=True, verbose_name='Write a description of this page')),
                ('additional_content', wagtail.core.fields.RichTextField(blank=True, verbose_name='Write any additional content describing the service')),
                ('additional_content_ar', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Write any additional content describing the service')),
                ('additional_content_en', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Write any additional content describing the service')),
                ('additional_content_es', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Write any additional content describing the service')),
                ('additional_content_vi', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Write any additional content describing the service')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='contact.Contact')),
            ],
            options={
                'abstract': False,
            },
            bases=('topic_page.janisbasepagewithtopics',),
        ),
    ]
