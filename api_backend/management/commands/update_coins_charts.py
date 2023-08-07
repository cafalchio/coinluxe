import json
import logging
import time
from django.core.management.base import BaseCommand
import requests
from api_backend.models import CryptoCurrency, PriceUpdate
from . import coins_set

COINGECKO = "https://api.coingecko.com/api/v3"
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Update the crypto databases"
    

    def add_arguments(self, parser):
            parser.add_argument('--coin', type=str, help='A coin id to be updated')
    

    def get_coin_details(self, coin_id):
        response = requests.get(
                    f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=eur&days=365")
        logger.debug(f"Data for {coin_id}")
        return response
    

    def handle(self, *args, **options):
        coin_selected = options['coin']
        objects = CryptoCurrency.objects.all()
        coins = objects.values_list("id", flat=True)
        
        if coin_selected:
            coins = [coin for coin in coins if coin == coin_selected]

        for coin_id in coins:
            response = self.get_coin_details(coin_id)
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

        self.stdout.write(self.style.SUCCESS('Historical data updated successful.'))
        logger.info("Historical data updated successful")