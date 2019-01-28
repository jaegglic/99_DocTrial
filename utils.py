# -*- coding: utf-8 -*-
""" This is the first line of the 'utils' module.

Notes
-----
    This is an example of an indented section. It's like any other section,
    but the body is indented to help it stand out from surrounding text.

If a section is indented, then a section break is created by
resuming unindented text.

Attributes
----------
my_pack_attr : str
    Yes, I have a useless module attribute
"""

# import numpy as np


my_pack_attr = 'A very fancy package attribute'


def my_fun(foo):
    """ This is the first line of the 'my_fun' docstring.

    This is the second line, that is a bit longer and contains more detailed
    information about the function and its implementation.

    Parameters
    ----------
    foo : str
        My fancy function just prints a string and returns it

    Returns
    -------
    str
        Yes, it returns the same string
    """
    print('my_fun says:', foo)
    return foo


# def my_fancy_fun(bar):
#     """ This is the first line of the 'my_fancy_fun' docstring.
#
#     Parameters
#     ----------
#     bar : str
#         My fancy function just prints a string and returns it
#
#     Returns
#     -------
#     numpy.ndarray
#         Yes, it returns a useless ndarray
#     """
#     print(bar)
#     return np.random.randn((5,))
