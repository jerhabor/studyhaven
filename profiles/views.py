from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def user_profile(request):
    """ A view to display a registered user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    # Handling the posting of the form
    if request.method == 'POST':
        # Create a new instance of the form into 'profile' defined above
        form = UserProfileForm(request.POST, instance=profile)
        # Add success message if form is valid
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your contact and shipping information \
                    have been updated successfully!')

    form = UserProfileForm(instance=profile)
    order_history = profile.order_history.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'order_history': order_history,
        'on_my_profile': True,
    }

    return render(request, template, context)
