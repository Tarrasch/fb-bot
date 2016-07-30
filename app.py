from flask import Flask, request
import os
import requests

app = Flask(__name__)

ACCESS_TOKEN = os.environ.get('FB_PAGE_ACCESS_TOKEN', 'conf_this')
VERIFY_TOKEN = "my_voice_is_my_password_verify_me"


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": "reply: " + msg}
    }
    location = ("https://graph.facebook.com/v2.6/me/messages?access_token="
                + ACCESS_TOKEN)
    resp = requests.post(location, json=data)
    print(resp.content)


def reply_test(user_id):
    from messengerbot import MessengerClient, messages
    from messengerbot import attachments, templates, elements

    # Manully initialise client
    messenger = MessengerClient(access_token=ACCESS_TOKEN)
    recipient = messages.Recipient(recipient_id=user_id)

    # Send text message
    message = messages.Message(text='Hello World')
    request = messages.MessageRequest(recipient, message)
    messenger.send(request)

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
    attachment = attachments.TemplateAttachment(template=outer_template)

    message = messages.Message(attachment=attachment)
    request = messages.MessageRequest(recipient, message)
    messenger.send(request)


@app.route('/')
def hello_world():
    return 'Hello, World! https://www.facebook.com/Quanbot-1658289714492002/'


@app.route('/webhook', methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"


@app.route('/webhook', methods=['POST'])
def handle_incoming_messages():
    try:
        data = request.json
        sender = data['entry'][0]['messaging'][0]['sender']['id']
        message = data['entry'][0]['messaging'][0]['message']['text']
        reply(sender, message)
        reply_test(sender)
    except Exception as ex:
        print(ex)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
