from flask import Flask, render_template, request, jsonify
from data import school_data

app = Flask(__name__)

FALLBACK = f"Sorry, I don't have information about that. You can contact the school at {', '.join(school_data['gcs_ai']['contact_numbers'])}."

# Map ordinals to numbers
ordinals = {
    "1st": "1", "first": "1",
    "2nd": "2", "second": "2",
    "3rd": "3", "third": "3",
    "4th": "4", "fourth": "4",
    "5th": "5", "fifth": "5",
    "6th": "6", "sixth": "6",
    "7th": "7", "seventh": "7",
    "8th": "8", "eighth": "8",
    "9th": "9", "ninth": "9",
    "10th": "10", "tenth": "10",
    "11th": "11", "eleventh": "11",
    "12th": "12", "twelfth": "12"
}

# Keywords for teacher queries
teacher_keywords = {
    "principal": ["management", "principal"],
    "director": ["management", "director"],
    "vice principal": ["management", "vice_principal"],
    "system manager": ["management", "system_manager"],
    "senior teachers": ["senior_teachers"],
    "junior teachers": ["junior_teachers"]
}

# Keywords for fee queries
fee_keywords = ["class", "fee"]

# Keywords for transport
transport_keywords = ["bus", "transport"]

# Keywords for other data
other_keywords = {
    "address": "address",
    "timing": "timings",
    "motto": ["vision_mission_motto", "motto"],
    "mission": ["vision_mission_motto", "mission"],
    "vision": ["vision_mission_motto", "vision"],
    "infrastructure": "infrastructure",
    "admission": "admission_requirements",
    "houses": "house_system",
    "house system": "house_system",
    "sports": ["sports_activities", "sports"],
    "activities": ["sports_activities", "activities"],
    "contact": ["gcs_ai", "contact_numbers"]
}

def fetch_answer(user_input):
    user_input_lower = user_input.lower()

    # -------------------------
    # 1. Class fee queries
    # -------------------------
    if any(k in user_input_lower for k in fee_keywords):
        for cls in school_data['fee_structure']:
            if f"class {cls}" in user_input_lower or cls in user_input_lower:
                return f"Class {cls} fee is ₹{school_data['fee_structure'][cls]}."
        # Check ordinals
        for ord_key, cls_num in ordinals.items():
            if ord_key in user_input_lower:
                return f"Class {cls_num} fee is ₹{school_data['fee_structure'][cls_num]}."

    # -------------------------
    # 2. Transport/Bus fees
    # -------------------------
    if any(k in user_input_lower for k in transport_keywords):
        for route, fee in school_data['transport']['routes_fees'].items():
            if route.lower() in user_input_lower:
                return f"Bus fee for {route} is ₹{fee}."

    # -------------------------
    # 3. Teacher queries
    # -------------------------
    for key, path in teacher_keywords.items():
        if key in user_input_lower:
            data = school_data
            if isinstance(path, list):
                for p in path:
                    data = data.get(p, None)
                    if data is None:
                        return FALLBACK
            if isinstance(data, dict):
                if key in ["senior teachers", "junior teachers"]:
                    # List teachers clearly
                    lines = [f"- {t}" for t in data] if key=="junior teachers" else [f"- {k}: {v}" for k,v in data.items()]
                    return f"{key.title()}:\n" + "\n".join(lines)
                else:
                    return f"{key.title()}: {data}"
            elif isinstance(data, list):
                return ", ".join(data)

    # -------------------------
    # 4. Other keywords
    # -------------------------
    for key, path in other_keywords.items():
        if key in user_input_lower:
            data = school_data
            if isinstance(path, list):
                for p in path:
                    data = data.get(p, None)
                    if data is None:
                        return FALLBACK
            else:
                data = data.get(path, None)
            if isinstance(data, dict):
                return "\n".join([f"{k}: {v}" for k,v in data.items()])
            elif isinstance(data, list):
                return ", ".join(data)
            else:
                return str(data)

    return FALLBACK

# -------------------------
# Flask routes
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form.get("message")
    answer = fetch_answer(user_input)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
