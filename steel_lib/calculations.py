import math
from typing import Any, Literal, Union, Dict, Optional, Type
from dataclasses import dataclass, field
from .si_units import si
from .data_models import (
    BoltConfiguration,
    Plate,
    PlateDimensions,
    LoadMultipliers,
    WeldConfiguration,
    Connection,
    ConnectionComponent,
)
from .debugging import DebugLogger

# Define a type hint for numbers for clarity
Numeric = Union[int, float]


def get_applicable_gross_area(member: Any, connection: Connection) -> float:
    """
    Determines the applicable gross area (Ag) based on the connection context.

    This function acts as the single source of truth for area selection. It prioritizes
    a manual override from the connection object, otherwise it uses the connection's
    specified component to look up the pre-calculated area from the member's
    geometry.

    Args:
        member (Any): The enriched member object, which must have a `.geometry` attribute.
        connection (Connection): The connection object, which provides the context.

    Returns:
        float: The applicable gross area for the calculation.

    Raises:
        AttributeError: If the member is missing the `.geometry` attribute or the
                        required pre-calculated area within it.
        ValueError: If the specified connection component does not have a corresponding
                    area in the member's geometry.
    """
    # 1. Prioritize the manual override if it exists
    if connection.override_Ag is not None:
        return connection.override_Ag

    # 2. Check for the mandatory geometry attribute on the member
    if not hasattr(member, 'geometry'):
        raise AttributeError("The provided 'member' object must be enriched with a '.geometry' attribute.")

    # 3. Look up the area based on the connection component
    component_name = connection.component.value
    applicable_area = getattr(member.geometry, component_name, None)

    if applicable_area is None:
        raise ValueError(
            f"The area for component '{component_name}' is not available in the "
            f"member's geometry. Available areas: {member.geometry}"
        )

    return applicable_area


def get_applicable_thickness(member: Any, connection: Connection) -> float:
    """
    Determines the applicable thickness based on the connection context.
    This ensures that calculations like net area are based on the correct
    thickness for the connected part (e.g., web vs. flange).

    Args:
        member (Any): The enriched member object.
        connection (Connection): The connection object providing context.

    Returns:
        float: The applicable thickness for the calculation.

    Raises:
        AttributeError: If the member lacks the required thickness attribute
                        (e.g., 'tw' for a web connection).
    """
    component = connection.component
    thickness = 0.0

    if component == ConnectionComponent.WEB:
        if not hasattr(member, 'tw'): raise AttributeError("Member lacks 'tw' for web thickness.")
        thickness = member.tw
    elif component == ConnectionComponent.FLANGE:
        if not hasattr(member, 'tf'): raise AttributeError("Member lacks 'tf' for flange thickness.")
        thickness = member.tf
    elif component in [ConnectionComponent.TOTAL, ConnectionComponent.LENGTH, ConnectionComponent.WIDTH]:
        # For plates or total sections, 't' is the primary attribute.
        # Fallback to 'tw' for other section types where 't' isn't defined.
        if hasattr(member, 't'):
            thickness = member.t
        elif hasattr(member, 'tw'):
            thickness = member.tw # A reasonable default for non-plate members
        else:
            raise AttributeError("Member has no recognizable thickness attribute ('t' or 'tw').")
    else:
        raise ValueError(f"Unknown connection component '{component}' for thickness lookup.")

    # Ensure units are applied if it's a raw number
    if isinstance(thickness, (int, float)) and not hasattr(thickness, 'units'):
        return thickness * si.inch
    return thickness


def round_to_interval(number: Numeric, interval: Numeric) -> Numeric:
    """
    Rounds a number to the nearest specified interval.
    """
    if interval == 0:
        raise ValueError("Interval cannot be zero.")
    return round(number / interval) * interval


def round_up_to_interval(number: Numeric, interval: Numeric) -> Numeric:
    """
    Rounds a number UP to the nearest specified interval (ceiling).
    """
    if interval == 0:
        raise ValueError("Interval cannot be zero.")
    return math.ceil(number / interval) * interval


def check_dcr(capacity, demand):
    return demand / capacity  # Returns the ratio of demand to capacity


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
        
        self.connection: BoltConfiguration = connection.configuration
        self.bolt_diameter = self.connection.bolt_diameter
        self.bolt_area = self._calculate_bolt_area()
        # Automatically get the nominal shear stress from the bolt grade
        self.fnv = self.connection.bolt_grade.Fnv

    def _calculate_bolt_area(self) -> float:
        """Calculates the gross area of the bolt."""
        return (self.bolt_diameter**2 / 4) * math.pi

    def calculate_capacity_fnv(
        self,
        number_of_shear_planes: int,
        resistance_factor: float = 0.75,
        debug: bool = False,
    ) -> float:
        """
        Calculates the design shear strength of the bolt.
        """
        logger = DebugLogger("Bolt Shear Strength", debug)
        logger.add_input("Nominal Shear Stress (Fnv)", self.fnv)
        logger.add_input("Bolt Diameter (d)", self.bolt_diameter)
        logger.add_input("Bolt Area (Ab)", self.bolt_area)
        logger.add_input("Number of Shear Planes", number_of_shear_planes)
        logger.add_input("Resistance Factor (φ)", resistance_factor)

        # Nominal strength (Rn) = Fnv * Ab * Ns
        nominal_strength = self.fnv * self.bolt_area * number_of_shear_planes
        logger.add_calculation("Nominal Strength (Rn = Fnv * Ab * Ns)", nominal_strength)

        # Design strength (φRn) = φ * Rn
        design_strength = resistance_factor * nominal_strength
        logger.add_output("Design Strength (φRn)", design_strength)

        logger.display()
        return design_strength
    def calculate_capacity_fnt(
        self,
        number_of_shear_planes: int,
        resistance_factor: float = 0.75,
        debug: bool = False,
    ) -> float:
        """
        Calculates the design tensile strength of the bolt.
        """
        logger = DebugLogger("Bolt Tensile Strength", debug)
        fnt = self.connection.bolt_grade.Fnt
        logger.add_input("Nominal Tensile Stress (Fnt)", fnt)
        logger.add_input("Bolt Area (Ab)", self.bolt_area)
        logger.add_input("Number of Shear Planes", number_of_shear_planes)
        logger.add_input("Resistance Factor (φ)", resistance_factor)

        # Nominal strength (Rn) = Fnt * Ab * Ns
        nominal_strength = fnt * self.bolt_area * number_of_shear_planes
        logger.add_calculation("Nominal Strength (Rn = Fnt * Ab * Ns)", nominal_strength)

        # Design strength (φRn) = φ * Rn
        design_strength = resistance_factor * nominal_strength
        logger.add_output("Design Strength (φRn)", design_strength)

        logger.display()
        return design_strength

