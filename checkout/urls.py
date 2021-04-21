from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkoutOrder, name='checkout')
]
