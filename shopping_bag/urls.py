from django.urls import path
from .views import add_debit, get_debit, payment_cancelled, payment_successful, sell_crypto, shopping_bag_view, stripe_webhook, buy_crypto

urlpatterns = [
    path("get-debit/", get_debit, name="get_debit"),
    path("add_debit/", add_debit, name="add_debit"),
    path("payment_successful/", payment_successful, name="payment_successful"),
    path("payment_cancelled/", payment_cancelled, name="payment_cancelled"),
    path("stripe_webhook/", stripe_webhook, name="stripe_webhook"),
    path("buy-crypto/<str:pk>/", buy_crypto, name="buy_crypto"),
    path("sell-crypto/<str:pk>/", sell_crypto, name="sell_crypto"),
    path("", shopping_bag_view, name="bag")
]
