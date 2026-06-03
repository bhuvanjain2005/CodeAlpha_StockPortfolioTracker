stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

print("Available Stocks:")

for stock, price in stocks.items():
    print(stock, "=", "$" + str(price))

stock_name = input("\nEnter Stock Name: ").upper()

quantity = int(input("Enter Quantity: "))

if stock_name in stocks:

    investment = stocks[stock_name] * quantity

    print("\nInvestment Value = $", investment)

    with open("portfolio.txt", "w") as file:
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Investment Value: ${investment}")

    print("Portfolio saved to portfolio.txt")

else:
    print("Stock not found!")