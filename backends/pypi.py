import subprocess
import xmlrpclib
from copr_rebuild_tools import Backend, CoprBackend, Entity


class Module(Entity):
    @property
    def version(self):
        raise NotImplementedError


class Pypi(Backend):
    def get_all(self):
        client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
        modules = client.list_packages()
        return [Module(name=m) for m in modules]


class CoprPypi(CoprBackend):
    name_attr = "pypi_package_name"

    def submit(self, package):
        command = ["/usr/bin/copr-cli", "--config", self.conf["copr-config"],
                   "buildpypi", self.copr_full_name, "--packagename", package.name,
                   "--nowait",
                   "--pythonversions"] + self.conf["python-version"].split(" ")
        subprocess.call(command)
