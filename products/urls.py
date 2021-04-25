from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='shop'),
    # Django uses the URL it finds a matching pattern for
    # so need to ensure product id is always an integer, as it is.
    path('<int:product_id>/', views.product_info, name='product_info'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
