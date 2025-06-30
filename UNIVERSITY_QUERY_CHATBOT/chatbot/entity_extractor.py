import json

def load_entities(filepath='data/entities.json'):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    entities = {}
    for item in data.get("entities", []):
        entity_name = item.get("entity")
        examples = item.get("examples", [])
        entities[entity_name] = examples

    return entities

def extract_entities(text, entities_dict):
    extracted = {}
    text_lower = text.lower()

    for entity, values in entities_dict.items():
        if isinstance(values, list): 
            for val in values:
                if isinstance(val, str) and val.lower() in text_lower:
                    extracted[entity] = val
                    break
    return extracted
