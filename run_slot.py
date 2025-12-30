from datetime import datetime
from pathlib import Path
import sys
import shutil

from price_providers.mcx_provider import MCXPriceProvider
from agents.price_trend_agent import PriceTrendAgent
from agents.strategy_agent import StrategyAgent
from agents.design_agent import DesignAgent
from agents.caption_agent import CaptionAgent

from poster_engine.composer import generate_poster
from utils.helpers import save_poster_metadata


# =====================================================
# SLOT HANDLING (for automation)
# =====================================================
if len(sys.argv) > 1:
    SLOT = sys.argv[1].lower()   # morning / afternoon / evening
else:
    SLOT = "morning"

print(f"\n=== Running Agentic Pipeline for SLOT: {SLOT.upper()} ===\n")


# =====================================================
# STEP 1: FETCH PRICE
# =====================================================
provider = MCXPriceProvider()
gold = provider.get_gold_price()
silver = provider.get_silver_price()
location = provider.get_location()

today = datetime.now().strftime("%Y-%m-%d")


# =====================================================
# STEP 2: ANALYZE TREND
# =====================================================
trend_agent = PriceTrendAgent()
trend = trend_agent.analyze_trend(today, SLOT)


# =====================================================
# STEP 3: DECIDE STRATEGY
# =====================================================
strategy_agent = StrategyAgent()
strategy = strategy_agent.decide_strategy(trend, SLOT)


# =====================================================
# STEP 4: DECIDE DESIGN
# =====================================================
design_agent = DesignAgent()
design_decision = design_agent.decide_design(strategy)


# =====================================================
# STEP 5: GENERATE CAPTION
# =====================================================
caption_agent = CaptionAgent()
caption = caption_agent.generate_caption(trend, SLOT, strategy)


# =====================================================
# STEP 6: GENERATE POSTER
# =====================================================
poster, layout_used, image_used = generate_poster(
    product_folder="assets/products/rings",
    background_folder="assets/backgrounds",
    logo_path="assets/logo/logo.jpeg",
    gold_price=gold,
    silver_price=silver,
    slot=SLOT,
    design_decision=design_decision,
    caption=caption
)


# =====================================================
# STEP 7: SAVE POSTER (ARCHIVE)
# =====================================================
generated_dir = Path("posters/generated")
generated_dir.mkdir(parents=True, exist_ok=True)

output_path = generated_dir / f"{today}_{SLOT}.jpg"
poster.save(output_path)


# =====================================================
# STEP 8: COPY POSTER TO FLASK STATIC (latest.jpg)
# =====================================================
static_posters = Path("static/posters")
static_posters.mkdir(parents=True, exist_ok=True)

latest_static = static_posters / "latest.jpg"
shutil.copyfile(output_path, latest_static)


# =====================================================
# STEP 9: SAVE METADATA
# =====================================================
save_poster_metadata(
    date=today,
    slot=SLOT,
    gold_price=gold,
    silver_price=silver,
    layout=layout_used,
    image_used=image_used,
    poster_path="static/posters/latest.jpg"
)


# =====================================================
# STEP 10: READY-TO-POST OUTPUT (MANUAL POSTING)
# =====================================================
ready_dir = Path("ready_to_post")
ready_dir.mkdir(exist_ok=True)

# Copy poster for posting
ready_poster_path = ready_dir / f"{today}_{SLOT}_poster.jpg"
shutil.copyfile(output_path, ready_poster_path)

# Save caption text
caption_file = ready_dir / f"{today}_{SLOT}_caption.txt"
with open(caption_file, "w", encoding="utf-8") as f:
    f.write(f"{caption['emoji']} {caption['headline']}\n\n")
    f.write(caption["body"] + "\n\n")
    f.write(" ".join(caption["hashtags"]))


# =====================================================
# FINAL LOGS
# =====================================================
print("✅ Poster generated via Agentic AI pipeline")
print("📊 Trend:", trend)
print("🧠 Strategy:", strategy)
print("🎨 Design:", design_decision)
print("📝 Caption:", caption)
print("🖼 Poster saved to:", output_path.resolve())
print("📌 Latest poster copied to:", latest_static.resolve())
print("📦 Ready-to-post poster:", ready_poster_path.resolve())
print("📄 Ready-to-post caption:", caption_file.resolve())
print("\n=== SLOT COMPLETED SUCCESSFULLY ===\n")
