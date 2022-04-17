import time
from munch import Munch
from copr.v3 import Client
from copr.v3.pagination import next_page
from .helpers import to_version


class CoprBackend(object):

    def __init__(self, conf):
        self.conf = conf
        self.project = conf["project"]
        self.owner = conf.get("owner", None)
        self.copr_config = conf.get("copr-config", None)
        self.chroots = conf.get("chroots", "").split()

    @property
    def client(self):
        return Client.create_from_config_file(self.copr_config)

    @property
    def copr_full_name(self):
        return "/".join(filter(None,[self.conf.get("owner", None), self.conf["project"]]))

    @property
    def enabled_chroots(self):
        project = self.client.project_proxy.get(self.owner, self.project)
        return list(project.chroot_repos.keys())

    def submit_all(self, packages, sleep=0, batch=None, batch_sleep=0,
                   callback=None):
        for i, package in enumerate(packages):
            if callback:
                callback(package)

            self.submit(package)
            time.sleep(sleep)

            if batch and (i+1) % batch == 0:
                time.sleep(batch_sleep)

    def submit(self, package):
        """
        Implemented in particular backends
        """
        raise NotImplementedError

    def get_all(self):
        monitor = self.client.monitor_proxy.monitor(
            self.owner, self.project)

        packages = [Munch(package) for package in monitor.packages]
        return self._modified_packages(packages)

    def _modified_packages(self, packages):
        scl = self.conf["scl"]
        for package in packages:
            if scl:
                prefix = "{}-".format(scl)
                if package.name.startswith(prefix):
                    package.name = package.name.replace(prefix, "", 1)
        return packages


class CoprQuery(object):
    def __init__(self, objects):
        self.objects = objects

    def get(self):
        return list(self.objects)

    def successful(self, chroots):
        result = []
        for package in self.objects:
            ok = True
            for chrootname in chroots:
                chroot = package["chroots"].get(chrootname)
                state = chroot["state"] if chroot else None
                if state not in ["succeeded", "forked"]:
                    ok = False
            if ok:
                result.append(package)

        return CoprQuery(result)


def package_version(package, chroots):
    versions = []
    for chrootname, chroot in package.chroots.items():
        if chroots and chrootname not in chroots:
            continue
        version = chroot["pkg_version"].split("-")[0]
        versions.append(version)
    return min(versions, key=lambda x: to_version(x))
