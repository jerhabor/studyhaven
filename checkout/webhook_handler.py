from django.http import HttpResponse

from .models import Order, EachLineOrder
from products.models import Product

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
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
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
