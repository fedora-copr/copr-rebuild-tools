import subprocess
import xmlrpclib
from copr_rebuild_tools import Backend, CoprBackend


class Pypi(Backend):
    def get_all(self):
        client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
        modules = client.list_packages()
        return modules


class CoprPypi(CoprBackend):
    def submit(self, package):
        command = ["/usr/bin/copr-cli", "--config", self.conf["copr-config"],
                   "buildpypi", self.copr_full_name, "--packagename", package,
                   "--nowait",
                   "--pythonversions"] + self.conf["python-version"].split(" ")
        subprocess.call(command)
