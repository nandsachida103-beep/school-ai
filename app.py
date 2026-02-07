from flask import Flask, render_template, request
from data import school_data
import re

app = Flask(__name__)

# ---------- CLASS DETECTOR ----------
def detect_class(text):
    text = text.lower()

    if "nursery" in text:
        return "nursery"
    if "lkg" in text:
        return "lkg"
    if "ukg" in text:
        return "ukg"

    match = re.search(r'\bclass\s*(\d{1,2})\b', text)
    if match:
        return int(match.group(1))

    match = re.search(r'\b(\d{1,2})\b', text)
    if match:
        num = int(match.group(1))
        if 1 <= num <= 12:
            return num

    return None


# ---------- AI BRAIN ----------
def sinoy_reply(user_text):
    text = user_text.lower()

    # ----- FEES (TOP PRIORITY) -----
    if any(word in text for word in ["fee", "fees", "paisa", "money"]):
        cls = detect_class(text)

        if cls == 11:
            f = school_data["class_11_fees"]
            return (
                "💰 Class 11 Fee Details:\n"
                f"School Fee: ₹{f['school_fee']}/month\n"
                f"Coaching Fee: ₹{f['coaching_fee']}/month\n"
                f"👉 Total: ₹{f['total']}/month"
            )

        if cls in school_data["fees"]:
            return f"💰 Monthly fee for Class {cls} is ₹{school_data['fees'][cls]}."

        return "Please specify the class clearly (example: Class 1 fee / Class 11 fees)."

    # ----- SUBJECT TEACHERS -----
    if "teacher" in text or "sir" in text or "maam" in text:
        for subject, info in school_data["senior_teachers"].items():
            if subject in text:
                return f"📘 {subject.title()} teacher is {info['name']}."

    # ----- PRINCIPAL / DIRECTOR -----
    if "principal" in text:
        return f"👩‍🏫 Principal: {school_data['management']['principal']}"
    if "director" in text:
        return f"👨‍💼 Director: {school_data['management']['director']}"

    # ----- BUS FEES -----
    if "bus" in text or "transport" in text:
        for route, fee in school_data["transport"]["bus_fees"].items():
            if route in text:
                return f"🚌 Bus fee for {route.title()} is ₹{fee}/month."
        return "🚌 Please tell the route name."

    # ----- BEST PLAYER -----
    if "best player" in text:
        return f"🏆 {school_data['best_player']}"

    # ----- TIMING -----
    if "time" in text or "timing" in text:
        t = school_data["timings"]
        return (
            "⏰ School Timings:\n"
            f"Nursery–UKG: {t['nursery_ukg']}\n"
            f"Class 1–12: {t['class_1_12']}"
        )

    # ----- FALLBACK -----
    return (
        "🤖 I am Sinoy, GCS AI.\n"
        "I can answer about fees, teachers, bus charges, classes & timings.\n"
        "Please ask clearly."
    )


@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        user_msg = request.form.get("message")
        reply = sinoy_reply(user_msg)
    return render_template("index.html", reply=reply)


if __name__ == "__main__":
    app.run(debug=True)
