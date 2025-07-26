import unittest
from chatbot.intent_classifier import predict_intent
from chatbot.model import train_model
from chatbot.preprocess import preprocess, load_intents

# This class tests if the intent prediction works correctly
class TestIntentClassifier(unittest.TestCase):

    # Sets up everything needed before running each test
    def setUp(self):
        intents = load_intents()                                               # Loads data from intents.json
        X, y, vectorizer, label_encoder = preprocess(intents)                  # Prepares training data
        self.model = train_model(X, y)                                         # Trains the model
        self.vectorizer = vectorizer                                           # Saves the vectorizer for use in prediction
        self.label_encoder = label_encoder                                     # Saves the label encoder

    # Tests if predict_intent returns a string and a confidence score
    def test_predict_intent(self):
        text = "Hello"                                                         # Dummy input for test
        intent, confidence = predict_intent(text, self.model, self.vectorizer, self.label_encoder)
        
        self.assertIsInstance(intent, str)                         # The result should be a string (like 'greeting' or 'goodbye')
        self.assertGreaterEqual(confidence, 0)                     # Makes sure confidence score is not negative

if __name__ == '__main__':
    unittest.main()
