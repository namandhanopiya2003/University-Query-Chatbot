import json
import random
import nltk
import joblib
import numpy as np

# Download NLTK tokenizer model
nltk.download('punkt')

# Loads chatbot data (intents and responses)
with open('data/intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

# Loads trained ML files (created while training model)
model = joblib.load('chatbot/model.pkl')
vectorizer = joblib.load('chatbot/vectorizer.pkl')
label_encoder = joblib.load('chatbot/label_encoder.pkl')

# Text cleaning is done
def preprocess_text(text):
    return text.lower()

# Finding the intent of the message
def predict_intent(text):
    text = preprocess_text(text)
    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]
    max_idx = np.argmax(probs)
    intent = label_encoder.inverse_transform([max_idx])[0]
    confidence = probs[max_idx]
    return intent, confidence

# Picksd one response based on intent
def get_response(intent):
    for item in intents['intents']:
        if item['tag'] == intent:
            return random.choice(item['responses'])
    return "Sorry, I didn't understand that."

# Understands the user input and give the best reply
def chatbot_response(text):
    intent, confidence = predict_intent(text)
    if confidence > 0.1:
        return get_response(intent)
    else:
        return "Sorry, I didn't understand that."

# Running chatbot
def main():
    print("Chatbot is running! (type 'quit' or 'exit' to stop)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == '__main__':
    main()
