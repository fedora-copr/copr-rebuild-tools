from copr_rebuild_tools import Backend, CoprBackend, Entity


class Dum(Entity):
    @property
    def pkgname(self):
        return "dummy-{}".format(self.name)


class Dummy(Backend):
    def get_all(self):
        packages = ["foo", "bar", "baz", "qux", "aaa", "bbb", "ccc"]
        return [Dum(name=p) for p in packages]


class CoprDummy(CoprBackend):
    def submit(self, entity):
        print("--> {}".format(entity.name))
        return entity
