import math
from typing import Any, Literal, Union, Dict, Optional, Type
from dataclasses import dataclass, field
import forallpeople as si
from .data_models import (
    BoltConfiguration,
    Plate,
    PlateDimensions,
    LoadMultipliers,
    WeldConfiguration,
)

si.environment('structural', top_level=False)


# Define a type hint for numbers for clarity
Numeric = Union[int, float]


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
    def __init__(self, connection: BoltConfiguration):
        """
        Initializes the calculator with the connection configuration.
        """
        self.connection = connection
        self.bolt_diameter = self.connection.bolt_diameter
        self.bolt_area = self._calculate_bolt_area()
        # Automatically get the nominal shear stress from the bolt grade
        self.fnv = self.connection.bolt_grade.Fnv

    def _calculate_bolt_area(self) -> float:
        """Calculates the gross area of the bolt."""
        return (self.bolt_diameter**2 / 4) * math.pi

    def calculate_capacity(
        self,
        number_of_shear_planes: int,
        resistance_factor: float = 0.75,
        debug: bool = False,
    ) -> float:
        """
        Calculates the design shear strength of the bolt.
        """
        # Nominal strength (Rn) = Fnv * Ab * Ns
        nominal_strength = self.fnv * self.bolt_area * number_of_shear_planes

        # Design strength (φRn) = φ * Rn
        design_strength = resistance_factor * nominal_strength

        if debug:
            print("\n--- DEBUG: Bolt Shear Strength Calculation ---")
            print(f"  Inputs:")
            print(f"    Nominal Shear Stress (Fnv): {self.fnv:.3f}")
            print(f"    Bolt Diameter (d):          {self.bolt_diameter:.3f}")
            print(f"    Bolt Area (Ab):             {self.bolt_area:.4f}")
            print(f"    Number of Shear Planes:     {number_of_shear_planes}")
            print(f"  Calculation:")
            print(f"    Nominal Strength (Rn = Fnv * Ab * Ns): {nominal_strength:.2f}")
            print(f"    Resistance Factor (φ):                 {resistance_factor}")
            print(f"  -------------------------------------------")
            print(f"    Design Strength (φRn):                 {design_strength:.2f}")

        return design_strength

class TensileYieldingCalculator:
    """
    Calculates the tensile yielding capacity of a member.
    """
    def __init__(self, member: Any):
        self.member = member
        self.Fy = self.member.Fy
        self.Ag = self.member.area
        self.loading_condition = getattr(self.member, 'loading_condition', 1)

    def calculate_capacity(self, resistance_factor: float = 0.9, debug: bool = False) -> float:
        """
        Calculates the design tensile yielding strength.
        """
        nominal_strength = self.Fy * self.Ag
        design_strength = resistance_factor * nominal_strength * self.loading_condition

        if debug:
            print("\n--- DEBUG: Tensile Yielding Calculation ---")
            print(f"  Inputs:")
            print(f"    Yield Strength (Fy):      {self.Fy:.3f}")
            print(f"    Gross Area (Ag):          {self.Ag:.4f}")
            print(f"    Loading Condition:        {self.loading_condition}")
            print(f"  Calculation:")
            print(f"    Nominal Strength (Rn = Fy * Ag): {nominal_strength:.2f}")
            print(f"    Resistance Factor (φ):           {resistance_factor}")
            print(f"  -------------------------------------------")
            print(f"    Design Strength (φRn):           {design_strength:.2f}")

        return design_strength

