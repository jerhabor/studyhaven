from django.test import TestCase


class TestFAQsViews(TestCase):

    """ A test that the FAQs page renders a 200 status code"""
    def test_get_faqs_page(self):
        response = self.client.get('/faqs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'faqs/faqs.html')