class TensileYieldingCalculator:
    """
    Calculates the tensile yielding capacity of a member.
    """
    def __init__(self, member: Any, connection: Connection):
        self.member = member
        self.connection = connection
        self.Fy = self.member.Fy
        self.Ag = get_applicable_gross_area(member, connection)
        self.loading_condition = getattr(self.member, 'loading_condition', 1)

    def calculate_capacity(self, resistance_factor: float = 0.9, debug: bool = False) -> float:
        """
        Calculates the design tensile yielding strength.
        """
        nominal_strength = self.Fy * self.Ag
        design_strength = resistance_factor * nominal_strength * self.loading_condition

        logger = DebugLogger(f"Tensile Yielding ({self.connection.component.name})", debug)
        logger.add_input("Yield Strength (Fy)", self.Fy)
        logger.add_input(f"Applicable Gross Area (Ag) for {self.connection.component.name}", self.Ag)
        logger.add_input("Loading Condition", self.loading_condition)
        logger.add_input("Resistance Factor (φ)", resistance_factor)
        logger.add_calculation("Nominal Strength (Rn = Fy * Ag)", nominal_strength)
        logger.add_output("Design Strength (φRn)", design_strength)
        logger.display()

        return design_strength

class TensileRuptureCalculator:
    """
    Calculates the tensile rupture capacity of a member.
    """
    def __init__(self, member: Any, connection: Connection):
        if connection.connection_type != "bolted":
            raise ValueError("TensileRuptureCalculator only supports bolted connections.")
        self.member = member
        self.connection = connection
        self.bolt_config: BoltConfiguration = connection.configuration
        self.Fu = self.member.Fu
        self.loading_condition = getattr(self.member, 'loading_condition', 1)

    def _ubs_angle(self, x_bar, l):
        return 1 - x_bar / l

    def _calculate_anet_area(self):
        t = get_applicable_thickness(self.member, self.connection)
        S_c = self.bolt_config.column_spacing
        N_c = self.bolt_config.n_columns
        dbolt = self.bolt_config.bolt_diameter
        l = S_c * (N_c - 1)
        
        # For a W-section's web or flange, or other symmetric connections, x_bar is 0.
        # It is non-zero for asymmetric sections like angles.
        x_bar = 0
        if self.connection.component == ConnectionComponent.TOTAL and hasattr(self.member, 'x'):
            x_bar = self.member.x
        
        Ubs = self._ubs_angle(x_bar=x_bar, l=l)
        Ag = get_applicable_gross_area(self.member, self.connection)
        dhole = dbolt + (1/8) * si.inch
        An = Ag - dhole * self.bolt_config.n_rows * t
        return An * Ubs, Ubs

    def calculate_capacity(self, resistance_factor: float = 0.75, debug: bool = False) -> float:
        """
        Calculates the design tensile rupture strength.
        """
        An, Ubs = self._calculate_anet_area()
        nominal_strength = self.Fu * An
        design_strength = resistance_factor * nominal_strength * self.loading_condition

        logger = DebugLogger(f"Tensile Rupture ({self.connection.component.name})", debug)
        logger.add_input("Ultimate Strength (Fu)", self.Fu)
        logger.add_input(f"Net Area (An) for {self.connection.component.name}", An)
        logger.add_input("Shear Lag Factor (Ubs)", Ubs)
        logger.add_input("Loading Condition", self.loading_condition)
        logger.add_input("Resistance Factor (φ)", resistance_factor)
        logger.add_calculation("Nominal Strength (Rn = Fu * An)", nominal_strength)
        logger.add_output("Design Strength (φRn)", design_strength)
        logger.display()

        return design_strength

MemberType = Any # Use 'Any' for robust compatibility with steelpy objects
LoadingOrientation = Literal["Axial", "Shear"]

