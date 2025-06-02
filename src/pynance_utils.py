from pynance import data
import logging

def get_current_price(ticker):
    try:
        price = data.get_price(ticker)
        return price
    except Exception as e:
        logging.error(f"pynance error for {ticker}: {e}")
        return None
