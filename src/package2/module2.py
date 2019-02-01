"""module2

This is topmost docstring of module2
"""

class class2():
    """
    The docstring of the class.
    """

    def method21(self):
        """
        Docstring of method1
        :return: 0
        """
        print("inside method21")
        return 0

    def method122(self):
        """
        Docstring of method12
        :return: None
        """
        print("inside method22")


def main(args=None, **kwargs):
    """
    Main function of module2
    :param args:
    :param kwargs:
    :return:
    """
    return run((class2), args=args, **kwargs)

if __name__ == '__main__':
    main()
