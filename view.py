class PortfolioView:
    def display_portfolio(self, portfolio):
        print("\n--- Your Investment Portfolio ---")
        if not portfolio.securities:
            print("Your portfolio is empty.")
        else:
            for security in portfolio.securities:
                print(security)
            print(f"Total Risk: {portfolio.calculate_total_risk():.2f}")

    def get_user_input(self):
        print("\nSelect an option:")
        print("1. Buy Stock")
        print("2. Buy Bond")
        print("3. Sell Security")
        print("4. Display Portfolio")
        print("5. Exit")
        return input("Choose an option (1-5): ")

    def get_stock_input(self):
        name = input("Enter stock name: ")
        value = float(input("Enter stock value: "))
        risk_level = float(input("Enter stock risk level: "))
        dividend_yield = float(input("Enter stock dividend yield: "))
        return Stock(name, value, risk_level, dividend_yield)

    def get_bond_input(self):
        name = input("Enter bond name: ")
        value = float(input("Enter bond value: "))
        risk_level = float(input("Enter bond risk level: "))
        interest_rate = float(input("Enter bond interest rate: "))
        return Bond(name, value, risk_level, interest_rate)
