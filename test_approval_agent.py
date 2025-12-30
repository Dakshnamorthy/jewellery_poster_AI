from agents.approval_agent import ApprovalAgent

agent = ApprovalAgent()

tests = [
    ("APPROVE", None),
    ("REJECT", "Layout not good"),
    ("MODIFY", "Change wording")
]

for decision, reason in tests:
    result = agent.process_decision(decision, reason)
    print(f"Decision={decision} → {result}")
