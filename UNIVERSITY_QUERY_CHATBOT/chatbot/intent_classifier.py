import numpy as np

def predict_intent(text, model, vectorizer, label_encoder):
    # Makes the input text lowercase
    text = text.lower()

    # Converts the text into a numeric format (for model understanding)
    text_vec = vectorizer.transform([text])

    # Gets prediction probabilities for each possible intent
    probs = model.predict_proba(text_vec)[0]

    # Finds the intent with the highest probability
    idx = np.argmax(probs)

    # Converts the predicted index back to the intent name (eg. "greeting" or "ask_fees")
    intent = label_encoder.inverse_transform([idx])[0]

    # Gets how confident the model is about the prediction and return intent, confidence
    confidence = probs[idx]
    return intent, confidence
