"""
AYUNGO BITOTO - THE PYTHON QUEST
"I'll be changing the tech world with Python."
"""

import sys
import time

# Ensure safe output encoding on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class AyungoBitotoQuest:
    def __init__(self):
        self.developer = "Ayungo Bitoto"
        self.motto = "I'll be changing the tech world with Python."
        self.weapon = f"Python {sys.version.split()[0]}"
        self.pillars = [
            ("Core Algorithmic Precision", "Writing pure, readable, high-performance logic"),
            ("Distributed Concurrency", "Architecting scalable asynchronous backends"),
            ("Artificial Intelligence", "Orchestrating autonomous agents & neural pipelines"),
            ("Global Transformation", "Disrupting tech and empowering human potential")
        ]

    def launch(self):
        print("=" * 64)
        print(f"[>] DEVELOPER : {self.developer}")
        print(f"[*] RUNTIME   : {self.weapon}")
        print(f"[!] MISSION   : \"{self.motto}\"")
        print("=" * 64)
        print("\n[INITIATING THE 4 PILLARS OF TRANSFORMATION]:\n")

        for idx, (pillar, description) in enumerate(self.pillars, 1):
            time.sleep(0.05)
            print(f"  [{idx}/4] {pillar.upper()}")
            print(f"        -> {description}")

        print("\n" + "-" * 64)
        print(">> STATUS: UNSTOPPABLE. The tech world will never be the same.")
        print("=" * 64)

if __name__ == "__main__":
    quest = AyungoBitotoQuest()
    quest.launch()
