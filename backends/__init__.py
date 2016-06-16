from pypi import Pypi, CoprPypi
from rubygems import Rubygems, CoprRubygems


backends = {
    "pypi": (Pypi, CoprPypi),
    "rubygems": (Rubygems, CoprRubygems),
}


def name(args, conf):
    return conf.get("backend", args.backend)


def get(name):
    try:
        return backends[name]
    except KeyError:
        raise NoSuchBackend


class NoSuchBackend(Exception):
    pass
