from datetime import timedelta
import json
from django.db import models
from random import randint


class CryptoCurrency(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    image = models.URLField(null=True)
    current_price = models.FloatField(null=True)
    market_cap = models.BigIntegerField(null=True)
    market_cap_rank = models.PositiveIntegerField(null=True)
    fully_diluted_valuation = models.BigIntegerField(null=True)
    total_volume = models.BigIntegerField(null=True)
    high_24h = models.FloatField(null=True)
    low_24h = models.FloatField(null=True)
    price_change_24h = models.FloatField(null=True)
    price_change_percentage_24h = models.FloatField(null=True)
    market_cap_change_24h = models.FloatField(null=True)
    market_cap_change_percentage_24h = models.FloatField(null=True)
    circulating_supply = models.FloatField(null=True)
    total_supply = models.FloatField(null=True)
    max_supply = models.FloatField(null=True)
    ath = models.FloatField(null=True)
    ath_change_percentage = models.FloatField(null=True)
    ath_date = models.DateTimeField(null=True)
    atl = models.FloatField(null=True)
    atl_change_percentage = models.FloatField(null=True)
    atl_date = models.DateTimeField(null=True)
    last_updated = models.DateTimeField()
    sell_price_multiplier = models.FloatField(editable=True, default=1.001)

    @property
    def formatted_current_price(self):
        if self.current_price < 1 and self.current_price > 0.1:
            return '{:,.3f}'.format(self.current_price)
        elif self.current_price < 0.1 and self.current_price > 0.01:
            return '{:,.4f}'.format(self.current_price)
        elif self.current_price < 0.01:
            return '{:,.6f}'.format(self.current_price)
        return '{:,.2f}'.format(self.current_price)

    @property
    def formatted_market_cap(self):
        if self.market_cap >= 1000000000:
            return '{:,.2f} bi'.format(self.market_cap / 1000000000)
        elif self.market_cap >= 1000000:
            return '{:,.2f} mi'.format(self.market_cap / 1000000)
        else:
            return '{:,.2f}'.format(self.market_cap)

    @property
    def formatted_price_change_24h(self):
        return f"{self.price_change_percentage_24h:.2f}"

    @property
    def integer_24h_change(self):
        return int(float(self.formatted_price_change_24h) * 100)

    @property
    def selling_text(self):
        negative_phrases = [
            f"Buy {self.id.capitalize()} on the dip!",
            f"Opportunity: {self.id.capitalize()} at a discount!",
            f"Don't be discouraged! Buy {self.id.capitalize()} low."
        ]
        positive_phrases = [
            f"Upward momentum for {self.id.capitalize()}. Buy now!",
            f"Positive trend: {self.id.capitalize()} rising!",
            f"Join the rally: Buy {self.id.capitalize()}!"
        ]
        if int(float(self.formatted_price_change_24h) * 100) < 0:
            return negative_phrases[randint(0, 2)]
        else:
            return positive_phrases[randint(0, 2)]

    @property
    def formatted_symbol(self):
        return f"{self.symbol.upper()}"

    @property
    def formatted_last_updated(self):
        updated_time = self.last_updated + timedelta(hours=1)
        return updated_time.strftime("%d %B - %H:%M:%S")

    @property
    def formatted_total_volume(self):
        if self.total_volume >= 1000000000:
            return '{:,.2f} bi'.format(self.total_volume / 1000000000)
        elif self.total_volume >= 1000000:
            return '{:,.2f} mi'.format(self.total_volume / 1000000)
        else:
            return '{:,.2f}'.format(self.total_volume)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-market_cap']


# Coin Detail
class Coins(models.Model):
    id = models.CharField(max_length=300, primary_key=True)
    symbol = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    block_time_in_minutes = models.PositiveIntegerField(default=0, null=True)
    description = models.TextField(null=True)
    homepage = models.JSONField(max_length=100, null=True)
    blockchain_site = models.JSONField(max_length=100, null=True)
    market_cap_rank = models.PositiveIntegerField(default=0)
    categories = models.JSONField(max_length=100, null=True)

    @property
    def formatted_symbol(self):
        return f"{self.symbol.upper()}"

    @property
    def formatted_homepage(self):
        homepage_list = json.loads(self.homepage)
        return homepage_list[0]

    @property
    def formatted_categories(self):
        categories = json.loads(self.categories)
        return categories

    @property
    def formatted_blockchain_site(self):
        blockchain_sites = json.loads(self.blockchain_site)
        return blockchain_sites[0]

    def __str__(self):
        return self.name


class PriceUpdate(models.Model):
    id = models.CharField(max_length=300, primary_key=True)
    price_time = models.JSONField(max_length=1000, null=True)

    @property
    def formatted_price_time(self):
        price_time = json.loads(self.price_time)
        return price_time

    def __str__(self):
        return f"Coin: {self.coin}, Price: {self.price}, Date: {self.date}"
