from django.shortcuts import render
from .models import Product


def all_products(request):
    """" View to return a page showing all products
    and also handle searching and sorting queries """

    products = Product.objects.all()
    context = {
        'shop': products,
    }

    return render(request, 'products/products.html', context)
