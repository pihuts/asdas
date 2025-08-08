# forallpeople (v2.7.0)

## Overview

`forallpeople` is a Python library that provides a robust and intuitive system for performing unit-aware calculations. It is designed for engineers, scientists, and students who need to ensure dimensional correctness in their computations. The library's core philosophy is "convention over configuration," aiming for a user experience where units behave as expected with minimal setup. It supports the full SI unit system and other systems defined by it (e.g., US customary units). A key feature is that physical quantities automatically reduce during calculations, and dimensionless results are returned as simple numbers.

## Installation

**Installation Command:**
```bash
pip install forallpeople
```

**Detected Requirements:**
```
- No explicit dependencies found.
- The library is designed to work with numpy, pandas, and handcalcs.
- The 'tuplevector' library is included directly within forallpeople.
```

## Core Concepts

*   **Main Modules:** The library is primarily used through the top-level `forallpeople` module, typically imported with the alias `si`.
*   **Key Classes/Functions:**
    *   `Physical`: The central class representing any physical quantity. It encapsulates a value, its dimensions, and a scaling factor. `Physical` instances are immutable.
    *   `si.environment()`: A crucial function used to load predefined unit environments (like 'default' or 'structural'). This function populates the namespace with unit variables (e.g., `si.N`, `si.Pa`) and configures the representation of calculated quantities.
*   **Important Terminology:**
    *   `Dimension Vector`: An internal vector that tracks the powers of the base SI units (kg, m, s, A, K, mol, cd) for any `Physical` instance.
    *   `Environment`: A JSON definition that maps unit names (e.g., "N") and symbols to their corresponding dimension vectors and values. This allows for automatic unit representation and conversion.
    *   `Auto-prefixing`: The automatic scaling of SI units to appropriate prefixes (e.g., 1200 `Ohm` is displayed as 1.2 `kOhm`).

## Quick Start Example

A runnable example demonstrating best-practice style.

```python
# Example: Clear, explicit configuration and execution
import forallpeople as si

# Load the default environment to get access to derived units like N, Pa, etc.
si.environment('default')

# Use descriptive names and explicit structures
beam_area = 3 * si.m * 4 * si.m
applied_force = 2500 * si.N

# Calculations are dimensionally aware
pressure_on_beam = applied_force / beam_area

# The result is automatically displayed in the most appropriate unit (Pascals)
print(f"Beam Area: {beam_area}")
print(f"Applied Force: {applied_force}")
print(f"Resulting Pressure: {pressure_on_beam}")
```
> [!TIP]
> **Best Practices:**
> * Explicit is better than implicit. Always load an environment.
> * Use descriptive variable names to clarify the physical quantities.
> * Let the library handle unit conversions and representations.

## Advanced Usage

This example shows how `forallpeople` can be used with `numpy` for more complex calculations.

```python
import forallpeople as si
import numpy as np

si.environment('default')

# Create Physical quantities
force_a = 5 * si.kN
force_b = 3.5 * si.kN
force_c = 7.7 * si.kN
force_d = 6.6 * si.kN

# Create numpy matrices with Physical instances as elements
stiffness_matrix = np.matrix([[force_a, force_b], [force_b, force_a]])
load_matrix = np.matrix([[force_c, force_d], [force_d, force_c]])

# Perform matrix multiplication
# The dimensions are correctly handled (kN * kN = kN^2)
result_matrix = stiffness_matrix @ load_matrix

print("Stiffness Matrix:\n", stiffness_matrix)
print("\nLoad Matrix:\n", load_matrix)
print("\nResult Matrix:\n", result_matrix)
```

## Tutorial

#### 1. Install
Run the following command in your terminal:
```bash
pip install forallpeople
```

#### 2. Initialize
Create a file `main.py` with the following minimal code to start using the library:
```python
import forallpeople as si

# Load the default environment of SI units
si.environment('default')

# Define some physical quantities
length = 5 * si.m
time = 2 * si.s

# Perform a calculation
velocity = length / time

print(f"The calculated velocity is: {velocity}")
```

#### 3. Extend
Here is a common pattern for integrating the library into a larger application, such as a function for calculating kinetic energy:
```python
import forallpeople as si
si.environment('default')

def calculate_kinetic_energy(mass_kg: float, velocity_mps: float) -> si.Physical:
    """Calculates kinetic energy using dimensionally-aware objects."""
    mass = mass_kg * si.kg
    velocity = velocity_mps * (si.m / si.s)
    
    kinetic_energy = 0.5 * mass * velocity**2
    return kinetic_energy

# Calculate energy for a 10kg object moving at 5 m/s
energy_joules = calculate_kinetic_energy(10, 5)

# The result is automatically in Joules because the environment is loaded
print(f"Kinetic Energy: {energy_joules}")
```

#### 4. Test
Verify your setup is working correctly by running tests. The project uses `pytest`.```bash
pytest
```

## What to Avoid

*   **Pitfall 1: Using `float()` without understanding its behavior:** Calling `float(quantity)` returns the numerical part of the *displayed, prefixed* value, not the value in base SI units. For the base value, use `quantity.value`. This can lead to incorrect results in functions that implicitly call `float()`, like `math.sqrt()`.
*   **Pitfall 2: Using Floor Division:** The floor division operator (`//`) is not implemented for `Physical` objects to avoid ambiguity. Use true division (`/`) and then `int()` if you need an integer result, but be aware this removes the units.
*   **Pitfall 3: Forgetting to Load an Environment:** If you don't load an environment with `si.environment()`, derived units like `N` or `Pa` will not be available, and results will only be shown in terms of base SI units (e.g., `kg*m/s^2`), which is less readable.

## Troubleshooting

| Issue                     | Probable Cause                               | Solution                                                     |
| ------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| `AttributeError: 'module' object has no attribute 'N'` | You tried to use a derived unit (like Newton) without loading an environment. | Call `si.environment('default')` after importing the library. |
| `TypeError: unsupported operand type(s) for +: 'Physical' and 'Physical'` | You tried to add or subtract two quantities with different dimensions (e.g., mass and length). | Check your formulas and ensure dimensional consistency. |
| `NameError: name 'N' is not defined` | You tried to use a unit directly without the `si.` prefix after loading the environment with `top_level=False` (the default). | Either use the `si.` prefix (e.g., `si.N`) or load the environment with `si.environment('default', top_level=True)`. |

## Testing

A sample test case to verify core functionality.

```python
import unittest
import forallpeople as si

class TestForallpeople(unittest.TestCase):
    def setUp(self):
        """Load the default environment before each test."""
        si.environment('default')

    def test_basic_functionality(self):
        """Test a simple force calculation."""
        mass = 10 * si.kg
        acceleration = 9.8 * si.m / si.s**2
        force = mass * acceleration
        # The result should be in Newtons, which are kg*m/s^2
        self.assertAlmostEqual(force.value, 98.0)
        self.assertEqual(force.repr.split(" "), "N")

    def test_edge_case_handling(self):
        """Test adding incompatible units."""
        with self.assertRaises(TypeError):
            5 * si.m + 2 * si.kg
```

## AI Agent Notes
{{This space is reserved for future AI agents to append clarifications, usage caveats, or observations based on code changes.}}

## Change Log

| Version | Date         | Key Changes                                                 |
| ------- | ------------ | ----------------------------------------------------------- |
| `2.7.0` | `2024-07-12` | (From GitHub) Latest release. Specific changes not retrieved. |
| ...     | ...          | For a full history, see the "Releases" section on the GitHub repository. |