from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal


def bag_contents(request):
    """ This context processor allows the contexts dictionary
    to be made available across all templates in StudyHaven. """
    bag_products = []
    total_price = 0
    product_count = 0
    shopping_bag = request.session.get('bag', {})

    for pk, quantity in shopping_bag.items():
        product = get_object_or_404(Product, pk=pk)
        total_price += product.price * quantity
        product_count += quantity
        bag_products.append({
            'product': product,
            'item_id': pk,
            'quantity': quantity
        })

    if total_price < settings.THRESHOLD_FOR_FREE_DELIVERY:
        delivery = total_price + Decimal(settings.STANDARD_DELIVERY)
        left_for_free_delivery = settings.THRESHOLD_FOR_FREE_DELIVERY - total_price
    else:
        delivery = 0
        left_for_free_delivery = 0

    grand_total = delivery + total_price

    context = {
        'bag_products': bag_products,
        'total': total_price,
        'product_count': product_count,
        'left_for_free_delivery': left_for_free_delivery,
        'threshold_for_free_delivery': settings.THRESHOLD_FOR_FREE_DELIVERY,
        'grand_total': grand_total,
    }

    return context
