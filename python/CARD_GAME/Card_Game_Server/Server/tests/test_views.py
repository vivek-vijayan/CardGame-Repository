from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import homepage


class TestCase(SimpleTestCase):
    def test_list(self):
        url = reverse('gameplay', args=['1'])
        self.assertEqual(resolve(url).func, homepage)
