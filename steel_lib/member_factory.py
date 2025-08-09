from typing import Any, Type
from .data_models import Plate, GeometricProperties, Material
from .si_units import si

class MemberFactory:
    """
    A factory class responsible for creating and enriching member objects.

    This factory ensures that any member object used in calculations has a
    standardized 'geometry' attribute, which contains all the pre-calculated
    gross areas for its various components. This centralizes the geometric
    calculations and decouples the calculators from the member's specific shape.
    """

    @staticmethod
    def create_steelpy_member(
        section_class: Type, section_name: str, material: Material, shape_type: str,
        loading_condition: int = 1,
    ) -> Any:
        """
        Creates a steelpy member, assigns material and loading properties,
        and enriches it with the GeometricProperties dataclass.
        """
        # 1. Create the basic steelpy section object
        section = getattr(section_class, section_name)

        # 2. Add the necessary material and type properties
        section.add_property("Fy", material.Fy)
        section.add_property("Fu", material.Fu)
        section.add_property("E", material.E)
        section.add_property("Type", shape_type)
        section.loading_condition = loading_condition

        # 3. Now that 'Type' exists, enrich it with geometric properties
        section.geometry = MemberFactory._create_geometric_properties(section)
        
        return section

    @staticmethod
    def _create_geometric_properties(member: Any) -> GeometricProperties:
        """
        Private helper to calculate and assemble the GeometricProperties for any member.
        """
        # For W-shapes and other standard sections from steelpy
        total_area = getattr(member, 'area', None)
        web_area = getattr(member, 'd', 0) * getattr(member, 'tw', 0) if hasattr(member, 'd') else None
        flange_area = getattr(member, 'bf', 0) * getattr(member, 'tf', 0) if hasattr(member, 'bf') else None

        # For Plate objects, this function is not needed as they self-populate.
        # This logic is now exclusively for external (e.g., steelpy) members.
        return GeometricProperties(
            total=total_area,
            web=web_area if web_area > 0 else None,
            flange=flange_area if flange_area > 0 else None
        )