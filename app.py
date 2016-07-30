from flask import Flask, request
import os
from pprint import pprint
import requests

app = Flask(__name__)

ACCESS_TOKEN = os.environ.get('FB_PAGE_ACCESS_TOKEN', 'this_should_be_configured')
VERIFY_TOKEN = "my_voice_is_my_password_verify_me"

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": "reply: " + msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/')
def hello_world():
    return 'Hello, World! https://www.facebook.com/Quanbot-1658289714492002/'


@app.route('/webhook/', methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"


@app.route('/webhook/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    pprint(data)
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
