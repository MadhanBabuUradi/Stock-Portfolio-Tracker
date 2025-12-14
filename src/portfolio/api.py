import yfinance as yf

def get_live_price(symbol: str):
    try:
        stock = yf.Ticker(symbol)
        price = stock.info.get("regularMarketPrice")
        if price:
            return round(price, 2)
        return None
    except Exception:
        return None
