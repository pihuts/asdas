from dataclasses import dataclass, field
from typing import Optional, Any
import forallpeople as si

si.environment('structural', top_level=False)

@dataclass(frozen=True)
class Material:
    """Represents the engineering properties of a steel material."""
    Fy: si.ksi
    Fu: si.ksi
    E: si.ksi

@dataclass
class Plate:
    """
    Represents a custom plate member. Includes loading_condition as an
    intrinsic property, defaulting to 1.
    """
    t: si.inch
    material: Material
    loading_condition: int = 1
    length: Any = None
    width: Any = None
    Type: str = "Plate"

    @classmethod
    def create_plate_member(
        cls, t: si.inch, material, loading_condition: int = 1,
    ) -> "Plate":
        """Creates a custom Plate member."""
        return cls(t=t, material=material, loading_condition=loading_condition)

    @property
    def Fy(self) -> si.ksi: return self.material.Fy
    @property
    def Fu(self) -> si.ksi: return self.material.Fu
    @property
    def E(self) -> si.ksi: return self.material.E

@dataclass(frozen=True)
class BoltGrade:
    """Represents the nominal strength properties of a bolt material."""
    Fnt: si.ksi  # Nominal tensile stress
    Fnv: si.ksi  # Nominal shear stress

@dataclass
class BoltConfiguration:
    """Defines the geometry and properties of a bolted connection."""
    row_spacing: si.inch
    column_spacing: si.inch
    n_rows: int
    n_columns: int
    edge_distance_vertical: si.inch
    edge_distance_horizontal: si.inch
    bolt_diameter: si.inch
    bolt_grade: BoltGrade # Link to the BoltGrade object
    material: Material
from steelpy import aisc
from typing import Any, Type

@dataclass
class SteelpyMemberFactory:
    """Factory for creating steelpy members."""

    @classmethod
    def create_steelpy_member(
        cls, section_class: Type, section_name: str, material, shape_type: str,
        loading_condition: int = 1,
    ) -> Any:
        """Creates a steelpy member, assigning material and loading properties."""
        section = getattr(section_class, section_name)
        section.add_property("Fy", material.Fy)
        section.add_property("Fu", material.Fu)
        section.add_property("E", material.E)
        section.add_property("Type", shape_type)
        section.loading_condition = loading_condition
        return section