import json
from pathlib import Path

PRICE_FILE = Path("data/prices/prices.json")

SLOT_ORDER = ["morning", "afternoon", "evening"]

class PriceTrendAgent:

    def analyze_trend(self, date, slot):
        # If price file doesn't exist
        if not PRICE_FILE.exists():
            return "STABLE"

        data = json.loads(PRICE_FILE.read_text())

        # If date not present
        if date not in data:
            return "STABLE"

        day_data = data[date]

        # If current slot price not yet available
        if slot not in day_data:
            return "STABLE"

        slot_index = SLOT_ORDER.index(slot)

        # First slot has no previous comparison
        if slot_index == 0:
            return "STABLE"

        prev_slot = SLOT_ORDER[slot_index - 1]

        # If previous slot price not available
        if prev_slot not in day_data:
            return "STABLE"

        current_price = day_data[slot]["gold_22k"]
        prev_price = day_data[prev_slot]["gold_22k"]

        if current_price > prev_price:
            return "UP"
        elif current_price < prev_price:
            return "DOWN"
        else:
            return "STABLE"
