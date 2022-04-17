from distutils.version import StrictVersion, LooseVersion


def is_greater(a, b):
    """
    :param a: version number
    :param b: version number
    """
    try:
        return StrictVersion(a) > StrictVersion(b)
    except ValueError:
        return LooseVersion(a) > LooseVersion(b)


def to_version(a):
    try:
        return StrictVersion(a)
    except ValueError:
        return LooseVersion(a)
