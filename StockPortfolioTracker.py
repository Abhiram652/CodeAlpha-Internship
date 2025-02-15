import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
    
    def add_stock(self, ticker, shares):
        if ticker in self.portfolio:
            self.portfolio[ticker] += shares
        else:
            self.portfolio[ticker] = shares
        print(f"Added {shares} shares of {ticker}.")
    
    def remove_stock(self, ticker, shares):
        if ticker in self.portfolio:
            if self.portfolio[ticker] > shares:
                self.portfolio[ticker] -= shares
                print(f"Removed {shares} shares of {ticker}.")
            elif self.portfolio[ticker] == shares:
                del self.portfolio[ticker]
                print(f"Removed all shares of {ticker}.")
            else:
                print("Not enough shares to remove.")
        else:
            print("Stock not found in portfolio.")
    
    def view_portfolio(self):
        if not self.portfolio:
            print("Portfolio is empty.")
            return
        
        print("\nYour Portfolio:")
        for ticker, shares in self.portfolio.items():
            stock = yf.Ticker(ticker)
            price = stock.history(period='1d')['Close'].iloc[-1]
            total_value = shares * price
            print(f"{ticker}: {shares} shares @ ${price:.2f} each, Total Value: ${total_value:.2f}")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(ticker, shares)
        elif choice == "2":
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(ticker, shares)
        elif choice == "3":
            portfolio.view_portfolio()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")
