from django.urls import path

from .views import Home, done


urlpatterns = [
    path('', Home.as_view(), name='home'),  # класс Home для вывода всех файлов на главной странице '/'
    path('done/<int:pk>', done, name='done'),  # функция done для получения определенного файла, пример: /done/3
]