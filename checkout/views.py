from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages

from .forms import checkoutOrderForm
from bag.contexts import bag_contents

import stripe


def checkoutOrder(request):
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You have not added an item to your bag yet!")
        return redirect(reverse('shop'))

    user_bag = bag_contents(request)
    total_price = user_bag['grand_total']
    # Stripe works with whole numbers so it's easier to convert to pence
    stripe_charge = round(total_price*100)
    stripe.api_key = stripe_secret_key
    stripePaymentIntent = stripe.PaymentIntent.create(
        amount=stripe_charge,
        currency=settings.STRIPE_CURRENCY,
    )

    print(stripePaymentIntent)

    # Incase developer has forgotten to set Stripe publishable key in enviroment
    if not stripe_publishable_key:
        messages.warning(request, 'No Stripe Publishable Key was detected in your environment variables')

    checkout_order_form = checkoutOrderForm()
    template = 'checkout/checkout.html'
    context = {
        'form': checkout_order_form,
        'stripe_publishable_key': stripe_publishable_key,
        'client_secret_key': stripePaymentIntent.client_secret,
    }

    return render(request, template, context)
