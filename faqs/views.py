from django.shortcuts import render


def faqs(request):
    """" View to returns the tutoring page """
    return render(request, 'faqs/faqs.html')
