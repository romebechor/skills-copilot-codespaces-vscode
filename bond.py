from Security import * 
class Bond(Security):
    def __init__(self, name, value, risk_level, industry):
        super().__init__(name, value, risk_level, industry)

    def __str__(self):
        return f"{self.name} (Bond) - Value: {self.value}, Risk: {self.risk_level}, Industry: {self.industry}"