class BlockShearCalculator:
    """
    Calculates block shear capacity with correct unit handling and debug mode.
    """
    def __init__(
        self,
        member: MemberType,
        connection: Connection,
        loading_orientation: LoadingOrientation,
        loading_condition: int = 1,
        thickness: float = None,
    ):
        self.member = member
        if connection.connection_type != "bolted":
            raise ValueError("BlockShearCalculator only supports bolted connections.")
        self.connection: BoltConfiguration = connection.configuration
        self.loading_orientation = loading_orientation
        self.loading_condition = loading_condition

        # CORRECTED: _get_member_thickness now always returns a unit-aware value
        self.thickness = thickness if thickness is not None else self._get_member_thickness()
        self.bolt_hole_diameter = self.connection.bolt_diameter + (1/8) * si.inch

        if self.loading_orientation == "Shear" or self.member.Type == "L":
            self.failure_pattern = "L"
        else:
            self.failure_pattern = "U"

    def _get_member_thickness(self) -> float:
        """
        Determines thickness from various member types and ensures it has units.
        """
        if isinstance(self.member, Plate):
            # For Plate, .t already has units
            return self.member.t
        elif hasattr(self.member, 't'): # For steelpy L-shapes
            # Steelpy's .t is a float; we must add units.
            return self.member.t * si.inch
        elif hasattr(self.member, 'tw'): # For steelpy W-shape webs
            # Steelpy's .tw is a float; we must add units.
            return self.member.tw * si.inch
        raise AttributeError("Member has no recognizable thickness attribute.")

    # --- Calculation methods now correctly include loading_condition ---
    def _calculate_l_shear_yield_path(self) -> float:
        spacing, rows , edge_dist = (self.connection.row_spacing, self.connection.n_rows, self.connection.edge_distance_vertical) if self.loading_orientation == "Shear" else (self.connection.column_spacing, self.connection.n_columns, self.connection.edge_distance_horizontal)
        length = spacing * (rows - 1) + edge_dist
        # Apply loading_condition to the area calculation as in the original code
        return length * self.thickness * self.loading_condition

    def _calculate_l_shear_rupture_path(self) -> float:
        gross_area = self._calculate_l_shear_yield_path()
        rows = self.connection.n_rows if self.loading_orientation == "Shear" else self.connection.n_columns
        # Hole deduction must also be scaled by loading_condition
        hole_area_deduction = (rows - 0.5) * self.bolt_hole_diameter * self.thickness * self.loading_condition
        return gross_area - hole_area_deduction

    def _calculate_l_tension_rupture_path(self) -> float:
        if self.loading_orientation == "Axial":
            spacing, rows, edge_dist = self.connection.row_spacing, self.connection.n_rows, self.connection.edge_distance_vertical
        else:
            spacing, rows, edge_dist = self.connection.column_spacing, self.connection.n_columns, self.connection.edge_distance_horizontal

        net_length = (spacing * (rows - 1) + edge_dist) - ((rows - 0.5) * self.bolt_hole_diameter)
        return net_length * self.thickness * self.loading_condition

    def _calculate_u_tension_rupture_path(self) -> float:
        spacing, rows = self.connection.row_spacing, self.connection.n_rows
        net_length = (spacing * (rows - 1)) - ((rows - 1) * self.bolt_hole_diameter)
        return net_length * self.thickness * self.loading_condition

    def calculate_capacity(self, resistance_factor: float = 0.75, debug: bool = False) -> float:
        Ubs = 1.0
        Fu, Fy = self.member.Fu, self.member.Fy
        tension_rupture_component = 0.0

        if self.failure_pattern == "L":
            shear_yield_component = self._calculate_l_shear_yield_path()
            shear_rupture_component = self._calculate_l_shear_rupture_path()
            tension_rupture_component = self._calculate_l_tension_rupture_path()
            # ... (debug print statements)

        elif self.failure_pattern == "U":
            shear_yield_component = self._calculate_l_shear_yield_path() * 2
            shear_rupture_component = self._calculate_l_shear_rupture_path() * 2
            tension_rupture_component = self._calculate_u_tension_rupture_path()
            # ... (debug print statements)

        shear_force = 0.60 * min(shear_yield_component * Fy, shear_rupture_component * Fu)
        tension_force = Ubs * Fu * tension_rupture_component

        nominal_capacity = tension_force + shear_force
        design_capacity = resistance_factor * nominal_capacity

        logger = DebugLogger(f"Block Shear {self.failure_pattern}-Pattern", debug)
        logger.add_input("Gross Shear Area (Agv)", shear_yield_component)
        logger.add_input("Net Shear Area (Anv)", shear_rupture_component)
        logger.add_input("Net Tension Area (Ant)", tension_rupture_component)
        logger.add_input("Resistance Factor (φ)", resistance_factor)
        logger.add_calculation("Shear Yielding (0.6*Fy*Agv)", (0.6 * Fy * shear_yield_component))
        logger.add_calculation("Shear Rupture (0.6*Fu*Anv)", (0.6 * Fu * shear_rupture_component))
        logger.add_calculation("Tension Rupture (Ubs*Fu*Ant)", tension_force)
        logger.add_calculation("Nominal Capacity (Rn)", nominal_capacity)
        logger.add_output("Design Capacity (φRn)", design_capacity)
        logger.display()

        return design_capacity

