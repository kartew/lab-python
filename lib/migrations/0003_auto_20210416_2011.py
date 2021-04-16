# Generated by Django 3.2 on 2021-04-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0002_alter_doc_downloads'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='slug',
            field=models.SlugField(default=9, max_length=100, unique=True, verbose_name='Url'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doc',
            name='downloads',
            field=models.IntegerField(default=0),
        ),
    ]
