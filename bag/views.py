from django.shortcuts import render


def view_shopping_bag(request):
    """" View to return the shopping bag page for the
    user to see the contents that they have chosen to
    add to the bag. """
    return render(request, 'bag/bag.html')
