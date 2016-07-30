import os
import quanbot.replies

ACCESS_TOKEN = os.environ.get('FB_PAGE_ACCESS_TOKEN', 'conf_this')


def handler_message(sender, message):
    replies = quanbot.replies.Replies(
            access_token=ACCESS_TOKEN,
            recipient_id=sender,
            )
    replies.reply_greeting()
    replies.reply_advanced()
