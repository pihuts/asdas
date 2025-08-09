# Connection Refactor Plan

This document outlines the plan to refactor the connection classes to unify bolted and welded connections.

## 1. Unified `Connection` Class

A new `Connection` data class will be added to `steel_lib/data_models.py`. This class will serve as a single interface for all connection types.

```python
from typing import Union, Literal

# ... existing code ...

@dataclass
class Connection:
    """A unified connection class that can represent either a bolted or welded connection."""
    connection_type: Literal["bolted", "welded"]
    configuration: Union[BoltConfiguration, WeldConfiguration]
```

This change introduces a generic `Connection` class that holds either a `BoltConfiguration` or a `WeldConfiguration`.

## 2. Refactor Calculation Classes

The calculation classes in `steel_lib/calculations.py` will be updated to accept the new `Connection` class. This will involve checking the `connection_type` and then accessing the appropriate configuration.

Here is an example of how `BoltShearCalculator` would be refactored:

```python
# In steel_lib/calculations.py

class BoltShearCalculator:
    """
    Calculates the shear strength of a single bolt based on its properties.
    """
    def __init__(self, connection: Connection):
        """
        Initializes the calculator with the connection configuration.
        """
        if connection.connection_type != "bolted":
            raise ValueError("BoltShearCalculator only supports bolted connections.")
        
        self.connection_config: BoltConfiguration = connection.configuration
        self.bolt_diameter = self.connection_config.bolt_diameter
        self.bolt_area = self._calculate_bolt_area()
        # Automatically get the nominal shear stress from the bolt grade
        self.fnv = self.connection_config.bolt_grade.Fnv

    # ... rest of the class remains the same
```

Similar changes will be applied to all other calculators that currently depend on `BoltConfiguration`.

## 3. Create a `ConnectionFactory`

To simplify the creation of `Connection` objects, a factory class will be added to `steel_lib/data_models.py`.

```python
# In steel_lib/data_models.py

@dataclass
class ConnectionFactory:
    """Factory for creating Connection objects."""

    @staticmethod
    def create_bolted_connection(*args, **kwargs) -> Connection:
        """Creates a bolted connection."""
        return Connection(
            connection_type="bolted",
            configuration=BoltConfiguration(*args, **kwargs)
        )

    @staticmethod
    def create_welded_connection(*args, **kwargs) -> Connection:
        """Creates a welded connection."""
        return Connection(
            connection_type="welded",
            configuration=WeldConfiguration(*args, **kwargs)
        )```

This factory will make it easier to create connection objects without having to manually instantiate the `Connection` and configuration classes.