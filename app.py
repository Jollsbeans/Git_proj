from flask import Flask, jsonify
from flask_cors import CORS
from twilio.rest import Client

account_sid='AC123d39c8b2f31740bb72b7c7f82d6976'
auth_token='8df4b2bedd927be2841883994c93b6b9'

twilio_number='+19289188219'
my_phone_number='+639511773048'


app = Flask(__name__)
CORS(app)


data = {
    "users": {
        "1": {"name": "John", "age": 25},
        "2": {"name": "Jane", "age": 30},
        "3": {"name": "Bob", "age": 40},
    }
}

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in data['users']:
        return data['users'][user_id]
    else:
        return f"User with ID {user_id} not found"

@app.route('/msg/<textmessage>/<mynumber>', methods=['GET'])
def get_message(textmessage,mynumber):
    client = Client(account_sid, auth_token)
    message= client.messages.create(
        body=textmessage,
        from_=twilio_number,
        to=mynumber
    )
    response = jsonify(message);
    response.headers.add('Access-Control-Allow-Origin', '*');
    return response;

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
