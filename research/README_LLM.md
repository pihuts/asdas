# steel_lib (v0.1.0)

## Overview
`steel_lib` is a Python library designed for structural engineers to perform steel connection design calculations. It provides a suite of tools for analyzing various failure modes in bolted and welded connections, including bolt shear, tensile yielding, block shear, and web local crippling, among others. The library is built to be extensible and integrates with `steelpy` for member properties and `forallpeople` for unit-aware calculations, ensuring accuracy and consistency in engineering computations.

## Installation

**Installation Command:**
```bash
pip install -e .
```

**Detected Requirements:**
```
forallpeople
steelpy
```

## Core Concepts

*   **Main Modules:**
    *   `data_models.py`: Contains dataclasses that define the core entities of the library, such as `Plate`, `BoltConfiguration`, and `WeldConfiguration`. These models ensure data integrity and provide a clear structure for inputs.
    *   `calculations.py`: This is the computational core of the library, containing various calculator classes for different design checks (e.g., `BoltShearCalculator`, `TensileYieldingCalculator`, `WebLocalCrippingCalculator`).
    *   `materials.py`: A reference module that provides dictionaries of standard material properties for steel, bolts, and weld electrodes.
    *   `debugging.py`: Includes the `DebugLogger` class, a utility for printing detailed, step-by-step calculation breakdowns for verification and debugging.
*   **Key Classes/Functions:**
    *   `*Calculator`: The library is architected around a series of calculator classes (e.g., `BlockShearCalculator`, `ConnectionCapacityCalculator`). Each class is responsible for a specific AISC design check. They are initialized with member and connection objects and have a `calculate_capacity()` method that returns the design strength.
    *   `data_models`: The various dataclasses in this module (e.g., `Plate`, `BoltConfiguration`) are crucial for providing structured and validated input to the calculator classes.
    *   `DebugLogger`: A utility class used across all calculators to provide a verbose, formatted output of the entire calculation process when the `debug=True` flag is used.
*   **Important Terminology:**
    *   `Member`: A structural element, typically a steel shape like a W-beam or an L-angle, often represented by a `steelpy` object or a custom `Plate` object.
    *   `Connection`: The configuration of bolts or welds used to join members. This is defined by dataclasses like `BoltConfiguration` or `WeldConfiguration`.
    *   `Capacity`: The design strength (e.g., in kips or kN) of a component or connection for a specific failure mode, calculated according to AISC specifications.
    *   `DCR`: Demand-Capacity Ratio, a common engineering term representing the ratio of applied load (demand) to the calculated strength (capacity).

## Quick Start Example

A runnable example demonstrating a best-practice style for calculating bolt shear capacity.

```python
# Example: Clear, explicit configuration and execution
import forallpeople as si
from steel_lib.data_models import BoltGrade, BoltConfiguration
from steel_lib.calculations import BoltShearCalculator
from steel_lib.materials import BOLT_GRADES

# 1. Define the bolt properties using the structured data models
# Use descriptive names and explicit structures
a325_bolt_grade = BOLT_GRADES["A325"]

connection_config = BoltConfiguration(
    bolt_grade=a325_bolt_grade,
    bolt_diameter=0.75 * si.inch,
    n_rows=3,
    n_columns=2,
    row_spacing=3 * si.inch,
    column_spacing=3 * si.inch,
    edge_distance_horizontal=1.5 * si.inch,
    edge_distance_vertical=1.5 * si.inch,
)

# 2. Initialize the appropriate calculator
bolt_shear_checker = BoltShearCalculator(connection=connection_config)

# 3. Calculate the capacity for a specific condition
# Ns = 1 for single shear
design_shear_strength = bolt_shear_checker.calculate_capacity(
    number_of_shear_planes=1,
    debug=True  # Use debug=True for a detailed calculation breakdown
)

print(f"Design Bolt Shear Strength (φRn): {design_shear_strength:.2f}")
```
> [!TIP]
> **Best Practices:**
> * Explicit is better than implicit. Always define all required parameters in the configuration objects.
> * Use descriptive variable names that clearly state the purpose (e.g., `connection_config`).
> * Avoid magic numbers; use the `si` environment from `forallpeople` to define units explicitly (e.g., `3 * si.inch`).

