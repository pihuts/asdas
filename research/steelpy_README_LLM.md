# steelpy (v1.1.1)

## Overview

`steelpy` is a lightweight Python library that serves as a database for AISC (American Institute of Steel Construction) steel shapes. Its primary purpose is to provide engineers and developers with easy, programmatic access to the section properties of standard steel profiles (W, L, HSS, etc.). The data is consistent with the AISC Steel Construction Manual, 16th Edition. The library is ideal for use in structural calculation scripts and applications where steel properties are required.

## Installation

**Installation Command:**
```bash
pip install steelpy
```

**Detected Requirements:**```
- Python >=3.9, <4.0
- No other external dependencies are required.
```

## Core Concepts

*   **Main Modules:** The core functionality is accessed through the `steelpy.aisc` module.
*   **Key Classes/Functions:**
    *   `aisc.{SHAPE}_shapes`: These are collection objects that hold all the profiles for a given shape type (e.g., `aisc.W_shapes`, `aisc.L_shapes`).
    *   `section object`: Individual steel profiles (e.g., `aisc.W_shapes.W12X26`) are objects whose attributes are their geometric properties (e.g., `.d`, `.tw`, `.Ix`).
    *   `.filter()`: A powerful method on shape collections that allows you to select a subset of profiles based on specified criteria for their properties (e.g., find all W-shapes with a depth between 8 and 12 inches).
*   **Important Terminology:**
    *   `Shape Group`: A collection of all profiles of a certain type, like `W_shapes`.
    *   `Section`: A specific steel profile, like `W12X26`.
    *   `Property`: An attribute of a section, like `d` (depth) or `Ix` (moment of inertia).

## Quick Start Example

A runnable example demonstrating best-practice style.

```python
# Example: Retrieve properties for a specific steel beam
from steelpy import aisc

# Access the W-shape collection and select a specific section
beam_section = aisc.W_shapes.W12X26

# Define the steel yield strength
Fy_ksi = 50

# Retrieve properties directly as attributes
web_area = beam_section.d * beam_section.tw
shear_capacity_kips = 0.6 * Fy_ksi * web_area

print(f"Section: {beam_section.name}")
print(f"Depth (d): {beam_section.d} in")
print(f"Web Thickness (tw): {beam_section.tw} in")
print(f"Nominal Shear Capacity (Vn): {shear_capacity_kips:.2f} kips")
```
> [!TIP]
> **Best Practices:**
> * Import the `aisc` object directly for clean access to shape groups.
> * Use descriptive variable names to avoid confusion with section properties.
> * For sections with special characters in their names (e.g., "1/4", "-"), replace the character with an underscore (e.g., `L4X4X1_4`).

## Advanced Usage

This example shows how to filter for sections that meet specific design criteria.

```python
from steelpy import aisc

# Define the design criteria for a W-beam
design_criteria = {
    'd': {'min': 10, 'max': 14},  # Depth between 10 and 14 inches
    'Zx': {'min': 50},            # Plastic section modulus >= 50 in^3
    'bf': {'max': 8}              # Flange width <= 8 inches
}

# Filter the W-shape collection and sort the results by weight (default)
filtered_beams = aisc.W_shapes.filter(criteria=design_criteria)

print("Found the following beams matching the criteria:")
for section_name, section_object in filtered_beams.items():
    print(
        f"- {section_name}: "
        f"d={section_object.d} in, "
        f"Zx={section_object.Zx} in^3, "
        f"bf={section_object.bf} in, "
        f"Weight={section_object.weight} lb/ft"
    )```

## Tutorial

#### 1. Install
Run the following command in your terminal:
```bash
pip install steelpy
```

#### 2. Initialize
Create a file `main.py` with the following minimal code to look up a shape:
```python
from steelpy import aisc

# Access the C-shape (channel) collection
channel_shapes = aisc.C_shapes

# Get a specific channel, replacing 'x' with '_'
my_channel = channel_shapes.C12X20_7

print(f"Looking up section: {my_channel.name}")
print(f"Area: {my_channel.area} in^2")
print(f"Moment of Inertia (Ix): {my_channel.Ix} in^4")
```

