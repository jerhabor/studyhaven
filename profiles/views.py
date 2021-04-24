from django.shortcuts import render


def user_profile(request):
    """ A view to display the registered user's profile """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
