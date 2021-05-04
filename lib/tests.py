from django.test import TestCase
from django.urls import reverse, resolve

from lib.views import Home


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, Home)


class DocTest(TestCase):
    fixtures = ['my_dump.json']

    def test_document_view_status_code(self):
        url = reverse('file', args=('biografiya-stivena-spilberga',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_load_file_view_redirect(self):
        url = reverse('done', args=('1',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
