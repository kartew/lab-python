from django.urls import path

from .views import Home, done


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('done/<int:pk>', done, name='done'),
]