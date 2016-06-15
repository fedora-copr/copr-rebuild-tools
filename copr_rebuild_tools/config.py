import os
import ConfigParser


def read(path, backend):
    conf = ConfigParser.ConfigParser()
    conf.read(path)

    confd = to_dict(conf, ["general", backend])
    confd["copr-config"] = os.path.expanduser(confd["copr-config"])
    confd["sleep"] = int(confd["sleep"])
    return confd


def to_dict(conf, sections):
    return dict(sum([conf.items(s) for s in sections], []))
