# Successful Implementation Patterns

## Design Patterns That Work

### Repository Pattern for Data Access
```python
from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')

class Repository(ABC, Generic[T]):
    @abstractmethod
    async def get(self, id: int) -> Optional[T]:
        pass
    
    @abstractmethod
    async def get_all(self) -> List[T]:
        pass
    
    @abstractmethod
    async def add(self, entity: T) -> T:
        pass
    
    @abstractmethod
    async def update(self, entity: T) -> T:
        pass
    
    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass

class UserRepository(Repository[User]):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get(self, id: int) -> Optional[User]:
        result = await self.session.execute(
            select(User).where(User.id == id)
        )
        return result.scalar_one_or_none()
```

### Factory Pattern for Object Creation
```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class StripeGateway(PaymentGateway):
    def pay(self, amount: float):
        print(f"Paying {amount} via Stripe")

class PaypalGateway(PaymentGateway):
    def pay(self, amount: float):
        print(f"Paying {amount} via Paypal")

def get_payment_gateway(gateway: str) -> PaymentGateway:
    if gateway == "stripe":
        return StripeGateway()
    elif gateway == "paypal":
        return PaypalGateway()
    raise ValueError("Unknown Gateway")
```

### Strategy Pattern for Varying Algorithms
```python
from typing import Protocol

class DiscountStrategy(Protocol):
    def apply_discount(self, price: float) -> float:
        ...

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, price: float) -> float:
        return price * (1 - self.percentage / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, price: float) -> float:
        return max(0, price - self.amount)

class Order:
    def __init__(self, price: float, strategy: DiscountStrategy):
        self.price = price
        self.strategy = strategy

    def get_final_price(self) -> float:
        return self.strategy.apply_discount(self.price)