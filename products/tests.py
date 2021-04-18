from django.test import TestCase
from .models import Category, Product


class TestViews(TestCase):

    """ A test that the products page renders a 200 status code"""
    def test_get_products_page(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/products.html')

    """ A test that the product info page renders a 200 status code"""
    def test_get_product_info_page(self):
        test_product = Product.objects.create(
            name='Test StudyHaven Product',
            price=1.00
        )
        response = self.client.get(f'/shop/{test_product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/product_info.html')
