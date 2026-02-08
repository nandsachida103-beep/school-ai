# app.py
from flask import Flask, render_template, request, jsonify
from data import school_data

app = Flask(__name__)

# Fallback message
FALLBACK = f"Sorry, I don't have information about that. You can contact the school at {', '.join(school_data['gcs_ai']['contact_numbers'])}."

# Map keywords to data paths
keywords = {
    "school info": "basic_info",
    "timing": "timings",
    "address": "address",
    "director": ["management", "director"],
    "principal": ["management", "principal"],
    "vice principal": ["management", "vice_principal"],
    "system manager": ["management", "system_manager"],
    "motto": ["vision_mission_motto", "motto"],
    "mission": ["vision_mission_motto", "mission"],
    "vision": ["vision_mission_motto", "vision"],
    "senior teachers": "senior_teachers",
    "junior teachers": "junior_teachers",
    "fee": "fee_structure",
    "class": "fee_structure",
    "class 11": "class_11_details",
    "infrastructure": "infrastructure",
    "transport": "transport",
    "admission": "admission_requirements",
    "houses": "house_system",
    "house system": "house_system",
    "sports": ["sports_activities", "sports"],
    "activities": ["sports_activities", "activities"],
    "contact": ["gcs_ai", "contact_numbers"]
}

def fetch_answer(user_input):
    user_input_lower = user_input.lower()
    
    # Special check for class fee queries
    if "class" in user_input_lower and "fee" in user_input_lower:
        for cls in school_data['fee_structure']:
            if cls in user_input_lower or f"class {cls}" in user_input_lower:
                return f"Class {cls} fee: ₹{school_data['fee_structure'][cls]}"
    
    # Regular keyword matching
    for key, path in keywords.items():
        if key in user_input_lower:
            data = school_data
            # Handle nested path
            if isinstance(path, list):
                for p in path:
                    data = data.get(p, None)
                    if data is None:
                        break
            else:
                data = data.get(path, None)
            
            if data is None:
                return FALLBACK
            
            # Format output based on type
            if isinstance(data, dict):
                return "\n".join([f"{k}: {v}" for k, v in data.items()])
            elif isinstance(data, list):
                return ", ".join(data)
            else:
                return str(data)
    
    return FALLBACK

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
