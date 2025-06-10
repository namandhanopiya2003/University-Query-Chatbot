import unittest
from chatbot.context_manager import ContextManager

class TestContextManager(unittest.TestCase):
    def setUp(self):
        self.cm = ContextManager()

    def test_context_storage(self):
        user_id = "user123"
        context = {"state": "greeting"}
        self.cm.set_context(user_id, context)
        self.assertEqual(self.cm.get_context(user_id), context)
        self.cm.clear_context(user_id)
        self.assertEqual(self.cm.get_context(user_id), {})

if __name__ == '__main__':
    unittest.main()
