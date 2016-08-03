from distutils.version import StrictVersion


def is_greater(a, b):
    """
    :param a: version number
    :param b: version number
    """
    return StrictVersion(a) > StrictVersion(b)
