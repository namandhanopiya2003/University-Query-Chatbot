def get_next_action(intent, context, entities):
    if intent == 'greeting':
        return 'greeting'
    elif intent == 'goodbye':
        return 'goodbye'
    elif intent == 'ask_hours':
        return 'ask_hours'
    elif intent == 'ask_library_location':
        return 'ask_library_location'
    else:
        return 'default_response'