class ConnectionCapacityCalculator:
    """
    Calculates the governing bolt capacity for an entire connection, considering
    bolt shear and bolt bearing/tearout for inner and outer bolts.
    """
    def __init__(self, member: Any, connection: Connection, loading_orientation: Literal["Axial", "Shear"]):
        self.member = member
        if connection.connection_type != "bolted":
            raise ValueError("ConnectionCapacityCalculator only supports bolted connections.")
        self.connection: BoltConfiguration = connection.configuration
        self.loading_orientation = loading_orientation

        # Extract common properties
        self.Fu = self.member.Fu
        self.thickness = self._get_member_thickness()
        self.bolt_diameter = self.connection.bolt_diameter
        self.bolt_diameter_nominal = self.connection.bolt_diameter + (1/16) * si.inch

        # Per AISC, standard hole diameter is bolt diameter + 1/8"
        self.hole_diameter = self.connection.bolt_diameter + (1/8) * si.inch

        # Determine geometry based on loading orientation (DRY principle)
        if self.loading_orientation == "Axial":
            self.longitudinal_spacing = self.connection.column_spacing
            self.longitudinal_edge_dist = self.connection.edge_distance_horizontal
            self.bolts_per_line = self.connection.n_columns
            self.num_lines = self.connection.n_rows
        else: # Shear
            self.longitudinal_spacing = self.connection.row_spacing
            self.longitudinal_edge_dist = self.connection.edge_distance_vertical
            self.bolts_per_line = self.connection.n_rows
            self.num_lines = self.connection.n_columns

    def _get_member_thickness(self) -> float:
        """
        Determines thickness from various member types and ensures it has units.
        """
        if isinstance(self.member, Plate):
            # For Plate, .t should have units from the data model
            return self.member.t
        elif hasattr(self.member, 't'): # For steelpy L-shapes
            # Assuming factory now provides units
            return self.member.t
        elif hasattr(self.member, 'tw'): # For steelpy W-shape webs
            # Assuming factory now provides units
            return self.member.tw
        raise AttributeError("Member has no recognizable thickness attribute.")

    def _calculate_lc_inner(self) -> float:
        """Calculates clear distance for an inner bolt."""
        return self.longitudinal_spacing - self.bolt_diameter_nominal

    def _calculate_lc_outer(self) -> float:
        """Calculates clear distance for an edge bolt."""
        return self.longitudinal_edge_dist - (self.bolt_diameter_nominal / 2)

    def calculate_capacity(
        self,
        number_of_shear_planes: int,
        resistance_factor: float = 0.75,
        debug: bool = False,
    ) -> float:
        """
        Calculates the total design capacity of the bolted connection.
        """
        # 1. Get the shear capacity of a single bolt (this is an upper limit)
        # Create a new Connection object to pass to the shear checker
        shear_connection = Connection(connection_type="bolted", configuration=self.connection)
        shear_checker = BoltShearCalculator(shear_connection)
        bolt_shear_strength = shear_checker.calculate_capacity_fnv(number_of_shear_planes, resistance_factor=0.75) # Use nominal for comparison

        # 2. Calculate clear distances
        lc_in = self._calculate_lc_inner()
        lc_out = self._calculate_lc_outer()

        # 3. Calculate nominal bearing/tearout capacities per bolt
        # Based on AISC J3-6a for standard holes where deformation is a consideration
        bearing_limit = 2.4 * self.bolt_diameter * self.thickness * self.Fu  * resistance_factor
        tearout_inner = 1.2 * lc_in * self.thickness * self.Fu * resistance_factor
        tearout_outer = 1.2 * lc_out * self.thickness * self.Fu *  resistance_factor

        # 4. Determine the governing nominal strength for inner and outer bolts
        r_nominal_inner = min(bolt_shear_strength, bearing_limit, tearout_inner)
        r_nominal_outer = min(bolt_shear_strength, bearing_limit, tearout_outer)

        # 5. Sum the capacities for all bolts in the connection
        total_nominal_capacity = (r_nominal_inner * (self.bolts_per_line - 1) + r_nominal_outer) * self.num_lines

        # 6. Apply resistance factor and loading condition for the final design strength
        # The member's loading_condition (e.g., 2 for double angle) scales the final result
        loading_condition = getattr(self.member, 'loading_condition', 1)
        design_capacity = total_nominal_capacity  * loading_condition

        logger = DebugLogger("Connection Capacity", debug)
        logger.add_input("Member Fu", self.Fu)
        logger.add_input("Member Thickness", self.thickness)
        logger.add_input("Bolt Diameter", self.bolt_diameter)
        logger.add_input("Hole Diameter", self.hole_diameter)
        logger.add_input("Longitudinal Spacing", self.longitudinal_spacing)
        logger.add_input("Longitudinal Edge Dist", self.longitudinal_edge_dist)
        logger.add_input("Bolts per Line", self.bolts_per_line)
        logger.add_input("Number of Lines", self.num_lines)
        logger.add_input("Resistance Factor (φ)", resistance_factor)
        logger.add_input("Loading Condition Multiplier", loading_condition)
        logger.add_calculation("Inner Bolt Clear Distance (lc_in)", lc_in)
        logger.add_calculation("Outer Bolt Clear Distance (lc_out)", lc_out)
        logger.add_calculation("Bolt Shear Strength", bolt_shear_strength)
        logger.add_calculation("Bearing Limit (2.4*d*t*Fu)", bearing_limit)
        logger.add_calculation("Tearout (Inner Bolt)", tearout_inner)
        logger.add_calculation("Tearout (Outer Bolt)", tearout_outer)
        logger.add_calculation("Governing Strength (Inner)", r_nominal_inner)
        logger.add_calculation("Governing Strength (Outer)", r_nominal_outer)
        logger.add_calculation("Total Nominal Strength (Rn)", total_nominal_capacity)
        logger.add_output("Final Design Capacity (φRn)", design_capacity)
        logger.display()

        return design_capacity


