import math
import traceback
from steel_lib.si_units import si
from steelpy import aisc

from steel_lib.data_models import (
    Plate,
    ConnectionFactory,
    ConnectionComponent,
)
from steel_lib.materials import MATERIALS, BOLT_GRADES, WELD_ELECTRODES
from steel_lib.member_factory import MemberFactory
from steel_lib.calculations import (
    BoltShearCalculator,
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
    ShearYieldingCalculator,
)

# --- 1. Define Members and Connections ---

try:
    # Create and enrich steelpy members using the consolidated factory
    beam = MemberFactory.create_steelpy_member(
        section_class=aisc.W_shapes,
        section_name="W21X83",
        material=MATERIALS["a992"],
        shape_type="W"
    )

    support = MemberFactory.create_steelpy_member(
        section_class=aisc.W_shapes,
        section_name="W14X90",
        material=MATERIALS["a992"],
        shape_type="W"
    )

    # End Plate for Column Connection (Geometry is calculated on creation)
    end_plate_column = Plate(
        t=1 * si.inch,
        material=MATERIALS["a572_gr50"]
    )

    # Gusset Plate for Bracing Connection (Geometry is calculated on creation)
    gusset_plate_bracing = Plate(
        t=1 * si.inch,
        material=MATERIALS["a572_gr50"],
        clipping=3/4 * si.inch,
    )

    # --- Define Connection Configurations ---

    bracing_connection = ConnectionFactory.create_bolted_connection(
        component=ConnectionComponent.TOTAL,
        row_spacing=3.0 * si.inch,
        column_spacing=3.0 * si.inch,
        n_rows=2,
        n_columns=7,
        edge_distance_vertical=2 * si.inch,
        edge_distance_horizontal=1.5 * si.inch,
        bolt_diameter=7/8 * si.inch,
        bolt_grade=BOLT_GRADES["a325_x"],
        material=MATERIALS["a572_gr50"],
        angle=47.2 * math.pi / 180
    )

    column_endplate_connection = ConnectionFactory.create_bolted_connection(
        component=ConnectionComponent.FLANGE,
        row_spacing=3.0 * si.inch,
        column_spacing=3.0 * si.inch,
        n_rows=7,
        n_columns=2,
        edge_distance_vertical=3 * si.inch,
        edge_distance_horizontal=1.5 * si.inch,
        bolt_diameter=7/8 * si.inch,
        bolt_grade=BOLT_GRADES["a490_x"],
        material=MATERIALS["a572_gr50"],
        angle=47.2 * math.pi / 180
    )

    column_gusset_connection = ConnectionFactory.create_bolted_connection(
        component=ConnectionComponent.WEB,
        row_spacing=3.0 * si.inch,
        column_spacing=3.0 * si.inch,
        n_rows=2,
        n_columns=7,
        edge_distance_vertical=2 * si.inch,
        edge_distance_horizontal=1.5 * si.inch,
        bolt_diameter=7/8 * si.inch,
        bolt_grade=BOLT_GRADES["a325_x"],
        material=MATERIALS["a572_gr50"],
    )


    # gusset_weld = ConnectionFactory.create_welded_connection(
    #     component=ConnectionComponent.TOTAL,
    #     weld_size=0.3125 * si.inch,
    #     length=31.50 * si.inch,
    #     electrode=WELD_ELECTRODES["e70xx"]
    # )


    # --- 2. Perform Calculations ---

    print("--- Starting Steel Connection Calculations ---")

    # a) UFM Plate Dimension and Load Multiplier Calculation
    print("\n1. UFM Calculator...")
    ufm_checker = UFMCalculator(
        beam=beam,
        support=support,
        endplate=end_plate_column,
        connection=column_endplate_connection # UFM needs the bolt config
    )
    final_dimensions = ufm_checker.get_dimensions(debug=True)
    final_multipliers = ufm_checker.get_loads_multipliers(debug=True)

    # Assign calculated dimensions to the plate object for subsequent checks
    gusset_plate_bracing.set_dimensions(final_dimensions)
    print(f"\n   Calculated Plate Dimensions: {final_dimensions}")
    print(f"   Calculated Load Multipliers: {final_multipliers}")

    beam_gusset_connection = ConnectionFactory.create_welded_connection(
        component=ConnectionComponent.LENGTH,
        weld_size=0.3125 * si.inch,
        length = gusset_plate_bracing.length,
        electrode=WELD_ELECTRODES["e70xx"]
    )
    endpl_gusset_connection = ConnectionFactory.create_welded_connection(
        component=ConnectionComponent.WIDTH,
        weld_size=0.3125 * si.inch,
        length = gusset_plate_bracing.width,
        electrode=WELD_ELECTRODES["e70xx"]
    )
    

    # b) Plate Tensile Yielding Calculation (based on UFM dimensions)
    print("\n2. Plate Tensile Yielding Calculator...")
    plate_yielding_checker = PlateTensileYieldingCalculator(gusset_plate_bracing)
    horiz_yield = plate_yielding_checker.calculate_capacity_horizontal(debug=True)
    vert_yield = plate_yielding_checker.calculate_capacity_vertical(debug=True)
    print(f"\n   Horizontal Yielding Capacity: {horiz_yield:.2f}")
    print(f"   Vertical Yielding Capacity:   {vert_yield:.2f}")


    # c) Whitmore Section Tensile Yielding
    print("\n3. Whitmore Section Tensile Yielding Calculator...")
    # Whitmore needs the full connection object for context
    whitmore_checker = TensileYieldWhitmore(gusset_plate_bracing, bracing_connection)
    whitmore_capacity = whitmore_checker.calculate_capacity(debug=True)
    print(f"\n   Whitmore Section Capacity: {whitmore_capacity:.2f}")


    # d) Compression Buckling
    print("\n4. Compression Buckling Calculator...")
    # Comp Buckling needs the bolt configuration
    comp_buckling_checker = CompressionBucklingCalculator(gusset_plate_bracing, bracing_connection)
    try:
        comp_capacity = comp_buckling_checker.calculate_capacity(debug=True)
        print(f"\n   Compression Buckling Capacity: {comp_capacity:.2f}")
    except ValueError as e:
        print(f"\n   Compression Buckling Check Failed: {e}")


    # e) Web Local Yielding (SIMPLIFIED API)
    print("\n5. Web Local Yielding Calculator...")
    web_yield_checker = WebLocalYieldingCalculator(
        member=beam,
        connection=beam_gusset_connection, # Pass the WeldConfiguration directly
        end_plate=end_plate_column           # Pass the end plate object
    )
    web_yield_capacity = web_yield_checker.calculate_capacity(debug=True)
    print(f"\n   Web Local Yielding Capacity: {web_yield_capacity.to('kip'):.2f}")


    # f) Web Local Crippling (SIMPLIFIED API)
    print("\n6. Web Local Crippling Calculator...")
    web_local_crippling_checker = WebLocalCrippingCalculator(
        member=beam,
        connection=beam_gusset_connection, # Pass the WeldConfiguration directly
        end_plate=end_plate_column           # Pass the end plate object
    )
    web_crippling_capacity = web_local_crippling_checker.calculate_capacity(debug=True)
    print(f"\n   Web Local Crippling Capacity: {web_crippling_capacity.to('kip'):.2f}")

    # g) Bolt Shear (SIMPLIFIED API)
    print("\n7. Bolt Shear Calculator...")
    # Pass the BoltConfiguration directly
    bolt_shear_checker = BoltShearCalculator(column_gusset_connection)
    bolt_shear_capacity_fnv = bolt_shear_checker.calculate_capacity_fnv(debug=True, number_of_shear_planes=1)
    bolt_shear_capacity_fnt = bolt_shear_checker.calculate_capacity_fnt(debug=True, number_of_shear_planes=1)
    print(f"\n   Bolt Shear Fnv Capacity: {bolt_shear_capacity_fnv.to('kip'):.2f}")
    print(f"   Bolt Shear Fnt Capacity: {bolt_shear_capacity_fnt.to('kip'):.2f}")


    # h) Shear Yielding
    print("\n8. Shear Yielding Calculator...")
    shear_yielding_checker = ShearYieldingCalculator(
        member=gusset_plate_bracing,
        connection=beam_gusset_connection, # This calculator needs the full connection context
    )
    shear_yielding_capacity = shear_yielding_checker.calculate_capacity(debug=True)
    print(f"\n   Shear Yielding Capacity: {shear_yielding_capacity:.2f}")


    print("\n9. Shear Yielding Calculator...")
    shear_yielding_checker = ShearYieldingCalculator(
        member=gusset_plate_bracing,
        connection=endpl_gusset_connection, # This calculator needs the full connection context
    )
    shear_yielding_capacity = shear_yielding_checker.calculate_capacity(debug=True)
    print(f"\n   Shear Yielding Capacity: {shear_yielding_capacity:.2f}")


    print("\nScript finished successfully.")
 
except Exception as e:
    print("\n--- SCRIPT FAILED WITH AN ERROR ---")
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Message: {e}")
    print("Traceback:")
    traceback.print_exc()