class TensileRuptureCalculator:
    """
    Calculates the tensile rupture capacity of a member.
    """
    def __init__(self, member: Any, connection: BoltConfiguration):
        self.member = member
        self.connection = connection
        self.Fu = self.member.Fu
        self.loading_condition = getattr(self.member, 'loading_condition', 1)

    def _ubs_angle(self, x_bar, l):
        return 1 - x_bar / l

    def _calculate_anet_area(self):
        t = self.member.t
        S_c = self.connection.column_spacing
        N_c = self.connection.n_columns
        dbolt = self.connection.bolt_diameter
        l = S_c * (N_c - 1)
        x_bar = self.member.x
        Ubs = self._ubs_angle(x_bar=x_bar, l=l)
        Ag = self.member.area
        dhole = dbolt + (1/8) * si.inch
        An = Ag - dhole * self.connection.n_rows * t
        return An * Ubs, Ubs

    def calculate_capacity(self, resistance_factor: float = 0.75, debug: bool = False) -> float:
        """
        Calculates the design tensile rupture strength.
        """
        An, Ubs = self._calculate_anet_area()
        nominal_strength = self.Fu * An
        design_strength = resistance_factor * nominal_strength * self.loading_condition

        if debug:
            print("\n--- DEBUG: Tensile Rupture Calculation ---")
            print(f"  Inputs:")
            print(f"    Ultimate Strength (Fu):   {self.Fu:.3f}")
            print(f"    Net Area (An):            {An:.4f}")
            print(f"    Shear Lag Factor (Ubs):   {Ubs:.4f}")
            print(f"    Loading Condition:        {self.loading_condition}")
            print(f"  Calculation:")
            print(f"    Nominal Strength (Rn = Fu * An): {nominal_strength:.2f}")
            print(f"    Resistance Factor (φ):           {resistance_factor}")
            print(f"  -------------------------------------------")
            print(f"    Design Strength (φRn):           {design_strength:.2f}")

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
        connection: BoltConfiguration,
        loading_orientation: LoadingOrientation,
        loading_condition: int = 1,
        thickness: float = None,
    ):
        self.member = member
        self.connection = connection
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

        if debug:
            print(f"\n--- DEBUG: Block Shear {self.failure_pattern}-Pattern Calculation ---")
            print(f"  Areas:")
            print(f"    Gross Shear Area (Agv):   {shear_yield_component:.4f}")
            print(f"    Net Shear Area (Anv):     {shear_rupture_component:.4f}")
            print(f"    Net Tension Area (Ant):   {tension_rupture_component:.4f}")
            print(f"  Forces:")
            print(f"    Shear Yielding (0.6*Fy*Agv):   {(0.6 * Fy * shear_yield_component):.2f}")
            print(f"    Shear Rupture (0.6*Fu*Anv):    {(0.6 * Fu * shear_rupture_component):.2f}")
            print(f"    Tension Rupture (Ubs*Fu*Ant):  {tension_force:.2f}")
            print(f"  Capacities:")
            print(f"    Nominal Capacity (Rn):      {nominal_capacity:.2f}")
            print(f"    Resistance Factor (φ):      {resistance_factor}")
            print(f"  -------------------------------------------")
            print(f"    Design Capacity (φRn):      {design_capacity:.2f}")

        return design_capacity

