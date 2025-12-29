# 🛡️ DeFi Guardian Agent (v0.1 - Simulated)

> **Status:** MVP (Simulated Mode)
> **Built on:** Base, Coinbase AgentKit, CDP
> **Category:** Security Infrastructure / AI Agent

## 📖 Overview
The **DeFi Guardian Agent** is an automated AI security bot designed to protect users from "rug pulls" and sudden market crashes while they sleep.

DeFi users often lose funds because they cannot monitor their positions 24/7. This Agent acts as a "Dead Man Switch" for your portfolio. It monitors the price of a specific asset (e.g., BRETT, DEGEN) every 60 seconds. If the price drops below a user-defined threshold, the Agent executes a protective maneuver.

**Current Version (v0.1):** This is a **Simulated** proof-of-concept. Instead of executing real swaps, it monitors data and "alerts" the console when a protective sale *would* have occurred. This proves the logic without risking real user funds.

## ⚙️ How It Works (The Logic Loop)

1.  **Initialization:** The Agent boots up using **Coinbase AgentKit** and generates a dedicated CDP Wallet.
2.  **Monitoring:** The Agent queries the **Pyth Network** or **Uniswap** oracle on Base every 60 seconds to get the real-time price of the target asset.
3.  **Decision Engine:**
    * *Input:* `Target Price` (e.g., $0.10)
    * *Logic:* `IF current_price < target_price`
    * *Action:* Trigger "Panic Mode."
4.  **Execution (Simulated):**
    * The Agent logs a **High-Priority Alert** to the console/logs: *"⚠️ GUARDIAN ALERT: Price dropped to $0.09. Executing emergency swap to USDC..."*
    * (In v0.2, this step will execute an actual Uniswap transaction).

## 🛠️ Tech Stack

* **Network:** Base Mainnet (for Data)
* **AI Framework:** LangChain (Python)
* **Wallet Infrastructure:** Coinbase Developer Platform (CDP) AgentKit
* **Data Source:** Pyth Network Oracle / CDP Onchain Data

## 🚀 Quick Start

### Prerequisites
* Python 3.10+
* A Coinbase Developer Platform (CDP) API Key

### Installation & Run

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/yourusername/defi-guardian-agent.git](https://github.com/yourusername/defi-guardian-agent.git)
    cd defi-guardian-agent
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Simulation**
    ```bash
    python guardian.py
    ```

## 🗺️ Roadmap

* **Phase 1 (Current):** Read-only simulation. Proves the "Watch & Alert" logic.
* **Phase 2:** Testnet Integration. Agent performs swaps on Base Sepolia using fake USDC.
* **Phase 3:** Mainnet Beta. "Paper Hands" protection live for trusted users.

---
*Built with ❤️ for the Base Builder ecosystem.*
