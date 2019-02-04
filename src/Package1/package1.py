"""module1

This is topmost docstring of module1
"""

class class1():
    """
    The docstring of the class.
    """

    def method11(self):
        """
        Docstring of method1
        :return: 0
        """
        print("inside method11")
        return 0

    def method12(self):
        """
        Docstring of method12
        :return: None
        """
        print("inside method12")


def main(args=None, **kwargs):
    """
    Main function of module1
    :param args:
    :param kwargs:
    :return:
    """
    return run((class1), args=args, **kwargs)

if __name__ == '__main__':
    main()
