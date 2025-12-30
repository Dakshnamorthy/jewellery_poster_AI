from PIL import Image

POSTER_SIZE = (1080, 1080)  # Instagram standard

def create_canvas(background_path=None):
    if background_path:
        bg = Image.open(background_path).convert("RGB")
        return bg.resize(POSTER_SIZE)
    else:
        return Image.new("RGB", POSTER_SIZE, color=(255, 255, 255))
