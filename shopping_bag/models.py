from django.db import models
from django.contrib.auth.models import User


class Bag(models.Model):
    """ Shopping Bag model """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    holdings = models.ManyToManyField(
        "api_backend.CryptoCurrency",
        through="Holding")

    class Meta:
        """ Meta """
        db_table = 'Bag'


class Holding(models.Model):
    """ Holding cryptos model"""
    shopping_bag = models.ForeignKey(Bag, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(
        "api_backend.CryptoCurrency", on_delete=models.CASCADE
    )
    amount = models.FloatField(null=True, default=0)

    @property
    def formatted_amount(self):
        """ format amount in K, mi, bi """
        if self.amount >= 1000:
            return f"{self.amount / 1000}K"
        elif self.amount >= 1000000:
            return f"{self.amount / 1000000}Mi"
        return self.amount
