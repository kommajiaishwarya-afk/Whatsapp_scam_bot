from flask import Flask
import os

application = Flask(__name__)

def analyze_message_for_scam(message_text):
    message_text = message_text.lower()

    if "free" in message_text or "win" in message_text or "loan" in message_text:
        return "This message looks suspicious."

    if ".xyz" in message_text or ".top" in message_text:
        return " This link may be a scam."

    return "This message looks safe."


@application.route("/")
def index():
    return "WhatsApp Scam Detector Bot Running!"


@application.route("/scan/<input_message>")
def scan_message(input_message):
    return analyze_message_for_scam(input_message)


if __name__ == "__main__":
    port=int(os.environ.get("PORT",10000))
    application.run(host="0.0.0.0",port=port)