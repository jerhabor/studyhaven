from django.test import TestCase
from .forms import CheckoutOrderForm


class TestCheckoutForms(TestCase):

    """ A test that the fields listed in the metaclass
    are the only ones that should be displayed. """
    def test_fields_in_metaclass_are_explicit(self):
        form = CheckoutOrderForm()
        self.assertEqual(
            form.Meta.fields, ('full_name', 'email_address', 'phone_number',
                               'country', 'address_line1', 'address_line2',
                               'city_or_town', 'postcode'))

    """ A test that the full name field in the checkout
    form cannot be empty. """
    def test_full_name_is_required(self):
        form = CheckoutOrderForm({
            'full_name': '',
            'email_address': 'test@test.com',
            'phone_number': '0123456789',
            'address_line1': 'Test Address',
            'city_or_town': 'Test City',
            'postcode': 'T35T1NG',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    """ A test that the user cannot submit with entering a valid credit/debit
    card even if they enter all of the models.py form inputs. """
    def test_checkout_form_still_not_valid_without_card(self):
        form = CheckoutOrderForm({
            'full_name': 'Test',
            'email_address': 'tester@test.com',
            'phone_number': '0123456789',
            'address_line1': 'Test Address',
            'city_or_town': 'Test City',
            'postcode': 'T35T1NG',
        })
        self.assertFalse(form.is_valid())


class TestCheckoutViews(TestCase):

    """ A test that the checkout page cannot be opened if there
    are no items in the bag. """
    def test_get_checkout_page(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)
