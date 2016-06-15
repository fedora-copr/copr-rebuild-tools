import time


class CoprBackend(object):

    def __init__(self, conf):
        self.conf = conf

    @property
    def copr_full_name(self):
        return "/".join(filter(None,[self.conf.get("owner", None), self.conf["project"]]))

    def submit_all(self, packages, sleep=0):
        for package in packages:
            self.submit(package)
            time.sleep(sleep)

    def submit(self, package):
        """
        Implemented in particular backends
        """
        raise NotImplementedError
