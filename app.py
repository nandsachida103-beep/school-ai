from flask import Flask, request, jsonify
from data import SCHOOL_DATA, CONTACT

app = Flask(__name__)

BOT_NAME = "Sinoy"

def find_answer(user_msg):
    user_msg = user_msg.lower()

    for key, value in SCHOOL_DATA.items():
        if key in user_msg:
            return value

    # common keyword handling
    if "fee" in user_msg or "fees" in user_msg:
        return SCHOOL_DATA.get("class 11 fee")

    if "timing" in user_msg or "time" in user_msg:
        return SCHOOL_DATA.get("school timing")

    if "teacher" in user_msg or "sir" in user_msg or "mam" in user_msg:
        return (
            "Some senior teachers are:\n"
            "- Chemistry: Mr. Kuldeep Kumar\n"
            "- Physics: Mr. Manish Mishra\n"
            "- Maths: Mr. Manoj Dwivedi\n"
            "- Biology: Mrs. Vibha Ma’am\n"
            "- English: Mr. Mohsin Khan\n"
            "- Hindi: Mrs. Kanchan Shukla"
        )

    if "transport" in user_msg or "bus" in user_msg:
        return SCHOOL_DATA.get("transport")

    if "monitor" in user_msg:
        for key in SCHOOL_DATA:
            if "monitor" in key and key in user_msg:
                return SCHOOL_DATA[key]

    if "principal" in user_msg:
        return SCHOOL_DATA.get("principal")

    if "director" in user_msg:
        return SCHOOL_DATA.get("director")

    if "admission" in user_msg or "document" in user_msg:
        return SCHOOL_DATA.get("documents required")

    # fallback
    return (
        "Sorry, I don’t have exact information for that right now.\n"
        f"Please contact the school office at: {CONTACT['numbers']}"
    )


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Gurukul Convent School AI",
        "chatbot": BOT_NAME
    })


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    if not user_msg:
        return jsonify({
            "reply": f"{BOT_NAME}: Please ask a valid question."
        })

    answer = find_answer(user_msg)

    return jsonify({
        "reply": f"{BOT_NAME}: {answer}"
    })


if __name__ == "__main__":
    app.run(debug=True)
