# -*- coding: utf-8 -*-
""" This is the first line of the `trial.py` module.

Attributes
----------
test_str : str
    Just another test string
"""

# Local dependencies
from classes import MyClass
import utils as utl

test_str = 'Yuhuuuui, I can print a string'


if __name__ == '__main__':
    foo = MyClass(test_str)
    utl.my_fun(foo.print_and_return_useless_string())
    utl.my_fun(foo.reverse_and_return_string())
