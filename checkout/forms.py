from django import forms
from .models import Order


class CheckoutOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email_address',
                  'phone_number', 'country', 'address_line1',
                  'address_line2', 'city_or_town', 'postcode',)

    def __init__(self, *args, **kwargs):
        # Taken from Code Institute Boutique Ado
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        form_input_placeholders = {
            'full_name': 'Full Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'city_or_town': 'Town/City',
            'postcode': 'Postal Code',
        }

        # Cursor to start on Full Name input field when page loads
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # Custom CSS Django Styling
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{form_input_placeholders[field]} *'
            else:
                placeholder = form_input_placeholders[field]

            """ Assigning above styles to the values in the
            form_input_placeholders dictionary above."""
            self.fields[field].widget.attrs[
                'placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
