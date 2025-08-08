import math
from steel_lib.si_units import si
from steelpy import aisc

from steel_lib.data_models import (
    Plate,
    BoltConfiguration,
    SteelpyMemberFactory,
    WeldConfiguration,
    PlateDimensions,
)
from steel_lib.materials import MATERIALS, BOLT_GRADES, WELD_ELECTRODES
from steel_lib.calculations import (
    BoltShearCalculator,
    check_dcr,
    BlockShearCalculator,
    ConnectionCapacityCalculator,
    TensileYieldingCalculator,
    TensileRuptureCalculator,
    TensileYieldWhitmore,
    CompressionBucklingCalculator,
    UFMCalculator,
    PlateTensileYieldingCalculator,
    WebLocalYieldingCalculator,
    WebLocalCrippingCalculator,
)

# Set up the unit system

# --- 1. Define Members and Connections ---

# Gusset Plate for Bracing Connection
gusset_plate_bracing = Plate.create_plate_member(
    t=1 * si.inch,
    material=MATERIALS["a572_gr50"]
)

# Bracing Connection Bolt Configuration
bracing_connection = BoltConfiguration(
    row_spacing=3.0 * si.inch,
    column_spacing=3.0 * si.inch,
    n_rows=2,
    n_columns=7,
    edge_distance_vertical=2 * si.inch,
    edge_distance_horizontal=1.5 * si.inch,
    bolt_diameter=7/8 * si.inch,
    bolt_grade=BOLT_GRADES["a325_x"],
    material=MATERIALS["a572_gr50"],
    connection_type="bracing",
    angle=47.2 * math.pi / 180
)

# End Plate for Column Connection
end_plate_column = Plate.create_plate_member(
    t=1 * si.inch,
    material=MATERIALS["a572_gr50"]
)

# Column to End Plate Connection
column_endplate_connection = BoltConfiguration(
    row_spacing=3.0 * si.inch,
    column_spacing=3.0 * si.inch,
    n_rows=7,
    n_columns=2,
    edge_distance_vertical=3 * si.inch,
    edge_distance_horizontal=1.5 * si.inch,
    bolt_diameter=7/8 * si.inch,
    bolt_grade=BOLT_GRADES["a325_x"],
    material=MATERIALS["a572_gr50"],
    connection_type="bracing",
    angle=47.2 * math.pi / 180
)

# Steel Members (Beam and Support)
beam = SteelpyMemberFactory.create_steelpy_member(
    section_class=aisc.W_shapes,
    section_name="W21X83",
    material=MATERIALS["a992"],
    shape_type="W"
)

support = SteelpyMemberFactory.create_steelpy_member(
    section_class=aisc.W_shapes,
    section_name="W14X90",
    material=MATERIALS["a992"],
    shape_type="W"
)

# Weld Configuration
gusset_weld = WeldConfiguration(
    weld_size=0.3125 * si.inch,  # 5/16"
    length=31.50 * si.inch,
    electrode=WELD_ELECTRODES["e70xx"]
)


# --- 2. Perform Calculations ---

print("--- Starting Steel Connection Calculations ---")

# a) UFM Plate Dimension and Load Multiplier Calculation
print("\n1. UFM Calculator...")
ufm_checker = UFMCalculator(
    beam=beam,
    support=support,
    endplate=end_plate_column,
    connection=column_endplate_connection
)
final_dimensions = ufm_checker.get_dimensions(debug=True)
final_multipliers = ufm_checker.get_loads_multipliers(debug=True)

# Assign calculated dimensions to the plate object for subsequent checks
gusset_plate_bracing.dimensions = final_dimensions
print(f"\n   Calculated Plate Dimensions: {final_dimensions}")
print(f"   Calculated Load Multipliers: {final_multipliers}")


# b) Plate Tensile Yielding Calculation (based on UFM dimensions)
print("\n2. Plate Tensile Yielding Calculator...")
plate_yielding_checker = PlateTensileYieldingCalculator(gusset_plate_bracing)
horiz_yield = plate_yielding_checker.calculate_capacity_horizontal(debug=True)
vert_yield = plate_yielding_checker.calculate_capacity_vertical(debug=True)
print(f"\n   Horizontal Yielding Capacity: {horiz_yield:.2f}")
print(f"   Vertical Yielding Capacity:   {vert_yield:.2f}")


# c) Whitmore Section Tensile Yielding
print("\n3. Whitmore Section Tensile Yielding Calculator...")
whitmore_checker = TensileYieldWhitmore(gusset_plate_bracing, bracing_connection)
whitmore_capacity = whitmore_checker.calculate_capacity(debug=True)
print(f"\n   Whitmore Section Capacity: {whitmore_capacity:.2f}")


# d) Compression Buckling
print("\n4. Compression Buckling Calculator...")
comp_buckling_checker = CompressionBucklingCalculator(gusset_plate_bracing, bracing_connection)
try:
    comp_capacity = comp_buckling_checker.calculate_capacity(debug=True)
    print(f"\n   Compression Buckling Capacity: {comp_capacity:.2f}")
except ValueError as e:
    print(f"\n   Compression Buckling Check Failed: {e}")


# e) Web Local Yielding
print("\n5. Web Local Yielding Calculator...")
web_yield_checker = WebLocalYieldingCalculator(beam, gusset_weld)
web_yield_capacity = web_yield_checker.calculate_capacity(
    thickness_pl=end_plate_column.t,
    debug=True
)
print(f"\n   Web Local Yielding Capacity: {web_yield_capacity.to('kip'):.2f}")

print("\n--- All Calculations Complete ---")
web_local_crippling_checker = WebLocalCrippingCalculator(beam, gusset_weld)
web_crippling_capacity = web_local_crippling_checker.calculate_capacity(
    thickness_pl=end_plate_column.t,
    debug=True
)
print(f"\n   Web Local Crippling Capacity: {web_crippling_capacity.to('kip'):.2f}")