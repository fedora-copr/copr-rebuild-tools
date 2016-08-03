import time
from copr import CoprClient


class CoprBackend(object):

    def __init__(self, conf):
        self.conf = conf
        self.project = conf["project"]
        self.owner = conf.get("owner", None)
        self.copr_config = conf.get("copr-config", None)

    @property
    def client(self):
        return CoprClient.create_from_file_config(self.copr_config)

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
        result = self.client.get_packages_list(projectname=self.project, ownername=self.owner,
                                               with_latest_succeeded_build=True)
        return result.packages_list


class CoprQuery(object):
    def __init__(self, objects):
        self.objects = objects

    def get(self):
        return self.objects

    def successful(self):
        return CoprQuery(filter(lambda x: x.latest_succeeded_build, self.objects))


def package_version(package):
    return package.data["latest_succeeded_build"]["pkg_version"].split("-")[0]
