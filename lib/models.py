from django.db import models


class Doc(models.Model):

    CHOICES = (
        ('pdf', 'pdf'),
        ('docx', 'docx'),
        ('doc', 'doc'),
        ('txt', 'txt'),
        ('odt', 'odt'),
        ('other', 'other'),
    )

    name = models.CharField(max_length=100, verbose_name='Имя файла')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    downloads = models.IntegerField(default=0, verbose_name='К-во загрузок')
    type = models.CharField(max_length=50, choices=CHOICES, verbose_name='Тип документа')
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='Файл')

    def __str__(self):
        return self.name

    def set_download(self):
        self.downloads += 1
        self.save()

    def get_url(self):
        return self.upload.url

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
