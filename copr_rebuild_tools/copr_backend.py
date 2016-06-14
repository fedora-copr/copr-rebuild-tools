class CoprBackend(object):
    def submit_all(self, packages, limit=None):
        for package in packages[:limit]:
            self.submit(package)

    def submit(self, package):
        """
        Implemented in particular backends
        """
        raise NotImplementedError
