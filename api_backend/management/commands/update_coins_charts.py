import json
import logging
import time
from django.core.management.base import BaseCommand
import requests
from api_backend.models import PriceUpdate
from . import coins_set

COINGECKO = "https://api.coingecko.com/api/v3"
logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")
TRIES = 3
TIME_BTW_TRIES = 60


class Command(BaseCommand):
    """ Django command class to update crypto charts
        run with python manage.py update_coin_charts
    """
    help = "Update the crypto databases"

    def get_coin_details(self, coin_id):
        """ get coin details from the api"""
        for i in range(1, TRIES+1):
            try:
                response = requests.get(
                    f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=eur&days=365",
                    timeout=3)
                break
            except Exception as e:
                logger.warning(
                    f" Failed {i}/TRIES times to retrieve: {coin_id}")
                logger.info(
                    f" Sleeping for {TIME_BTW_TRIES}s befor the next try..")

        logger.info(f" Data for {coin_id}")
        return response

    def handle(self, *args, **options):

        for coin_id in list(coins_set.coins):
            response = self.get_coin_details(coin_id)
            if response.status_code != 200:
                logger.warning(f' Failed to retrieve data for {coin_id}')
            coin = response.json()
            logger.debug(f" Getting {coin_id}")
            # Extract relevant data from the coin object
            price_time = coin["prices"]
            try:
                coin_obj = PriceUpdate.objects.get(id=coin_id)
            except PriceUpdate.DoesNotExist:
                coin_obj = PriceUpdate(id=coin_id)
            # update
            coin_obj.price_time = json.dumps(price_time)

            coin_obj.save()
            logger.info(" wait 8s..")
            time.sleep(8)  # to avoid max requests

        self.stdout.write(self.style.SUCCESS(
            'Historical data updated successful.'))
        logger.info(" Historical data updated successful")
