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

    def reply_msg(self, text):
        message = messages.Message(text=text)
        request = messages.MessageRequest(self.recipient, message)
        self.messenger.send(request)

    def ask_where(self):
        self.reply_msg('Xin chào! Bạn muốn ăn ở đâu?')

    def give_suggestions(self, location):
        text = 'kết quả từ {district} nè'.format(district=location.district)
        self.reply_msg(text)

    def failed_read_location(self):
        self.reply_msg('Vui lòng viết lại')

    def reply_button_template(self):
        web_button = elements.WebUrlButton(
                title='Show website',
                url='https://petersapparel.parseapp.com'
                )
        postback_button = elements.PostbackButton(
                title='Start chatting',
                payload='USER_DEFINED_PAYLOAD'
                )
        button_template = templates.ButtonTemplate(
                text='What do you want eat?',
                buttons=[
                    web_button, postback_button
                    ]
                )
        attachment = attachments.TemplateAttachment(template=button_template)

        message = messages.Message(attachment=attachment)
        request = messages.MessageRequest(self.recipient, message)
        self.messenger.send(request)

    def reply_generic_template(self):
        web_button = elements.WebUrlButton(
                title='Show website',
                url='https://petersapparel.parseapp.com'
                )
        postback_button = elements.PostbackButton(
                title='Start chatting',
                payload='USER_DEFINED_PAYLOAD'
                )
        element = elements.Element(
                title='Hi world',
                item_url='https://petersapparel.parseapp.com',
                image_url='https://media.foody.vn/res/g23/229195/prof/s640x400/foody-mobile-yen-sushi-nk-mb-jpg-805-636030069462797351.jpg',
                subtitle='Hải sản',
                buttons=[
                    web_button,
                    postback_button,
                ],
                )

        generic_template = templates.GenericTemplate(
                elements=[
                    element,
                    element,
                    element,
                    ]
                )
        attachment = attachments.TemplateAttachment(template=generic_template)

        message = messages.Message(attachment=attachment)
        request = messages.MessageRequest(self.recipient, message)
        self.messenger.send(request)
