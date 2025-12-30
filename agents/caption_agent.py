class CaptionAgent:

    def generate_caption(self, trend, slot, strategy):
        caption = {
            "headline": "",
            "body": "",
            "emoji": "",
            "hashtags": ["#GoldRate", "#SilverRate", "#ChennaiJewellery"]
        }

        # Headline & emoji
        if trend == "DOWN":
            caption["headline"] = "இன்றைய தங்கம் விலை குறைந்துள்ளது"
            caption["emoji"] = "📉"
        elif trend == "UP":
            caption["headline"] = "இன்றைய தங்கம் விலை உயர்ந்துள்ளது"
            caption["emoji"] = "📈"
        else:
            caption["headline"] = "இன்றைய தங்கம் விலை நிலையாக உள்ளது"
            caption["emoji"] = "➖"

        # Body text based on strategy
        if strategy["urgency"] == "HIGH":
            caption["body"] = "இன்றைய சிறப்பு விலையில் நகைகள் வாங்க சிறந்த நேரம்!"
        elif strategy["focus"] == "PRODUCT":
            caption["body"] = "உங்கள் விருப்பமான நகைகளை இன்று தேர்வு செய்யுங்கள்."
        else:
            caption["body"] = "இன்றைய தங்கம் மற்றும் வெள்ளி விலைகளை பார்க்கவும்."

        # Slot-based enhancement
        if slot == "evening":
            caption["body"] += " இன்று மாலை சலுகையை தவற விடாதீர்கள்."

        return caption
