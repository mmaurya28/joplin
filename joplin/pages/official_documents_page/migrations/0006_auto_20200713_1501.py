# Generated by Django 2.2.13 on 2020-07-13 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('topic_page', '0001_initial'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('official_documents_page', '0005_auto_20200709_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officialdocumentpageold',
            name='janisbasepagewithtopics_ptr',
        ),
        migrations.DeleteModel(
            name='OfficialDocumentPageDocument',
        ),
        migrations.DeleteModel(
            name='OfficialDocumentPageOld',
        ),
    ]