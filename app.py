from flask import Flask

app = Flask(__name__)

def detect_scam(text):
    text = text.lower()

    if "free" in text or "win" in text or "loan" in text:
        return "⚠️ This message looks suspicious."

    if ".xyz" in text or ".top" in text:
        return "❌ This link may be a scam."

    return "✅ This message looks safe."


@app.route("/")
def home():
    return "WhatsApp Scam Detector Bot Running!"


# 👇 ADD THIS PART BELOW
@app.route("/test/<message>")
def test(message):
    return detect_scam(message)


if __name__ == "__main__":
    app.run(debug=True)