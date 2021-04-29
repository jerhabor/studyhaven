from django import template


# From Django documentation - in order to register filter
register = template.Library()


# Function to calculate the subtotal in the bag
@register.filter(name='subtotal_calculation')
def subtotal_calculation(quantity, price):
    return quantity * price
