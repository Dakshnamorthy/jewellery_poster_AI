from poster_engine.composer import generate_poster
from price_providers.mcx_provider import MCXPriceProvider
from utils.helpers import save_daily_price
from datetime import datetime
from pathlib import Path

SLOT = "evening"  # morning / afternoon / evening

provider = MCXPriceProvider()

gold = provider.get_gold_price()
silver = provider.get_silver_price()
location = provider.get_location()

# Generate poster
poster, layout_used, image_used = generate_poster(
    product_folder="assets/products/rings",
    background_folder="assets/backgrounds",
    logo_path="assets/logo/logo.jpeg",
    gold_price=gold,
    silver_price=silver,
    slot=SLOT
)


# Save poster
from datetime import datetime
from pathlib import Path
from utils.helpers import save_poster_metadata

SLOT = "morning"

# define today ONCE
today = datetime.now().strftime("%Y-%m-%d")

output_dir = Path("posters/generated")
output_dir.mkdir(parents=True, exist_ok=True)

output_path = output_dir / f"{today}_{SLOT}.jpg"
poster.save(output_path)

save_poster_metadata(
    date=today,
    slot=SLOT,
    gold_price=gold,
    silver_price=silver,
    layout=layout_used,
    image_used=image_used,
    poster_path=str(output_path)
)

print(f"Poster saved at: {output_path}")

