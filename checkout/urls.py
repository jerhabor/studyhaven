from django.urls import path
from . import views
from .webhooks import webhook_view

urlpatterns = [
    path('', views.checkout_order, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('cached_checkout_info/',
         views.cached_checkout_info, name='cached_checkout_info'),
    path('wh/', webhook_view, name='webhook'),
]
