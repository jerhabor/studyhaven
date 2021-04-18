from django.test import TestCase


class TestViews(TestCase):

    """ A test that the home page renders a 200 status code"""
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'home/index.html')
