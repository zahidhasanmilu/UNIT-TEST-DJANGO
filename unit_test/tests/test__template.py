from django.test import SimpleTestCase
from django.urls import reverse


class Test__templatetest(SimpleTestCase):
    def test_index_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
