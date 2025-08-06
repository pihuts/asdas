from steelpy import aisc
import forallpeople as si
from typing import Any, Type

from steel_lib.data_models import Plate, BoltConfiguration, SteelpyMemberFactory
from steel_lib.materials import MATERIALS, BOLT_GRADES
from steel_lib.calculations import (
    BoltShearCalculator,
    check_dcr,
    BlockShearCalculator,
    ConnectionCapacityCalculator,
    TensileYieldingCalculator,
    TensileRuptureCalculator,
)

si.environment('structural', top_level=False)

if __name__ == "__main__":
    dbolt = 7/8 * si.inch

    # Create steelpy members using the specific factory function
    beam = SteelpyMemberFactory.create_steelpy_member(
        section_class=aisc.W_shapes,
        section_name="W21X83",
        material=MATERIALS["a992"],
        shape_type="W"
    )

    support = SteelpyMemberFactory.create_steelpy_member(
        section_class=aisc.W_shapes,
        section_name="W14X90",
        material=MATERIALS["a572_gr50"],
        shape_type="W"
    )

    bracing = SteelpyMemberFactory.create_steelpy_member(
        section_class=aisc.L_shapes,
        section_name="L8X6X1",
        material=MATERIALS["a36"],
        shape_type="L"
    )
    bracing.loading_condition = 2
    # Create a plate member using its dedicated factory
    gusset_plate = Plate.create_plate_member(
        t=1 * si.inch,
        material=MATERIALS["a572_gr50"]
    )
    selected_bolt_grade = BOLT_GRADES["a325_x"]
    gusset_connection = BoltConfiguration(
        row_spacing=3.0 * si.inch,
        column_spacing=3.0 * si.inch,
        n_rows=2,
        n_columns=7,
        edge_distance_vertical=2 * si.inch,
        edge_distance_horizontal=1.5 * si.inch,
        bolt_diameter=7/8 * si.inch,
        bolt_grade=selected_bolt_grade, # Assign the object directly
        material=MATERIALS["a572_gr50"]
    )

    loads_dict = {
        "shear": None, # Shear load in kips
        "axial": 840 * si.kip, # Axial load (set to None in this case)
        "moment": None # Moment load (set to None in this case)
    }
    shear = loads_dict["shear"]
    axial = loads_dict["axial"]
    moment = loads_dict["moment"]

    # shear_checker = BoltShearCalculator(connection=gusset_connection)
    # double_shear_capacity = shear_checker.calculate_capacity(
    #     number_of_shear_planes=2,
    #     debug=False
    # )
    # tensile_yield_checker = TensileYieldingCalculator(member=bracing)
    # brace_tensile_yield_capacity = tensile_yield_checker.calculate_capacity(debug=False)
    # brace_tensile_yield_dcr = check_dcr(capacity=brace_tensile_yield_capacity, demand=axial)
    # tensile_rupture_checker = TensileRuptureCalculator(member=bracing, connection=gusset_connection)
    # brace_tensile_rupture_capacity = tensile_rupture_checker.calculate_capacity(debug=False)
    # brace_tensile_rupture_dcr = check_dcr(capacity=brace_tensile_rupture_capacity, demand=axial)

    gusset_connection_main = BoltConfiguration(
        row_spacing=3.0 * si.inch, column_spacing=3.0 * si.inch, n_rows=2, n_columns=7,
        edge_distance_vertical=2 * si.inch, edge_distance_horizontal=1.5 * si.inch,
        bolt_diameter=7/8 * si.inch, bolt_grade=BOLT_GRADES["a325_x"],
        material=MATERIALS["a572_gr50"]
    )


    # # --- 2. Instantiate the Calculator ---
    # # Check the capacity for the bracing member in an axial loading scenario
    # connection_checker = ConnectionCapacityCalculator(
    #     member=gusset_plate,
    #     connection=gusset_connection_main,
    #     loading_orientation="Axial"
    # )

    # # --- 3. Run the Calculation ---
    # # Assume the connection is in double shear (e.g., gusset plate between two angles)
    # total_capacity = connection_checker.calculate_capacity(
    #     number_of_shear_planes=2,
    #     debug=True
    # )


    u_checker = BlockShearCalculator(member=gusset_plate, connection=gusset_connection_main, loading_orientation="Axial")
    u_capacity = u_checker.calculate_capacity(debug=True)


    # The thickness of L8X6X1 is 1.0 inch.
    # l_checker = BlockShearCalculator(
    #     member=bracing, connection=gusset_connection_main, loading_orientation="Axial", loading_condition=2
    # )
    # l_capacity = l_checker.calculate_capacity(debug=True)
