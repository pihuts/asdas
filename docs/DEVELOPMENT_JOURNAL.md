# Development Journal

## Project Overview
- **Started**: 2025-08-07
- **Tech Stack**: Python 3, forallpeople
- **Purpose**: Track development decisions, problems, and solutions
- **Conventions**: PEP 8, Type Hints, Black formatting

---

## Entry Template

### 📅 [Date] - [Time] - Entry #[Number]

#### 📋 Task/Request
> Brief description of what was requested

#### 🎯 Approach
- Step-by-step approach taken
- Key decisions made
- Files modified: `[list files]`
- Design patterns used: [e.g., Factory, Singleton, Repository]

#### 🐛 Problems Encountered
1. **Problem**: [Description]
   
- **Error Message**: `[if applicable]`
   - **Root Cause**: [Analysis]
   - **Solution**: [How it was fixed]
   - **Prevention**: [How to avoid in future]
   - **Time to Resolve**: [Approximate]

#### ✅ Solution Implemented
```python
# Code snippet of the solution
```
#### 🔍 Code Review Notes
- **Complexity**: [Cyclomatic complexity if relevant]
- **Test Coverage**: [Percentage]
- **Performance Impact**: [If applicable]

#### 📝 Lessons Learned
- What worked well
- What to avoid next time
- Patterns to remember
- Dependencies added/removed

#### 🏷️ Tags
`#feature` `#bugfix` `#refactor` `#performance` `#security`

#### 🔗 Related Entries
- **Previous**: Entry #[X]
- **Next**: Entry #[Y]
- **Related**: Entry #[Z]

---

### 📅 2025-08-07 - 17:08 - Entry #1

#### 📋 Task/Request
> Refactor the codebase to centralize unit definitions in `steel_lib/data_models.py` and remove redundant unit assignments in `steel_lib/calculations.py`. This is based on the "Don't Repeat Yourself (DRY)" principle from the project's `guidelines.md`.

#### 🎯 Approach
1.  **Analyzed Guidelines**: Reviewed `guidelines.md` and identified the DRY principle as the primary driver for this refactoring task.
2.  **Centralized Units in Data Models**: Modified `steel_lib/data_models.py` to embed `forallpeople` units directly into the `Material`, `Plate`, and `BoltConfiguration` data classes. Switched from SI to English units (`ksi`, `inch`) as requested.
3.  **Refactored Calculations**: Updated `steel_lib/calculations.py` to remove all manual unit assignments (e.g., `* si.inch**2`). The calculation functions now rely on the unit-aware data models.
4.  **Removed Redundant Code**: Deleted the `boltbearing`, `lc_outer`, and `lc_inner` functions from `steel_lib/calculations.py`, as their logic was either duplicated or better handled within the `ConnectionCapacityCalculator` class.
5.  **Verified Consistency**: Checked `steel_lib/materials.py` to ensure the material definitions were compatible with the new unit-aware data models. No changes were required.

-   **Files modified**: `steel_lib/data_models.py`, `steel_lib/calculations.py`
-   **Design patterns used**: DRY Principle

#### 🐛 Problems Encountered
1.  **Problem**: `ValueError: Can only compare between Physical instances of equal dimension.`
    -   **Error Message**: `ValueError: Can only compare between Physical instances of equal dimension.`
    -   **Root Cause**: The `forallpeople` library is not compatible with `typing.Optional` for type hinting in dataclasses.
    -   **Solution**: Changed the type hint for `length` and `width` in the `Plate` dataclass from `Optional[si.inch]` to `Any`.
    -   **Prevention**: Avoid using `typing.Optional` with `forallpeople` types in dataclasses. Use `Any` instead.
2.  **Problem**: Unit inconsistency in `BlockShearCalculator`.
    -   **Error Message**: N/A (logical error).
    -   **Root Cause**: The `_get_member_thickness` method was not correctly applying units to the thickness of `steelpy` members.
    -   **Solution**: Modified `_get_member_thickness` to explicitly multiply the thickness by `si.inch` for `steelpy` members.
    -   **Prevention**: Ensure that all values retrieved from external libraries are converted to the appropriate `forallpeople` units.

#### ✅ Solution Implemented
```python
# In steel_lib/data_models.py
@dataclass
class Plate:
    # ...
    length: Any = None
    width: Any = None

# In steel_lib/calculations.py
def _get_member_thickness(self) -> float:
    if isinstance(self.member, Plate):
        return self.member.t
    elif hasattr(self.member, 't'):
        return self.member.t * si.inch
    elif hasattr(self.member, 'tw'):
        return self.member.tw * si.inch
    raise AttributeError("Member has no recognizable thickness attribute.")
```

#### 🔍 Code Review Notes
-   **Complexity**: Reduced. By removing redundant code and centralizing unit definitions, the codebase is now easier to maintain and understand.
-   **Test Coverage**: N/A. No tests were provided or created.
-   **Performance Impact**: Negligible.

#### 📝 Lessons Learned
-   Centralizing units at the data model level is a clean and effective way to enforce consistency and reduce errors.
-   Adhering to the DRY principle significantly improves code quality.

#### 🏷️ Tags
`#refactor`

