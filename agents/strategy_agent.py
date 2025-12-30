class StrategyAgent:

    def decide_strategy(self, trend, slot):
        strategy = {
            "focus": "PRODUCT",
            "urgency": "LOW",
            "tone": "INFORMATIONAL"
        }

        if trend == "DOWN":
            strategy["focus"] = "PRICE"
            strategy["urgency"] = "HIGH"
            strategy["tone"] = "URGENT"

        elif trend == "UP":
            if slot == "evening":
                strategy["focus"] = "PRICE"
                strategy["urgency"] = "MEDIUM"
                strategy["tone"] = "PROMOTIONAL"

        elif trend == "STABLE":
            if slot == "evening":
                strategy["focus"] = "PRICE"
                strategy["tone"] = "NEUTRAL"

        return strategy
    