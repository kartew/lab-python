from django.shortcuts import redirect

from django.views.generic import ListView

from .models import Doc


class Home(ListView):
    model = Doc
    template_name = 'index.html'
    context_object_name = 'docs'


def done(request, pk):
    maintenance = Doc.objects.get(pk=pk)
    maintenance.set_download()
    return redirect(maintenance.get_url())
