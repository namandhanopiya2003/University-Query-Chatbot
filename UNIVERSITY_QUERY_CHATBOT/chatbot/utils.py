import random
import re

# Converts text to lowercase and remove special characters
def clean_text(text):
    text = text.lower()                                  # Makes everything lowercase
    text = re.sub(r'[^a-z0-9\s]', '', text)              # Keeps only letters, numbers, and spaces
    return text

# Picks a random item from a list
def random_choice(choices):
    return random.choice(choices)
