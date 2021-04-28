from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, EachLineOrder
from products.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWebhookHandler:
    """ Functions to handle all of StudyHaven's required
    Stripe webhooks. (Inspired by Boutique Ado) """

    def __init__(self, request):
        """
        A setup method anytime an instance of the class
        StripeWebhookHandler is created.
        """
        self.request = request

    def _order_confirmation_email(self, order):
        """
        A private method to be able to send confirmation emails to the
        email address that the customer provided at the time of checking out.
        """
        customer_email = order.email_address
        email_subject = render_to_string(
            'checkout/confirmation_emails/email_subject.txt',
            {'order': order})
        email_body = render_to_string(
            'checkout/confirmation_emails/email_body.txt',
            {'order': order,
             'studyhaven_email': settings.DEFAULT_EMAIL_SENDER})
        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_EMAIL_SENDER,
            [customer_email]
        )

    def handle_generic_event(self, event):
        """
        Function to handle any unknown or unexpected event
        which could occur on either the site server's side or
        the customer's side.
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Function to handle the payment_intent.succeeded
        Stripe webhook.
        """
        intent = event.data.object  # retrieves the payment intent
        pi_id = intent.id  # get the payment intent id
        bag = intent.metadata.bag  # get the bag from metadata in the PI
        # get the save_contact Boolean
        save_contact = intent.metadata.save_contact

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Replace any empty strings in shipping details with None
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        """ Need to handle updating profile information here in the webhook
        handler in the event that the app views fail """
        user_profile = None
        user_username = intent.metadata.username
        if user_username != 'AnonymousUser':
            user_profile = UserProfile.objects.get(
                user__username=user_username)
            # Check if 'save information' box is checked
            # If so, then save to profile
            if save_contact:
                user_profile.default_full_name = shipping_details.name
                user_profile.default_email_address = billing_details.email
                user_profile.default_phone_number = shipping_details.phone
                user_profile.default_country = shipping_details.address.country
                user_profile.default_address_line1 = shipping_details.address.line1
                user_profile.default_address_line2 = shipping_details.address.line2
                user_profile.default_city_or_town = shipping_details.address.city
                user_profile.default_postcode = shipping_details.address.postal_code
                user_profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    # Use '__ixact' to find an exact case-insensitive match
                    full_name__iexact=shipping_details.name,
                    email_address__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    city_or_town__iexact=shipping_details.address.city,
                    address_line1__iexact=shipping_details.address.line1,
                    address_line2__iexact=shipping_details.address.line2,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pi_id=pi_id,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            # Send confirmation email at this point if order is in the database
            self._order_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} \
                    | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    user_profile=user_profile,
                    full_name=shipping_details.name,
                    email_address=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    city_or_town=shipping_details.address.city,
                    address_line1=shipping_details.address.line1,
                    address_line2=shipping_details.address.line2,
                    original_bag=bag,
                    stripe_pi_id=pi_id,
                )
                for product_id, product_data in json.loads(bag).items():
                    product = Product.objects.get(id=product_id)
                    order_line_item = EachLineOrder(
                        order=order,
                        product=product,
                        quantity=product_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # Send confirmation email at this point if order was created by handler
        self._order_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} \
                | SUCCESS: Order has been created in the webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Function to handle the payment_intent.payment_failed
        Stripe webhook.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
