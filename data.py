# data.py - Stores all school data in a structured dictionary

school_data = {
    "basic_details": {
        "school_name": "Gurukul Convent School",
        "type": "Co-educational",
        "board": "CBSE pattern (NCERT-based syllabus)",
        "established": 2005,
        "max_students_per_class": 40,
        "total_teaching_staff": "40+",
        "timings": {
            "general": "10:00 AM – 3:00 PM",
            "nursery_ukg": "8:00 AM – 12:00 PM",
            "class_1_12": "9:30 AM – 2:00 PM"
        }
    },
    "address": "Siyarapar, Bahbol, Bansi, Siddharth Nagar",
    "management": {
        "director": "Mr. Shailesh Pandey",
        "principal": "Mrs. Neha Pandey",
        "vice_principal": "Mr. Ram Jit Yadav",
        "system_manager": "Mr. Mustkeem Sir"
    },
    "vision_mission_motto": {
        "motto": "Holistic Education, Diverse Learning",
        "mission": ["Moral values & discipline", "Leadership development", "Life skills & personality building"],
        "vision": "To bring out the best in every student through holistic education"
    },
    "teaching_staff": {
        "senior_teachers": {
            "Mr. Kuldeep Kumar": {"subject": "Chemistry", "qualification": "B.Sc, M.A, D.El.Ed, B.Ed", "role": "Lecturer – Chemistry, Head of Science Exhibition (2025–26)"},
            "Mrs. Vibha Ma’am": {"subject": "Biology", "qualification": "M.Sc, B.Ed"},
            "Mr. Manoj Dwivedi": {"subject": "Mathematics", "qualification": "M.Sc, B.Ed"},
            "Mr. Manish Mishra": {"subject": "Physics", "qualification": "B.Sc Biotechnology"},
            "Mr. Mohsin Khan": {"subject": "English"},
            "Mrs. Kanchan Shukla": {"subject": "Hindi"}
        },
        "junior_teachers": ["Harshit Agrahari – Mathematics", "Sunil Sir – Mathematics", "Sehbal Sir – Physical Education", "Priya Ma’am – English", "Pooja Ma’am – Science", "Sweta Ma’am – Sanskrit / Art / Hindi", "Asha Ma’am", "Laxmi Ma’am", "Other junior-class teachers"]
    },
    "non_teaching_staff": {
        "receptionists": ["Sakshi Ma’am", "Sadhana Ma’am"],
        "peons": 2,
        "security_guards": 2
    },
    "fee_structure": {
        "monthly_fees": {
            "Nursery": 500,
            "LKG": 550,
            "UKG": 600,
            "Class 1": 700,
            "Class 2": 800,
            "Class 3": 900,
            "Class 4": 1000,
            "Class 5": 1100,
            "Class 6": 1200,
            "Class 7": 1300,
            "Class 8": 1400,
            "Class 9": 1500,
            "Class 10": 1800,
            "Class 11": 2000,
            "Class 12": 2200
        }
    },
    "class_11_details": {
        "fees": {"school_fee": 2000, "coaching_fee": 2000},
        "boys": ["Shashi Kapoor", "Prince Bharti", "Raunak Shukla", "Siddharth Srivastav", "Neeraj Kumar", "Aditya Jaiswal", "Anuj Chaubey", "Vicky Agrahari", "Zaid", "Yuvraj Yadav", "Prem Sagar"],
        "girls": ["Srushti Tripathi", "Sahista Khatoon", "Ishika Singh", "Khushi Agrahari", "Kritika Agrahari", "Khushi Soni", "Saziya Khatoon", "Sristy Bharti", "Aafrin Khan", "Samayara", "Eram", "Rawan Siddique", "Prasansa", "Janvi Singh", "Aditi"]
    },
    "class_monitors": {
        "Class 5": "Abhay Bharti",
        "Class 9": "Adarsh Agrahari",
        "Class 11": "Shashi Kapoor"
    },
    "academics_class_11": {
        "subjects": ["Mathematics – Full Book", "Physics – Full Book", "Chemistry – Full Book", "Biology – Full Book", "Hindi – Full Book (with Grammar)", "English – Full Book (with Grammar)"],
        "final_exams": "1st week of March"
    },
    "science_exhibition": {
        "date": "7 February 2026",
        "head": "Mr. Kuldeep Kumar",
        "support": ["Manoj Sir", "Manish Sir", "Vibha Ma’am", "Mohsin Sir"]
    },
    "infrastructure_facilities": ["AC Classrooms", "Science Labs", "Computer Lab (15+ computers)", "Projectors (Junior Classes)", "Online Classes", "Sports Facilities", "Scholarships / Fee Concessions"],
    "transport_facility": {
        "vehicles": {"buses": 3, "vans": 4, "force_vehicle": 1},
        "bus_fees": {
            "Pathra Road": 1150,
            "Chetiya Road": 1200,
            "Beloha Road": 1100,
            "Rudhauli Road": 900,
            "Kaji Rudhauli Road": 1000,
            "Supa Road": 950
        }
    },
    "admission_requirements": ["Birth Certificate", "Aadhaar Card (Student)", "Address Proof", "Passport-size Photos", "Transfer Certificate (if applicable)", "Previous School Report Card"],
    "house_system": ["Yellow", "Red", "Blue", "Green"],
    "sports_activities": {
        "sports": ["Cricket", "Kho-Kho", "Chess", "Carrom", "Badminton", "Volleyball", "Long Jump"],
        "activities": ["Debate", "Rangoli", "Dance", "Science Exhibition", "Educational Tours"],
        "best_player": "Raj Kapoor – Cricket & Volleyball"
    },
    "gcs_ai_project": {
        "founders": ["Shashi Kapoor", "Prince Bharti"],
        "chatbot_name": "Sinoy"
    }
}