class TensileYieldWhitmore:
    """
    Calculates the tensile yielding capacity based on the Whitmore section.
    """

    def __init__(self, member: Any, connection: Connection):
        """Initializes the calculator with the member and connection objects."""
        self.member = member
        if connection.connection_type != "bolted":
            raise ValueError("TensileYieldWhitmore only supports bolted connections.")
        self.connection: BoltConfiguration = connection.configuration
        self.Fy = self.member.Fy
        self.loading_condition = getattr(self.member, "loading_condition", 1)
        self.n_cols = self.connection.n_columns
        self.spacing_col = self.connection.column_spacing
        self.spacing_row = self.connection.row_spacing
        self.t = self._get_member_thickness()

    def _get_member_thickness(self) -> float:
        """Determines thickness from various member types and ensures it has units."""
        if hasattr(self.member, "t"):
            t_val = self.member.t
            if hasattr(t_val, 'units'):
                return t_val
            if isinstance(t_val, (int, float)):
                return t_val * si.inch
            return t_val
        elif hasattr(self.member, "tw"):
            tw_val = self.member.tw
            if isinstance(tw_val, (int, float)):
                return tw_val * si.inch
            return tw_val
        raise AttributeError("Member does not have a recognizable thickness attribute.")

    @property
    def length_whitmore(self) -> float:
        """Calculates the effective width of the Whitmore section."""
        bolt_group_length = (self.n_cols - 1) * self.spacing_col
        spread_width = 2 * (bolt_group_length * math.tan(math.radians(30)))
        return self.spacing_row + spread_width

    @property
    def area_whitmore(self) -> float:
        """Calculates the area of the Whitmore section."""
        return (
            self.length_whitmore - 4.7 * si.inch
        ) * self.t + 4.7 * si.inch * 0.515 * si.inch

    def calculate_capacity(
        self, resistance_factor: float = 0.9, debug: bool = False
    ) -> float:
        """
        Calculates the design tensile yield strength of the Whitmore section.
        """
        nominal_capacity = self.Fy * self.area_whitmore
        design_capacity = (
            nominal_capacity * resistance_factor * self.loading_condition
        )
        logger = DebugLogger("Whitmore Section Tensile Yield", debug)
        logger.add_input("Yield Strength (Fy)", self.Fy)
        logger.add_input("Member Thickness (t)", self.t)
        logger.add_input("Resistance Factor (φ)", resistance_factor)
        logger.add_input("Loading Condition Multiplier", self.loading_condition)
        logger.add_calculation("Effective Length (Lw)", self.length_whitmore)
        logger.add_calculation("Effective Area (Aw)", self.area_whitmore)
        logger.add_calculation("Nominal Capacity (Rn)", nominal_capacity)
        logger.add_output("Final Design Capacity (φRn)", design_capacity)
        logger.display()
        return design_capacity


class CompressionBucklingCalculator:
    """
    Calculates the compression buckling capacity of a member.
    """

    def __init__(self, member: Any, connection: Connection):
        """Initializes the calculator with the member and connection objects."""
        self.member = member
        if connection.connection_type != "bolted":
            raise ValueError("CompressionBucklingCalculator only supports bolted connections.")
        self.connection: BoltConfiguration = connection.configuration
        self.connection_type = self.connection.connection_type
        self.Fy = self.member.Fy
        self.t = self._get_member_thickness()

    def _get_member_thickness(self) -> float:
        """Determ-ines thickness from various member types and ensures it has units."""
        if hasattr(self.member, "t"):
            t_val = self.member.t
            if hasattr(t_val, 'units'):
                return t_val
            if isinstance(t_val, (int, float)):
                return t_val * si.inch
            return t_val
        elif hasattr(self.member, "tw"):
            tw_val = self.member.tw
            if isinstance(tw_val, (int, float)):
                return tw_val * si.inch
            return tw_val
        raise AttributeError("Member does not have a recognizable thickness attribute.")

    @property
    def k(self) -> float:
        return (
            0.5
            if self.connection_type == "bracing"
            else 1.2
        )

    @property
    def r(self):
        return self.t / math.sqrt(12)

    @property
    def slenderness_ratio(self):
        return (self.k * 9.76 * si.inch) / (self.r)

    def calculate_capacity(self, resistance_factor=0.9, debug: bool = False) -> float:
        """
        Calculates the design compression buckling strength of the member.
        """
        logger = DebugLogger("Compression Buckling", debug)
        logger.add_input("k", self.k)
        logger.add_input("r", self.r)
        logger.add_input("Slenderness Ratio", self.slenderness_ratio)
        logger.add_input("Fy", self.Fy)
        logger.add_input("Resistance Factor (φ)", resistance_factor)

        if self.slenderness_ratio <= 25:
            capacity = self.Fy * 20.9 * si.inch**2 * resistance_factor
            logger.add_output("Design Capacity (φRn)", capacity)
            logger.display()
            return capacity
        else:
            raise ValueError(
                "Member is not slender enough for compression buckling calculation."
            )


