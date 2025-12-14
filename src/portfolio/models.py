from dataclasses import dataclass

@dataclass
class Stock:
    symbol: str
    quantity: int
    price: float  # Manual price

    @property
    def value(self) -> float:
        return round(self.quantity * self.price, 2)
