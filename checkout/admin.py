from django.contrib import admin
from .models import Order, EachLineOrder


class eachProductOrderManagement(admin.TabularInline):
    model = EachLineOrder
    readonly_fields = ('product_order_total',)


class OrderManagement(admin.ModelAdmin):
    inlines = (eachProductOrderManagement,)

    fields = ('order_number', 'full_name', 'email_address',
              'phone_number', 'country', 'address_line1',
              'address_line2', 'city_or_town', 'postcode',
              'order_date', 'order_total', 'delivery_cost',
              'grand_total', 'original_bag', 'stripe_pi_id',)

    readonly_fields = ('order_date', 'order_number', 'delivery_cost',
                       'order_total', 'grand_total', 'original_bag',
                       'stripe_pi_id',)

    list_display = ('order_number', 'order_date', 'full_name',
                    'delivery_cost', 'order_total', 'grand_total',)

    ordering = ('-order_date',)


admin.site.register(Order, OrderManagement)
