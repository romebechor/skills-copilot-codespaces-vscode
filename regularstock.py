from stock import Stock

class regularstock(Stock):
    def __init__(self, name, sector, risk_level, price):
        super().__init__(name, sector, risk_level, price, "regular")
