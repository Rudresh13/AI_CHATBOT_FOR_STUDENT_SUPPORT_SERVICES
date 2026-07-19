from flask import Flask, render_template, request, jsonify
from chatbot import get_ai_response

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Chat API
@app.route("/chat", methods=["POST"])
def chat():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "reply": "No data received."
            })

        user_message = data.get("message", "").strip()

        if user_message == "":
            return jsonify({
                "reply": "Please enter a question."
            })

        bot_reply = get_ai_response(user_message)

        return jsonify({
            "reply": bot_reply
        })

    except Exception as e:

        return jsonify({
            "reply": f"Error : {str(e)}"
        })


# Health Check
@app.route("/status")
def status():

    return jsonify({
        "status": "Running",
        "project": "AI Chatbot for Student Support"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
