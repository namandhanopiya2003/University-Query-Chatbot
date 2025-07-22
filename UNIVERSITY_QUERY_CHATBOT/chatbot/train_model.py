import json
import nltk
import numpy as np
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib

# Downloads the tokenizer data (used by NLTK)
nltk.download('punkt')

# Loads intents from the JSON file
with open('data/intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

# Lists to store training data
patterns = []                # User input examples
labels = []                  # Corresponding intent tags

# Extracts patterns and labels from intents
for intent in intents['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        labels.append(intent['tag'])

# Tokenizer to split sentences into words
tokenizer = RegexpTokenizer(r'\w+')
vectorizer = CountVectorizer(tokenizer=tokenizer.tokenize)

# Converts text into numerical feature vectors
X = vectorizer.fit_transform(patterns)

# Encodes intent labels as numbers
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)

# Trains a logistic regression model on the data
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Saves the model and other components for later use
joblib.dump(model, 'chatbot/model.pkl')
joblib.dump(vectorizer, 'chatbot/vectorizer.pkl')
joblib.dump(label_encoder, 'chatbot/label_encoder.pkl')

# Prints completion message
print("Training complete. Model saved as chatbot/model.pkl")
