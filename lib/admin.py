from django.contrib import admin
from .models import Doc


class DocAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'type', 'downloads']


admin.site.register(Doc, DocAdmin)
