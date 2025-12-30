from agents.strategy_agent import StrategyAgent

agent = StrategyAgent()

tests = [
    ("UP", "morning"),
    ("UP", "evening"),
    ("DOWN", "afternoon"),
    ("STABLE", "evening")
]

for trend, slot in tests:
    decision = agent.decide_strategy(trend, slot)
    print(f"Trend={trend}, Slot={slot} → {decision}")
