import unittest
from chatbot.intent_classifier import predict_intent
from chatbot.model import train_model
from chatbot.preprocess import preprocess, load_intents

class TestIntentClassifier(unittest.TestCase):
    def setUp(self):
        intents = load_intents()
        X, y, vectorizer, label_encoder = preprocess(intents)
        self.model = train_model(X, y)
        self.vectorizer = vectorizer
        self.label_encoder = label_encoder

    def test_predict_intent(self):
        text = "Hello"
        intent, confidence = predict_intent(text, self.model, self.vectorizer, self.label_encoder)
        self.assertIsInstance(intent, str)
        self.assertGreaterEqual(confidence, 0)

if __name__ == '__main__':
    unittest.main()
