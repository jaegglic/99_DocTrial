# -*- coding: utf-8 -*-
""" This is the first line of the `classes.py` module.
"""


class MyClass:
    """ This is the first line of the 'MyClass' docstring.

    This is the second line of the 'MyClass' docstring where longer and more
    detailed explanations go.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (in a ``Parameters`` section
    within __init__ ). In the first case, we don't need to add the
    special members to the class documentation (i.e. ``:special-members:``).

    Attributes
    ----------
    mystr : str
            Yes, I just store a useless string
    """

    def __init__(self, mystr):
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
