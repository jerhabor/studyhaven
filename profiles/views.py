from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def user_profile(request):
    """ A view to display a registered user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    order_history = profile.order_history.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'order_history': order_history,
    }

    return render(request, template, context)
