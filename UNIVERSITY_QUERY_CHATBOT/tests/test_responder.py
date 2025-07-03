import unittest
from chatbot.responder import respond

class TestResponder(unittest.TestCase):
    def test_respond_known_action(self):
        response = respond('greeting')
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, '')

    def test_respond_unknown_action(self):
        response = respond('unknown_action')
        self.assertEqual(response, "Sorry, I don't understand.")

if __name__ == '__main__':
    unittest.main()
