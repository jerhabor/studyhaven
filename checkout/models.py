import uuid

from django.conf import settings
from django.db import models
from django.db.models import Sum

from products.models import Product
from profiles.models import UserProfile

# In order to access the two letter country code
# for the forms to be processed by Stripe:
from django_countries.fields import CountryField

from decimal import Decimal


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    # Keep an order history in the admin regardless of whether user profile
    # has been deleted.
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='order_history')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    address_line1 = models.CharField(max_length=90, null=False, blank=False)
    address_line2 = models.CharField(max_length=90, null=True, blank=True)
    city_or_town = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(
        max_digits=4, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, default=0)

    """ Need to save the original bag items on order in the event of
    buying during a sale for instance, and buying the same item(s) another
    time when there is no longer a sale. """
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pi_id = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def order_number_generator(self):
        """ Generate a random string of 32 characters
        which will be used as the user's order number """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Grand total is aggregated as each product order's
        total is analysed """

        self.order_total = self.each_line.aggregate(
            Sum('product_order_total'))['product_order_total__sum'] or 0
        if self.order_total < settings.THRESHOLD_FOR_FREE_DELIVERY:
            self.delivery_cost = Decimal(settings.STANDARD_DELIVERY)
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """ Set order number when order is generated
        (Inspired by Boutique Ado) """
        if not self.order_number:
            self.order_number = self.order_number_generator()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class EachLineOrder(models.Model):
    product = models.ForeignKey(
        Product, blank=False, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False, blank=False)
    order = models.ForeignKey(
        Order, blank=False, null=False, on_delete=models.CASCADE,
        related_name='each_line')
    product_order_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ Each product order total will be calculated so that
        the grand total will be calculated accordingly.
        (Inspired by Boutique Ado) """

        self.product_order_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order.order_number}'
