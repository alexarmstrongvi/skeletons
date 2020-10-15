""" Test subpackage functions together """

from skeletons import add, subtract
from skeletons.subpackage2.helpers import divide
from skeletons.subpackage1.helpers import multiply

def test_math():
    """ Test combining math functions """
    assert add(subtract(multiply(divide(4,2),2),2),2) == 4
