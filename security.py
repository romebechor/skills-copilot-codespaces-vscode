from abc import ABC, abstractmethod

class Security(ABC):
    def __init__(self, name, value, risk_level, industry):
        self.name = name
        self.value = value
        self.risk_level = risk_level
        self.industry = industry

    @abstractmethod
    def calculate_risk(self):
        pass

    def __str__(self):
        return f"{self.name} - Value: {self.value}, Risk: {self.risk_level}, Industry: {self.industry}"