class UFMCalculator:
    """
    Calculates UFM endplate dimensions and load multipliers with a
    comprehensive debug mode to show all intermediate values.
    """

    def __init__(self, beam: Any, support: Any, endplate: Any, connection: Any):
        self._beam_depth = self._get_attribute(beam, ["d", "depth"])
        self._support_depth = self._get_attribute(support, ["d", "depth"])
        self._end_plate_thickness = self._get_attribute(endplate, ["t", "thickness"])
        self._edge_dist = connection.edge_distance_vertical
        self._row_spacing = connection.row_spacing
        self._n_rows = connection.n_rows
        self._angle_rad = connection.angle

    def _get_attribute(self, obj: Any, potential_names: list[str]) -> float:
        for name in potential_names:
            if hasattr(obj, name):
                value = getattr(obj, name)
                if hasattr(value, 'units'):
                    return value
                # Check if the value is a number before applying units
                if isinstance(value, (int, float)):
                    return value * si.inch
                return value # Return as is if it's not a number and has no units
        raise AttributeError(
            f"Object does not have any of the expected attributes: {potential_names}"
        )

    @property
    def _beam_half_depth(self) -> float:
        return self._beam_depth / 2

    @property
    def _support_half_depth(self) -> float:
        return self._support_depth / 2

    @property
    def _beta(self) -> float:
        return self._edge_dist + ((self._n_rows - 1) * self._row_spacing) / 2

    @property
    def _alpha(self) -> float:
        return (
            (self._beam_half_depth + self._beta) * math.tan(self._angle_rad)
            - self._support_half_depth
        )

    @property
    def _r(self) -> float:
        return (
            (self._alpha + self._support_half_depth) ** 2
            + (self._beam_half_depth + self._beta) ** 2
        ) ** 0.5

    @property
    def _horizontal_plate_length(self) -> float:
        k_line_clearance = 0.75 * si.inch
        return 2 * self._alpha - 2 * self._end_plate_thickness - k_line_clearance

    def get_dimensions(self, debug: bool = False) -> PlateDimensions:
        """Calculates and returns the final, rounded plate dimensions."""
        logger = DebugLogger("UFM Plate Dimensions", debug)
        logger.add_input("Beam Depth", self._beam_depth)
        logger.add_input("Support Depth", self._support_depth)
        logger.add_input("End Plate Thickness", self._end_plate_thickness)
        logger.add_input("Edge Distance (vert)", self._edge_dist)
        logger.add_input("Row Spacing", self._row_spacing)
        logger.add_input("Number of Rows", self._n_rows)
        logger.add_input("Connection Angle", f"{math.degrees(self._angle_rad):.2f} degrees")

        logger.add_calculation("_beta", self._beta)
        logger.add_calculation("_alpha", self._alpha)
        logger.add_calculation("Horizontal Plate Length (unrounded)", self._horizontal_plate_length)

        unrounded_vertical = (
            self._edge_dist * 2
            + ((self._n_rows - 1) * self._row_spacing)
            + 0.5 * si.inch
        )
        logger.add_calculation("Vertical Plate Length (unrounded)", unrounded_vertical)

        vertical_dim = round_up_to_interval(
            number=unrounded_vertical, interval=0.25 * si.inch
        )
        horizontal_dim = round_up_to_interval(
            number=self._horizontal_plate_length, interval=0.25 * si.inch
        )

        logger.add_output("Final Vertical Dimension", vertical_dim)
        logger.add_output("Final Horizontal Dimension", horizontal_dim)
        logger.display()

        return PlateDimensions(
            vertical=vertical_dim,
            horizontal=horizontal_dim,
            thickness=self._end_plate_thickness,
        )

    def get_loads_multipliers(self, debug: bool = False) -> LoadMultipliers:
        """Calculates and returns the load multipliers for the UFM interfaces."""
        logger = DebugLogger("UFM Load Multipliers", debug)
        logger.add_input("Beam Depth", self._beam_depth)
        logger.add_input("Support Depth", self._support_depth)
        logger.add_input("Edge Distance (vert)", self._edge_dist)
        logger.add_input("Row Spacing", self._row_spacing)
        logger.add_input("Number of Rows", self._n_rows)
        logger.add_input("Connection Angle", f"{math.degrees(self._angle_rad):.2f} degrees")

        logger.add_calculation("_beta", self._beta)
        logger.add_calculation("_alpha", self._alpha)
        logger.add_calculation("_r", self._r)

        multipliers = LoadMultipliers(
            shear_force_column_interface=self._beta / self._r,
            shear_force_beam_interface=self._beam_half_depth / self._r,
            normal_force_column=self._support_half_depth / self._r,
            normal_force_beam=self._alpha / self._r,
        )

        logger.add_output("Shear Force (Column Interface)", multipliers.shear_force_column_interface)
        logger.add_output("Shear Force (Beam Interface)", multipliers.shear_force_beam_interface)
        logger.add_output("Normal Force (Column)", multipliers.normal_force_column)
        logger.add_output("Normal Force (Beam)", multipliers.normal_force_beam)
        logger.display()

        return multipliers


class PlateTensileYieldingCalculator:
    """
    Calculates design tensile strength based on gross section yielding (AISC J4.1a).
    This calculator expects to be initialized with a member object that has a
    '.dimensions' attribute containing a PlateDimensions object.
    """

    def __init__(self, member: Any):
        """
        Initializes the calculator by extracting required data from the member object.
        """
        if not hasattr(member, "dimensions"):
            raise AttributeError(
                "The provided 'member' object must have a '.dimensions' attribute."
            )
        self.dimensions: PlateDimensions = member.dimensions
        self.Fy = member.Fy
        self.loading_condition = getattr(member, "loading_condition", 1)
        self._thickness = self.dimensions.thickness

    def _calculate_capacity_for_path(
        self,
        gross_length: float,
        interface_name: str,
        resistance_factor: float,
        debug: bool,
    ) -> float:
        """A private helper to perform the core calculation, avoiding code duplication."""
        effective_length = gross_length - 0.75 * si.inch
        gross_area = effective_length * self._thickness
        nominal_capacity = self.Fy * gross_area
        design_capacity = (
            nominal_capacity * resistance_factor * self.loading_condition
        )
        logger = DebugLogger(f"Plate Tensile Yielding ({interface_name})", debug)
        logger.add_input("Yield Strength (Fy)", self.Fy)
        logger.add_input("Gross Length", gross_length)
        logger.add_input("Thickness", self._thickness)
        logger.add_input("Resistance Factor (φ)", resistance_factor)
        logger.add_input("Loading Condition", self.loading_condition)
        logger.add_calculation("Effective Length", effective_length)
        logger.add_calculation("Gross Area (Ag)", gross_area)
        logger.add_calculation("Nominal Capacity (Pn)", nominal_capacity)
        logger.add_output("Final Design Capacity (φPn)", design_capacity)
        logger.display()
        return design_capacity

    def calculate_capacity_horizontal(
        self, resistance_factor: float = 0.9, debug: bool = False
    ) -> float:
        """Calculates the design tensile yield strength along the HORIZONTAL path."""
        return self._calculate_capacity_for_path(
            gross_length=self.dimensions.horizontal,
            interface_name="Horizontal",
            resistance_factor=resistance_factor,
            debug=debug,
        )

    def calculate_capacity_vertical(
        self, resistance_factor: float = 0.9, debug: bool = False
    ) -> float:
        """Calculates the design tensile yield strength along the VERTICAL path."""
        return self._calculate_capacity_for_path(
            gross_length=self.dimensions.vertical,
            interface_name="Vertical",
            resistance_factor=resistance_factor,
            debug=debug,
        )