class ConnectionCapacityCalculator:
    """
    Calculates the governing bolt capacity for an entire connection, considering
    bolt shear and bolt bearing/tearout for inner and outer bolts.
    """
    def __init__(self, member: Any, connection: BoltConfiguration, loading_orientation: Literal["Axial", "Shear"]):
        self.member = member
        self.connection = connection
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
        shear_checker = BoltShearCalculator(self.connection)
        bolt_shear_strength = shear_checker.calculate_capacity(number_of_shear_planes, resistance_factor=0.75) # Use nominal for comparison

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

        if debug:
            print("\n--- DEBUG: Connection Capacity Calculation ---")
            print(f"  Inputs:")
            print(f"    Member Fu:                {self.Fu:.3f}")
            print(f"    Member Thickness:         {self.thickness:.3f}")
            print(f"    Bolt Diameter:            {self.bolt_diameter:.3f}")
            print(f"    Hole Diameter:            {self.hole_diameter:.3f}")
            print(f"    Longitudinal Spacing:     {self.longitudinal_spacing:.3f}")
            print(f"    Longitudinal Edge Dist:   {self.longitudinal_edge_dist:.3f}")
            print(f"    Bolts per Line:           {self.bolts_per_line}")
            print(f"    Number of Lines:          {self.num_lines}")
            print(f"  Clear Distances:")
            print(f"    Inner Bolt (lc_in):       {lc_in:.3f}")
            print(f"    Outer Bolt (lc_out):      {lc_out:.3f}")
            print(f"  Single Bolt Capacities (Nominal):")
            print(f"    Bolt Shear Strength:        {bolt_shear_strength:.2f}")
            print(f"    Bearing Limit (2.4*d*t*Fu): {bearing_limit:.2f}")
            print(f"    Tearout (Inner Bolt):       {tearout_inner:.2f}")
            print(f"    Tearout (Outer Bolt):       {tearout_outer:.2f}")
            print(f"    -------------------------------------------")
            print(f"    Governing Strength (Inner): {r_nominal_inner:.2f}")
            print(f"    Governing Strength (Outer): {r_nominal_outer:.2f}")
            print("\n  Total Connection Capacity:")
            print(f"    Total Nominal Strength (Rn): {total_nominal_capacity:.2f}")
            print(f"    Resistance Factor (φ):       {resistance_factor}")
            print(f"    Loading Condition Multiplier:{loading_condition}")
            print(f"    -------------------------------------------")
            print(f"    Final Design Capacity (φRn): {design_capacity:.2f}")

        return design_capacity


class TensileYieldWhitmore:
    """
    Calculates the tensile yielding capacity based on the Whitmore section.
    """

    def __init__(self, member: Any, connection: BoltConfiguration):
        """Initializes the calculator with the member and connection objects."""
        self.member = member
        self.connection = connection
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
        if debug:
            print("--- DEBUG: Whitmore Section Tensile Yield ---")
            print(f"  Inputs:")
            print(f"    Yield Strength (Fy):         {self.Fy}")
            print(f"    Member Thickness (t):        {self.t:.3f}")
            print(f"  Whitmore Geometry:")
            print(f"    Effective Length (Lw):       {self.length_whitmore:.4f}")
            print(f"    Effective Area (Aw):         {self.area_whitmore:.4f}")
            print(f"  Calculation:")
            print(f"    Nominal Capacity (Rn):       {nominal_capacity:.2f}")
            print(f"    Resistance Factor (φ):       {resistance_factor}")
            print(
                f"    Loading Condition Multiplier:{self.loading_condition}"
            )
            print(f"    -------------------------------------------")
            print(f"    Final Design Capacity (φRn): {design_capacity:.2f}")
        return design_capacity


