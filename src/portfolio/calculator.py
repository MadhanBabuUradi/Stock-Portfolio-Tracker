from typing import List
from portfolio.models import Stock

class PortfolioCalculator:
    @staticmethod
    def total_portfolio_value(stocks: List[Stock]) -> float:
        return round(sum(stock.value for stock in stocks), 2)
