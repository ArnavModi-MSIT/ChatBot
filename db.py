from pymongo import MongoClient

def get_db():
    """
    Establish a connection to the MongoDB database.
    """
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["chatbot_db"]
        print("✅ Connected to MongoDB successfully!")
        return db
    except Exception as e:
        print("❌ Failed to connect to MongoDB:", e)
        return None
