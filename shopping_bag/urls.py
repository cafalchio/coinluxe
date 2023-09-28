from django.urls import path
from .views import add_to_bag, get_debit, pay, payment_cancelled, payment_successful, remove_crypto, shopping_bag_view

urlpatterns = [
    path("get-debit/", get_debit, name="get_debit"),
    path("payment_successful/", payment_successful, name="payment_successful"),
    path("payment_cancelled/", payment_cancelled, name="payment_cancelled"),
    path("pay/", pay, name="pay"),
    path("add_to_bag/<str:pk>/", add_to_bag, name="add_to_bag"),
    path("sell-crypto/<str:pk>/", remove_crypto, name="sell_crypto"),
    path("", shopping_bag_view, name="bag")
]
