from bond import * 

class governmentbond(Bond):
    def __init__(self, name, value, risk_level, industry):
        super().__init__(name, value, risk_level, industry)
        self.bond_type = "Government"

    def __str__(self):
        return f"{self.name} (Government Bond) - Value: {self.value}, Risk: {self.risk_level}, Industry: {self.industry}"
