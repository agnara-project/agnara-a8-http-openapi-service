from dataclasses import dataclass

@dataclass
class OrderCreate:
    amount: float
    currency: str

@dataclass
class OrderResponse:
    id: str
    amount: float
    currency: str
    status: str

@dataclass
class CancelReason:
    reason: str
