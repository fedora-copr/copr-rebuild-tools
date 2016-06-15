import unittest
from copr_rebuild_tools import CoprBackend


class CoprDummy(CoprBackend):
    pass


class TestCoprBackend(unittest.TestCase):
    def test_copr_full_name(self):
        cb1 = CoprDummy({"project": "copr"})
        self.assertEqual(cb1.copr_full_name, "copr")

        cb2 = CoprDummy({"owner": "@group", "project": "copr"})
        self.assertEqual(cb2.copr_full_name, "@group/copr")


if __name__ == "__main__":
    unittest.main()
