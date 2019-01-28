# -*- coding: utf-8 -*-
""" This is the first line of the 'classes' module.
"""


class MyClass():
    """ This is the first line of the 'MyClass' docstring.

    This is the second line of the 'MyClass' docstring where longer and more
    detailed explanations go.

    Attributes
    ----------
    mystr : str
            Yes, I just store a useless string
    """

    def __init__(self, mystr):
        """ This is the fist line of the __init__ function of 'MyClass'

        Parameters
        ----------
        mystr : str
            Yes, I just store a useless string
        """
        self.mystr = mystr

    def print_and_return_useless_string(self):
        """ This is the first line of the class method.

        This is the second line of the class method and contains more precise
        information about the method and its implementation.

        Returns
        -------
        str
            The same string as we just printed
        """
        print('MyClass says:', self.mystr)
        return self.mystr

    def reverse_and_return_string(self):
        """ This is the first line of the class method.

        This is the second line of the class method and contains more precise
        information about the method and its implementation.

        Returns
        -------
        str
            The reversed string
        """
        self.mystr = self.mystr[::-1]
        print('MyClass says:', self.mystr)
        return self.mystr
