from bond import * 
class corporatebond(Bond):
    def __init__(self, name, value, risk_level, industry):
        super().__init__(name, value, risk_level, industry)
        self.bond_type = "Corporate"

    def __str__(self):
        return f"{self.name} (Corporate Bond) - Value: {self.value}, Risk: {self.risk_level}, Industry: {self.industry}"
