from typing import Any
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
    def enrich_steelpy_member(steelpy_member: Any) -> Any:
        """
        Enriches a steelpy member object with the GeometricProperties dataclass.
        The enriched properties are attached to a '.geometry' attribute.
        """
        if not hasattr(steelpy_member, 'Type'):
             raise AttributeError("Provided steelpy_member must have a 'Type' attribute.")

        steelpy_member.geometry = MemberFactory._create_geometric_properties(steelpy_member)
        return steelpy_member

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