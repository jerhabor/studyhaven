from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history_table, name='order_history'),
]
