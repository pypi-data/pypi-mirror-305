"""
This module provides functionality to read and process PDF files to extract
Electronic Control Units (ECUs) using the pymupdf library.
"""

from collections.abc import Generator

import pymupdf
from shapely import Polygon

from .models import ElectronicControlUnit


class PDFReader:
    """
    A class to read and process PDF files to extract Electronic Control Units (ECUs).
    This class provides methods to open a PDF file, extract drawings from a specified page,
    and identify rectangular shapes that represent ECUs based on their height.
    """

    def __init__(self, pdfpath: str, pagenumber: int = 0) -> None:
        self.path = pdfpath
        doc = pymupdf.open(pdfpath)
        assert pagenumber <= doc.page_count
        self.page = doc.load_page(pagenumber)

    def __color2str(self, color: tuple[float, float, float]) -> str:
        assert color is not None
        return "#" + "".join([f"{int(x * 255):02x}" for x in color])

    def __remove_nested_ecus(
        self, ecus: list[ElectronicControlUnit]
    ) -> Generator[ElectronicControlUnit]:
        for ecu in ecus:
            for other_ecu in ecus:
                if ecu == other_ecu:
                    continue
                if other_ecu.polygon().contains(ecu.polygon()):
                    break
            else:
                yield ecu

    def get_ecus(
        self, min_height: int = 15, max_height: int = 21
    ) -> Generator[ElectronicControlUnit]:
        """
        Extracts Electronic Control Units (ECUs) from the page drawings based on their height.

        This method iterates through the drawings on the page, identifies rectangular shapes,
        and filters them based on the specified height range. It then creates
        `ElectronicControlUnit` instances for the filtered rectangles and returns a generator
        of unique ECUs.

        :param min_height: Minimum height of the rectangle to be considered as an ECU. Default: 15
        :type min_height: int
        :param max_height: Maximum height of the rectangle to be considered as an ECU. Default: 21
        :type max_height: int
        :return: A generator of unique ECUs.
        :rtype: Generator[ElectronicControlUnit]
        """

        ecus: dict[Polygon, ElectronicControlUnit] = dict()
        for path in self.page.get_drawings(extended=False):
            if not "items" in path:
                continue

            for item in path["items"]:
                if item[0] == "re":
                    rect = item[1]

                    if rect.height > min_height and rect.height < max_height:
                        ecu = ElectronicControlUnit(
                            x0=rect.x0,
                            y0=rect.y0,
                            y1=rect.y1,
                            x1=rect.x1,
                            color=self.__color2str(path.get("fill")),
                            seqno=path.get("seqno"),
                        )

                        polygon = ecu.polygon()
                        if not polygon in ecus:
                            ecus[polygon] = ecu
                        else:
                            ecus[polygon] = max(
                                ecus[polygon], ecu, key=lambda e: e.seqno
                            )

        return self.__remove_nested_ecus(list(ecus.values()))
