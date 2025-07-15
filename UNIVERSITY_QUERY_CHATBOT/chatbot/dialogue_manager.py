def get_next_action(intent, context, entities):

    # If user said hello
    if intent == 'greeting':
        return 'greeting'

    # If user said goodbye
    elif intent == 'goodbye':
        return 'goodbye'

    # If user is asking about office or working hours
    elif intent == 'ask_hours':
        return 'ask_hours'

    # If user wants to know where the library is
    elif intent == 'ask_library_location':
        return 'ask_library_location'

    # If the intent is something else or unknown
    else:
        return 'default_response'
