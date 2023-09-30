from django.urls import path
from wallet.views import wallet_view

urlpatterns = [
    path("", wallet_view, name="wallet"),
]