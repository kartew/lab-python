from django.contrib import admin
from .models import Doc


# кастомизируем админскую панель: prepopulated_fields для автоматической подстановки url
# list_display для отображаемой информации в списке экземпляров модели
class DocAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'type', 'downloads']


# регистрируем модель Doc и класс DocAdmin в админке
admin.site.register(Doc, DocAdmin)
