from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_bag, name='view_bag'),
    path('add/<product_id>/', views.add_item_to_bag, name='add_to_bag'),
    path('update/<product_id>/', views.update_bag, name='update_bag'),
    path('remove/<product_id>/', views.remove_bag_item, name='remove_bag_item'),
]
