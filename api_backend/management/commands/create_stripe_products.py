import stripe
import logging
import time
from django.conf import settings
from django.core.management.base import BaseCommand
from api_backend.models import Coins, CryptoCurrency
from . import coins_set

stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


class Command(BaseCommand):
    help = "Create stripe coin as products"

    def handle(self, *args, **options):
        for coin_id in list(coins_set.coins):
            cryptos = CryptoCurrency.objects.get(id=coin_id)
            coins = Coins.objects.get(id=coin_id)
            try:
                stripe.Product.create(
                    id=coin_id,
                    name=coin_id.capitalize(),
                    url=coins.homepage,
                    images=[cryptos.image]
                )
            except stripe.error.InvalidRequestError:
                logger.warning(f" {coin_id} already exists")

        self.stdout.write(self.style.SUCCESS(
            'Coin Prices Updated on Stripe!'))
        logger.info(" Coin Prices Updated on Stripe")
