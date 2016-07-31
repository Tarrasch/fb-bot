from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
import requests
import quanbot.handler

app = Flask(__name__)
db = SQLAlchemy(app)

VERIFY_TOKEN = "my_voice_is_my_password_verify_me"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dict_str = db.Column(db.String())

    def __init__(self, dict_str):
        self.dict_str = dict_str

    def __repr__(self):
        return '<Name %r>' % self.dict_str


def reply_test(recipient_id):
    from messengerbot import MessengerClient, messages
    from messengerbot import attachments, templates, elements


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
        entries = data['entry'][0]['messaging']
        for entry in entries:
            sender = entry['sender']['id']
            # user = User('John Doe', 'john.doe@example.com')
            # db.session.add(user)
            # db.session.commit()

            message = entry.get('message', {}).get('text')
            payload = entry.get('postback', {}).get('payload')
            simplify = message or payload
            if simplify:
                quanbot.handler.handler_message(sender, simplify)
    except Exception as ex:
        print(ex)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
