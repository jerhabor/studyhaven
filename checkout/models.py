import uuid

from django.conf import settings
from django.db import models
from django.db.models import Sum
from products.models import Product


class Order(models.Model):

    # Inspired by Boutique Ado
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.EmailField(max_length=20, null=False, blank=False)
    country = models.EmailField(max_length=40, null=False, blank=False)
    address_line1 = models.CharField(max_length=90, null=False, blank=False)
    address_line2 = models.CharField(max_length=90, null=False, blank=False)
    city_or_town = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=10, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, default=0)
    delivery = models.DecimalField(
        max_digits=4, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, default=0)

    def order_number_generator(self):
        """ Generate a random string of 32 characters
        which will be used as the user's order number """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Grand total is aggregated as each product order's
        total is analysed """

        self.order_total = self.each_product.aggregate(Sum('product_order_total'))['product_order_total__sum']
        if self.order_total < settings.THRESHOLD_FOR_FREE_DELIVERY:
            self.delivery = settings.STANDARD_DELIVERY
        else:
            self.delivery = 0
        self.grand_total = self.order_total + self.delivery
        self.save()

    def save(self, *args, **kwargs):
        """ Set order number when order is generated
        (Inspired by Boutique Ado) """
        if not self.order_number:
            self.order_number = self.order_number_generator()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class eachProductOrder(models.Model):
    product = models.ForeignKey(
        Product, blank=False, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False, blank=False)
    order = models.ForeignKey(
        Order, blank=False, null=False, on_delete=models.CASCADE,
        related_name='each_product')
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