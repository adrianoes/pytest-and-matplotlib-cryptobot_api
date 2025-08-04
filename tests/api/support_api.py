# tests/api/support_api.py
import requests

def get_binance_btc_brl_price():
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCBRL"
    response = requests.get(url)
    data = response.json()
    return float(data['lastPrice'])

def get_coindesk_btc_brl_price():
    url = "https://data-api.coindesk.com/index/cc/v1/latest/tick?market=cadli&instruments=BTC-BRL&apply_mapping=true"
    response = requests.get(url)
    data = response.json()
    return float(data["Data"]["BTC-BRL"]["VALUE"])
