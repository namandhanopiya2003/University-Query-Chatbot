import pickle
from sklearn.naive_bayes import MultinomialNB

MODEL_PATH = 'chatbot/model_intent.pkl'
VECTORIZER_PATH = 'chatbot/vectorizer.pkl'
LABEL_ENCODER_PATH = 'chatbot/label_encoder.pkl'

def train_model(X, y):
    """
    Train a Multinomial Naive Bayes model on given data.
    """
    model = MultinomialNB()
    model.fit(X, y)
    return model

def save_model(model, filepath=MODEL_PATH):
    """
    Save the trained model to a file.
    """
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)

def load_model(filepath=MODEL_PATH):
    """
    Load the trained model from a file.
    """
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    return model

def save_vectorizer(vectorizer, filepath=VECTORIZER_PATH):
    """
    Save the vectorizer to a file.
    """
    with open(filepath, 'wb') as f:
        pickle.dump(vectorizer, f)

def load_vectorizer(filepath=VECTORIZER_PATH):
    """
    Load the vectorizer from a file.
    """
    with open(filepath, 'rb') as f:
        vectorizer = pickle.load(f)
    return vectorizer

def save_label_encoder(label_encoder, filepath=LABEL_ENCODER_PATH):
    """
    Save the label encoder to a file.
    """
    with open(filepath, 'wb') as f:
        pickle.dump(label_encoder, f)

def load_label_encoder(filepath=LABEL_ENCODER_PATH):
    """
    Load the label encoder from a file.
    """
    with open(filepath, 'rb') as f:
        label_encoder = pickle.load(f)
    return label_encoder
