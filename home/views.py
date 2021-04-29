from django.shortcuts import render
from .models import Review


def index(request):
    """" View to return the index page """

    reviews = Review.objects.all()
    template = 'home/index.html'
    context = {
        'reviews': reviews,
    }

    return render(request, template, context)
