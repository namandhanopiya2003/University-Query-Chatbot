import json

def load_entities(filepath='data/entities.json'):
    # Loads entities from a JSON file.
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Goes through each entity and gets it examples
    entities = {}
    for item in data.get("entities", []):
        entity_name = item.get("entity")
        examples = item.get("examples", [])
        entities[entity_name] = examples

    return entities

# Checks if any entity values are written in the user's message
def extract_entities(text, entities_dict):
    extracted = {}
    text_lower = text.lower()

    # Goes through each entity and its list of values
    for entity, values in entities_dict.items():
        if isinstance(values, list): 
            for val in values:

                # Checks if the value is present in the user’s message
                if isinstance(val, str) and val.lower() in text_lower:
                    extracted[entity] = val
                    break
    return extracted
