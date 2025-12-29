import time
import os
import random

# NOTE: In a real environment, you would use 'python-dotenv' to load keys
# from a .env file. For this v0.1 Simulation, we run locally.

class DeFiGuardian:
    def __init__(self, asset_name, stop_loss_price):
        self.asset = asset_name
        self.stop_loss = stop_loss_price
        self.is_running = True
        print(f"🤖 Guardian Agent Initialized for {self.asset}")
        print(f"🛡️ Safety Threshold set at: ${self.stop_loss}")

    def get_mock_price(self):
        # In a real app, this calls the Pyth/Coinbase API.
        # For this v0.1 Simulation, we simulate market fluctuation.
        # It returns a random price between $0.08 and $0.12
        return round(random.uniform(0.08, 0.12), 3)

    def monitor(self):
        print("--------------------------------")
        print("👁️  Watching markets...")
        
        while self.is_running:
            current_price = self.get_mock_price()
            print(f"📉 Current {self.asset} Price: ${current_price}")

            if current_price < self.stop_loss:
                self.trigger_emergency_swap(current_price)
                # Stop running after "saving" the funds
                self.is_running = False 
            else:
                print("✅ Funds are safe. Sleeping for 5 seconds...")
                time.sleep(5)

    def trigger_emergency_swap(self, price):
        print("\n🚨 🚨 ALERT: STOP LOSS TRIGGERED! 🚨 🚨")
        print(f"CRASH DETECTED AT ${price}")
        print("🔄 SIMULATING: Swapping 100% of portfolio to USDC...")
        time.sleep(1)
        print("✅ SUCCESS: Funds saved in USDC. Transaction Hash: 0x7a9...simulated")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # We want to protect "BRETT" if it drops below $0.10
    agent = DeFiGuardian(asset_name="BRETT", stop_loss_price=0.10)
    agent.monitor()
          
