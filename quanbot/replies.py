from messengerbot import MessengerClient, messages
from messengerbot import attachments, templates, elements


class Replies(object):

    def __init__(self, access_token, recipient_id):
        self.access_token = access_token
        self.recipient_id = recipient_id
        self.messenger = MessengerClient(access_token=access_token)

    @property
    def recipient(self):
        return messages.Recipient(recipient_id=self.recipient_id)

    def _reply_msg(self, msg):
        message = messages.Message(text='Hello World')
        request = messages.MessageRequest(self.recipient, message)
        self.messenger.send(request)

    def reply_greeting(self):
        self._reply_msg('Xin chào! Bạn muốn ăn ở đâu?')
