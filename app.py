from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
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
        return getattr(self, 'json', None)

    @property
    def recipient_id(self):
        return self.json['recipient_id']


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

            message = entry.get('message', {}).get('text')
            payload = entry.get('postback', {}).get('payload')
            simplify = message or payload
            if simplify:
                user = getuser(sender)
                new_user = quanbot.handler.handler_message(user, simplify)
                saveuser(new_user)

    except Exception as ex:
        print(ex)
    return "ok"


def getuser(recipient_id):
    import json
    all_users = User.query.all()
    parsed_users = []
    for user in all_users:
        try:
            user.json = json.loads(user.dict_str)
            parsed_users.append(user)
        except json.JSONDecodeError:
            pass
    for parsed_user in parsed_users:
        if parsed_user.json['recipient_id'] == recipient_id:
            return parsed_user

    user = User('TODO')
    user.json = dict(recipient_id=recipient_id)


def saveuser(user):
    import json
    user.dict_str = json.dumps(user.json)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
