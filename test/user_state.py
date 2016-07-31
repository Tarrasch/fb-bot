import unittest
from unittest.mock import Mock
import quanbot.user_state


class TestUserState(unittest.TestCase):

    def setUp(self):
        quanbot.user_state.UserState.static_userids = {}
        self.replies = Mock()
        self.sender = '1234'
        self.user_state = quanbot.user_state.UserState(
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
        self.replies.give_suggestions.assert_called_once_with('Quận 5', [])

    def test_misunderstands_garbage(self):
        self.user_state.run_behavior("Hi bot!")
        self.user_state.run_behavior("Stockholm")
        self.replies.failed_read_location.assert_called_once_with()

    def test_understands_q5_after_fail(self):
        self.user_state.run_behavior("blahblah")
        self.user_state.run_behavior("Dsj")
        self.replies.failed_read_location.assert_called_once_with()
        self.user_state.run_behavior("djjdu")
        self.replies.failed_read_location.assert_has_calls(2*[[]])
        self.user_state.run_behavior("q5")
        self.replies.failed_read_location.assert_has_calls(2*[[]])
        self.replies.give_suggestions.assert_called_once_with('Quận 5', [])

    def test_can_restart(self):
        self.user_state.run_behavior("Hi bot!")
        self.replies.ask_where.assert_called_once_with()
        self.user_state.run_behavior("q5")
        self.replies.ask_where.assert_called_once_with()
        self.user_state.run_behavior("chao")
        self.replies.say_restarting.assert_has_calls(1*[[]])
        self.replies.ask_where.assert_has_calls(2*[[]])
        self.user_state.run_behavior("chao")
        self.replies.say_restarting.assert_has_calls(2*[[]])
        self.replies.ask_where.assert_has_calls(3*[[]])

if __name__ == '__main__':
    unittest.main()
