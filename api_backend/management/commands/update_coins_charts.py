import json
import logging
import time
from django.conf import settings
from django.core.management.base import BaseCommand
import requests
from api_backend.models import PriceUpdate
from . import coins_set

COINGECKO = "https://api.coingecko.com/api/v3"
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Update the crypto databases"

    def handle(self, *args, **kwargs):
        for coin_id in coins_set.coins:
            try:
                response = requests.get(
                    f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=eur&days=365")
            except BaseException as be:
                logger.warning(f"error connecting to endpoint {be}")
                continue
            if response.status_code != 200:
                logger.warning(f'Failed to retrieve data for {coin_id}')
                continue
            coin = response.json()
            logger.debug(f"Getting {coin_id}")
            # Extract relevant data from the coin object
            price_time = coin["prices"]
            try:
                coin_obj = PriceUpdate.objects.get(id=coin_id)
            except PriceUpdate.DoesNotExist:
                coin_obj = PriceUpdate(id=coin_id)

            # update
            coin_obj.price_time = json.dumps(price_time)

            coin_obj.save()
            logger.debug("wait 6s..")
            time.sleep(6)  # to avoid max requests

        self.stdout.write(self.style.SUCCESS('Database update complete.'))
