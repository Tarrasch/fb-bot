import unittest
import quanbot.quan


class TestUserState(unittest.TestCase):

    def test_search_simple(self):
        q = quanbot.quan.Quan
        res = q.search("Quận 11", [])
        self.assertGreaterEqual(len(res), 3)


if __name__ == '__main__':
    unittest.main()
