from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(chatbot_for_student)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    reply = get_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
