"""
This module defines the `ElectronicControlUnit` dataclass, which represents an electronic control 
unit with geometric properties and additional metadata.
"""

from dataclasses import dataclass
from typing import Any

from shapely import Polygon


@dataclass
class ElectronicControlUnit:
    """
    A dataclass representing an Electronic Control Unit (ECU) with geometric properties and 
    metadata.
    """
    x0: float
    y0: float
    x1: float
    y1: float
    color: str
    seqno: int

    inner_text: str | None = None
    upper_label: str | None = None

    def id(self) -> str:
        """
        Returns a unique identifier for the ECU based on its coordinates and color.

        :return: A unique identifier for the ECU.
        :rtype: str
        """
        return f"{self.inner_text} | {self.upper_label} ({self.seqno})".replace(
            "\n", ""
        ).strip()

    def polygon(self) -> Polygon:
        """
        Returns the polygon representation of the ECU.

        :return: The polygon representation of the ECU.
        :rtype: Polygon
        """
        return Polygon(
            (
                (self.x0, self.y0),
                (self.x0, self.y1),
                (self.x1, self.y1),
                (self.x1, self.y0),
                (self.x0, self.y0),
            )
        )

    def __hash__(self) -> int:
        return hash((self.x0, self.y0, self.x1, self.y1, self.color, self.seqno))
