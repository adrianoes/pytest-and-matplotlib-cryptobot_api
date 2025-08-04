# tests/api/cryptobot_api_test.py

import os
import time
import matplotlib

RUN_ENV = os.getenv("RUN_ENV", "local").lower()

if RUN_ENV == "ci":
    matplotlib.use('Agg')  # Non-interactive backend for CI
else:
    # Para local, pode usar backend padrão com GUI
    pass

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
        now = time.time()
        elapsed = now - start_time
        if elapsed > 30:
            break

        try:
            price_binance = get_binance_btc_brl_price()
            price_coindesk = get_coindesk_btc_brl_price()
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

        if RUN_ENV == "ci":
            time.sleep(0.1)
        else:
            plt.pause(0.1)

        print(f"[{round(elapsed, 1)}s] Binance: {price_binance:.2f} | Coindesk: {price_coindesk:.2f}")

    if RUN_ENV != "ci":
        plt.ioff()

    fig.tight_layout()
    fig.savefig("reports/btc_brl_prices_plot.png", dpi=100, bbox_inches='tight')

    if RUN_ENV != "ci":
        plt.show(block=False)
        time.sleep(10)
        plt.close(fig)
