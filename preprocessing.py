import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_input(text):
    """
    Preprocess the input text by removing stop words and lemmatizing.
    """
    doc = nlp(text)
    
    # Remove stop words and non-alphabetical tokens, then return lemmatized words
    return " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])
