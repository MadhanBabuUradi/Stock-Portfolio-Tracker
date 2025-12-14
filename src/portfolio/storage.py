import sqlite3
from portfolio.models import Stock

DB_FILE = "portfolio.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            symbol TEXT PRIMARY KEY,
            quantity INTEGER,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_stock(stock: Stock):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO stocks (symbol, quantity, price)
        VALUES (?, ?, ?)
    ''', (stock.symbol, stock.quantity, stock.price))
    conn.commit()
    conn.close()

def delete_stock(symbol: str):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('DELETE FROM stocks WHERE symbol = ?', (symbol,))
    conn.commit()
    conn.close()

def load_stocks():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT symbol, quantity, price FROM stocks')
    rows = c.fetchall()
    conn.close()
    return [Stock(symbol=row[0], quantity=row[1], price=row[2]) for row in rows]
