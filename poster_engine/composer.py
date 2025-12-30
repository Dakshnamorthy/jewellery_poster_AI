from PIL import Image, ImageDraw
from datetime import datetime
from poster_engine.canvas import create_canvas
from poster_engine.layouts import LAYOUTS
from utils.helpers import get_random_image
from utils.helpers import load_font, get_random_image

def generate_poster(
    product_folder,
    background_folder,
    logo_path,
    gold_price,
    silver_price,
    slot,
    design_decision,
    caption
):
    layout_name = design_decision["layout"]
    layout = LAYOUTS[layout_name]

    canvas = create_canvas(get_random_image(background_folder))
    draw = ImageDraw.Draw(canvas)

    product_path = get_random_image(product_folder)
    product = Image.open(product_path).convert("RGBA")
    product = product.resize(layout["product_size"])

    logo = Image.open(logo_path).convert("RGBA")
    logo = logo.resize((180, 180))

    canvas.paste(product, layout["product_position"], product)
    canvas.paste(logo, (30, 30), logo)

    # Font sizes based on design decision
    price_size = 56 if design_decision["price_size"] == "LARGE" else 42
    font_price = load_font(price_size)
    font_text = load_font(32)

    today = datetime.now().strftime("%d-%m-%Y")
    y = layout["text_start_y"]

    # Prices
    draw.text((300, y), f"Gold 22K: ₹{gold_price}", fill="black", font=font_price)
    draw.text((300, y + 60), f"Silver: ₹{silver_price}", fill="black", font=font_price)

    # Caption text
    draw.text((300, y + 130), caption["headline"], fill="black", font=font_text)
    draw.text((300, y + 170), caption["body"], fill="gray", font=font_text)

    # Footer
    draw.text((300, y + 230), f"{slot.capitalize()} | {today}", fill="gray", font=font_text)

    return canvas, layout_name, product_path
