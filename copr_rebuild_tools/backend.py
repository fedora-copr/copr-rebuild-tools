import json
from helpers import is_greater


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
        try:
            i = self.objects.index(obj) + 1
            return Query(self.objects[i:])
        except ValueError:
            return Query(self.objects)

    def get(self):
        return self.objects

    def succeeded(self, packages, name_key):
        return [json.loads(p.source_json)[name_key] for p in packages]

    def unsucessful(self, packages, name_key):
        return Query([p for p in self.get() if p not in self.succeeded(packages, name_key)])

    def newer(self, packages, name_key):
        """
        :param packages: dict {pkg_name: version, ...}
        :return:
        """
        # @TODO conversion between module name and package name
        # @TODO how to get version of module?
        rebuild = []
        for p in self.get():
            name = getattr(p, name_key)
            if name not in packages or is_greater(None, packages[name]):
                rebuild.append(p)
        return rebuild
