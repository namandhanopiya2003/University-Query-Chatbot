import json
import nltk
import numpy as np
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib

nltk.download('punkt')

with open('data/intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

patterns = []
labels = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        labels.append(intent['tag'])

tokenizer = RegexpTokenizer(r'\w+')
vectorizer = CountVectorizer(tokenizer=tokenizer.tokenize)

X = vectorizer.fit_transform(patterns)

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)

model = LogisticRegression(max_iter=200)
model.fit(X, y)

joblib.dump(model, 'chatbot/model.pkl')
joblib.dump(vectorizer, 'chatbot/vectorizer.pkl')
joblib.dump(label_encoder, 'chatbot/label_encoder.pkl')

print("Training complete. Model saved as chatbot/model.pkl")
