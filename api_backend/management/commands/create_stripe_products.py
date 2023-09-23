import stripe
from stripe.error import InvalidRequestError
import logging
from django.conf import settings
from django.core.management.base import BaseCommand
from api_backend.models import Coins, CryptoCurrency
from . import coins_set

stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


class Command(BaseCommand):
    help = "Create or update Stripe coin products"

    def handle(self, *args, **options):
        for coin_id in list(coins_set.coins):
            crypto = CryptoCurrency.objects.get(id=coin_id)
            coin = Coins.objects.get(id=coin_id)

            if crypto.current_price < .01:
                min_quantity = 100
                total_price = crypto.current_price * quantity

            try:
                existing_product = stripe.Product.retrieve(coin_id)
                existing_product.name = coin_id.capitalize()
                existing_product.images = [crypto.image]
                existing_product.save()

                price = stripe.Price.create(
                    currency="eur",
                    billing_scheme="per_unit",
                    unit_amount=int(total_price * 100),
                    product=coin_id,
                    active=True,
                )
                existing_product.default_price = price.id
                existing_product.save()
            except InvalidRequestError as e:
                logger.error(
                    f"Error creating or updating Stripe product for {coin_id}: {str(e)}")

        self.stdout.write(self.style.SUCCESS(
            'Coin Prices Updated on Stripe!'))
        logger.info("Coin Prices Updated on Stripe")