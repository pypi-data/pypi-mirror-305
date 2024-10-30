"""
This module provides serialization functions for Electronic Control Units (ECUs).
"""

import json
from collections.abc import Generator
from dataclasses import asdict

from .models import ElectronicControlUnit


def ecus2json(
    ecus: list[ElectronicControlUnit] | Generator[ElectronicControlUnit],
) -> str:
    """
    Converts a list or generator of ECUs to a JSON string.

    :param ecus: A list or generator of ElectronicControlUnit instances.
    :type ecus: list[ElectronicControlUnit] | Generator[ElectronicControlUnit]
    :return: A JSON string representation of the ECUs.
    :rtype: str

    """
    return json.dumps([asdict(e) for e in ecus])


def ecus2jsonl(
    ecus: list[ElectronicControlUnit] | Generator[ElectronicControlUnit],
) -> str:
    """
    Converts a list or generator of ECUs to a JSON Lines string.

    :param ecus: A list or generator of ElectronicControlUnit instances.
    :type ecus: list[ElectronicControlUnit] | Generator[ElectronicControlUnit]
    :return: A JSON Lines string representation of the ECUs.
    :rtype: str
    """

    lines = []
    for e in ecus:
        lines.append(json.dumps(asdict(e)))
    return "\n".join(lines)
