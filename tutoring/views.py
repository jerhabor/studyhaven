from django.shortcuts import render
from .models import TutoringRate


def tutoring(request):
    """" View to return the tutoring page """
    rates = TutoringRate.objects.all()
    template = 'tutoring/tutoring.html'
    context = {
        'rates': rates,
    }
    return render(request, template, context)
