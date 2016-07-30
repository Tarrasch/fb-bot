import unittest
from unittest.mock import Mock
import quanbot.quan
from quanbot.location import Location


class TestUserState(unittest.TestCase):

    def test_search_simple(self):
        q = quanbot.quan.Quan
        res = q.search(Location(district="Quận 11"))
        self.assertGreaterEqual(len(res), 3)


if __name__ == '__main__':
    unittest.main()
