from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_response(user_message, tone="default"):
    # Prompt-engineering: prepend a style instruction
    system_prompts = {
        "concise": "Answer briefly and to the point.",
        "detailed": "Give a thorough, step-by-step explanation.",
        "casual": "Answer in a friendly, informal tone.",
        "professional": "Answer in a formal, business-like manner."
    }
    style_instruction = system_prompts.get(tone, "")
    
    # Here you'd call the ChatGPT API, but we'll mock it:
    return f"[{tone.upper()} STYLE] {style_instruction} Response to: {user_message}"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    tone = data.get("tone", "default")
    response_text = generate_response(user_message, tone)
    return jsonify({"response": response_text})


