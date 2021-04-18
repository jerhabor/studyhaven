from django.shortcuts import render, redirect


def view_shopping_bag(request):
    """" View to return the shopping bag page for the
    user to see the contents that they have chosen to
    add to the bag. """
    return render(request, 'bag/bag.html')


def add_item_to_bag(request, product_id):
    """" View for the user to be able to add a product
    to their shopping bag. """

    qty = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    shopping_bag = request.session.get('bag', {})

    if product_id in list(shopping_bag.keys()):
        shopping_bag[product_id] += qty
    else:
        shopping_bag[product_id] = qty

    request.session['bag'] = shopping_bag
    return redirect(redirect_url)