class WebLocalYieldingCalculator:
    """
    Calculates the web local yielding capacity based on AISC Specification J10.2,
    with a clear separation between input and calculation debugging.
    """

    def __init__(self, member: Any, connection: Any):
        """Initializes the calculator by extracting all necessary primitive values."""
        self._Fy = member.Fy
        self._tw = self._get_attribute(member, ["tw"])
        self._k = self._get_attribute(member, ["k", "k_det"])
        self._d = self._get_attribute(member, ["d", "depth"])
        self._connection_length = connection.length
        self._loading_condition = getattr(member, "loading_condition", 1)

    def _get_attribute(self, obj: Any, potential_names: list[str]) -> float:
        """Safely gets a numeric attribute from an object and ensures it has units."""
        for name in potential_names:
            if hasattr(obj, name):
                value = getattr(obj, name)
                return value if hasattr(value, "units") else value * si.inch
        raise AttributeError(
            f"Object does not have any of the expected attributes: {potential_names}"
        )

    def calculate_capacity(
        self, thickness_pl: float, resistance_factor: float = 1.0, debug: bool = False
    ) -> float:
        """
        Calculates the design web local yielding strength (φRn).
        """
        logger = DebugLogger("Web Local Yielding", debug)
        logger.add_input("Yield Strength (Fy)", self._Fy)
        logger.add_input("Web Thickness (tw)", self._tw)
        logger.add_input("Detailing Distance (k)", self._k)
        logger.add_input("Member Depth (d)", self._d)
        logger.add_input("Connection Length (lb)", self._connection_length)
        logger.add_input("End Plate Thickness (tpl)", thickness_pl)
        logger.add_input("Resistance Factor (φ)", resistance_factor)
        logger.add_input("Loading Condition", self._loading_condition)

        clip_dist = 3 / 4 * si.inch
        connection_load_centroid = (
            self._connection_length / 2 + clip_dist + thickness_pl
        )
        logger.add_calculation("Connection Load Centroid", connection_load_centroid)

        if connection_load_centroid <= self._d:
            multiplier_k = 2.5
        else:
            multiplier_k = 5.0
        logger.add_calculation("Multiplier (k)", multiplier_k)

        bearing_length = (multiplier_k * self._k) + self._connection_length
        logger.add_calculation("Bearing Length", bearing_length)

        nominal_capacity = self._Fy * self._tw * bearing_length
        logger.add_calculation("Nominal Capacity (Pn)", nominal_capacity)

        design_capacity = (
            nominal_capacity * resistance_factor * self._loading_condition
        )
        logger.add_output("Design Capacity (φRn)", design_capacity)
        logger.display()

        return design_capacity
    
