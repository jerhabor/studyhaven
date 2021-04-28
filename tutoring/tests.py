from django.test import TestCase


class TestTutoringViews(TestCase):

    """ A test that the Tutoring page renders a 200 status code"""
    def test_get_tutoring_page(self):
        response = self.client.get('/tutoring/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'tutoring/tutoring.html')
