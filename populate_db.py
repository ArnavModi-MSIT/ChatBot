import json
from db import get_db

def populate_knowledge_base():
    """
    Populate the knowledge_base collection with predefined data.
    """
    db = get_db()
    if db is not None:
        knowledge_base = db["knowledge_base"]
        
        # Clear existing data (optional, to avoid duplicates)
        knowledge_base.delete_many({})
        
        # Load JSON data
        with open("knowledge_base.json", "r") as file:
            data = json.load(file)
        
        # Insert data into MongoDB
        knowledge_base.insert_many(data)
        print("✅ Knowledge base populated successfully!")
    else:
        print("❌ Failed to connect to the database.")

if __name__ == "__main__":
    populate_knowledge_base()
