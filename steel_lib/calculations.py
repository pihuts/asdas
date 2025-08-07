import math
from typing import Any, Literal
import forallpeople as si
from .data_models import BoltConfiguration, Plate

si.environment('structural', top_level=False)

def check_dcr(capacity,demand):
  return demand/capacity # Returns the ratio of demand to capacity

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