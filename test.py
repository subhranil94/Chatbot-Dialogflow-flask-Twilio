from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils_final import fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    number = request.form.get('From')
    # Create reply
    resp = MessagingResponse()
    x=fetch_reply(msg,number)
    resp.message(x)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
