# Stock-Portfolio-Tracker



Importing Required Modules :
--> import requests
--> from prettytable import PrettyTable

Setting Up API Configuration :
--> API_KEY = "YOUR_API_KEY"
--> BASE_URL = "https://www.alphavantage.co/query"

Runs a menu-driven loop : 
Add Stock - Takes stock symbol and shares, then calls add_stock().

Remove Stock - Takes stock symbol and shares, then calls remove_stock().

View Portfolio - Calls display_portfolio().

Exit - Terminates the program.

Output : 
--> Stock Portfolio Tracker
1. Add Stock
2. Remove Stock
3. View Portfolio
4. Exit
Enter your choice: 1
Enter stock symbol: AAPL
Enter number of shares: 10
Added 10 shares of AAPL.

Stock Portfolio Tracker
1. Add Stock
2. Remove Stock
3. View Portfolio
4. Exit
Enter your choice: 3

+-------+--------+------------+----------------+
| Stock | Shares | Price (USD) | Total Value (USD) |

+-------+--------+------------+----------------+

| AAPL  |   10   |  180.25    |    1802.50    |
+-------+--------+------------+----------------+

Total Portfolio Value: $1802.50

