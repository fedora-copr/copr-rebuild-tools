def require_attribute(query, attr):
    if len(query.get()) != 0 and getattr(query.get()[0], attr) == NotImplemented:
        clazz = query.get()[0].__class__.__name__
        raise NotImplementedError("Attribute `{}` of `{}` entity must be set or implemented".format(attr, clazz))


def require_pkgname(func):
    def wrapper(*args):
        require_attribute(args[0], "pkgname")
        return func(*args)
    return wrapper


def require_version(func):
    def wrapper(*args):
        require_attribute(args[0], "version")
        return func(*args)
    return wrapper
