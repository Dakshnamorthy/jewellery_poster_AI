from agents.price_trend_agent import PriceTrendAgent
from datetime import datetime

agent = PriceTrendAgent()

today = datetime.now().strftime("%Y-%m-%d")
slot = "afternoon"  # test different slots

trend = agent.analyze_trend(today, slot)
print("Trend:", trend)
