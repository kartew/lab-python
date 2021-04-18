from django.shortcuts import redirect

from django.views.generic import ListView

from .models import Doc


class Home(ListView):
    # используем модель Doc
    model = Doc
    # подклбчаем шаблон
    template_name = 'index.html'
    # alias для объекта модели в шаблоне
    context_object_name = 'docs'


def done(request, pk):
    # получаем обхект по primary key из строки URL
    maintenance = Doc.objects.get(pk=pk)
    # увеличиваем счетчик скачиваний у полученного объекта
    maintenance.set_download()
    # перенаправляем пользователся на скачивание файла
    return redirect(maintenance.get_url())
