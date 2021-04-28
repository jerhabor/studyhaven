from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWebhookHandler

import stripe


@require_POST
@csrf_exempt
def webhook_view(request):
    """ A view for listening to Stripe Webhooks. General flow following:
    https://stripe.com/docs/payments/\
        handling-payment-events#build-your-own-webhook """
    # Setup of the Webhook permissions & verify it came from Stripe
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Obtain data from the Webhook (including the signature)
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret)
    except ValueError as e:
        # If the payload is invalid:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # If the signature verification is invalid
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Create a Stripe Webhook handler
    handler = StripeWebhookHandler(request)

    # Webhook events are matched to the functions defined in webhook_handler.py
    webhook_events = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Store the type of Webhook/event from Stripe
    event_type = event['type']

    # By default, use the generic webhook handler but if there the
    # event is stored in webhook_events, then summon its function.
    event_handler = webhook_events.get(
        event_type, handler.handle_generic_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
