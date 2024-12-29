from db import get_db
from preprocessing import preprocess_input
from semantic_search import find_best_match

def get_answer_from_db(question):
    """
    Retrieve the answer for a given question from the knowledge base.
    """
    db = get_db()
    if db is not None:  # Explicit check for None instead of truth value testing
        knowledge_base = db["knowledge_base"]
        
        # Preprocess the user's question
        preprocessed_question = preprocess_input(question)
        
        # Find the best match using semantic search
        best_match = find_best_match(preprocessed_question, knowledge_base)
        
        # Return the answer or a default response if not found
        return best_match["answer"] if best_match else "Sorry, I don't have an answer for that."
    else:
        return "Error connecting to the database."

def save_chat_history(user_input, bot_response):
    """
    Save the user input and bot response to the chat_history collection.
    """
    db = get_db()
    if db is not None:  # Explicit check for None instead of truth value testing
        chat_history = db["chat_history"]
        chat_history.insert_one({"user": user_input, "bot": bot_response})
    else:
        print("❌ Failed to save chat history.")

def chatbot():
    """
    The main chatbot function that interacts with the user.
    """
    print("Knowledge Chatbot (type 'exit' to quit)")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Get response from the knowledge base
        response = get_answer_from_db(user_input)
        
        # Save the conversation to the database
        save_chat_history(user_input, response)
        
        # Print the chatbot's response
        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()
