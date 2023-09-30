from django.db import models
from django.contrib.auth.models import User
from api_backend.models import CryptoCurrency

class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrencies = models.ManyToManyField(CryptoCurrency, through='CryptoAmount')

class CryptoAmount(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
