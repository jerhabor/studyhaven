from django.http import HttpResponse


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
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Function to handle the payment_intent.payment_failed
        Stripe webhook.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
