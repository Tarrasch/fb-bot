import os
import quanbot.replies
import quanbot.user_state

ACCESS_TOKEN = os.environ.get('FB_PAGE_ACCESS_TOKEN', 'conf_this')


def handler_message(sender, message):
    replies = quanbot.replies.Replies(
            access_token=ACCESS_TOKEN,
            recipient_id=sender,
            )
    user_state = quanbot.user_state.UserState.getIfNew(
            recipient_id=sender,
            replies=replies,
            )
    user_state.run_behavior(message)
