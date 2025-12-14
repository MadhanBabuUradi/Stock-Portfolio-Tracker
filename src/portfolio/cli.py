from portfolio.stock_universe import load_stock_universe
from portfolio.models import Stock
from portfolio.calculator import PortfolioCalculator
from portfolio.storage import init_db, save_stock, delete_stock, load_stocks
from portfolio.api import get_live_price

from prettytable import PrettyTable
from rich import print
import logging
import sys

# --------------------------------------------------
# Setup
# --------------------------------------------------

logging.basicConfig(
    filename="portfolio.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

init_db()

try:
    STOCK_UNIVERSE = load_stock_universe()
except Exception as e:
    print("[red]Failed to load stock universe[/red]")
    logging.error(e)
    sys.exit(1)

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------

def choose_exchange():
    print("\nAvailable Exchanges: [bold]NSE, NASDAQ[/bold]")
    exchange = input("Choose exchange: ").upper()
    return exchange


def get_available_stocks(exchange):
    return {
        k: v for k, v in STOCK_UNIVERSE.items()
        if v["exchange"] == exchange
    }


def input_quantity_price():
    try:
        quantity = int(input("Quantity: "))
        price = float(input("Price per stock (₹): "))
        if quantity <= 0 or price <= 0:
            raise ValueError
        return quantity, price
    except ValueError:
        print("[red]Invalid quantity or price[/red]")
        return None, None


# --------------------------------------------------
# Menu Actions
# --------------------------------------------------

def add_stock_menu():
    exchange = choose_exchange()
    available = get_available_stocks(exchange)

    if not available:
        print("[red]Invalid exchange[/red]")
        return

    print(f"\nAvailable stocks ({exchange}):")
    print(", ".join(list(available.keys())[:10]), "...")

    symbol = input("Enter stock symbol: ").upper()

    if symbol not in available:
        print("[red]Invalid stock symbol[/red]")
        return

    quantity, price = input_quantity_price()
    if not quantity:
        return

    save_stock(Stock(symbol, quantity, price))
    logging.info(f"Added {symbol}")
    print(f"[green]Added {symbol} ({available[symbol]['name']})[/green]")


def delete_stock_menu():
    symbol = input("Enter stock symbol to delete: ").upper()
    delete_stock(symbol)
    logging.info(f"Deleted {symbol}")
    print(f"[green]{symbol} removed (if existed)[/green]")


def list_stocks_menu():
    stocks = load_stocks()

    if not stocks:
        print("[yellow]No stocks found[/yellow]")
        return

    table = PrettyTable(["Symbol", "Quantity", "Buy Price (₹)", "Value (₹)"])

    for s in stocks:
        table.add_row([s.symbol, s.quantity, s.price, s.value])

    print(table)


def summary_menu(live=False):
    stocks = load_stocks()

    if not stocks:
        print("[yellow]No stocks found[/yellow]")
        return

    table = PrettyTable(["Symbol", "Qty", "Price (₹)", "Value (₹)"])
    total = 0

    for s in stocks:
        price = s.price
        if live:
            live_price = get_live_price(s.symbol)
            if live_price:
                price = live_price

        value = round(price * s.quantity, 2)
        total += value
        table.add_row([s.symbol, s.quantity, price, value])

    print(table)
    print(f"[bold green]Total Portfolio Value: ₹{round(total, 2)}[/bold green]")


# --------------------------------------------------
# Main Menu Loop
# --------------------------------------------------

def menu():
    while True:
        print("\n[bold cyan]📊 Stock Portfolio Manager[/bold cyan]")
        print("1. Add Stock")
        print("2. Delete Stock")
        print("3. List Stocks")
        print("4. Portfolio Summary")
        print("5. Live Portfolio Summary")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        try:
            if choice == "1":
                add_stock_menu()
            elif choice == "2":
                delete_stock_menu()
            elif choice == "3":
                list_stocks_menu()
            elif choice == "4":
                summary_menu(live=False)
            elif choice == "5":
                summary_menu(live=True)
            elif choice == "6":
                print("[bold]Exiting...[/bold]")
                break
            else:
                print("[red]Invalid choice[/red]")
        except Exception as e:
            logging.error(e)
            print("[red]Unexpected error occurred[/red]")


if __name__ == "__main__":
    menu()
