# tests/api/cryptobot_api_test.py

import os
import time
import json
import matplotlib
import requests

RUN_ENV = os.getenv("RUN_ENV", "local").lower()

if RUN_ENV == "ci":
    matplotlib.use('Agg')  # Non-interactive backend for CI

import matplotlib.pyplot as plt
from .support_api import get_binance_btc_brl_price, get_coindesk_btc_brl_price

def test_plot_btc_brl_prices_realtime():
    binance_prices = []
    coindesk_prices = []
    timestamps = []

    os.makedirs("reports", exist_ok=True)

    if RUN_ENV != "ci":
        plt.ion()

    fig, ax = plt.subplots()
    line1, = ax.plot([], [], 'o-', label="Binance BTC/BRL", color="blue", markersize=4)
    line2, = ax.plot([], [], 'o-', label="Coindesk BTC/BRL", color="orange", markersize=4)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Price (R$)")
    ax.set_title("BTC/BRL - Binance vs Coindesk (30s)")
    ax.legend()

    start_time = time.time()

    while True:
        elapsed = time.time() - start_time
        if elapsed > 30:
            break

        try:
            # fetch prices
            price_binance = get_binance_btc_brl_price()
            price_coindesk = get_coindesk_btc_brl_price()

            # log Binance response (CI only)
            if RUN_ENV == "ci":
                binance_resp = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCBRL", timeout=5)
                with open("reports/binance_response_ci.json", "w") as f:
                    json.dump(binance_resp.json(), f, indent=2)

        except Exception as e:
            print("Error fetching data:", e)
            continue

        binance_prices.append(price_binance)
        coindesk_prices.append(price_coindesk)
        timestamps.append(round(elapsed, 1))

        line1.set_data(timestamps, binance_prices)
        line2.set_data(timestamps, coindesk_prices)

        ax.relim()
        ax.autoscale_view()

        print(f"[{round(elapsed, 1)}s] Binance: {price_binance:.2f} | Coindesk: {price_coindesk:.2f}")

        time.sleep(1)  # <= 1 request per second

    if RUN_ENV != "ci":
        plt.ioff()

    fig.tight_layout()
    fig.savefig("reports/btc_brl_prices_plot.png", dpi=100, bbox_inches='tight')

    if RUN_ENV != "ci":
        plt.show(block=False)
        time.sleep(10)
        plt.close(fig)