#### 🔗 Related Entries
-   **Previous**: N/A
-   **Next**: N/A
-   **Related**: N/A
---

### 📅 2025-08-07 - 17:25 UTC - Entry #2

#### 📋 Task/Request
> Refactor the initial `untitled3.py` script to align with the project's `guidelines.md`. This includes structuring the project, consolidating duplicated code, separating concerns, and establishing the development journal system.

#### 🎯 Approach
- **Guideline Implementation**: Created the `docs/COMMON_PROBLEMS.md` and `docs/SUCCESS_PATTERNS.md` files to establish the full documentation structure required by the guidelines.
- **Code Analysis**: Reviewed `untitled3.py` and identified significant code duplication, particularly with the `UFMCalculator` and various tensile yielding calculators. The script also mixed class definitions with procedural test code.
- **Refactoring & Consolidation**:
    - Migrated all calculation-related classes (`TensileYieldWhitmore`, `CompressionBucklingCalculator`, `UFMCalculator`, `PlateTensileYieldingCalculator`, `WebLocalYieldingCalculator`) and utility functions (`round_to_interval`, `round_up_to_interval`) from `untitled3.py` into `steel_lib/calculations.py`.
    - This addressed the "Don't Repeat Yourself" (DRY) and "Single Responsibility" principles by creating a single, authoritative source for all calculation logic.
- **Separation of Concerns**:
    - Transformed `main.py` into a clean, high-level script that demonstrates how to use the library. It now handles object instantiation and calls the refactored calculators, serving as a clear example.
    - All raw calculation logic and class definitions were removed from `main.py`.
- **Cleanup**: Deleted the now-obsolete `untitled3.py` file.
- **Files Modified**: `docs/DEVELOPMENT_JOURNAL.md`, `docs/COMMON_PROBLEMS.md`, `docs/SUCCESS_PATTERNS.md`, `steel_lib/calculations.py`, `main.py`.
- **Files Deleted**: `untitled3.py`.
- **Design Patterns Used**: Adapter (in the calculators, which adapt raw member/connection objects into a consistent format for calculation), Strategy (implied by having multiple calculator classes for different limit states).

#### 🐛 Problems Encountered
1. **Problem**: The initial script (`untitled3.py`) was a mix of class definitions, object instantiations, and calculation calls, making it difficult to understand and maintain.
   - **Root Cause**: The script was likely developed in a notebook environment (`.ipynb`) where this style is common, but it's not suitable for a structured library.
   - **Solution**: The code was refactored by separating the core logic (calculators) from the example usage. The calculators were moved to `steel_lib/calculations.py` and the usage example was moved to `main.py`.
   - **Prevention**: Adhering to the project structure defined in `guidelines.md` will prevent this from happening in the future. New logic should be added to the appropriate module, and `main.py` should only be used for demonstration or as an application entry point.

2. **Problem**: Multiple, conflicting definitions for classes like `UFMCalculator` and `TensileYieldingCalculator` existed within the same file.
   - **Root Cause**: Iterative development without refactoring led to duplicated and slightly modified classes being added instead of updating existing ones.
   - **Solution**: The best implementation of each duplicated class was identified and consolidated into a single class in `steel_lib/calculations.py`. Redundant versions were removed.
   - **Prevention**: Before adding new functionality, developers should check for existing classes that can be extended or modified. Code reviews should flag duplicated logic.

#### ✅ Solution Implemented
```python
# In steel_lib/calculations.py (Example of consolidated UFMCalculator)
class UFMCalculator:
    """
    Calculates UFM endplate dimensions and load multipliers with a
    comprehensive debug mode to show all intermediate values.
    """
    def __init__(self, beam: Any, support: Any, endplate: Any, connection: Any):
        self._beam_depth = self._get_attribute(beam, ['d', 'depth'])
        self._support_depth = self._get_attribute(support, ['d', 'depth'])
        # ... more attributes ...

    def get_dimensions(self, debug: bool = False) -> PlateDimensions:
        # ... implementation ...

    def get_loads_multipliers(self, debug: bool = False) -> LoadMultipliers:
        # ... implementation ...

# In main.py (Example of clean usage)
ufm_checker = UFMCalculator(
    beam=beam,
    support=support,
    endplate=end_plate_column,
    connection=column_endplate_connection
)
final_dimensions = ufm_checker.get_dimensions(debug=True)
```

#### 🔍 Code Review Notes
- **Complexity**: The cyclomatic complexity of the individual calculator methods is low. The overall complexity of the system was reduced by removing duplicated code.
- **Test Coverage**: Not measured, but the `main.py` script serves as an initial integration test. Formal unit tests should be the next step.
- **Performance Impact**: Negligible. The changes were primarily for structure and readability.

#### 📝 Lessons Learned
- Strict adherence to project structure guidelines from the start is crucial for maintainability.
- Notebook-style code (`.ipynb`) must be refactored before being integrated into a formal Python library.
- Consolidating duplicated logic into single, well-defined classes is a primary goal of refactoring.

#### 🏷️ Tags
#refactor #project-structure #best-practices

#### 🔗 Related Entries
- **Previous**: Entry #1
- **Next**: TBD