class Backend(object):
    def get_all(self):
        """
        Implemented in particular backends
        """
        raise NotImplementedError


class Query(object):
    def __init__(self, objects):
        self.objects = objects

    def limit(self, n):
        return Query(self.objects[:n])

    def offset(self, obj):
        i = self.objects.index(obj) + 1
        return Query(self.objects[i:])

    def get(self):
        return self.objects
