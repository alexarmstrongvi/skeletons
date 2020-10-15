"""
TODO: Brief synopsis
"""

from skeletons.subpackage1.helpers import multiply

def add(var1 : int, var2 : int) -> int:
    """ Add two numbers

    Args:
        var1 : first number
        var2 : second number

    Returns:
        Sum of two numbers

    Examples:
        >>> add(2,4)
        6
    """
    var1 = multiply(1, var1)
    var2 = multiply(1, var2)
    return int(var1 + var2)
