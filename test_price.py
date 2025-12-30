from price_providers.mcx_provider import MCXPriceProvider
from utils.helpers import save_daily_price

SLOT = "afternoon"   # morning / afternoon / evening

provider = MCXPriceProvider()

gold = provider.get_gold_price()
silver = provider.get_silver_price()
location = provider.get_location()

print("Gold 22K:", gold)
print("Silver:", silver)
print("Location:", location)
print("Slot:", SLOT)

save_daily_price(gold, silver, location, SLOT)
