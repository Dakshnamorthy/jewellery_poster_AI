from flask import Flask, render_template, request, redirect, url_for
from agents.approval_agent import ApprovalAgent
import subprocess

app = Flask(__name__)
approval_agent = ApprovalAgent()

@app.route("/")
def index():
    # Always show latest poster
    return render_template("approval.html")

@app.route("/decision", methods=["POST"])
def decision():
    decision = request.form.get("decision")
    result = approval_agent.process_decision(decision)

    if result["action"] == "REGENERATE":
        # Run the agentic pipeline again to generate a new poster
        subprocess.run(["python", "run_slot.py", "evening"])

    elif result["action"] == "PUBLISH":
        print("✅ Poster approved and ready for posting")

    # Always return back to the same approval page
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
