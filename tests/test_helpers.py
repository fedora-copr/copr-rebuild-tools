import unittest
from copr_rebuild_tools.helpers import is_greater


class TestHelpers(unittest.TestCase):
    def test_is_greater(self):
        assert is_greater("1.2.0", "1.2") == False
        assert is_greater("1.2.3", "1.2.3") == False
        assert is_greater("0.2.3", "1.2.3") == False
        assert is_greater("1.2.3", "0.2.3") == True
        assert is_greater("1.1.3", "1.2.3") == False
        assert is_greater("1.2", "1.2.3") == False
        assert is_greater("1.3", "1.2.3") == True
        assert is_greater("1.2.3.4", "1.2.3.4") == False
        assert is_greater("1.2.3.5", "1.2.3.4") == True


if __name__ == "__main__":
    unittest.main()
