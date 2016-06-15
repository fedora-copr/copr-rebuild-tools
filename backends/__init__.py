from rubygems import Rubygems, CoprRubygems


backends = {
    "rubygems": (Rubygems, CoprRubygems)
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
