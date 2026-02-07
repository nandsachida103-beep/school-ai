# app.py - Flask-based chatbot (Sinoy)

from flask import Flask, request, jsonify
from data import school_data

app = Flask(__name__)

def get_response(query):
    q = query.lower()

    # Teacher questions
    if "chemistry" in q and "teacher" in q:
        return f"The chemistry teacher is {school_data['teaching_staff']['senior_teachers']['chemistry']}."

    if "biology" in q and "teacher" in q:
        return f"The biology teacher is {school_data['teaching_staff']['senior_teachers']['biology']}."

    # Fee questions (VERY IMPORTANT FOR MONEY)
    if "fee" in q and "class" in q:
        for cls, fee in school_data["fee_structure"]["monthly_fees"].items():
            if f"class {cls}" in q:
                return f"The monthly fee for Class {cls} is Rs. {fee}."

    if "class 11" in q and "fee" in q:
        s = school_data["class_11_details"]["school_fee"]
        c = school_data["class_11_details"]["coaching_fee"]
        return f"Class 11 school fee is Rs. {s} per month and coaching fee is Rs. {c} per month."

    # Bus fee questions
    if "bus" in q or "transport" in q:
        for road, fee in school_data["transport_facility"]["bus_fees"].items():
            if road in q:
                return f"The monthly bus fee for {road.title()} is Rs. {fee}."
        return "Please mention the road name for bus fee."

    # Management
    if "principal" in q:
        return f"The principal is {school_data['management']['principal']}."

    if "director" in q:
        return f"The director is {school_data['management']['director']}."

    return "I am Sinoy. You can ask me about fees, bus fees, teachers, or school details."

@app.route("/")
def home():
    return "Sinoy (GCS AI) is running."

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    reply = get_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
