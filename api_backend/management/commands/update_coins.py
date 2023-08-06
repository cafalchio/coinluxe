from django.core.management.base import BaseCommand
import requests
from django.core.exceptions import ObjectDoesNotExist
from api_backend.models import CryptoCurrency
from . import coins_set

coingecko = "https://api.coingecko.com/api/v3"
coins = '/coins/markets?vs_currency=eur&order=market_cap_desc&per_page=250&page=1&sparkline=false&locale=en'


class Command(BaseCommand):
    help = "Update the crypto databases"

    def handle(self, *args, **kwargs):
        response = requests.get(coingecko + coins)
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(
                'Failed to retrieve data from the endpoint.'))
            return
        coin_data = response.json()
        for coin in coin_data:
            if coin["id"] not in coins_set.coins:
                continue
            # Extract relevant data from the coin object
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
            except ObjectDoesNotExist:
                crypto_obj = CryptoCurrency(id=coin_id)

            # Update the coin object with the new data
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

            # Save the coin object in the database
            crypto_obj.save()

        self.stdout.write(self.style.SUCCESS('Database update complete.'))
