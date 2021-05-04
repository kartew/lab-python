from django.db import models
from django.urls import reverse


class Doc(models.Model):
    """
    name (str) - имя файла
    slug (str) - url файла
    description (text) - описание файла
    downloads (int) - к-во скачиваний файла
    type (str) - тип файла
    upload (file) - файл документа
    """

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

    # возращать имя файла, а не  имя объекта
    def __str__(self):
        return self.name

    # для инкрементирования счетчика загрузки
    def set_download(self):
        self.downloads += 1
        self.save()

    # получение относительной ссылки на загруженный файл
    def get_url(self):
        return self.upload.url

    def get_absolute_url(self):
        return reverse('file', kwargs={'slug': self.slug})

    # отображение в админской панели
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
