import csv
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "stocks.csv"

def load_stock_universe():
    universe = {}

    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            universe[row["symbol"]] = {
                "name": row["name"],
                "exchange": row["exchange"]
            }

    return universe
