import unittest
from backends import pypi, rubygems


class TestPypiModule(unittest.TestCase):
    def test_pkgname(self):
        self.assertEqual(pypi.Module(name="foo").pkgname, "python-foo")
        self.assertEqual(pypi.Module(name="python-bar").pkgname, "python-bar")


class TestRubygemsGem(unittest.TestCase):
    def test_pkgname(self):
        self.assertEqual(rubygems.Gem(name="foo").pkgname, "rubygem-foo")
        self.assertEqual(rubygems.Gem(name="rubygem-bar").pkgname, "rubygem-bar")


if __name__ == "__main__":
    unittest.main()
