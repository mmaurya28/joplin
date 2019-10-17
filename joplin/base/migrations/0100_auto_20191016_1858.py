# Generated by Django 2.2.5 on 2019-10-16 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0099_auto_20191016_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='janisbranchsettings',
            name='preview_options',
        ),
        migrations.AddField(
            model_name='janisbranchsettings',
            name='preview_input',
            field=models.CharField(choices=[('1', 'Url'), ('2', 'Branch Name')], default='Url', max_length=11, verbose_name='Preview Input Options'),
        ),
        migrations.AddField(
            model_name='janisbranchsettings',
            name='preview_janis_url',
            field=models.TextField(blank=True, help_text='Url of deployed Janis branch to preview pages. Ex: "https://janis.austintexas.io", "localhost:3000" (Don\'t add quotes)', null=True, verbose_name='Preview Janis URL'),
        ),
        migrations.AlterField(
            model_name='janisbranchsettings',
            name='preview_janis_branch',
            field=models.TextField(blank=True, help_text='Name of Janis branch to preview pages. Ex: "3000-my-issue-name" (Don\'t add quotes)', null=True, verbose_name='Preview Janis Branch Name'),
        ),
    ]
