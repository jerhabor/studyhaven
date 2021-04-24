from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """ Each user is only allowed one profile and
    only one profile is attached to one user """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    """ A model of the user's shipping information """
    default_full_name = models.CharField(max_length=50, blank=True)
    default_email_address = models.EmailField(max_length=254, blank=True)
    default_phone_number = models.CharField(max_length=20, blank=True)
    default_country = CountryField(
        blank_label='Country *', null=True, blank=True)
    default_address_line1 = models.CharField(max_length=90, blank=True)
    default_address_line2 = models.CharField(max_length=90, blank=True)
    default_city_or_town = models.CharField(max_length=50, blank=True)
    default_postcode = models.CharField(max_length=10, blank=True)

    # String Method to return the user's username
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    A receiver in the post save event that either creates
    or updates the user's profile.
    """
    # If new user/no profile filled in
    if created:
        UserProfile.objects.create(user=instance)
    # Otherwise for registered users, the profile will be updated and saved.
    instance.userprofile.save()
