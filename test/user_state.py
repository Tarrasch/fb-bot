import unittest
from unittest.mock import Mock
import quanbot.user_state



class TestUserState(unittest.TestCase):

    def test_transitions(self):
        replies = Mock()
        sender = '1234'
        user_state = quanbot.user_state.UserState.getIfNew(sender, replies)
        user_state.run_behavior("Hi bot!")
        replies.ask_where().assert_called()

if __name__ == '__main__':
    unittest.main()
