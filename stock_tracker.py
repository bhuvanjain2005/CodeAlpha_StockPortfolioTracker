stocks = {
    "RELIANCE": 1450,
    "TCS": 3800,
    "INFY": 1600,
    "HDFCBANK": 1700,
    "ICICIBANK": 1200,
    "SBIN": 850,
    "ITC": 430,
    "WIPRO": 520
}

print("📈 Indian Stock Portfolio Tracker")
print("\nAvailable Stocks:")

for stock, price in stocks.items():
    print(stock, "= ₹" + str(price))

stock_name = input("\nEnter Stock Name: ").upper()

quantity = int(input("Enter Quantity: "))

if stock_name in stocks:

    investment = stocks[stock_name] * quantity

    print("\nInvestment Value = ₹", investment)

    with open("portfolio.txt", "w", encoding="utf-8") as file:
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Investment Value: ₹{investment}")

    print("Portfolio saved to portfolio.txt")

else:
    print("Stock not found!")