import logging
import time
from django.core.management.base import BaseCommand
import requests
from django.core.exceptions import ObjectDoesNotExist
from api_backend.models import CryptoCurrency
from . import coins_set

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """This command will be used to both update coin prices hourly using a scheduler as well
    as create new coins when requested by the admin, via command line or using the manage tool.

    Argument:
        --coin (str): An coin id to be added or updated using coingecko api

    """
    help = "Update the crypto databases"


    def add_arguments(self, parser):
        parser.add_argument('--coin', type=str, help='A coin id to be updated')


    def get_coin_details(self, page=1):
        coingecko = "https://api.coingecko.com/api/v3"
        coins = f'/coins/markets?vs_currency=eur&order=market_cap_desc&per_page=250&page={page}&sparkline=false&locale=en'    
        response = requests.get(coingecko + coins)
        return response


    def handle(self, *args, **options):
        
        coin_selected = options['coin']
        
        for i in range(1, 4):
            response = self.get_coin_details(i)
            if response.status_code == 200:
                coin_data = response.json()
                if coin_selected:
                    message = [self.update_create_coin(coin) for coin in coin_data if coin['id'] == coin_selected]
                else:
                    for coin in coin_data:
                        self.update_create_coin(coin)
            else:
                logger.warning(f"Could not get coin info for page {i}")
                return f"Error connecting to coingecko for page {i}, please try later"
            time.sleep(10)

        if not coin_selected:
            self.stdout.write(self.style.SUCCESS('Database update complete.'))
        return "Update Completed"

    
    def update_create_coin(self, coin):
        
        coin_id = coin['id']
        symbol = coin['symbol']
        name = coin['name']
        image = coin['image']
        current_price = coin['current_price'] if 'current_price' in coin else None
        market_cap = coin['market_cap'] if 'market_cap' in coin else None
        market_cap_rank = coin['market_cap_rank'] if 'market_cap_rank' in coin else None
        fully_diluted_valuation = coin['fully_diluted_valuation'] if 'fully_diluted_valuation' in coin else None
        total_volume = coin['total_volume'] if 'total_volume' in coin else None
        high_24h = coin['high_24h'] if 'high_24h' in coin else None
        low_24h = coin['low_24h'] if 'low_24h' in coin else None
        price_change_24h = coin['price_change_24h'] if 'price_change_24h' in coin else None
        price_change_percentage_24h = coin['price_change_percentage_24h'] if 'price_change_percentage_24h' in coin else None
        market_cap_change_24h = coin['market_cap_change_24h'] if 'market_cap_change_24h' in coin else None
        market_cap_change_percentage_24h = coin[
            'market_cap_change_percentage_24h'] if 'market_cap_change_percentage_24h' in coin else None
        circulating_supply = coin['circulating_supply'] if 'circulating_supply' in coin else None
        total_supply = coin['total_supply'] if 'total_supply' in coin else None
        max_supply = coin['max_supply'] if 'max_supply' in coin else None
        ath = coin['ath'] if 'ath' in coin else None
        ath_change_percentage = coin['ath_change_percentage'] if 'ath_change_percentage' in coin else None
        ath_date = coin['ath_date'] if 'ath_date' in coin else None
        atl = coin['atl'] if 'atl' in coin else None
        atl_change_percentage = coin['atl_change_percentage'] if 'atl_change_percentage' in coin else None
        atl_date = coin['atl_date'] if 'atl_date' in coin else None
        last_updated = coin['last_updated'] if 'last_updated' in coin else None

        # Check if the coin already exists in the database
        try:
            crypto_obj = CryptoCurrency.objects.get(id=coin_id)
            message = "coins updated"
        except ObjectDoesNotExist:
            crypto_obj = CryptoCurrency(id=coin_id)
            message = "coin created"

        crypto_obj.symbol = symbol
        crypto_obj.name = name
        crypto_obj.image = image
        crypto_obj.current_price = current_price
        crypto_obj.market_cap = market_cap
        crypto_obj.market_cap_rank = market_cap_rank
        crypto_obj.fully_diluted_valuation = fully_diluted_valuation
        crypto_obj.total_volume = total_volume
        crypto_obj.high_24h = high_24h
        crypto_obj.low_24h = low_24h
        crypto_obj.price_change_24h = price_change_24h
        crypto_obj.price_change_percentage_24h = price_change_percentage_24h
        crypto_obj.market_cap_change_24h = market_cap_change_24h
        crypto_obj.market_cap_change_percentage_24h = market_cap_change_percentage_24h
        crypto_obj.circulating_supply = circulating_supply
        crypto_obj.total_supply = total_supply
        crypto_obj.max_supply = max_supply
        crypto_obj.ath = ath
        crypto_obj.ath_change_percentage = ath_change_percentage
        crypto_obj.ath_date = ath_date
        crypto_obj.atl = atl
        crypto_obj.atl_change_percentage = atl_change_percentage
        crypto_obj.atl_date = atl_date
        crypto_obj.last_updated = last_updated
        logger.debug(f"Saving {coin_id} in DB")
        crypto_obj.save() # Save the coin object in the database
        return message
