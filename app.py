from flask import Flask, render_template, request, jsonify
from data import school_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"].lower()

    # Fees (class-wise)
    for cls, fee in school_data["fees"].items():
        if cls in msg:
            return jsonify({"reply": f"Monthly fee for {cls.title()} is ₹{fee}."})

    # Bus route fee
    for route, fee in school_data["transport"].items():
        if route in msg:
            return jsonify({"reply": f"Bus fee for {route.title()} is ₹{fee} per month."})

    # Management
    for post, name in school_data["management"].items():
        if post.replace("_", " ") in msg:
            return jsonify({"reply": f"The {post.replace('_',' ')} is {name}."})

    # Teachers
    for teacher, detail in school_data["senior_teachers"].items():
        if teacher in msg:
            return jsonify({"reply": f"{teacher.title()} teaches {detail}."})

    # Timings
    if "timing" in msg or "time" in msg:
        return jsonify({"reply": school_data["timing"]})

    # Address
    if "address" in msg or "location" in msg:
        return jsonify({"reply": school_data["address"]})

    # Sports
    if "sports" in msg or "games" in msg:
        return jsonify({"reply": school_data["sports"]})

    # Science Exhibition
    if "science" in msg or "exhibition" in msg:
        return jsonify({"reply": school_data["science_exhibition"]})

    # Founders
    if "founder" in msg or "created" in msg:
        return jsonify({"reply": school_data["founders"]})

    return jsonify({
        "reply": "I am Sinoy 🤖. Ask me about fees, bus routes, teachers, timings, management, sports, address, exams, or facilities."
    })

if __name__ == "__main__":
    app.run(debug=True)
