# Generated by Django 2.2.10 on 2020-03-06 11:41

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('official_documents_page', '0001_initial'),
        ('topic_page', '0001_initial'),
        ('wagtaildocs', '0010_document_file_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='officialdocumentpagetopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='topic_page.TopicPage', verbose_name='Select a Topic'),
        ),
        migrations.AddField(
            model_name='officialdocumentpageofficialdocument',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AddField(
            model_name='officialdocumentpageofficialdocument',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='official_documents', to='official_documents_page.OfficialDocumentPage'),
        ),
        migrations.AddIndex(
            model_name='officialdocumentpageofficialdocument',
            index=models.Index(fields=['-date'], name='official_do_date_49ad87_idx'),
        ),
    ]
