class CoprBackend(object):
    def submit_all(self, packages, limit=None, previous=None):
        if previous:
            previous = packages.index(previous)

        for package in packages[previous + 1:limit]:
            self.submit(package)

    def submit(self, package):
        """
        Implemented in particular backends
        """
        raise NotImplementedError
