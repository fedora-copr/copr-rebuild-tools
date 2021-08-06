import json
import requests
import subprocess
from xmlrpc.client import ServerProxy
from pip._vendor.packaging.version import parse
from copr_rebuild_tools import Backend, CoprBackend, Entity


class Module(Entity):
    @property
    def version(self):
        """Return version of package on pypi.python.org using json."""
        URL_PATTERN = 'https://pypi.python.org/pypi/{package}/json'
        req = requests.get(URL_PATTERN.format(package=self.name))
        version = parse('0')
        if req.status_code == requests.codes.ok:
            j = json.loads(req.text.encode(req.encoding))
            if 'releases' in j:
                releases = j['releases']
                for release in releases:
                    ver = parse(release)
                    if not ver.is_prerelease:
                        version = max(version, ver)
        return str(version)

    @property
    def pkgname(self):
        return self.name if self.name.startswith("python-") else "python-{}".format(self.name)


class Pypi(Backend):
    def get_all(self):
        client = ServerProxy('https://pypi.python.org/pypi')
        modules = client.list_packages()
        return [Module(name=m) for m in modules]


class CoprPypi(CoprBackend):
    def submit(self, package):
        command = ["/usr/bin/copr-cli", "--config", self.conf["copr-config"],
                   "buildpypi", self.copr_full_name, "--packagename", package.name,
                   "--nowait",
                   "--pythonversions"] + self.conf["python-version"].split(" ")
        subprocess.call(command)