## Advanced Usage

This example shows a more complex check for block shear, involving a `steelpy` member and demonstrating the library's integration capabilities.

```python
import forallpeople as si
import steelpy
from steel_lib.data_models import BoltConfiguration, SteelpyMemberFactory
from steel_lib.calculations import BlockShearCalculator
from steel_lib.materials import BOLT_GRADES, MATERIALS

try:
    # 1. Create a steel member using the factory
    # This ensures consistent unit handling and property extraction
    member_factory = SteelpyMemberFactory(steel_grade="A992")
    angle_member = member_factory.create_steelpy_member(shape_name="L6x4x1/2")

    # 2. Define the connection configuration
    connection_config = BoltConfiguration(
        bolt_grade=BOLT_GRADES["A325"],
        bolt_diameter=(7/8) * si.inch,
        n_rows=4,
        n_columns=1,
        row_spacing=3 * si.inch,
        column_spacing=0 * si.inch,
        edge_distance_horizontal=1.25 * si.inch,
        edge_distance_vertical=1.5 * si.inch,
    )

    # 3. Initialize the calculator for the specific failure mode
    block_shear_checker = BlockShearCalculator(
        member=angle_member,
        connection=connection_config,
        loading_orientation="Axial"
    )

    # 4. Calculate and print the capacity
    block_shear_capacity = block_shear_checker.calculate_capacity(debug=True)
    print(f"Block Shear Design Capacity (φRn): {block_shear_capacity:.2f}")

except AttributeError as e:
    print(f"ERROR: An attribute was not found. Check member properties. Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## Tutorial

#### 1. Install
Ensure you have `setuptools` installed (`pip install setuptools`). Then, run the following command in your terminal from the project root:
```bash
pip install -e .
```

#### 2. Initialize
Create a file `main.py` with the following minimal code to calculate the tensile yielding capacity of a steel plate.

```python
import forallpeople as si
from steel_lib.data_models import Plate
from steel_lib.calculations import TensileYieldingCalculator
from steel_lib.materials import MATERIALS

# Define a simple plate member
steel_plate = Plate(
    material=MATERIALS["A36"],
    thickness=0.5 * si.inch,
    width=6 * si.inch
)

# Initialize the calculator
yielding_checker = TensileYieldingCalculator(member=steel_plate)

# Calculate the capacity
tensile_yield_capacity = yielding_checker.calculate_capacity(debug=True)

print(f"Tensile Yielding Capacity (φRn): {tensile_yield_capacity:.2f}")
```

#### 3. Extend
Here is a common pattern for integrating the library into a larger application function that checks multiple failure modes.

```python
import forallpeople as si
from steel_lib.data_models import Plate, BoltConfiguration
from steel_lib.calculations import TensileYieldingCalculator, ConnectionCapacityCalculator
from steel_lib.materials import MATERIALS, BOLT_GRADES

def check_plate_connection(plate: Plate, connection: BoltConfiguration) -> dict:
    """
    Checks a plate for multiple connection failure modes.
    Returns a dictionary of capacities.
    """
    results = {}

    # Check tensile yielding
    yielding_checker = TensileYieldingCalculator(member=plate)
    results["tensile_yielding"] = yielding_checker.calculate_capacity()

    # Check bolt connection capacity (bearing/tearout)
    connection_checker = ConnectionCapacityCalculator(
        member=plate,
        connection=connection,
        loading_orientation="Axial"
    )
    results["connection_bearing_tearout"] = connection_checker.calculate_capacity(number_of_shear_planes=1)

    return results

# Example usage:
my_plate = Plate(material=MATERIALS["A572_50"], thickness=0.75 * si.inch, width=8 * si.inch)
my_connection = BoltConfiguration(
    bolt_grade=BOLT_GRADES["A490"],
    bolt_diameter=1 * si.inch,
    n_rows=3, n_columns=2,
    row_spacing=3 * si.inch, column_spacing=3 * si.inch,
    edge_distance_horizontal=2 * si.inch, edge_distance_vertical=2 * si.inch
)

