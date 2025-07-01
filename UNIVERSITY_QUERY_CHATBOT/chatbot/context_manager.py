class ContextManager:
    def __init__(self):
        self.contexts = {}

    def get_context(self, user_id):
        return self.contexts.get(user_id, {})

    def set_context(self, user_id, context):
        self.contexts[user_id] = context

    def clear_context(self, user_id):
        if user_id in self.contexts:
            del self.contexts[user_id]
