from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # Render all fields except the user field which will not change
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        form_input_placeholders = {
            'default_full_name': 'Full Name',
            'default_email_address': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_address_line1': 'Address Line 1',
            'default_address_line2': 'Address Line 2',
            'default_city_or_town': 'Town/City',
            'default_postcode': 'Zip/Postal Code',
        }

        # Cursor to start on Full Name input field when page loads
        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        # Custom CSS Django Styling
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{form_input_placeholders[field]} *'
                else:
                    placeholder = form_input_placeholders[field]

                """ Assigning above styles to the values in the
                form_input_placeholders dictionary above."""
                self.fields[field].widget.attrs[
                    'placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'class'] = 'border border-dark user-profile-form-input'
            self.fields[field].label = False
