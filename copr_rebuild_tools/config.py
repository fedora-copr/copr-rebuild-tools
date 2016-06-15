import ConfigParser


def read(path, backend):
    conf = ConfigParser.ConfigParser()
    conf.read(path)
    return to_dict(conf, ["general", backend])


def to_dict(conf, sections):
    return dict([(s, dict(conf.items(s))) for s in sections])
