
import json
import time
import logging
from django.core.management.base import BaseCommand
import requests
from api_backend.models import Coins
from api_backend.models import AllCryptosList

COINGECKO = "https://api.coingecko.com/api/v3"
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


class Command(BaseCommand):
    """ Django command class to update crypto details
        run with python manage.py update_coin_details
    """
    help = "Update the crypto databases"


    def get_coin_details(self, coin_id):
        """ get coin details from the api """
        logger.info(f" Getting data for {coin_id}..")
        response = requests.get(
            COINGECKO +
            f'/coins/{coin_id}?localization=false&tickers=false&market_data=false&community_data=true&developer_data=true&sparkline=false',
            timeout=1)
        return response

    def handle(self, *args, **options):

        coins = [obj.id for obj in AllCryptosList.objects.all()]

        logger.info("Updating coins details")
        for coin_id in coins:
            response = self.get_coin_details(coin_id)
            logger.info(f" Updating details for: {coin_id}")
            if response.status_code != 200:
                logger.warning(f" Coin {coin_id} Not Found!")
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
            logger.info(f" Saved {coin_id} detail to the database")
            time.sleep(6)  # to avoid max requests

        self.stdout.write(self.style.SUCCESS(' Database update complete.'))
        logger.info(" Coins Details database update complete.")
