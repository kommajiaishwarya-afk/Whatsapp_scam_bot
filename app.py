from flask import Flask, request
import os

application = Flask(__name__)

def analyze_message_for_scam(message_text):
    message_text = message_text.lower()
    if "free" in message_text or "win" in message_text or "loan" in message_text:
        return " This message looks suspicious."
    if ".xyz" in message_text or ".top" in message_text:
        return " This link may be a scam."
    return "This message looks safe."

# Twilio WhatsApp webhook route
@application.route("/webhook", methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '')
    response_text = analyze_message_for_scam(incoming_msg)
    
    # Twilio expects XML response
    return f"<Response><Message>{response_text}</Message></Response>", 200, {'Content-Type': 'application/xml'}

# Optional: test server running
@application.route("/")
def index():
    return "WhatsApp Scam Detector Bot Running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    application.run(host="0.0.0.0", port=port)
