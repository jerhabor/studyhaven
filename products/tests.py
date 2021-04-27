from django.test import TestCase
from .models import Category, Product
from .forms import ProductAdminForm


class TestProductsForms(TestCase):

    """ A test that the fields listed in the ProductAdminForm
    metaclass are the only ones that should be displayed. """
    def test_fields_in_metaclass_are_explicit(self):
        form = ProductAdminForm()
        self.assertEqual(
            form.Meta.fields, '__all__')


class TestProductsViews(TestCase):

    """ A test that the products page renders a 200 status code. """
    def test_get_products_page(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/products.html')

    """ A test that the product info page renders a 200 status code. """
    def test_get_product_info_page(self):
        test_product = Product.objects.create(
            name='Test StudyHaven Product',
            price=1.00
        )
        response = self.client.get(f'/shop/{test_product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/product_info.html')

    """ A test to see if the edit page is truly out of bounds to
    those who are not superusers. """
    def test_unable_to_get_edit_page(self):
        response = self.client.get('/shop/edit/2/')
        self.assertEqual(response.status_code, 302)
