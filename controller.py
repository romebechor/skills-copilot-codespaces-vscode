class PortfolioController:
    def __init__(self):
        self.portfolio = Portfolio()  # תיק ההשקעות
        self.db = Database()  # חיבור למסד נתונים
        self.db.create_table()  # יצירת טבלה אם אין כזאת

    def run(self):
        while True:
            print("\nSelect an option:")
            print("1. Buy Regular Stock")
            print("2. Buy Preferred Stock")
            print("3. Buy Government Bond")
            print("4. Buy Corporate Bond")
            print("5. Sell Security")
            print("6. Display Portfolio")
            print("7. Set Risk Level")
            print("8. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.buy_regular_stock()
            elif choice == '2':
                self.buy_preferred_stock()
            elif choice == '3':
                self.buy_government_bond()
            elif choice == '4':
                self.buy_corporate_bond()
            elif choice == '5':
                self.sell_security()
            elif choice == '6':
                self.display_portfolio()
            elif choice == '7':
                self.set_risk_level()
            elif choice == '8':
                break

    def buy_regular_stock(self):
        name = input("Enter stock name: ")
        value = float(input("Enter stock value: "))
        risk_level = input("Enter stock risk level (High/Low/Medium): ")
        industry = input("Enter stock industry: ")
        stock = Stock(name, value, risk_level, industry)
        self.portfolio.add_security(stock)
        self.db.insert_security(stock)
        print(f"Bought regular stock: {stock}")

    def buy_preferred_stock(self):
        name = input("Enter stock name: ")
        value = float(input("Enter stock value: "))
        risk_level = input("Enter stock risk level (High/Low/Medium): ")
        industry = input("Enter stock industry: ")
        stock = Stock(name, value, risk_level, industry, stock_type="Preferred")
        self.portfolio.add_security(stock)
        self.db.insert_security(stock)
        print(f"Bought preferred stock: {stock}")

    def buy_government_bond(self):
        name = input("Enter bond name: ")
        value = float(input("Enter bond value: "))
        risk_level = input("Enter bond risk level (High/Low/Medium): ")
        industry = input("Enter bond industry: ")
        bond = Bond(name, value, risk_level, industry, bond_type="Government")
        self.portfolio.add_security(bond)
        self.db.insert_security(bond)
        print(f"Bought government bond: {bond}")

    def buy_corporate_bond(self):
        name = input("Enter bond name: ")
        value = float(input("Enter bond value: "))
        risk_level = input("Enter bond risk level (High/Low/Medium): ")
        industry = input("Enter bond industry: ")
        bond = Bond(name, value, risk_level, industry, bond_type="Corporate")
        self.portfolio.add_security(bond)
        self.db.insert_security(bond)
        print(f"Bought corporate bond: {bond}")

    def sell_security(self):
        name = input("Enter the name of the security to sell: ")
        for security in self.portfolio.securities:
            if security.name == name:
                self.portfolio.remove_security(security)
                print(f"Sold: {security}")
                break
        else:
            print("Security not found.")

    def display_portfolio(self):
        print("\nPortfolio Overview:")
        print(self.portfolio)

    def set_risk_level(self):
        risk = input("Enter desired risk level (Low/Medium/High): ")
        self.portfolio.set_risk_profile(risk)
        print(f"Risk level set to {risk}.")
