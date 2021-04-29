from django.test import TestCase


class TestBagViews(TestCase):

    """ A test that the shopping bag page renders a 200 status code"""
    def test_get_shopping_bag_page(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'bag/bag.html')

    def test_adding_to_shopping_bag(self):
        shopping_bag = {
            '1': 2
        }
        product_id = '2'
        quantity = 3
        if product_id in list(shopping_bag.keys()):
            shopping_bag[product_id] += quantity
        else:
            shopping_bag[product_id] = quantity
        self.assertEqual(shopping_bag, {
            '1': 2,
            '2': 3,
        })