class CompressionBucklingCalculator:
    """
    Calculates the compression buckling capacity of a member.
    """

    def __init__(self, member: Any, connection: BoltConfiguration):
        """Initializes the calculator with the member and connection objects."""
        self.member = member
        self.connection = connection
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
        if self.slenderness_ratio <= 25:
            return self.Fy * 20.9 * si.inch**2 * resistance_factor
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
        self._debug_header_printed = False

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

    def _print_debug_inputs(self):
        """Prints a standard header with all initial inputs, but only once."""
        if not self._debug_header_printed:
            print("--- DEBUG: UFM Calculator Initial Inputs ---")
            print(f"  Beam Depth:              {self._beam_depth:.3f}")
            print(f"  Support Depth:           {self._support_depth:.3f}")
            print(f"  End Plate Thickness:     {self._end_plate_thickness:.3f}")
            print(f"  Edge Distance (vert):    {self._edge_dist:.3f}")
            print(f"  Row Spacing:             {self._row_spacing:.3f}")
            print(f"  Number of Rows:          {self._n_rows}")
            print(
                f"  Connection Angle:        {math.degrees(self._angle_rad):.2f} degrees"
            )
            self._debug_header_printed = True

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
        if debug:
            self._print_debug_inputs()
            print("\n--- Debugging get_dimensions() ---")
            print(f"  1. Calculate alpha (_alpha):")
            print(
                f"     _beta = {self._edge_dist:.2f} + (({self._n_rows}-1) * {self._row_spacing:.2f}) / 2 = {self._beta:.4f}"
            )
            print(
                f"     _alpha = ({self._beam_half_depth:.2f} + {self._beta:.2f}) * tan({math.degrees(self._angle_rad):.1f}°) - {self._support_half_depth:.2f} = {self._alpha:.4f}"
            )
            print(f"  2. Calculate Horizontal Length (lh):")
            print(
                f"     lh = 2*{self._alpha:.2f} - 2*{self._end_plate_thickness:.2f} - 0.75 = {self._horizontal_plate_length:.4f}"
            )
        unrounded_vertical = (
            self._edge_dist * 2
            + ((self._n_rows - 1) * self._row_spacing)
            + 0.5 * si.inch
        )
        vertical_dim = round_up_to_interval(
            number=unrounded_vertical, interval=0.25 * si.inch
        )
        horizontal_dim = round_up_to_interval(
            number=self._horizontal_plate_length, interval=0.25 * si.inch
        )
        if debug:
            print(f"  3. Calculate Final Dimensions:")
            print(
                f"     Vertical (unrounded) = 2*{self._edge_dist:.2f} + (({self._n_rows}-1)*{self._row_spacing:.2f}) + 0.5 = {unrounded_vertical:.4f}"
            )
            print(f'     -> Rounded to 0.25": {vertical_dim:.2f}')
            print(
                f"     Horizontal (unrounded) = {self._horizontal_plate_length:.4f}"
            )
            print(f'     -> Rounded to 0.25": {horizontal_dim:.2f}')
        return PlateDimensions(
            vertical=vertical_dim,
            horizontal=horizontal_dim,
            thickness=self._end_plate_thickness,
        )

    def get_loads_multipliers(self, debug: bool = False) -> LoadMultipliers:
        """Calculates and returns the load multipliers for the UFM interfaces."""
        if debug:
            self._print_debug_inputs()
            print("\n--- Debugging get_loads_multipliers() ---")
            print(f"  1. Calculate geometric properties (_alpha, _beta, _r):")
            print(
                f"     _beta = {self._edge_dist:.2f} + (({self._n_rows}-1) * {self._row_spacing:.2f}) / 2 = {self._beta:.4f}"
            )
            print(
                f"     _alpha = ({self._beam_half_depth:.2f} + {self._beta:.2f}) * tan({math.degrees(self._angle_rad):.1f}°) - {self._support_half_depth:.2f} = {self._alpha:.4f}"
            )
            print(
                f"     _r = sqrt(({self._alpha:.2f} + {self._support_half_depth:.2f})² + ({self._beam_half_depth:.2f} + {self._beta:.2f})²) = {self._r:.4f}"
            )
            print(f"  2. Calculate Final Multipliers:")
        multipliers = LoadMultipliers(
            shear_force_column_interface=self._beta / self._r,
            shear_force_beam_interface=self._beam_half_depth / self._r,
            normal_force_column=self._support_half_depth / self._r,
            normal_force_beam=self._alpha / self._r,
        )
        if debug:
            print(
                f"     Shear (Column) = _beta / _r = {multipliers.shear_force_column_interface:.4f}"
            )
            print(
                f"     Shear (Beam)   = beam_half_depth / _r = {multipliers.shear_force_beam_interface:.4f}"
            )
            print(
                f"     Normal (Column)= support_half_depth / _r = {multipliers.normal_force_column:.4f}"
            )
            print(
                f"     Normal (Beam)  = _alpha / _r = {multipliers.normal_force_beam:.4f}"
            )
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
        if debug:
            print(f"\n--- DEBUG: Tensile Yielding ({interface_name}) ---")
            print(f"  Inputs:")
            print(f"    Yield Strength (Fy):     {self.Fy}")
            print(f"    Gross Length:            {gross_length:.2f}")
            print(f"    Thickness:               {self._thickness:.3f}")
            print(f"  Calculation:")
            print(
                f'    Effective Length:        {effective_length:.2f} (Gross Length - 0.75")'
            )
            print(f"    Gross Area (Ag):         {gross_area:.4f}")
            print(f"    Nominal Capacity (Pn):   {nominal_capacity:.2f}")
            print(f"    Resistance Factor (φ):   {resistance_factor}")
            print(f"    Loading Condition:       {self.loading_condition}")
            print(f"  -------------------------------------------")
            print(f"  Final Design Capacity (φPn): {design_capacity:.2f}")
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

    def _print_debug_inputs(self, thickness_pl: float):
        """A private helper to print a clean block of all initial input values."""
        print("--- DEBUG: Web Local Yielding Inputs ---")
        print(f"  Yield Strength (Fy):        {self._Fy}")
        print(f"  Web Thickness (tw):         {self._tw:.3f}")
        print(f"  Detailing Distance (k):     {self._k:.3f}")
        print(f"  Member Depth (d):           {self._d:.2f}")
        print(f"  Connection Length (lb):     {self._connection_length:.2f}")
        print(f"  End Plate Thickness (tpl):  {thickness_pl:.3f}")

    def _print_debug_calculation(
        self, centroid, multiplier, bearing_len, Pn, phiRn, phi
    ):
        """A private helper to print the detailed step-by-step calculation."""
        print("\n--- DEBUG: Calculation Steps ---")
        print(f"  1. Calculate Connection Load Centroid:")
        print(
            f'     Centroid = lb/2 + clip + tpl = {self._connection_length/2:.2f} + 0.75" + {centroid - self._connection_length/2 - 0.75*si.inch:.2f} = {centroid:.2f}'
        )
        print(f"  2. Determine Multiplier:")
        print(
            f"     Condition: Is load centroid ({centroid:.2f}) <= member depth ({self._d:.2f})?"
        )
        print(f"     Result: {centroid <= self._d}, therefore multiplier = {multiplier}")
        print(f"  3. Calculate Bearing Length:")
        print(
            f"     Bearing Length = {multiplier}*k + lb = ({multiplier}*{self._k:.2f}) + {self._connection_length:.2f} = {bearing_len:.2f}"
        )
        print(f"  4. Calculate Nominal Capacity (Pn):")
        print(
            f"     Pn = Fy * tw * Bearing Length = {self._Fy} * {self._tw:.3f} * {bearing_len:.2f} = {Pn:.2f}"
        )
        print(f"  5. Calculate Design Capacity (φRn):")
        print(
            f"     φRn = Pn * φ * loading_condition = {Pn:.2f} * {phi} * {self._loading_condition} = {phiRn:.2f}"
        )

    def calculate_capacity(
        self, thickness_pl: float, resistance_factor: float = 1.0, debug: bool = False
    ) -> float:
        """
        Calculates the design web local yielding strength (φRn).
        """
        if debug:
            self._print_debug_inputs(thickness_pl)

        clip_dist = 3 / 4 * si.inch
        connection_load_centroid = (
            self._connection_length / 2 + clip_dist + thickness_pl
        )

        if connection_load_centroid <= self._d:
            multiplier_k = 2.5
        else:
            multiplier_k = 5.0

        bearing_length = (multiplier_k * self._k) + self._connection_length
        nominal_capacity = self._Fy * self._tw * bearing_length
        design_capacity = (
            nominal_capacity * resistance_factor * self._loading_condition
        )

        if debug:
            self._print_debug_calculation(
                connection_load_centroid,
                multiplier_k,
                bearing_length,
                nominal_capacity,
                design_capacity,
                resistance_factor,
            )

        return design_capacity