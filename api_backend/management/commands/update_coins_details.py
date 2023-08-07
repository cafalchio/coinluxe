import json
import time
import logging
from django.core.management.base import BaseCommand
import requests
from api_backend.models import Coins, CryptoCurrency


COINGECKO = "https://api.coingecko.com/api/v3"
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Update the crypto databases"
    
    def add_arguments(self, parser):
        parser.add_argument('--coin', type=str, help='A coin id to be updated')
        
        
    def get_coin_details(self, coin_id):
        response = requests.get(COINGECKO +
            f'/coins/{coin_id}?localization=false&tickers=false&market_data=false&community_data=true&developer_data=true&sparkline=false')
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
                logger.warning(f"Coin {coin_id} Not Found!")
                continue
            coin = response.json()
            # Extract relevant data from the coin object
            coin_id = coin["id"]
            symbol = coin["symbol"]
            name = coin["name"]
            block_time_in_minutes = coin["block_time_in_minutes"]
            categories = coin["categories"]
            description = coin["description"]['en']
            homepage = coin["links"]["homepage"]
            blockchain_site = coin["links"]["blockchain_site"]
            market_cap_rank = coin["market_cap_rank"]
            homepage_value = homepage if homepage else None
            bsv = blockchain_site if blockchain_site else None
            categories_value = categories if categories else None

            try:
                coin_obj = Coins.objects.get(id=coin_id)
            except Coins.DoesNotExist:
                coin_obj = Coins(id=coin_id)

            # update
            coin_obj.symbol = symbol
            coin_obj.name = name
            coin_obj.block_time_in_minutes = block_time_in_minutes
            coin_obj.categories = json.dumps(categories_value)
            coin_obj.description = description
            coin_obj.homepage = json.dumps(homepage_value)
            coin_obj.blockchain_site = json.dumps(bsv)
            coin_obj.market_cap_rank = market_cap_rank

            coin_obj.save()
            time.sleep(6)  # to avoid max requests

        self.stdout.write(self.style.SUCCESS('Database update complete.'))
        logger.info("Coins Details database update complete.")
