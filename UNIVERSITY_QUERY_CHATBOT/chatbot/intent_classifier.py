import numpy as np

def predict_intent(text, model, vectorizer, label_encoder):
    text = text.lower()
    text_vec = vectorizer.transform([text])
    probs = model.predict_proba(text_vec)[0]
    idx = np.argmax(probs)
    intent = label_encoder.inverse_transform([idx])[0]
    confidence = probs[idx]
    return intent, confidence
