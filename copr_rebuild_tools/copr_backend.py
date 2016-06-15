class CoprBackend(object):

    def __init__(self, conf):
        self.conf = conf

    def submit_all(self, packages):
        for package in packages:
            self.submit(package)

    def submit(self, package):
        """
        Implemented in particular backends
        """
        raise NotImplementedError
