from flask import Flask, render_template, request, jsonify
import re
from data import school_data

app = Flask(__name__)

FALLBACK = f"Sorry, I don't have info about that. Contact: {', '.join(school_data['gcs_ai']['contact_numbers'])}."

# Ordinals
ordinals = {
    "1st":"1","first":"1","2nd":"2","second":"2","3rd":"3","third":"3",
    "4th":"4","fourth":"4","5th":"5","fifth":"5","6th":"6","sixth":"6",
    "7th":"7","seventh":"7","8th":"8","eighth":"8","9th":"9","ninth":"9",
    "10th":"10","tenth":"10","11th":"11","eleventh":"11","12th":"12","twelfth":"12"
}

# Teacher & staff keywords (common)
staff_keywords = {
    "principal":["management","principal"],
    "director":["management","director"],
    "vice principal":["management","vice_principal"],
    "system manager":["management","system_manager"],
    "senior teacher":["senior_teachers"],
    "junior teacher":["junior_teachers"],
    "teacher":["senior_teachers","junior_teachers"],  # general
    "reception":["support_staff","receptionists"],
    "peon":["support_staff","peons"],
    "security":["support_staff","security_guards"]
}

# Other keywords
other_keywords = {
    "address":"address",
    "timing":"timings",
    "motto":["vision_mission_motto","motto"],
    "mission":["vision_mission_motto","mission"],
    "vision":["vision_mission_motto","vision"],
    "infrastructure":"infrastructure",
    "admission":"admission_requirements",
    "houses":"house_system",
    "house system":"house_system",
    "sports":["sports_activities","sports"],
    "activities":["sports_activities","activities"],
    "contact":["gcs_ai","contact_numbers"]
}

# --------------------------
# FETCH ANSWER
# --------------------------
def fetch_answer(user_input):
    user_input_lower = user_input.lower()

    # ---- CLASS FEES (exact match) ----
    class_fee_pattern = r"(?:class\s*)?(?P<classnum>\d{1,2}|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|10th|11th|12th|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth)(?:st|nd|rd|th)?(?:\s*class)?\s*(?:fee|fees)?\b"
    match = re.search(class_fee_pattern, user_input_lower)
    if match:
        cls = match.group("classnum")
        cls_num = ordinals.get(cls, cls)
        if cls_num in school_data['fee_structure']:
            return f"Class {cls_num} fee is ₹{school_data['fee_structure'][cls_num]}."
        else:
            return FALLBACK

    # ---- BUS / TRANSPORT FEES ----
    if "bus" in user_input_lower or "transport" in user_input_lower:
        for route, fee in school_data['transport']['routes_fees'].items():
            if route.lower() in user_input_lower:
                return f"Bus fee for {route} is ₹{fee}."

    # ---- STAFF / TEACHERS ----
    for key, path in staff_keywords.items():
        if key in user_input_lower:
            data = school_data
            for p in path:
                data = data.get(p, None)
                if data is None:
                    return FALLBACK
            if isinstance(data, dict):
                if key in ["senior teacher","junior teacher","teacher"]:
                    # format nicely
                    lines = []
                    if key=="teacher":
                        # combine all teachers
                        lines += [f"- {k}: {v}" for k,v in school_data['senior_teachers'].items()]
                        lines += [f"- {t}" for t in school_data['junior_teachers']]
                    elif key=="senior teacher":
                        lines += [f"- {k}: {v}" for k,v in data.items()]
                    else:
                        lines += [f"- {t}" for t in data]
                    return "\n".join(lines)
                else:
                    return str(data)
            elif isinstance(data, list):
                return ", ".join(data)
            else:
                return str(data)

    # ---- OTHER INFO ----
    for key, path in other_keywords.items():
        if key in user_input_lower:
            data = school_data
            if isinstance(path,list):
                for p in path:
                    data = data.get(p,None)
                    if data is None: return FALLBACK
            else:
                data = data.get(path,None)
            if isinstance(data, dict):
                return "\n".join([f"{k}: {v}" for k,v in data.items()])
            elif isinstance(data,list):
                return ", ".join(data)
            else:
                return str(data)

    return FALLBACK

# --------------------------
# FLASK ROUTES
# --------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form.get("message")
    answer = fetch_answer(user_input)
    return jsonify({"response": answer})

if __name__=="__main__":
    app.run(debug=True)