class WebLocalCrippingCalculator:
    """
    Calculates the web local crippling capacity based on AISC Specification J10.2,
    with a clear separation between input and calculation debugging.
    """

    def __init__(self, member: Any, connection: Any):
        """Initializes the calculator by extracting all necessary primitive values."""
        self._Fy = member.Fy
        self._tw = self._get_attribute(member, ["tw"])
        self._k = self._get_attribute(member, ["k", "k_det"])
        self._d = self._get_attribute(member, ["d", "depth"])
        self._connection_length = connection.length
        self._loading_condition = getattr(member, "loading_condition", 1)
        self._E = member.E if hasattr(member, 'E') else 29000 * si.ksi
        self._tf = self._get_attribute(member, ["tf", "thickness_flange"])


    def _get_attribute(self, obj: Any, potential_names: list[str]) -> float:
        """Safely gets a numeric attribute from an object and ensures it has units."""
        for name in potential_names:
            if hasattr(obj, name):
                value = getattr(obj, name)
                return value if hasattr(value, "units") else value * si.inch
        raise AttributeError(
            f"Object does not have any of the expected attributes: {potential_names}"
        )

    def calculate_capacity(
        self, thickness_pl: float, resistance_factor: float = 0.75, debug: bool = False
    ) -> float:
        """
        Calculates the design web local crippling strength (φRn) based on AISC J10.3.
        """
        logger = DebugLogger("Web Local Crippling", debug)
        logger.add_input("Yield Strength (Fy)", self._Fy)
        logger.add_input("Web Thickness (tw)", self._tw)
        logger.add_input("Flange Thickness (tf)", self._tf)
        logger.add_input("Modulus of Elasticity (E)", self._E)
        logger.add_input("Member Depth (d)", self._d)
        logger.add_input("Connection Length (lb)", self._connection_length)
        logger.add_input("End Plate Thickness (tpl)", thickness_pl)
        logger.add_input("Resistance Factor (φ)", resistance_factor)
        logger.add_input("Loading Condition", self._loading_condition)

        # Common term in AISC J10.3 equations
        ef_term = ((self._E * self._Fy * self._tf) / self._tw) ** 0.5
        ef_term = ef_term.to('ksi')
        logger.add_calculation("EF Term ((E*Fy*tf)/tw)^0.5", ef_term)

        # Determine which case of J10.3 applies
        clip_dist = 3 / 4 * si.inch
        connection_load_centroid = (
            self._connection_length / 2 + clip_dist + thickness_pl
        )
        logger.add_calculation("Connection Load Centroid", connection_load_centroid)

        # Ratio of bearing length to member depth
        lb_d_ratio = self._connection_length / self._d
        logger.add_calculation(
            "Bearing Length to Depth Ratio (lb/d)", lb_d_ratio
        )

        # Ratio of web thickness to flange thickness
        tw_tf_ratio = self._tw / self._tf
        logger.add_calculation(
            "Web to Flange Thickness Ratio (tw/tf)", tw_tf_ratio
        )

        nominal_capacity = 0.0

        # Case 1: Load is applied at a distance from the member end >= d
        if connection_load_centroid >= self._d/2:
            formula_part = 1 + 3 * (lb_d_ratio) * (tw_tf_ratio**1.5)
            nominal_capacity = 0.80 * self._tw**2 * formula_part * ef_term
            logger.add_calculation(
                "Formula Part (1 + 3*(lb/d)*(tw/tf)^1.5)", formula_part
            )
            logger.add_calculation(
                "Nominal Capacity (Rn) - Eq. J10-4", nominal_capacity
            )

        # Case 2: Load is applied at a distance from the member end < d
        else:
            # Subcase a: lb/d <= 0.2
            if lb_d_ratio <= 0.2:
                formula_part = 1 + 3 * (lb_d_ratio) * (tw_tf_ratio**1.5)
                nominal_capacity = 0.40 * self._tw**2 * formula_part * ef_term
                logger.add_calculation(
                    "Formula Part (1 + 3*(lb/d)*(tw/tf)^1.5)", formula_part
                )
                logger.add_calculation(
                    "Nominal Capacity (Rn) - Eq. J10-5a", nominal_capacity
                )
            # Subcase b: lb/d > 0.2
            else:
                formula_part = 1 + (4 * lb_d_ratio - 0.2) * (tw_tf_ratio**1.5)
                nominal_capacity = 0.40 * self._tw**2 * formula_part * ef_term
                logger.add_calculation(
                    "Formula Part (1 + (4*lb/d - 0.2)*(tw/tf)^1.5)",
                    formula_part,
                )
                logger.add_calculation(
                    "Nominal Capacity (Rn) - Eq. J10-5b", nominal_capacity
                )

        design_capacity = (
            nominal_capacity * resistance_factor * self._loading_condition
        )
        logger.add_output("Design Capacity (φRn)", design_capacity)
        logger.display()

        return design_capacity
class ShearYieldingCalculator:
    """
    Calculates the shear yielding capacity of a member based on AISC Specification J3.2.
    This class is designed to handle both L and U patterns for block shear calculations.
    """

    def __init__(self, member: Any, connection: Connection, loading_orientation: Literal["Axial", "Shear"], failure_pattern: Literal["L", "U"]):
        self.member = member
        if connection.connection_type not in ["bolted", "welded"]:
            raise ValueError("ShearYieldingCalculator only supports bolted and welded connections.")
        self.connection: BoltConfiguration = connection.configuration
        self.connection_type = connection.connection_type
        self.loading_orientation = loading_orientation
        self.failure_pattern = failure_pattern

        # Extract common properties
        self.Fy = self.member.Fy
        self.Fu = self.member.Fu
        self.thickness = self._get_member_thickness()


    def _get_member_thickness(self) -> float:
        """Determines thickness from various member types and ensures it has units."""
        if hasattr(self.member, "t"):
            t_val = self.member.t
            if hasattr(t_val, 'units'):
                return t_val
            if isinstance(t_val, (int, float)):
                return t_val * si.inch
            return t_val
        elif hasattr(self.member, "tw"):
            tw_val = self.member.tw
            if isinstance(tw_val, (int, float)):
                return tw_val * si.inch
            return tw_val
        raise AttributeError("Member does not have a recognizable thickness attribute.")

    def calculate_capacity(self, resistance_factor: float = 1.0, debug: bool = False) -> float:
        """
        Calculates the design shear yielding strength (φRn).
        """
        logger = DebugLogger("Shear Yielding", debug)
        logger.add_input("Yield Strength (Fy)", self.Fy)
        logger.add_input("Resistance Factor (φ)", resistance_factor)

        if self.connection_type == "bolted":
            gross_area = self._calculate_bolted_gross_area()
            logger.add_input("Gross Area (Ag)", gross_area)
        elif self.connection_type == "welded":
            # Placeholder for welded connection logic
            gross_area = 0 # Replace with actual calculation
            logger.add_input("Gross Area (Ag)", "N/A for welded connection")


        nominal_capacity = 0.6 * self.Fy * gross_area
        design_capacity = resistance_factor * nominal_capacity

        logger.add_calculation("Nominal Capacity (0.6 * Fy * Ag)", nominal_capacity)
        logger.add_output("Design Capacity (φRn)", design_capacity)
        logger.display()

        return design_capacity

