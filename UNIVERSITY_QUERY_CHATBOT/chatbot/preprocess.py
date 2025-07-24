import json
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer

def load_intents(filepath='data/intents.json'):
    # Loads the list of intents from the JSON file
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['intents']

def clean_text(text):
    # Makes the text lowercase and remove special characters
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def preprocess(intents):
    patterns = []                    # Saves all example user enters/messages
    labels = []                      # Save the matching intent name for each message
    for intent in intents:
        for pattern in intent.get('patterns', []):
            patterns.append(clean_text(pattern))
            labels.append(intent['tag'])

    # Converts intent tags to numbers
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)

    # Converts text to bag-of-words vectors
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(patterns)
    
    return X, y, vectorizer, label_encoder
