# import json
# import nltk
# import numpy as np
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.preprocessing import LabelEncoder
# from sklearn.linear_model import LogisticRegression
# import joblib

# nltk.download('punkt')

# # Load intents
# with open('data/intents.json', 'r', encoding='utf-8') as f:
#     intents = json.load(f)

# patterns = []
# labels = []

# for intent in intents['intents']:
#     for pattern in intent['patterns']:
#         patterns.append(pattern)
#         labels.append(intent['tag'])

# # Vectorize text patterns
# vectorizer = CountVectorizer(tokenizer=nltk.word_tokenize)
# X = vectorizer.fit_transform(patterns)

# # Encode labels
# label_encoder = LabelEncoder()
# y = label_encoder.fit_transform(labels)

# # Train classifier
# model = LogisticRegression(max_iter=200)
# model.fit(X, y)

# # Save model and vectorizer and label encoder
# joblib.dump(model, 'chatbot/model.pkl')
# joblib.dump(vectorizer, 'chatbot/vectorizer.pkl')
# joblib.dump(label_encoder, 'chatbot/label_encoder.pkl')

# print("Training complete. Model saved as chatbot/model.pkl")










import json
import nltk
import numpy as np
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib

# Download necessary NLTK data
nltk.download('punkt')  # Still useful for other parts if needed later

# Load intents JSON
with open('data/intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

patterns = []
labels = []

# Extract patterns and corresponding tags
for intent in intents['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        labels.append(intent['tag'])

# Use RegexpTokenizer to avoid punkt_tab issue
tokenizer = RegexpTokenizer(r'\w+')
vectorizer = CountVectorizer(tokenizer=tokenizer.tokenize)

# Vectorize patterns
X = vectorizer.fit_transform(patterns)

# Encode labels (tags)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)

# Train classifier
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save the model, vectorizer, and label encoder
joblib.dump(model, 'chatbot/model.pkl')
joblib.dump(vectorizer, 'chatbot/vectorizer.pkl')
joblib.dump(label_encoder, 'chatbot/label_encoder.pkl')

print("✅ Training complete. Model saved as chatbot/model.pkl")
