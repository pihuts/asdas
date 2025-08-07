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