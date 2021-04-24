from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def user_profile(request):
    """ A view to display a registered user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile
    }

    return render(request, template, context)
