import requests
from price_providers.base import PriceProvider

class MCXPriceProvider(PriceProvider):

    def __init__(self):
        self.gold_24k_per_10g = None
        self.silver_per_kg = None

    def fetch_mcx_prices(self):
        """
        NOTE:
        For Phase 1, we simulate MCX fetch.
        In production, this method will pull from:
        - MCX official feeds
        - OR authorized data partners
        """

        # ---- TEMP SAFE VALUES (replaceable later) ----
        self.gold_24k_per_10g = 62000   # example MCX value
        self.silver_per_kg = 74000

    def get_gold_price(self):
        if self.gold_24k_per_10g is None:
            self.fetch_mcx_prices()

        # Convert 24K → 22K
        gold_22k = round(self.gold_24k_per_10g * 0.916)
        return gold_22k

    def get_silver_price(self):
        if self.silver_per_kg is None:
            self.fetch_mcx_prices()

        return self.silver_per_kg

    def get_location(self):
        return "Chennai"
