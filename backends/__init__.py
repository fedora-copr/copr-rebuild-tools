from rubygems import Rubygems, CoprRubygems


backends = {
    "rubygems": (Rubygems, CoprRubygems)
}


def get(name):
    try:
        return backends[name]
    except KeyError:
        raise NoSuchBackend


class NoSuchBackend(Exception):
    pass
