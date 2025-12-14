from portfolio.models import Stock
from portfolio.calculator import PortfolioCalculator

def test_total_portfolio_value():
    stocks = [Stock("AAPL", 10, 100), Stock("TSLA", 5, 200)]
    assert PortfolioCalculator.total_portfolio_value(stocks) == 2000
