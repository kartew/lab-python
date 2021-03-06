# Generated by Django 3.2 on 2021-04-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0003_auto_20210416_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='downloads',
            field=models.IntegerField(default=0, verbose_name='К-во загрузок'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя файла'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='type',
            field=models.CharField(choices=[('pdf', 'PDF'), ('docx', 'Microsoft Office'), ('txt', 'Text'), ('doc', 'Microsoft Office (old)'), ('odt', 'OpenDocument')], max_length=50, verbose_name='Тип документа'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='upload',
            field=models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='Файл'),
        ),
    ]
