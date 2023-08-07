from django.urls import path

from products.views import add_product, delete_product, edit_product
from .views import CoinDetailView, CryptoListView, ManageCryptos, add_crypto, delete_crypto, edit_crypto


urlpatterns = [
    path('', CryptoListView.as_view(), name='crypto_list'),
    path('<str:pk>/', CoinDetailView.as_view(), name='coin'),
    path('manage', ManageCryptos.as_view(), name='manage_cryptos'),
    path('add_crypto', add_crypto, name='add_crypto'),
    path('edit/<str:crypto_id>/', edit_crypto, name='edit_crypto'),
    path('delete/<str:crypto_id>/', delete_crypto, name='delete_crypto'),
]
