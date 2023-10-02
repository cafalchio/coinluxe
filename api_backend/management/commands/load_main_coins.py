""" Initial coins """
from django.core.management.base import BaseCommand
from api_backend.models import AllCryptosList


cryptocurrencies = [
        "bitcoin",
        "ethereum",
        "tether",
        "binancecoin",
        "ripple",
        "usd-coin",
        "staked-ether",
        "dogecoin",
        "cardano",
        "solana",
        "tron",
        "polkadot",
        "matic-network",
        "litecoin",
        "shiba-inu",
        "wrapped-bitcoin",
        "uniswap",
        "bitcoin-cash",
        "avalanche-2",
        "the-open-network",
        "dai",
        "stellar",
        "chainlink",
        "leo-token",
        "binance-usd",
        "true-usd",
        "monero",
        "okb",
        "ethereum-classic",
        "cosmos",
        "filecoin",
        "internet-computer",
        "hedera-hashgraph",
        "mantle",
        "lido-dao",
        "crypto-com-chain",
        "aptos",
        "quant-network",
        "arbitrum",
        "vechain",
        "near",
        "optimism",
        "maker",
        "kaspa",
        "xdce-crowd-sale",
        "rocket-pool-eth",
        "the-graph",
        "aave",
        "algorand",
        "the-sandbox",
        "havven",
        "eos",
        "frax",
        "blockstack",
        "whitebit",
        "immutable-x",
        "elrond-erd-2",
        "axie-infinity",
    ]

class Command(BaseCommand):
    help = 'Load all cryptos into AllCryptosList model'


    def handle(self, *args, **kwargs):
        for crypto in cryptocurrencies:
            AllCryptosList.objects.create(id=crypto)
        self.stdout.write(self.style.SUCCESS('Cryptocurrencies loaded successfully.'))