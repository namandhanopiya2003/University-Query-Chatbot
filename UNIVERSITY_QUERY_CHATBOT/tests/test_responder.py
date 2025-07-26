import unittest
from chatbot.responder import respond

# This class tests if the responder function gives correct replies
class TestResponder(unittest.TestCase):

    # Tests if respond() returns a valid reply for a known intent
    def test_respond_known_action(self):
        
        response = respond('greeting')                          # Try a known tag
        self.assertIsInstance(response, str)                    # The response should be a string
        self.assertNotEqual(response, '')                       # Response should not be empty

    # Tests if respond() returns the default message for unknown intents
    def test_respond_unknown_action(self):
        response = respond('unknown_action')                           # Try an unknown tag
        self.assertEqual(response, "Sorry, I don't understand.")       # Should return default/fallback response

if __name__ == '__main__':
    unittest.main()
