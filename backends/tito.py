import os
import subprocess
from copr_rebuild_tools import Backend, CoprBackend, Entity


class Package(Entity):
    path = None


class Tito(Backend):

    def __init__(self, *args, **kwargs):
        super(Tito, self).__init__(*args, **kwargs)
        self.conf["path"] = os.path.expanduser(self.conf["path"])
        self.path = self.find_tito_dir()

    def get_all(self):
        return [self.parse(p) for p in self.packages()]

    def packages(self):
        return [p for p in os.listdir(self.path) if not p.startswith(".")]

    def parse(self, package):
        with open(os.path.join(self.path, package), "r") as f:
            version, subdir = f.read().strip().strip("/").split()
        return Package(name=package, version=version,
                       path=os.path.join(self.conf["path"], subdir))

    def find_tito_dir(self):
        for d in [".tito", "rel-eng"]:
            path = os.path.join(self.conf["path"], d, "packages")
            if os.path.exists(path):
                return path
        raise ValueError("No tito directory in {}".format(self.conf["path"]))


class CoprTito(CoprBackend):
    def submit(self, package):
        try:
            cmd = ["tito", "release", self.conf["releaser"]]
            subprocess.call(cmd, cwd=package.path)
        except OSError as e:
            print("ERROR")
            print("Package: {}".format(package.name))
            print("Path: {}".format(package.path))
            print(e)
