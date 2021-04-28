from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
# to allow for search criteria in product name OR description
from django.db.models import Q, functions

from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ProductAdminForm


def all_products(request):
    """" View to return a page showing all products
    and also handle searching and sorting queries. """

    products = Product.objects.all()
    category_list = Category.objects.all()
    categories = None
    query = None
    sort = None
    method = None

    if request.GET:
        if 'sort' in request.GET:
            sort_choice = request.GET['sort']
            sort = sort_choice
            if sort_choice == 'name':
                sort_choice = 'name_lower'
                products = products.annotate(
                    name_lower=functions.Lower('name'))
            if sort_choice == 'category':
                sort_choice = 'category__name'
            if 'method' in request.GET:
                method = request.GET['method']
                if method == 'desc':
                    sort_choice = f'-{sort_choice}'
            products = products.order_by(sort_choice)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # search for the 'name' field from the category class in database
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter a search criteria.")
                return redirect(reverse('shop'))

            # Case-insensitive queries made to search product name/description
            queries = Q(
                name__icontains=query) | Q(
                    description__icontains=query)
            products = products.filter(queries)

    chosen_sort = f'{sort}_{method}'
    context = {
        'shop': products,
        'chosen_category': categories,
        'chosen_sort': chosen_sort,
        'all_categories': category_list,
        'query': query,
        'method': method
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


@login_required
def add_product(request):
    """ A view to allow StudyHaven superuser and owner to add
    a product to the shop. """
    if not request.user.is_superuser:
        messages.error(request, 'Only the site owners can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        admin_form = ProductAdminForm(request.POST, request.FILES)
        if admin_form.is_valid():
            product = admin_form.save()
            messages.success(
                request, f'You have successfully added: {product.name} to the StudyHaven shop!')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(
                request, 'Unable to add product to the StudyHaven shop. \
                    Please check that the form inputs are valid.')
    else:
        admin_form = ProductAdminForm()
    template = 'products/product_addition.html'
    context = {
        'form': admin_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ A view to allow StudyHaven superuser and owner to edit
    a product already in the shop. """
    if not request.user.is_superuser:
        messages.error(request, 'Only the site owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        admin_form = ProductAdminForm(
            request.POST, request.FILES, instance=product)
        if admin_form.is_valid():
            admin_form.save()
            messages.success(
                request, f'You have successfully updated: {product.name}.')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Unable to add product to the StudyHaven shop. \
                    Please check that the form inputs are valid.')
    else:
        admin_form = ProductAdminForm(instance=product)
        messages.info(request, f'You are now editing: {product.name}')
    template = 'products/product_editing.html'
    context = {
        'product': product,
        'form': admin_form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ A view to delete the product from the StudyHaven shop. """
    if not request.user.is_superuser:
        messages.error(request, 'Only the site owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} has now \
        been deleted from the StudyHaven shop!')
    return redirect(reverse('shop'))
