from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import checkoutOrderForm


def checkoutOrder(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You have not added an item to your bag yet!")
        return redirect(reverse('shop'))

    checkout_order_form = checkoutOrderForm()
    template = 'checkout/checkout.html'
    context = {
        'form': checkout_order_form,
    }

    return render(request, template, context)
