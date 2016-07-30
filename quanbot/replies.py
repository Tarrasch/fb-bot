from messengerbot import MessengerClient, messages
from messengerbot import attachments, templates, elements
import quanbot.quan


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
        results = quanbot.quan.Quan.search(location)
        if results:
            elements = list(map(self._quan_element, results))
            self._send_carousel(elements)
            return True
        else:
            self.reply_msg("Không tìm thành công thì restart")
            return False

    def failed_read_location(self):
        self.reply_msg('Vui lòng viết lại')

    def _quan_element(self, qd):
        web_button = elements.WebUrlButton(
                title='xem trên Foody.vn',
                url=qd['URL'],
                )
        postback_button = elements.PostbackButton(
                title="Không " + qd['maindish'],
                payload='TODO'
                )
        element = elements.Element(
                title=qd['Name'],
                item_url=qd['URL'],
                image_url=qd['Pic'],
                subtitle=qd['dish'],
                buttons=[
                    # web_button,
                    postback_button,
                ],
                )

        return element

    def _send_carousel(self, elements):
        generic_template = templates.GenericTemplate(
                elements=elements
                )
        attachment = attachments.TemplateAttachment(template=generic_template)

        message = messages.Message(attachment=attachment)
        request = messages.MessageRequest(self.recipient, message)
        self.messenger.send(request)
