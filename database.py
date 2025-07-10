# database.py
#
# This file handles all interactions with the MongoDB database.

import pymongo
from config import settings # Import settings from your config.py

# --- Database Connection ---
try:
    client = pymongo.MongoClient(settings.MONGO_URI)
    db = client.get_database("FastAPI_Auth_App") # You can name your database
    user_collection = db.get_collection("users")
    student_collection = db.get_collection("students")
    print("✅ Successfully connected to MongoDB.")
except pymongo.errors.ConnectionFailure as e:
    print(f"❌ Could not connect to MongoDB: {e}")
    # In a real app, you might want to exit or handle this more gracefully
    client = None
    db = None
    user_collection = None
    student_collection = None


# --- User Database Functions ---

def get_user(username: str):
    """Retrieves a user document from the 'users' collection."""
    if user_collection is None: return None
    return user_collection.find_one({"username": username})

def create_user(user_data: dict):
    """Inserts a new user document into the 'users' collection."""
    if user_collection is None: return None
    return user_collection.insert_one(user_data)


# --- Student Database Functions ---

def get_student_from_db(enrollment_number: str):
    """Retrieves a student document from the 'students' collection."""
    if student_collection is None: return None
    return student_collection.find_one({"enrollment_number": enrollment_number})

def populate_initial_student_data():
    """
    Populates the 'students' collection with sample data if it's empty.
    This is useful for initial setup.
    """
    if student_collection is None or student_collection.count_documents({}) > 0:
        return # Don't populate if not connected or if data already exists

    initial_students = [
        {
            "name": "Alice Smith",
            "enrollment_number": "ENR001",
            "branch": "Computer Science",
            "year": 3,
            "subjects": [
                {"subject_name": "Data Structures", "marks": 85},
                {"subject_name": "Algorithms", "marks": 92},
                {"subject_name": "Database Systems", "marks": 78},
            ]
        },
        {
            "name": "Bob Johnson",
            "enrollment_number": "ENR002",
            "branch": "Mechanical Engineering",
            "year": 2,
            "subjects": [
                {"subject_name": "Thermodynamics", "marks": 76},
                {"subject_name": "Fluid Mechanics", "marks": 88},
                {"subject_name": "Engineering Drawing", "marks": 95},
            ]
        },
    ]
    student_collection.insert_many(initial_students)
    print("📚 Initial student data populated in the database.")

