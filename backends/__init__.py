from dummy import Dummy, CoprDummy
from pypi import Pypi, CoprPypi
from rubygems import Rubygems, CoprRubygems
from tito import Tito, CoprTito


backends = {
    "dummy": (Dummy, CoprDummy),
    "pypi": (Pypi, CoprPypi),
    "rubygems": (Rubygems, CoprRubygems),
    "tito": (Tito, CoprTito),
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
