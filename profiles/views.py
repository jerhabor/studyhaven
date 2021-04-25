from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.utils import formats

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def user_profile(request):
    """ A view to display a registered user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    # Handling the posting of the form
    if request.method == 'POST':
        # Create a new instance of the form into 'profile' defined above
        form = UserProfileForm(request.POST, instance=profile)
        # Add success message if form is valid
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your contact and shipping information \
                    have been updated successfully!')

    form = UserProfileForm(instance=profile)
    order_history = profile.order_history.all()

    template = 'profiles/profile.html'
    context = {
        'on_my_profile': True,
        'form': form,
        'order_history': order_history,
    }

    return render(request, template, context)


def order_history_table(request, order_number):
    # Get the order model first
    order = get_object_or_404(Order, order_number=order_number)

    date_of_order = order.order_date
    formatted_datetime = formats.date_format(date_of_order, "SHORT_DATETIME_FORMAT")

    messages.info(request, (
        f'Please note that you have already made this order with \
            order number: {order_number}. A confirmation email had \
                been sent to {order.email_address} on {formatted_datetime}'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'came_from_profile': True,
        'order': order,
    }

    return render(request, template, context)
