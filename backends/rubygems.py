from subprocess import PIPE, Popen, call
from copr_rebuild_tools import Backend, CoprBackend, Entity


class Gem(Entity):
    @property
    def pkgname(self):
        return self.name if self.name.startswith("rubygem-") else "rubygem-{}".format(self.name)


class Rubygems(Backend):
    def get_all(self):
        # Require `rubygems` package
        cmd = ["gem", "search"]
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
        output, error = proc.communicate()
        return [Gem(name=x.split()[0], version=x.split()[1][1:-1])
                for x in output.decode("utf-8").split("\n")[:-1]]


class CoprRubygems(CoprBackend):
    def submit(self, package):
        command = [
            "/usr/bin/copr-cli",
            "--config",
            self.conf["copr-config"],
            "buildgem",
            self.copr_full_name,
            "--gem={0}".format(package.name),
            "--nowait",
            "--background"
        ]
        call(command)
