#!/usr/bin/python3
""" Module lolo polo """


class MyList(list):
    """Class inh from list"""

    def print_sorted(self):
        """Prints  list,  sorted (ascending )"""

        print(sorted(list(self)))