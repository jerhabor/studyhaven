from django.contrib import admin
from .models import Order, eachProductOrder


class eachProductOrderManagement(admin.TabularInline):
    model = eachProductOrder
    readonly_fields = ('product_order_total',)


class OrderManagement(admin.ModelAdmin):
    inlines = (eachProductOrderManagement,)

    fields = ('order_number', 'full_name', 'email_address',
                'phone_number', 'country', 'address_line1',
                'address_line2', 'city_or_town', 'postcode',
                'order_date', 'order_total', 'delivery',
                'grand_total',)

    readonly_fields = ('order_date', 'order_number', 'delivery',
                     'order_total', 'grand_total',)

    list_display = ('order_number', 'order_date', 'full_name',
                       'delivery', 'order_total', 'grand_total',)

    ordering = ('-order_date',)


admin.site.register(Order, OrderManagement)
