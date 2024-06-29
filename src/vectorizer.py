import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import json

def train_vectorizer():
    with open('data/faq_data.json', 'r') as file:
        faq_data = json.load(file)
    questions = list(faq_data.keys())
    
    vectorizer = TfidfVectorizer()
    vectorizer.fit(questions)
    
    with open('models/tfidf_vectorizer.pkl', 'wb') as file:
        pickle.dump(vectorizer, file)

def load_vectorizer():
    with open('models/tfidf_vectorizer.pkl', 'rb') as file:
        return pickle.load(file)

if __name__ == "__main__":
    train_vectorizer()
