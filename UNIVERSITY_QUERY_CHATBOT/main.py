# import json
# import random
# import string
# import nltk
# from nltk.stem import WordNetLemmatizer
# import numpy as np

# # Download necessary NLTK data files if not already downloaded
# nltk.download('punkt')
# nltk.download('wordnet')

# lemmatizer = WordNetLemmatizer()

# # Load intents JSON data
# with open('data/intents.json', 'r', encoding='utf-8') as file:
#     intents = json.load(file)

# # Build vocabulary and classes for simple rule-based matching
# words = []
# classes = []
# documents = []

# # Tokenize and build documents and word list from patterns
# for intent in intents['intents']:
#     for pattern in intent['patterns']:
#         # Tokenize each word in the pattern
#         tokens = nltk.word_tokenize(pattern.lower())
#         words.extend(tokens)
#         documents.append((tokens, intent['tag']))
#     if intent['tag'] not in classes:
#         classes.append(intent['tag'])

# # Lemmatize and remove duplicates, remove punctuation tokens
# words = [lemmatizer.lemmatize(w) for w in words if w not in string.punctuation]
# words = sorted(set(words))
# classes = sorted(set(classes))


# def clean_up_sentence(sentence):
#     """Tokenize, lowercase, and lemmatize the sentence"""
#     sentence_words = nltk.word_tokenize(sentence.lower())
#     sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words if word not in string.punctuation]
#     return sentence_words


# def bow(sentence, words):
#     """Return bag of words array: 1 for each known word that exists in the sentence, 0 otherwise"""
#     sentence_words = clean_up_sentence(sentence)
#     bag = [0] * len(words)
#     for s in sentence_words:
#         for i, w in enumerate(words):
#             if w == s:
#                 bag[i] = 1
#     return np.array(bag)


# def classify(sentence):
#     """
#     Simple classification using rule-based matching:
#     This function checks which intent has patterns matching the sentence tokens.
#     Returns best matching intent tag or None.
#     """
#     sentence_words = clean_up_sentence(sentence)
#     for intent in intents['intents']:
#         for pattern in intent['patterns']:
#             pattern_words = clean_up_sentence(pattern)
#             if all(word in sentence_words for word in pattern_words):
#                 return intent['tag']
#     return None


# def get_response(tag):
#     """Get a random response from the matched intent tag"""
#     for intent in intents['intents']:
#         if intent['tag'] == tag:
#             return random.choice(intent['responses'])
#     return "Sorry, I didn't understand that. Can you try again?"


# def chatbot_response(text):
#     tag = classify(text)
#     if tag:
#         return get_response(tag)
#     else:
#         return "Sorry, I didn't understand that. Can you try again?"


# def main():
#     print("Chatbot is running! (type 'quit' or 'exit' to stop)")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ['quit', 'exit']:
#             print("Chatbot: Goodbye! Have a nice day.")
#             break
#         response = chatbot_response(user_input)
#         print(f"Chatbot: {response}")


# if __name__ == '__main__':
#     main()










import json
import random
import nltk
import joblib
import numpy as np

nltk.download('punkt')

# Load intents JSON
with open('data/intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

# Load trained model, vectorizer, label encoder
model = joblib.load('chatbot/model.pkl')
vectorizer = joblib.load('chatbot/vectorizer.pkl')
label_encoder = joblib.load('chatbot/label_encoder.pkl')

def preprocess_text(text):
    # Just lowercase, no tokenizing or joining
    return text.lower()

def predict_intent(text):
    text = preprocess_text(text)
    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]
    max_idx = np.argmax(probs)
    intent = label_encoder.inverse_transform([max_idx])[0]
    confidence = probs[max_idx]
    return intent, confidence

def get_response(intent):
    for item in intents['intents']:
        if item['tag'] == intent:
            return random.choice(item['responses'])
    return "Sorry, I didn't understand that."

def chatbot_response(text):
    intent, confidence = predict_intent(text)
    if confidence > 0.1:  # you can adjust this threshold
        return get_response(intent)
    else:
        return "Sorry, I didn't understand that."

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
