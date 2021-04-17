from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
# to allow for search criteria in product name OR description
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """" View to return a page showing all products
    and also handle searching and sorting queries. """

    products = Product.objects.all()
    categories = None
    query = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # search for the 'name' field from the category class in database
            products = products.filter(category__name__in=categories)
            print(Category.objects)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter a search criteria.")
                return redirect(reverse('shop'))

            # Case-insensitive queries made to search product name/description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'shop': products,
        'query': query,
        'categories': categories,
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
