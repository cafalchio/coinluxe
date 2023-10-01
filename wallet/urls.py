from django.urls import path
from wallet.views import wallet_view, withdrawal

urlpatterns = [
    path("", wallet_view, name="wallet"),
    path("withdrawal/<str:pk>/", withdrawal, name="withdrawal"),
]