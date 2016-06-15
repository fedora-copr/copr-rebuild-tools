import unittest
from copr_rebuild_tools import Backend, Query


class Dummy(Backend):
    pass


class TestBackend(unittest.TestCase):
    pass


class TestQuery(unittest.TestCase):
    def test_query_operations(self):
        objects = ["foo", "bar", "baz", "qux", "aaa", "bbb", "ccc"]
        q = Query(objects)

        self.assertEqual(q.limit(3).get(), ["foo", "bar", "baz"])
        self.assertEqual(q.offset("aaa").get(), ["bbb", "ccc"])
        self.assertEqual(q.offset("baz").limit(2).get(), ["qux", "aaa"])

        self.assertEqual(q.limit(None).get(), objects)
        self.assertEqual(q.offset(None).get(), objects)
        self.assertEqual(q.offset("nonexisting").get(), objects)


if __name__ == "__main__":
    unittest.main()
