from django.urls import path
from .views import (ProductListView,
                    ProductDetailView,
                    add_product,
                    delete_product,
                    edit_product,
                    buy_product,
                    success)

urlpatterns = [
    path(
        'products/',
        ProductListView.as_view(),
        name='product_list'),
    path(
        'products/<int:pk>/',
        ProductDetailView.as_view(),
        name='product_detail'),
    path(
        'success/',
        success,
        name='success'),
    path(
        'buy_product/<int:pk>/',
        buy_product,
        name='buy_product'),
    path(
        'add/',
        add_product,
        name='add_product'),
    path(
        'edit/<int:product_id>/',
        edit_product,
        name='edit_product'),
    path(
        'delete/<int:product_id>/',
        delete_product,
        name='delete_product'),
]
