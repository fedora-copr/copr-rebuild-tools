import os
import ConfigParser


def read(path, backend):
    conf = ConfigParser.ConfigParser()
    conf.read(path)

    confd = to_dict(conf, ["general", backend])
    confd["sleep"] = int(confd["sleep"])
    confd["copr-config"] = os.path.expanduser(confd["copr-config"]) if "copr-config" in confd else \
        os.path.join(os.path.expanduser("~"), ".config", "copr")
    return confd


def to_dict(conf, sections):
    return dict(sum([conf.items(s) for s in sections], []))
