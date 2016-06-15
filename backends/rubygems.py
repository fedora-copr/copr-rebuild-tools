from subprocess import PIPE, Popen, call
from copr_rebuild_tools import Backend, CoprBackend


class Rubygems(Backend):
    def get_all(self):
        # Require `rubygems` package
        cmd = ["gem", "search"]
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
        output, error = proc.communicate()
        return [x.split()[0] for x in output.split("\n")[:-1]]


class CoprRubygems(CoprBackend):
    def submit(self, package):
        command = ["/usr/bin/copr-cli", "--config", self.conf["copr-config"],
                   "buildgem", self.copr_full_name, "--gem", package, "--nowait"]
        call(command)
