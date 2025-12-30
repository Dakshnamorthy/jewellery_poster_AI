class ApprovalAgent:

    def process_decision(self, decision):
        if decision == "APPROVE":
            return {
                "action": "PUBLISH",
                "message": "Poster approved and ready for posting"
            }

        if decision == "REJECT":
            return {
                "action": "REGENERATE",
                "message": "Poster rejected. Regenerating a new poster."
            }

        return {
            "action": "WAIT",
            "message": "Waiting for valid decision"
        }
