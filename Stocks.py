import requests
from prettytable import PrettyTable


API_KEY = "YOUR_API_KEY"
BASE_URL = "https://www.alphavantage.co/query"

portfolio = {}

def add_stock(symbol, shares):
    
    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares
    print(f"Added {shares} shares of {symbol}.")

def remove_stock(symbol, shares):
    if symbol in portfolio:
        if portfolio[symbol] > shares:
            portfolio[symbol] -= shares
            print(f"Removed {shares} shares of {symbol}.")
        elif portfolio[symbol] == shares:
            del portfolio[symbol]
            print(f"Removed all shares of {symbol}.")
        else:
            print("Error: You don't own enough shares to remove.")
    else:
        print("Error: Stock not in portfolio.")

def fetch_stock_price(symbol):
    try:
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": API_KEY,
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        return float(data["Global Quote"]["05. price"])
    except (KeyError, ValueError):
        print(f"Error fetching price for {symbol}.")
        return None

def display_portfolio():
    table = PrettyTable()
    table.field_names = ["Stock", "Shares", "Price (USD)", "Total Value (USD)"]
    total_value = 0

    for symbol, shares in portfolio.items():
        price = fetch_stock_price(symbol)
        if price is not None:
            total = price * shares
            total_value += total
            table.add_row([symbol, shares, f"{price:.2f}", f"{total:.2f}"])
        else:
            table.add_row([symbol, shares, "N/A", "N/A"])

    print(table)
    print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == "2":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            remove_stock(symbol, shares)
        elif choice == "3":
            display_portfolio()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
