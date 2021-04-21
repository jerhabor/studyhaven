from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import eachProductOrder

@receiver(post_save, sender=eachProductOrder)
def save_update(sender, instance, created, **kwargs):
    """ Handles signals from the post_save event so
    that the order_total is updated as line items are
    created """
    instance.order.update_total()

@receiver(post_delete, sender=eachProductOrder)
def delete_update(sender, instance, **kwargs):
    """ Handles signals from the post_delete event so
    that the order_total is updated as line items are
    deleted """
    instance.order.update_total()
