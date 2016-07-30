import os
import quanbot.replies
import quanbot.user_state

ACCESS_TOKEN = os.environ.get('FB_PAGE_ACCESS_TOKEN', 'conf_this')


def handler_message(sender, message):
    replies = quanbot.replies.Replies(
            access_token=ACCESS_TOKEN,
            recipient_id=sender,
            )
    user_state = quanbot.user_state.UserState.getIfNew(sender, replies)
    user_state.run_behavior(message)
    # if user_state.state_is_empty():
    #     replies.ask_where()
    #     user_state.next_behavior()
    # replies.reply_button_template()
    # replies.reply_generic_template()
