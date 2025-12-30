class DesignAgent:

    def decide_design(self, strategy):
        focus = strategy["focus"]
        urgency = strategy["urgency"]

        design = {
            "layout": "center_focus",
            "price_size": "MEDIUM",
            "image_priority": "MEDIUM"
        }

        if focus == "PRICE":
            design["layout"] = "center_focus"
            design["image_priority"] = "LOW"

            if urgency == "HIGH":
                design["price_size"] = "LARGE"
            elif urgency == "MEDIUM":
                design["price_size"] = "MEDIUM"

        elif focus == "PRODUCT":
            design["layout"] = "left_focus"
            design["image_priority"] = "HIGH"
            design["price_size"] = "SMALL"

        return design
