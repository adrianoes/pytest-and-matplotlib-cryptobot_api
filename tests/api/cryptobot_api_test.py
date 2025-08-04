# tests/api/cryptobot_api_test.py

import os
import time
import matplotlib.pyplot as plt
from .support_api import get_binance_btc_brl_price, get_coindesk_btc_brl_price

def test_plot_btc_brl_prices_realtime():
    binance_prices = []
    coindesk_prices = []
    timestamps = []

    # Ensure the 'reports' directory exists
    os.makedirs("reports", exist_ok=True)

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
        plt.pause(0.1)

        print(f"[{round(elapsed, 1)}s] Binance: {price_binance:.2f} | Coindesk: {price_coindesk:.2f}")

    plt.ioff()

    # Save the chart at the end
    fig.savefig("reports/btc_brl_prices_plot.png")

    # Show and close the figure automatically after 10 seconds
    plt.show(block=False)
    time.sleep(10)
    plt.close(fig)
