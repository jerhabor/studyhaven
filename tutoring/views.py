from django.shortcuts import render


def tutoring(request):
    """" View to returns the tutoring page """
    return render(request, 'tutoring/tutoring.html')
