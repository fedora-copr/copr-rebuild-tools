from rubygems import Rubygems, CoprRubygems


backends = {
    "rubygems": (Rubygems, CoprRubygems)
}


def get(name):
    return backends[name]
