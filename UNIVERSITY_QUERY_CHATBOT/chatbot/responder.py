import random
import json

with open('data/intents.json', 'r', encoding='utf-8') as f:
    INTENTS = json.load(f)['intents']

def respond(action, entities=None):
    for intent in INTENTS:
        if intent['tag'] == action:
            return random.choice(intent.get('responses', ['Sorry, I do not understand.']))
    return "Sorry, I don't understand."
