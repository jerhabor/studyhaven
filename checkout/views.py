from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages

from .forms import CheckoutOrderForm
from .models import Order, EachLineOrder
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cached_checkout_info(request):
    try:
        """ First part of split of the payment intent client_secret
        at '_secret' will be the Payment Intent ID. """
        pi_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pi_id, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_contact': request.POST.get('save_contact'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, unable to process your order at this time. \
            Please try again later.')
        return HttpResponse(content=e, status=400)


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
            # Prevent multiple save events by disallowing the first one
            order = checkout_order_form.save(commit=False)
            pi_id = request.POST.get('client_secret').split('_secret')[0]
            order.original_bag = json.dumps(shopping_bag)
            order.stripe_pi_id = pi_id
            order.save()
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
                        "We were unable to find one of the products in your bag. \
                            Please contact us for assistance!")
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
            messages.error(
                request, "You have not added an item to your bag yet!")
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

        """ A conditional statement to handle prefilling the form
        with the contact details that the user updated from their
        user profile. """
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                checkout_order_form = CheckoutOrderForm(initial={
                    'full_name': user_profile.default_full_name,
                    'email_address': user_profile.default_email_address,
                    'phone_number': user_profile.default_phone_number,
                    'country': user_profile.default_country,
                    'postcode': user_profile.default_postcode,
                    'city_or_town': user_profile.default_city_or_town,
                    'address_line1': user_profile.default_address_line1,
                    'address_line2': user_profile.default_address_line2,
                })
            except UserProfile.DoesNotExist:
                checkout_order_form = CheckoutOrderForm()
        else:
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

    if request.user.is_authenticated:
        # Render the customer's profile as they make an order
        profile_user = UserProfile.objects.get(user=request.user)
        order.user_profile = profile_user
        order.save()

        # Saving the customers detail if they checked the box
        if save_contact:
            profile_details = {
                'default_full_name': order.full_name,
                'default_email_address': order.email_address,
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_address_line1': order.address_line1,
                'default_address_line2': order.address_line2,
                'default_city_or_town': order.city_or_town,
                'default_postcode': order.postcode,
            }
            user_profile_form = UserProfileForm(
                profile_details, instance=profile_user)
            # Save to customer's profile only if their form inputs are valid
            if user_profile_form.is_valid():
                user_profile_form.save()

    # Send a success toast message on the UI that the purchase was successful
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
