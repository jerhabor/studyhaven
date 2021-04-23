from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages

from .forms import CheckoutOrderForm
from .models import Order, EachLineOrder
from products.models import Product
from bag.contexts import bag_contents

import stripe


def checkout_order(request):
    """ A view to handle the ability to process an order
    with Stripe's built-in functionality """
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'city_or_town': request.POST['city_or_town'],
            'postcode': request.POST['postcode'],
        }
        checkout_order_form = CheckoutOrderForm(form_data)
        if checkout_order_form.is_valid():
            order = checkout_order_form.save()
            for product_id, product_data in shopping_bag.items():
                try:
                    product = Product.objects.get(id=product_id)
                    each_line_order = EachLineOrder(
                        order=order,
                        product=product,
                        quantity=product_data,
                    )
                    each_line_order.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "We were unable to find one of the products in your bag."
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_shopping_bag'))
            request.session['save_contact'] = 'save-contact' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'Error processing your order. \
                Please recheck the information you have provided.')

    else:
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
        print(stripePaymentIntent)  # REMOVE
        checkout_order_form = CheckoutOrderForm()

    # Incase no Stripe publishable key is in environment
    if not stripe_publishable_key:
        messages.warning(
            request, 'No Stripe Publishable Key was detected \
                in your environment variables')

    template = 'checkout/checkout.html'
    context = {
        'form': checkout_order_form,
        'stripe_publishable_key': stripe_publishable_key,
        'client_secret_key': stripePaymentIntent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ A view to handle the page shown after successful
    order attempt """
    save_contact = request.session.get('save_contact')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order has been processed! \
        Here is your order number: {order_number}. A confirmation \
        email will be sent to {order.email_address} shortly.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
