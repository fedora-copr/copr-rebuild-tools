import os
import ConfigParser


def read(path, backend):
    conf = ConfigParser.ConfigParser()
    conf.read(path)
    conf.set("general", "copr-config", os.path.expanduser(conf.get("general", "copr-config")))
    return to_dict(conf, ["general", backend])


def to_dict(conf, sections):
    return dict([(s, dict(conf.items(s))) for s in sections])
