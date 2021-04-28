from django.shortcuts import render


def faqs(request):
    """" View to return the FAQs page """
    return render(request, 'faqs/faqs.html')
