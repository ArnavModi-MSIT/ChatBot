from transformers import pipeline
import numpy as np

# Load the transformer model for feature extraction (BERT model)
model = pipeline('feature-extraction', model='distilbert-base-uncased')

def get_embedding(text):
    """
    Get the BERT embedding of a given text.
    """
    embeddings = model(text)
    return np.mean(embeddings[0], axis=0)

def find_best_match(user_input, knowledge_base):
    """
    Find the most semantically similar question from the knowledge base.
    """
    user_embedding = get_embedding(user_input)
    
    best_match = None
    best_score = -1
    
    # Iterate over all the documents in the knowledge base using .find()
    for entry in knowledge_base.find():
        question_embedding = get_embedding(entry["question"])
        similarity_score = np.dot(user_embedding, question_embedding)  # Cosine similarity
        
        if similarity_score > best_score:
            best_score = similarity_score
            best_match = entry
    
    return best_match
