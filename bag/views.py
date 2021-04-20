from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, reverse
from products.models import Product


def view_shopping_bag(request):
    """" View to return the shopping bag page for the
    user to see the contents that they have chosen to
    add to the bag. """
    return render(request, 'bag/bag.html')


def add_item_to_bag(request, product_id):
    """" View for the user to be able to add a product
    to their shopping bag. """

    shop_product = Product.objects.get(pk=product_id)
    qty = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    shopping_bag = request.session.get('bag', {})

    if product_id in list(shopping_bag.keys()):
        shopping_bag[product_id] += qty
        messages.success(request, f'{qty} x {shop_product.name}')
    else:
        shopping_bag[product_id] = qty
        messages.success(request, f'{qty} x {shop_product.name}')

    request.session['bag'] = shopping_bag
    return redirect(redirect_url)


def update_bag(request, product_id):
    """" View for the user to be able to adjust quantity
    product in the bag and the bag updates accordingly """

    qty = int(request.POST.get('quantity'))
    shopping_bag = request.session.get('bag', {})

    if qty > 0:
        shopping_bag[product_id] = qty
    else:
        shopping_bag.pop(product_id)

    request.session['bag'] = shopping_bag
    return redirect(reverse('view_bag'))


def remove_bag_item(request, product_id):
    """" View for the user to be able to click the 'x'
    and remove the item from their bag. The bag template
    will also update once remove event occurs """

    try:
        shopping_bag = request.session.get('bag', {})
        shopping_bag.pop(product_id)

        request.session['bag'] = shopping_bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
