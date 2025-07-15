class ContextManager:
    def __init__(self):
        # This keeps track of each user's chat info
        self.contexts = {}

    def get_context(self, user_id):
        # Gets what the user was talking about (If nothing is saved, return an empty one)
        return self.contexts.get(user_id, {})

    def set_context(self, user_id, context):
        # Saves what the user is talking about
        self.contexts[user_id] = context

    def clear_context(self, user_id):
        # Deletes the saved info for the user (Useful when chat is done or reset)
        if user_id in self.contexts:
            del self.contexts[user_id]