#### 3. Extend
Here is a common pattern for integrating the library into a design function:
```python
from steelpy import aisc

def find_lightest_w_beam(required_Sx_in3: float):
    """Finds the lightest W-beam that meets a required section modulus."""
    
    criteria = {'Sx': {'min': required_Sx_in3}}
    
    # Filter for all beams meeting the criteria, sorted by weight
    candidate_beams = aisc.W_shapes.filter(criteria, sort_by='weight')
    
    if not candidate_beams:
        return None
        
    # The first item is the lightest because of the sort
    lightest_beam_name = list(candidate_beams.keys())[0]
    lightest_beam_object = candidate_beams[lightest_beam_name]
    
    return lightest_beam_object

# Find the lightest W-beam with an elastic section modulus (Sx) of at least 95 in^3
required_modulus = 95.0
result = find_lightest_w_beam(required_modulus)

if result:
    print(f"The lightest suitable beam is {result.name} with Sx = {result.Sx} in^3.")
else:
    print("No suitable beam found.")
```

#### 4. Test
The testing framework for this package is not specified. You can verify your setup with a simple check.
```bash
# No direct test command is available.
# Run a python script that imports the library and prints a value.
python -c "from steelpy import aisc; print(aisc.W_shapes.W10X49.bf)"
```

## What to Avoid

*   **Pitfall 1: Incorrectly Naming Sections:** Section names in the AISC database can contain characters like `.` or `/` (e.g., `W6X8.5`, `L4X4X1/4`). In `steelpy`, these must be accessed by replacing the special character with an underscore `_` (e.g., `W6X8_5`, `L4X4X1_4`).
*   **Pitfall 2: Assuming Metric Units:** The library's data is based on the imperial system (inches, lbs), consistent with the AISC manual. Do not assume metric units.

## Troubleshooting

| Issue                     | Probable Cause                               | Solution                                                     |
| ------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| `AttributeError: 'Shapes' object has no attribute 'W12-26'` | You used a hyphen `-` instead of an `X` in the section name, or you used a special character that should be an underscore. | Check the AISC naming convention (e.g., `W12X26`). Replace fractions or decimals with underscores (e.g., `W6X8_5`). |
| `AttributeError: 'Section' object has no attribute 'Iz'` | You are trying to access a property that is not available for that specific shape group (e.g., `Iz` is for single angles). | Consult the Property Table in the documentation to see which properties are available for each shape type. |

## Testing

A sample test case to verify core functionality (testing framework unknown).

```python
import unittest
from steelpy import aisc

class TestSteelpy(unittest.TestCase):
    def test_w_shape_lookup(self):
        """Test that a known W-shape property is correct."""
        w18x76 = aisc.W_shapes.W18X76
        # Value from AISC v16.0 manual
        expected_d = 17.7
        self.assertAlmostEqual(w18x76.d, expected_d)

    def test_filter_functionality(self):
        """Test the filter method."""
        criteria = {'d': {'min': 12, 'max': 12.1}}
        filtered_sections = aisc.W_shapes.filter(criteria)
        # Should find W12x14 and W12x16
        self.assertIn('W12X14', filtered_sections)
        self.assertIn('W12X16', filtered_sections)
        self.assertEqual(len(filtered_sections), 2)
```

## AI Agent Notes
{{This space is reserved for future AI agents to append clarifications, usage caveats, or observations based on code changes.}}

## Change Log

| Version | Date         | Key Changes                                                 |
| ------- | ------------ | ----------------------------------------------------------- |
| `1.1.1` | `2024-04-20` | (From PyPI) Latest release. Specific changes not listed.    |
| `1.1.0` | `2024-04-19` | (From PyPI) Specific changes not listed.                    |
| `1.0.3` | `2024-04-19` | (From PyPI) Specific changes not listed.                    |
| ...     | ...          | For a full history, see the "Release history" on the PyPI page. |