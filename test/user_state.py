import unittest
from unittest.mock import Mock
import quanbot.user_state
from quanbot.location import Location


class TestUserState(unittest.TestCase):

    def setUp(self):
        quanbot.user_state.UserState.static_userids = {}
        self.replies = Mock()
        self.sender = '1234'
        self.user_state = quanbot.user_state.UserState.getIfNew(
                self.sender,
                self.replies,
                )

    def test_asks_where(self):
        self.user_state.run_behavior("Hi bot!")
        self.replies.ask_where.assert_called_once_with()

    def test_understands_q5(self):
        self.user_state.run_behavior("Hi bot!")
        self.replies.ask_where.assert_called_once_with()
        self.user_state.run_behavior("q5")
        self.replies.ask_where.assert_called_once_with()
        location = Location(district='Quận 5')
        self.replies.give_suggestions.assert_called_once_with(location)

    def test_misunderstands_garbage(self):
        self.user_state.run_behavior("Hi bot!")
        self.user_state.run_behavior("Stockholm")
        self.replies.failed_read_location.assert_called_once_with()

    def test_understands_q5_after_fail(self):
        self.user_state.run_behavior("Chào")
        self.user_state.run_behavior("Dsj")
        self.replies.failed_read_location.assert_called_once_with()
        self.user_state.run_behavior("djjdu")
        self.replies.failed_read_location.assert_has_calls(2*[[]])
        self.user_state.run_behavior("q5")
        location = Location(district='Quận 5')
        self.replies.failed_read_location.assert_has_calls(2*[[]])
        self.replies.give_suggestions.assert_called_once_with(location)

if __name__ == '__main__':
    unittest.main()
