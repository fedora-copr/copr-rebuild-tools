import time
from copr.v3 import Client


class CoprBackend(object):

    def __init__(self, conf):
        self.conf = conf
        self.project = conf["project"]
        self.owner = conf.get("owner", None)
        self.copr_config = conf.get("copr-config", None)

    @property
    def client(self):
        return Client.create_from_config_file(self.copr_config)

    @property
    def copr_full_name(self):
        return "/".join(filter(None,[self.conf.get("owner", None), self.conf["project"]]))

    def submit_all(self, packages, sleep=0, callback=None):
        for package in packages:
            if callback:
                callback(package)
            self.submit(package)
            time.sleep(sleep)

    def submit(self, package):
        """
        Implemented in particular backends
        """
        raise NotImplementedError

    def get_all(self):
        result = self.client.package_proxy.get_list(
            ownername=self.owner,
            projectname=self.project,
            with_latest_succeeded_build=True)
        return self._modified_packages(result)

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
        return self.objects

    def successful(self):
        return CoprQuery(filter(lambda x: x["builds"]["latest_succeeded"], self.objects))


def package_version(package):
    version = package["builds"]["latest_succeeded"]["source_package"]["version"]
    return version.split("-")[0]
