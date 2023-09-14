from django.test import SimpleTestCase
from django.urls import resolve, reverse
from produit.views import produit
class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('home')
        #self.assertEquals(resolve(url).func, produit)