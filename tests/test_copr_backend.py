import unittest
from copr_rebuild_tools import CoprBackend


class CoprDummy(CoprBackend):
    pass


class TestCoprBackend(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
