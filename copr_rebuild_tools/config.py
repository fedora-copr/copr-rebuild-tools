import ConfigParser


def read(path):
    conf = ConfigParser.ConfigParser()
    conf.read(path)
    return conf
