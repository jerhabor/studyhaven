from django.test import TestCase


class TestBagViews(TestCase):

    """ A test that the shopping bag page renders a 200 status code"""
    def test_get_shopping_bag_page(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'bag/bag.html')
