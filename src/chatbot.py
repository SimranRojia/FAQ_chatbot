import json
from sklearn.metrics.pairwise import cosine_similarity
from src.vectorizer import load_vectorizer

def load_faq_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

faq_data = load_faq_data('data/faq_data.json')
vectorizer = load_vectorizer()
faq_vectors = vectorizer.transform(list(faq_data.keys()))

greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]

def find_best_match(query):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, faq_vectors)
    best_match_idx = similarities.argmax()
    highest_similarity = similarities[0, best_match_idx]
    
    # Set a more strict similarity threshold
    similarity_threshold = 0.5
    if highest_similarity < similarity_threshold:
        return None
    best_match = list(faq_data.keys())[best_match_idx]
    return best_match

def chatbot(query):
    if query.lower() in greetings:
        return "Hello! How can I assist you today?"
    
    best_match = find_best_match(query)
    if best_match:
        return faq_data[best_match]
    else:
        return "I'm sorry, I don't have an answer for that question."
