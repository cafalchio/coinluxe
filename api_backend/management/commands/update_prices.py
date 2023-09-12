import stripe
import logging
from django.conf import settings
from django.core.management.base import BaseCommand
from api_backend.models import CryptoCurrency
from . import coins_set

stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


class Command(BaseCommand):
    help = "Update stripe prices"

    def handle(self, *args, **options):
        for coin_id in list(coins_set.coins):
            crypto_obj = CryptoCurrency.objects.get(id=coin_id)
            stripe.Price.create(
                currency="eur",
                billing_scheme="per_unit",
                recurring=None,
                product=coin_id,
                unit_amount_decimal=crypto_obj.current_price,
                active=True
            )

        self.stdout.write(self.style.SUCCESS(
            'Coin Prices Updated on Stripe!'))
        logger.info("Coin Prices Updated on Stripe")
