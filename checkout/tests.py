from django.test import TestCase


class TestViews(TestCase):

    """ A test that the checkout page renders a 200 status code"""
    def test_get_checkout_page(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'checkout/checkout.html')
