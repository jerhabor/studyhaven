from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, reverse, get_object_or_404
from products.models import Product


def view_shopping_bag(request):
    """ View to return the shopping bag page for the
    user to see the contents that they have chosen to
    add to the bag. """
    return render(request, 'bag/bag.html')


def add_item_to_bag(request, product_id):
    """ View for the user to be able to add a product
    to their shopping bag. """

    # incase object isn't found
    shop_product = get_object_or_404(Product, pk=product_id)
    qty = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    shopping_bag = request.session.get('bag', {})

    if product_id in list(shopping_bag.keys()):
        shopping_bag[product_id] += qty
        messages.success(
            request, f'Updated {shop_product.name} quantity to {shopping_bag[product_id]}.')
    else:
        shopping_bag[product_id] = qty
        messages.success(
            request, f'Added {qty} x {shop_product.name} to your bag.')

    request.session['bag'] = shopping_bag
    return redirect(redirect_url)


def update_bag(request, product_id):
    """ View for the user to be able to adjust quantity
    product in the bag and the bag updates accordingly """

    # incase object isn't found
    shop_product = get_object_or_404(Product, pk=product_id)
    qty = int(request.POST.get('quantity'))
    shopping_bag = request.session.get('bag', {})

    if qty > 0:
        shopping_bag[product_id] = qty
        messages.success(
            request, f'Updated {shop_product.name} quantity to {shopping_bag[product_id]}.')
    else:
        shopping_bag.pop(product_id)
        messages.success(
            request, f'Removed {shop_product.name} from your bag.')

    request.session['bag'] = shopping_bag
    return redirect(reverse('view_bag'))


def remove_bag_item(request, product_id):
    """" View for the user to be able to click the 'x'
    and remove the item from their bag. The bag template
    will also update once remove event occurs """

    try:
        # incase object isn't found
        shop_product = get_object_or_404(Product, pk=product_id)
        shopping_bag = request.session.get('bag', {})
        shopping_bag.pop(product_id)
        messages.success(
            request, f'Removed {shop_product.name} from your bag.')

        request.session['bag'] = shopping_bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Unable to remove: {e}')
        return HttpResponse(status=500)
