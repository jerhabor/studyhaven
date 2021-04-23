
from django.http import HttpResponse


class StripeWebhookHandler:
    """ Functions to handle all of StudyHaven's required
    Stripe webhooks """

    def __init__(self, request):
        """
        A setup method anytime an instance of the class
        StripeWebhookHandler is created.
        """
        self.request = request

    def handle_event(self, event):
        """
        Function to handle any unknown or unexpected event
        which could occur on either the site server's side or
        the customer's side.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
