from django.urls import path
from .views import add_credits, get_credits, payment_cancelled, payment_successful, sell_crypto, stripe_webhook, buy_crypto, portfolio_view

urlpatterns = [
    path("get-credits/", get_credits, name="get_credits"),
    path("add_credits/", add_credits, name="add_credits"),
    path("payment_successful/", payment_successful, name="payment_successful"),
    path("payment_cancelled/", payment_cancelled, name="payment_cancelled"),
    path("stripe_webhook/", stripe_webhook, name="stripe_webhook"),
    path("buy-crypto/<str:pk>/", buy_crypto, name="buy_crypto"),
    path("sell-crypto/<str:pk>/", sell_crypto, name="sell_crypto"),
    path("", portfolio_view, name="bag")
]
