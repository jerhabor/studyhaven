from django.shortcuts import render


def index(request):
    """" View to returns the index page """
    return render(request, 'home/index.html')
