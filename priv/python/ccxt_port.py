# coding=utf-8

import time
import ccxt  
import json

def exchanges(): 
    exchanges = {}  

    for id in ccxt.exchanges:
        exchange = getattr(ccxt, id)
        exchanges[id] = exchange()
    return exchanges


def fetch_markets_for_exchange(exchange_id):
    exchange = exchanges()[exchange_id]
    res = exchange.load_markets()
    return json.dumps(res)

def fetch_ohlcv(exchange_id, symbol, timeframe, since, limit):
    exchange = exchanges()[exchange_id]
    res = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
    return json.dumps(res)