# app.py - Simple chatbot for GCS AI (Sinoy) using keyword matching

import difflib
from data import school_data  # Import the data dictionary

def get_response(query):
    query = query.lower().strip()
    keywords = query.split()  # Split query into words for matching
    
    # Define keyword mappings to data sections
    keyword_map = {
        "name": "basic_details.school_name",
        "type": "basic_details.type",
        "board": "basic_details.board",
        "established": "basic_details.established",
        "max students": "basic_details.max_students_per_class",
        "staff": "basic_details.total_teaching_staff",
        "timings": "basic_details.timings",
        "address": "address",
        "director": "management.director",
        "principal": "management.principal",
        "vice principal": "management.vice_principal",
        "system manager": "management.system_manager",
        "motto": "vision_mission_motto.motto",
        "mission": "vision_mission_motto.mission",
        "vision": "vision_mission_motto.vision",
        "senior teachers": "teaching_staff.senior_teachers",
        "junior teachers": "teaching_staff.junior_teachers",
        "non teaching": "non_teaching_staff",
        "fees": "fee_structure.monthly_fees",
        "class 11": "class_11_details",
        "monitors": "class_monitors",
        "academics": "academics_class_11",
        "exhibition": "science_exhibition",
        "infrastructure": "infrastructure_facilities",
        "transport": "transport_facility",
        "admission": "admission_requirements",
        "houses": "house_system",
        "sports": "sports_activities.sports",
        "activities": "sports_activities.activities",
        "best player": "sports_activities.best_player",
        "ai project": "gcs_ai_project"
    }
    
    # Find the best matching section
    best_match = None
    best_score = 0
    for key, path in keyword_map.items():
        score = sum(1 for word in keywords if word in key.lower())
        if score > best_score:
            best_score = score
            best_match = path
    
    if best_match and best_score > 0:
        data = school_data
        for part in best_match.split('.'):
            data = data.get(part, {})
        if isinstance(data, dict):
            response = "\n".join([f"{k}: {v}" for k, v in data.items()])
        elif isinstance(data, list):
            response = "\n".join(data)
        else:
            response = str(data)
        return f"Here's the info: {response}"
    
    # Fallback: Suggest similar queries
    suggestions = difflib.get_close_matches(query, keyword_map.keys(), n=3)
    if suggestions:
        return f"Sorry, I didn't understand. Did you mean: {', '.join(suggestions)}?"
    return "I'm Sinoy, the GCS AI chatbot. Ask me about school details like fees, staff, or timings!"

# Main loop for command-line interaction
if __name__ == "__main__":
    print("Hello! I'm Sinoy, your GCS AI assistant. Ask me anything about Gurukul Convent School. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = get_response(user_input)
        print(f"Sinoy: {response}")
