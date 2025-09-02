from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    print("🚀 Gelen mesaj:", user_message)   # debug 1 → tarayıcıdan gelen mesaj

    response = ollama.chat(
        model="llama2",
        messages=[{"role": "user", "content": user_message}]
    )

    print("📩 Ollama cevabı ham:", response)  # debug 2 → Ollama’dan dönen cevap

    try:
        bot_reply = response["message"]["content"]
    except:
        bot_reply = response["messages"][-1]["content"]

    print("🤖 Bot cevabı:", bot_reply)  # debug 3 → JSON’a dönmeden önceki cevap

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
