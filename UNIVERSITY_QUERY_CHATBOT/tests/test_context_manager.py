import unittest
from chatbot.context_manager import ContextManager

# This class checks if ContextManager is working correctly
class TestContextManager(unittest.TestCase):

    # This function runs before every test. It creates a new ContextManager so each test starts from new
    def setUp(self):
        self.cm = ContextManager()

    # This test checks if setting, getting, and clearing context works
    def test_context_storage(self):
        user_id = "user123"                               # Dummy user ID
        context = {"state": "greeting"}                   # Dummy context data
        
        self.cm.set_context(user_id, context)                                # Stores context for this user
        
        self.assertEqual(self.cm.get_context(user_id), context)              # Checks if we get the same context back
        
        self.cm.clear_context(user_id)                                       # Removes user's context
        
        self.assertEqual(self.cm.get_context(user_id), {})                   # The context is reset to empty

if __name__ == '__main__':
    unittest.main()
