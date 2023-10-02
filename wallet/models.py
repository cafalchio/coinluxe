from django.db import models
from django.contrib.auth.models import User


class CryptoWallet(models.Model):
    """ Wallet model """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto_amounts = models.ManyToManyField(
        "api_backend.CryptoCurrency",
        through="CryptoCollection")


class CryptoCollection(models.Model):
    """ Collection for wallet """
    wallet = models.ForeignKey(CryptoWallet, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(
        "api_backend.CryptoCurrency", on_delete=models.CASCADE
    )
    amount = models.FloatField(null=True, default=0)
