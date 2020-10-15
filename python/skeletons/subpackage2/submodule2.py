"""
TODO: Brief synopsis
"""

from skeletons.subpackage2.helpers import divide

def subtract(var1 : int, var2 : int) -> int:
    """ Subtract two numbers

    Args:
        var1 : first number
        var2 : second number

    Returns:
        Difference of two numbers

    Examples:
        >>> subtract(2,4)
        -2
    """
    var1 = divide(var1, 1)
    var2 = divide(var2, 1)
    return int(var1 - var2)
