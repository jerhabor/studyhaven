from django.shortcuts import render
from .models import FAQ
import sys


def faqs(request):
    """" View to return the FAQs page """
    faqs = FAQ.objects.all()
    template = 'faqs/faqs.html'
    count = sys.getsizeof(faqs)
    context = {
        'faqs': faqs,
    }
    return render(request, template, context)
