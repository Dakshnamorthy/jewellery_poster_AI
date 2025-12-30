from agents.caption_agent import CaptionAgent

agent = CaptionAgent()

tests = [
    ("DOWN", "morning", {"focus": "PRICE", "urgency": "HIGH", "tone": "URGENT"}),
    ("UP", "evening", {"focus": "PRICE", "urgency": "MEDIUM", "tone": "PROMOTIONAL"}),
    ("STABLE", "afternoon", {"focus": "PRODUCT", "urgency": "LOW", "tone": "INFORMATIONAL"})
]

for trend, slot, strategy in tests:
    caption = agent.generate_caption(trend, slot, strategy)
    print("\nInput:", trend, slot, strategy)
    print("Output:", caption)
