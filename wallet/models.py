from django.db import models
from django.contrib.auth.models import User
from api_backend.models import CryptoCurrency

class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrency = models.ManyToManyField(CryptoCurrency)
    amount = models.FloatField(null=True, default=0)
    @property
    def formatted_amount(self):
        if self.amount >= 1000:
            return f"{self.amount / 1000}K"
        elif self.amount >= 1000000:
            return f"{self.amount / 1000000}Mi"
        return self.amount