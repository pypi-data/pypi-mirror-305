"""
This module provides examples of using the logging framework in Python.

This module provides a simple function that calculates the sum of two numbers.
It also demonstrates how to log messages at different severity levels (DEBUG, INFO, WARNING, ERROR).
"""

import logging

_logger = logging.getLogger(__name__)

def demo_add(a: int = 0, b: int = 0) -> int:
    """
    Calculate and return the sum of two numbers, with logging at various levels.

    This function takes two integers, `a` and `b`, and returns their sum.
    Additionally, it logs messages at different severity levels (DEBUG, INFO, WARNING, ERROR)
    to demonstrate logging functionality.

    :param a: The first number, default is 0.
    :type a: int
    :param b: The second number, default is 0.
    :type b: int
    :return: The sum of the two numbers.
    :rtype: int

    :Example:
    
    >>> demo_add(2, 3)
    5

    """

    _logger.debug("This is a debug message")
    _logger.info("This is an info message")
    _logger.warning("This is a warning message")
    _logger.error("This is an error message")

    return a + b
