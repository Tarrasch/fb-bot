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

    def _reply_msg(self, text):
        message = messages.Message(text=text)
        request = messages.MessageRequest(self.recipient, message)
        self.messenger.send(request)

    def reply_greeting(self):
        self._reply_msg('Xin chào! Bạn muốn ăn ở đâu?')

    def reply_advanced(self):


        # Send button template
        web_button = elements.WebUrlButton(
                title='Show website',
                url='https://petersapparel.parseapp.com'
                )
        postback_button = elements.PostbackButton(
                title='Start chatting',
                payload='USER_DEFINED_PAYLOAD'
                )
        inner_template = templates.ButtonTemplate(
                text='What do you want eat?',
                buttons=[
                    web_button, postback_button
                    ]
                )
        inner_template2 = templates.ButtonTemplate(
                text='What do you want to drink?',
                buttons=[
                    web_button, postback_button
                    ]
                )
        outer_template = templates.GenericTemplate(
                elements=[
                    inner_template, inner_template2
                    ]
                )
        attachment = attachments.TemplateAttachment(template=inner_template)

        message = messages.Message(attachment=attachment)
        request = messages.MessageRequest(self.recipient, message)
        self.messenger.send(request)