capacities = check_plate_connection(my_plate, my_connection)

for mode, capacity in capacities.items():
    print(f"Capacity for {mode}: {capacity:.2f}")

```

#### 4. Test
This library does not yet have a formal test suite. Verification should be done by manually running examples and checking the debug output against hand calculations or other trusted software.

## What to Avoid

*   **Pitfall 1: Inconsistent Units:** Do not mix unit-aware numbers (from `forallpeople`) with raw floats. This can lead to incorrect calculations. Always use the `si` environment (e.g., `2.5 * si.inch`) for all physical measurements.
*   **Pitfall 2: Incorrect `loading_orientation`:** The `BlockShearCalculator` and `ConnectionCapacityCalculator` behave differently based on the `loading_orientation` ("Axial" or "Shear"). Ensure this is set correctly to match the physical condition, as it determines which edge distances and spacings are used.
*   **Performance Traps:** The calculators are not designed for high-performance, iterative analysis (e.g., finite element analysis). They are intended for single, discrete design checks. Calling them thousands of times in a loop may be slow.
*   **Implicit `loading_condition`:** Some members, like double angles, have a `loading_condition` of 2. This is handled internally but relies on the member object having this attribute. If creating a custom member, ensure this attribute is set if the capacity needs to be scaled.

## Troubleshooting

| Issue                     | Probable Cause                               | Solution                                                     |
| ------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| `AttributeError`          | The member object (e.g., from `steelpy`) is missing a required property (e.g., `tw` for web thickness, or `Fy` for yield strength). | Ensure the `steelpy` shape name is correct or that the custom member object has all required attributes defined. |
| `ModuleNotFoundError`     | A required dependency is not installed.      | Run `pip install -e .` to install all dependencies from `setup.py`. |
| `KeyError`                | The requested material or bolt grade (e.g., "A992") does not exist in the `materials.py` dictionaries. | Check `materials.py` for the list of available keys or add the new material if necessary. |

## Testing

A sample test case to verify core functionality. Since no test runner is configured, this can be run as a standalone script.

```python
import unittest
import forallpeople as si
from steel_lib.data_models import Plate
from steel_lib.calculations import TensileYieldingCalculator
from steel_lib.materials import MATERIALS

class TestSteelLib(unittest.TestCase):
    def test_tensile_yielding(self):
        """
        Tests the basic tensile yielding calculation.
        φRn = 0.9 * Fy * Ag
        Ag = 4" * 0.5" = 2 in^2
        φRn = 0.9 * 36 ksi * 2 in^2 = 64.8 kips
        """
        plate = Plate(
            material=MATERIALS["A36"],
            thickness=0.5 * si.inch,
            width=4 * si.inch
        )
        calculator = TensileYieldingCalculator(member=plate)
        capacity = calculator.calculate_capacity()
        # Use a tolerance for floating point comparisons
        self.assertAlmostEqual(capacity.value, 64.8, places=1)

    def test_invalid_material(self):
        with self.assertRaises(KeyError):
            # This material does not exist
            Plate(material=MATERIALS["FAKE_MATERIAL"], thickness=0.5*si.inch, width=4*si.inch)

if __name__ == '__main__':
    unittest.main()
```

## AI Agent Notes
This library follows a factory/calculator pattern. To add a new calculation, an agent should:
1.  Create a new `*Calculator` class in `calculations.py`.
2.  The calculator's `__init__` should accept member and/or connection data models.
3.  The `calculate_capacity()` method should perform the calculation and use the `DebugLogger`.
4.  If new input parameters are needed, they should be added to the relevant dataclass in `data_models.py`.

## Change Log

| Version | Date         | Key Changes                                                 |
| ------- | ------------ | ----------------------------------------------------------- |
| `0.1.0` | `2025-08-08` | Initial release. Includes calculators for bolt shear, tensile yielding/rupture, block shear, connection capacity, web local yielding/crippling, and UFM calculations. |
