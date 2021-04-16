from django.test import TestCase
from .models import Category, Product


class TestViews(TestCase):

    """ A test that the products page renders a 200 status code"""
    def test_get_products_page(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/products.html')
