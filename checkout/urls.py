from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout_order, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
]
