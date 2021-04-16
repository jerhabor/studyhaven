from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """" View to return a page showing all products
    and also handle searching and sorting queries. """

    products = Product.objects.all()
    context = {
        'shop': products,
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """" View to return a page showing further information
    of the product that the user has clicked on. """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)
