from agents.design_agent import DesignAgent

agent = DesignAgent()

strategies = [
    {"focus": "PRICE", "urgency": "HIGH", "tone": "URGENT"},
    {"focus": "PRICE", "urgency": "MEDIUM", "tone": "PROMOTIONAL"},
    {"focus": "PRODUCT", "urgency": "LOW", "tone": "INFORMATIONAL"}
]

for strategy in strategies:
    design = agent.decide_design(strategy)
    print(f"Strategy={strategy} → Design={design}")
