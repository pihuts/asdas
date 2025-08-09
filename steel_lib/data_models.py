from dataclasses import dataclass, field
from typing import Optional, Any, Literal, Union
from enum import Enum
from .si_units import si


class ConnectionComponent(Enum):
    """Defines the specific part of a member that is being connected."""
    TOTAL = "total"
    WEB = "web"
    FLANGE = "flange"
    LENGTH = "along_length"
    WIDTH = "along_width"


@dataclass(frozen=True)
class GeometricProperties:
    """
    A container for the pre-calculated gross area (Ag) of a member's various components.
    This makes the properties easy to access and prevents repeated calculations.
    """
    total: Optional[float] = None
    web: Optional[float] = None
    flange: Optional[float] = None
    along_length: Optional[float] = None
    along_width: Optional[float] = None


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
    clipping: Any = 0 * si.inch
    Type: str = "Plate"
    geometry: "GeometricProperties" = field(init=False)

    def __post_init__(self):
        """
        Post-initialization hook to automatically calculate and assign the
        geometric properties for the plate.
        """
        self.geometry = GeometricProperties(
            along_length=self.gross_area_length,
            along_width=self.gross_area_width,
            total=self.gross_area_length or self.gross_area_width # Default total
        )

    @classmethod
    def from_dimensions(
        cls,
        dimensions: "PlateDimensions",
        material: "Material",
        loading_condition: int = 1,
        clipping: Any = 0 * si.inch,
    ) -> "Plate":
        """
        Creates a Plate member from a PlateDimensions object. The geometry
        is calculated automatically after instantiation.
        """
        return cls(
            t=dimensions.thickness, # Already has units
            material=material,
            loading_condition=loading_condition,
            length=dimensions.vertical, # Already has units
            width=dimensions.horizontal, # Already has units
            clipping=clipping,
        )
    def set_dimensions(self, dimensions: "PlateDimensions"):
        """
        Updates the plate's dimensions from a PlateDimensions object.

        This method allows dimensions to be set or updated after the plate
        has been instantiated.

        Args:
            dimensions: A PlateDimensions object containing the geometric properties.
        """
        self.width = dimensions.vertical - self.clipping
        self.length = dimensions.horizontal - self.clipping
        # After updating dimensions, we must also update the geometry dataclass
        self.geometry = GeometricProperties(
            along_length=self.gross_area_length,
            along_width=self.gross_area_width,
            total=self.gross_area_length or self.gross_area_width
        )

    @property
    def Fy(self) -> si.ksi: return self.material.Fy
    @property
    def Fu(self) -> si.ksi: return self.material.Fu
    @property
    def E(self) -> si.ksi: return self.material.E
    @property
    def gross_area_length(self) :
        """Calculates the gross area of the plate."""
        return (self.length ) * self.t if self.length else None
    @property
    def gross_area_width(self):
        """Calculates the gross area of the plate."""
        return (self.width) * self.t if self.width else None
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
    bolt_grade: BoltGrade
    material: Material
    angle: float = 0.0
from steelpy import aisc
from typing import Any, Type

@dataclass(frozen=True)
class WeldElectrode:
    """
    Represents the properties of a weld electrode. It's frozen because
    these are standard, immutable values.
    """
    Fexx: float  # Nominal strength of the weld electrode (e.g., 70 ksi for E70XX)

WeldType = Literal["fillet", "groove"]

@dataclass
class WeldConfiguration:
    """
    Defines the geometry and properties of a specific weld line in a connection.
    """
    weld_size: float
    length: float
    electrode: WeldElectrode  # Link to the WeldElectrode object
    weld_type: WeldType = "fillet" # Default to fillet, the most common type

@dataclass(frozen=True)
class PlateDimensions:
    vertical: float; horizontal: float; thickness: float

@dataclass(frozen=True)
class LoadMultipliers:
    shear_force_column_interface: float; shear_force_beam_interface: float
    normal_force_column: float; normal_force_beam: float
from typing import Union

@dataclass
class Connection:
    """
    A unified connection class that holds the configuration for either a bolted or
    welded connection, and critically, defines the context of the connection.
    """
    connection_type: Literal["bolted", "welded"]
    component: ConnectionComponent
    configuration: Union["BoltConfiguration", "WeldConfiguration"]
    override_Ag: Optional[float] = None  # Allow manual override of gross area

@dataclass
class ConnectionFactory:
    """Factory for creating Connection objects."""

    @staticmethod
    def create_bolted_connection(component: ConnectionComponent, *args, **kwargs) -> Connection:
        """
        Creates a bolted connection, requiring the component to be specified.
        """
        # Pop override_Ag if present, as it belongs to the Connection, not BoltConfiguration
        override_ag = kwargs.pop('override_Ag', None)
        
        return Connection(
            connection_type="bolted",
            component=component,
            configuration=BoltConfiguration(*args, **kwargs),
            override_Ag=override_ag
        )

    @staticmethod
    def create_welded_connection(component: ConnectionComponent, *args, **kwargs) -> Connection:
        """
        Creates a welded connection, requiring the component to be specified.
        """
        override_ag = kwargs.pop('override_Ag', None)

        return Connection(
            connection_type="welded",
            component=component,
            configuration=WeldConfiguration(*args, **kwargs),
            override_Ag=override_ag
        )