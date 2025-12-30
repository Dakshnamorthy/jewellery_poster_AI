import json
from datetime import datetime
from pathlib import Path

PRICE_FILE = Path("data/prices/prices.json")

def save_daily_price(gold, silver, location, slot):
    PRICE_FILE.parent.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    data = {}
    if PRICE_FILE.exists():
        content = PRICE_FILE.read_text().strip()
        if content:
            data = json.loads(content)

    if today not in data:
        data[today] = {}

    data[today][slot] = {
        "time": datetime.now().strftime("%H:%M"),
        "gold_22k": gold,
        "silver": silver,
        "location": location
    }

    PRICE_FILE.write_text(json.dumps(data, indent=4))

import random
from pathlib import Path

def get_random_image(folder_path):
    images = list(Path(folder_path).glob("*"))
    if not images:
        raise ValueError(f"No images found in {folder_path}")
    return str(random.choice(images))

def save_poster_metadata(
    date,
    slot,
    gold_price,
    silver_price,
    layout,
    image_used,
    poster_path
):
    metadata_file = Path("data/posters/metadata.json")
    metadata_file.parent.mkdir(parents=True, exist_ok=True)

    data = {}
    if metadata_file.exists():
        content = metadata_file.read_text().strip()
        if content:
            data = json.loads(content)

    key = f"{date}_{slot}"

    data[key] = {
        "date": date,
        "slot": slot,
        "gold_22k": gold_price,
        "silver": silver_price,
        "layout": layout,
        "image_used": image_used,
        "poster_path": poster_path
    }

    metadata_file.write_text(json.dumps(data, indent=4))

from PIL import ImageFont
from pathlib import Path
import random

FONTS_DIR = Path("utils/fonts")

def load_font(size):
    """
    Loads a random TTF font from utils/fonts.
    Falls back to default font if loading fails.
    """
    try:
        font_files = list(FONTS_DIR.glob("*.ttf"))
        if not font_files:
            raise FileNotFoundError("No font files found")

        font_path = random.choice(font_files)
        return ImageFont.truetype(str(font_path), size)

    except Exception as e:
        # Fallback – never crash poster generation
        return ImageFont.load_default()
