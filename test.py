from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")

    # Ollama ile cevap al
    response = ollama.chat(
        model="llama2",
        messages=[{"role": "user", "content": user_message}]
    )

    bot_reply = response["message"]["content"]
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
