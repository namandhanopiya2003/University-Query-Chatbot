import random
import json

# Loads all intents from the JSON file
with open('data/intents.json', 'r', encoding='utf-8') as f:
    INTENTS = json.load(f)['intents']

def respond(action, entities=None):
    # Go through all intents to find the one that matches the predicted intent
    for intent in INTENTS:
        if intent['tag'] == action:

            # Returs a random response from the matched intent
            return random.choice(intent.get('responses', ['Sorry, I do not understand.']))
    return "Sorry, I don't understand."                  # If the intent doesn't match any tag, it returns a default message
