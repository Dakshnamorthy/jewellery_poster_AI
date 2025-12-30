from run_slot import SLOT
import subprocess

def regenerate_poster():
    # Re-run agent pipeline
    subprocess.run(["python", "run_slot.py"])
